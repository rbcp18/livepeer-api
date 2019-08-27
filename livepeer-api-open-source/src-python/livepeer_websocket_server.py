import asyncio
import websockets
import aiohttp

# Define how long to sleep between updates (in seconds)
sleepBetweenUpdatesInSeconds = 15.0
websocketHost = "localhost"
websocketPort = 8765

# Handle websocket connection
async def handler(websocket, path):
    try:
        # Get user to input the address of the transcoder they want to monitor
        await websocket.send("Enter Ethereum address of the transcoder you wish to monitor (ex: 0xe0a4a877cd0a07da7c08dffebc2546a4713147f2)")
        transcoderAddress = await websocket.recv()
        await websocket.send(f"Monitoring transcoder {transcoderAddress}:")

        # Loop on that transcoder, outputting round info, transcoder data, and reward data
        async with aiohttp.ClientSession() as session:
            while True:

                # Retrieve and pass along the current round info (as JSON string)
                async with session.get('https://apis.fabrx.io/v1.0/network/livepeer/getCurrentRoundInfo') as resp:
                    await websocket.send(await resp.text())

                # Retrieve and pass along the transcoder info for this particular transcoder (as JSON string).
                # Also, store this info as dict for reward calculations below.
                async with session.post('https://apis.fabrx.io/v1.0/network/livepeer/getTranscoder', data={"addr": transcoderAddress}) as resp:
                    transcoderText = await resp.text()
                    transcoderData = await resp.json()
                    await websocket.send(transcoderText)

                # Get the inflation rate and perform the rewards calculations
                async with session.get('https://apis.fabrx.io/v1.0/network/livepeer/getInflation') as resp:
                    # Extract the inflation rate, total stake and reward cut from this and previous calls
                    inflationJsonData = await resp.json()
                    inflationPerRoundPercent = int(inflationJsonData["inflation_per_round"]) / 10 ** 4
                    totalStake = int(transcoderData['transcoder_info']["totalStake"]) / 10 ** 18
                    rewardCutPercent = int(transcoderData['transcoder_info']["rewardCut"]) / 10 ** 4

                    # Run the rewards calculations for total rewards, user rewards, and transcoder rewards for this round
                    totalPerRoundRewards = totalStake * inflationPerRoundPercent
                    transcoderPerRoundRewards = totalPerRoundRewards * (rewardCutPercent / 100)
                    userPerRoundRewards = totalPerRoundRewards - transcoderPerRoundRewards

                    # Create a JSON string with all this data and send it on the websocket connection
                    await websocket.send('{{"totalStake": {}, "inflationPerRoundPercent": {}, "rewardCutPercent": {}, "transcoderPerRoundRewards": {}, "userPerRoundRewards": {}, "totalPerRoundRewards": {}}}'.format(
                        totalStake, inflationPerRoundPercent, rewardCutPercent, transcoderPerRoundRewards, userPerRoundRewards, totalPerRoundRewards))

                # Sleep between updates
                await asyncio.sleep(sleepBetweenUpdatesInSeconds)

    # Watch for unexpected connection closures (user just terminates websocket connection) and intercept for a clean close
    except websockets.exceptions.ConnectionClosed:
        print("Connection closed unexpectedly")

# Host the websocket server using asyncio
start_server = websockets.serve(handler, websocketHost, websocketPort)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()