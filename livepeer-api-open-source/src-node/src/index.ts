import express from 'express';
import bodyParser from 'express';
import LivepeerSDK from '@livepeer/sdk'

const app = express();

app.use(bodyParser.urlencoded({
  extended: true
}));
app.use(bodyParser.json());

const port = process.env.PORT || 3001;

const provider_livepeer = "https://mainnet.infura.io/v3/{YOUR-INFURA-API-KEY}"
const controllerAddress_livepeer = "0x37dC71366Ec655093b9930bc816E16e6b587F968"

var livepeer_rpc: any = {};

LivepeerSDK({ provider_livepeer, controllerAddress_livepeer, gas: 2.1*1000000 }).then(async sdk => {
  livepeer_rpc = sdk
})

app.get('/livepeer/:service', async (req, res) => {

    var { rpc } = livepeer_rpc
    
    if (req.params.service == "getUnbondingPeriod"){
      const unbonding_period = await rpc.getUnbondingPeriod()
      res.send({unbonding_period: unbonding_period})
    }

    if (req.params.service == "getNumActiveTranscoders"){
      const number_active_transcoders = await rpc.getNumActiveTranscoders()
      res.send({number_active_transcoders: number_active_transcoders})
    }

    if (req.params.service == "getMaxEarningsClaimsRounds"){
      const max_earnings_for_claims_rounds = await rpc.getMaxEarningsClaimsRounds()
      res.send({max_earnings_for_claims_rounds: max_earnings_for_claims_rounds})
    }

    if (req.params.service == "getTotalBonded"){
      const total_bonded_tokens = await rpc.getTotalBonded()
      res.send({total_bonded_tokens: total_bonded_tokens})
    }

    if (req.params.service == "getTokenTotalSupply"){
      const total_supply_tokens = await rpc.getTokenTotalSupply()
      res.send({total_supply_tokens: total_supply_tokens})
    }

    if (req.params.service == "getFaucetAmount"){
      const amt_tokens_faucet_distributes = await rpc.getFaucetAmount()
      res.send({amt_tokens_faucet_distributes: amt_tokens_faucet_distributes})
    }

    if (req.params.service == "getFaucetWait"){
      const faucet_wait_time_in_hours = await rpc.getFaucetWait()
      res.send({faucet_wait_time_in_hours: faucet_wait_time_in_hours})
    }

    if (req.params.service == "getInflation"){
      const inflation_per_round = await rpc.getInflation()
      res.send({inflation_per_round: inflation_per_round})
    }

    if (req.params.service == "getInflationChange"){
      const change_in_inflation_per_round = await rpc.getInflationChange()
      res.send({change_in_inflation_per_round: change_in_inflation_per_round})
    }

    if (req.params.service == "getTranscoderPoolMaxSize"){
      const transcoder_pool_max_size = await rpc.getTranscoderPoolMaxSize()
      res.send({transcoder_pool_max_size: transcoder_pool_max_size})
    }

    if (req.params.service == "getTranscoders"){
      const transcoders = await rpc.getTranscoders()
      res.send({transcoders: transcoders})
    }

    if (req.params.service == "getProtocolPaused"){
      const protocol_paused = await rpc.getProtocolPaused()
      res.send({protocol_paused: protocol_paused})
    }

    if (req.params.service == "getProtocol"){
      const protocol_info = await rpc.getProtocol()
      res.send({protocol_info: protocol_info})
    }

    if (req.params.service == "getRoundLength"){
      const length_of_round = await rpc.getRoundLength()
      res.send({length_of_round: length_of_round})
    }

    if (req.params.service == "getRoundsPerYear"){
      const number_rounds_per_year = await rpc.getRoundsPerYear()
      res.send({number_rounds_per_year: number_rounds_per_year})
    }

    if (req.params.service == "getCurrentRound"){
      const current_round = await rpc.getCurrentRound()
      res.send({current_round: current_round})
    }

    if (req.params.service == "getCurrentRoundIsInitialized"){
      const current_round_initialized = await rpc.getCurrentRoundIsInitialized()
      res.send({current_round_initialized: current_round_initialized})
    }

    if (req.params.service == "getCurrentRoundStartBlock"){
      const start_block_of_current_block = await rpc.getCurrentRoundStartBlock()
      res.send({start_block_of_current_block: start_block_of_current_block})
    }

    if (req.params.service == "getLastInitializedRound"){
      const previously_initialized_round = await rpc.getLastInitializedRound()
      res.send({previously_initialized_round: previously_initialized_round})
    }

    if (req.params.service == "getCurrentRoundInfo"){
      const current_round_info = await rpc.getCurrentRoundInfo()
      res.send({current_round_info: current_round_info})
    }

    if (req.params.service == "getTotalJobs"){
      const total_jobs_created = await rpc.getTotalJobs()
      res.send({total_jobs_created: total_jobs_created})
    }

    if (req.params.service == "getJobVerificationRate"){
      const job_verification_rate = await rpc.getJobVerificationRate()
      res.send({job_verification_rate: job_verification_rate})
    }

    if (req.params.service == "getJobVerificationPeriod"){
      const job_verification_period = await rpc.getJobVerificationPeriod()
      res.send({job_verification_period: job_verification_period})
    }

    if (req.params.service == "getJobVerificationSlashingPeriod"){
      const job_verification_slashing_period = await rpc.getJobVerificationSlashingPeriod()
      res.send({job_verification_slashing_period: job_verification_slashing_period})
    }

    if (req.params.service == "getJobFinderFee"){
      const job_finder_fee = await rpc.getJobFinderFee()
      res.send({job_finder_fee: job_finder_fee})
    }

    if (req.params.service == "getJobsInfo"){
      const job_info = await rpc.getJobsInfo()
      res.send({job_info: job_info})
    }

    if (req.params.service == "getJobs"){
      const jobs_info = await rpc.getJobs()
      res.send({jobs_info: jobs_info})
    }

    if (req.params.service == "getTargetBondingRate"){
      const target_bonding_rate = await rpc.getTargetBondingRate()
      res.send({target_bonding_rate: target_bonding_rate})
    }

    if (req.params.service == "getFaucetNext"){
      const next_timestamp_address_tap_faucet = await rpc.getFaucetNext()
      res.send({next_timestamp_address_tap_faucet: next_timestamp_address_tap_faucet})
    }
  
});

app.post('/livepeer/:service', async (req, res) => {
    var { rpc } = livepeer_rpc

    if (req.params.service == "getENSName"){
      var address = req.body.address
      const ens_name = await rpc.getENSAddress(address)
      res.send({ens_name: ens_name})
    }

    if (req.params.service == "getENSAddress"){
      var name = req.body.name
      const ens_address = await rpc.getENSAddress(name)
      res.send({ens_address: ens_address})
    }

    if (req.params.service == "getBlock"){
      var block = req.body.block
      const block_info = await rpc.getBlock(block)
      res.send({block_info: block_info})
    }

    if (req.params.service == "getEthBalance"){
      var addr = req.body.addr
      const eth_balance = await rpc.getEthBalance(addr)
      res.send({eth_balance: eth_balance})
    }

    if (req.params.service == "getTokenBalance"){
      var addr = req.body.addr
      const token_balance_user = await rpc.getTokenBalance(addr)
      res.send({token_balance_user: token_balance_user})
    }

    if (req.params.service == "transferToken"){
      var to = req.body.to
      var amount = req.body.amount
      var tx = req.body.tx
      const tx_receipt = await rpc.transferToken(to, amount, tx)
      res.send({unbonding_period: tx_receipt})
    }

    if (req.params.service == "getTokenInfo"){
      var addr = req.body.addr
      const token_info = await rpc.getTokenInfo(addr)
      res.send({token_info: token_info})
    }

    if (req.params.service == "getFaucetInfo"){
      var addr = req.body.addr
      const faucet_info = await rpc.getFaucetInfo(addr)
      res.send({faucet_info: faucet_info})
    }

    if (req.params.service == "getBroadcaster"){
      var addr = req.body.addr
      const broadcaster_info = await rpc.getBroadcaster(addr)
      res.send({broadcaster_info: broadcaster_info})
    }

    if (req.params.service == "getDelegatorStatus"){
      var addr = req.body.addr
      const delegator_status = await rpc.getDelegatorStatus(addr)
      res.send({delegator_status: delegator_status})
    }

    if (req.params.service == "getDelegator"){
      var addr = req.body.addr
      const delegator_info = await rpc.getDelegator(addr)
      res.send({delegator_info: delegator_info})
    }

    if (req.params.service == "getTranscoderIsActive"){
      var addr = req.body.addr
      const transcoder_active = await rpc.getTranscoderIsActive(addr)
      res.send({transcoder_active: transcoder_active})
    }

    if (req.params.service == "getTranscoderStatus"){
      var addr = req.body.addr
      const transcoder_status = await rpc.getTranscoderStatus(addr)
      res.send({transcoder_status: transcoder_status})
    } 

    if (req.params.service == "getTranscoderTotalStake"){
      var addr = req.body.addr
      const transcoder_total_stake = await rpc.getTranscoderTotalStake(addr)
      res.send({transcoder_total_stake: transcoder_total_stake})
    } 

    if (req.params.service == "getTranscoder"){
      var addr = req.body.addr
      const transcoder_info = await rpc.getTranscoder(addr)
      res.send({transcoder_info: transcoder_info})
    }

    if (req.params.service == "getJob"){
      var id = req.body.id
      const job_info = await rpc.getJob(id)
      res.send({job_info: job_info})
    }

    if (req.params.service == "tapFaucet"){
      var tx = req.body.tx
      const tx_receipt = await rpc.tapFaucet(tx)
      res.send({tx_receipt: tx_receipt})
    }

    if (req.params.service == "initializeRound"){
      var tx = req.body.tx
      const tx_receipt = await rpc.initializeRound(tx)
      res.send({tx_receipt: tx_receipt})
    }

    if (req.params.service == "claimEarnings"){
      var end_round = req.body.end_round
      var tx = req.body.tx
      const tx_receipt = await rpc.claimEarnings(end_round, tx)
      res.send({tx_receipt: tx_receipt})
    }

    if (req.params.service == "estimateGas"){
      var contract_name = req.body.contract_name
      var method_name = req.body.method_name
      var contract_args = req.body.contract_args
      var tx = req.body.tx
      const tx_receipt = await rpc.estimateGas(contract_name, method_name, contract_args, tx)
      res.send({tx_receipt: tx_receipt})
    }

    if (req.params.service == "unbond"){
      var tx = req.body.tx
      const tx_receipt = await rpc.unbond(tx)
      res.send({tx_receipt: tx_receipt})
    }

    if (req.params.service == "setupTranscoder"){
      var reward_cut = req.body.reward_cut
      var fee_share = req.body.fee_share
      var price_per_segment = req.body.price_per_segment
      var tx = req.body.tx
      const tx_receipt = await rpc.setupTranscoder(reward_cut, fee_share, price_per_segment, tx)
      res.send({tx_receipt: tx_receipt})
    }

    if (req.params.service == "deposit"){
      var amount = req.body.amount
      var tx = req.body.tx
      const tx_receipt = await rpc.deposit(amount, tx)
      res.send({tx_receipt: tx_receipt})
    }

    if (req.params.service == "withdraw"){
      var tx = req.body.tx
      const tx_receipt = await rpc.withdraw(tx)
      res.send({tx_receipt: tx_receipt})
    }

    if (req.params.service == "withdrawStake"){
      var tx = req.body.tx
      const tx_receipt = await rpc.withdrawStake(tx)
      res.send({tx_receipt: tx_receipt})
    }

    if (req.params.service == "withdrawFees"){
      var tx = req.body.tx
      const tx_receipt = await rpc.withdrawFees(tx)
      res.send({tx_receipt: tx_receipt})
    }

    if (req.params.service == "createJob"){
      var stream_id = req.body.stream_id
      var profiles = req.body.profiles
      var max_price_per_segment = req.body.max_price_per_segment
      var tx = req.body.tx
      const tx_receipt = await rpc.createJob(stream_id, profiles, max_price_per_segment, tx)
      res.send({tx_receipt: tx_receipt})
    }

    if (req.params.service == "getDelegatorUnbondingLock"){
      var addr = req.body.addr
      var unbonding_lock_id = req.body.unbonding_lock_id
      const unbonding_lock = await rpc.getDelegatorUnbondingLock(addr, unbonding_lock_id)
      res.send({unbonding_lock: unbonding_lock})
    }

});

app.listen(port, () => {
  console.log(`Node/express app listening on port ${port}!`);
});
