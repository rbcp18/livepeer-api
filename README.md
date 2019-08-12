# livepeer-api
**The Livepeer API** will act as a unified point of contact for Livepeer developers to perform queries, connect to websockets, run smart contract functions, and interact with nodes. 

Version 1.0.0 of the Livepeer API can be found here: https://app.swaggerhub.com/apis-docs/rfabrx/livepeer-api/1.0.0

--

The API will consist of two layers:

**Layer 1: Data and WebSockets**

Layer 1 will integrate all major Livepeer tools and access points. Platforms which are planned for integration include: the Livepeer SDK (for GET request functionality), Livepeer subgraph (for queries on transcoders, rewards, and rounds, and websockets on events), Livepeer studio (for staking alerts), and OpenMarketCap (or other token data feeds).

In addition, custom data-based API calls will be integrated, such as (1) retrieval of all Livepeer smart contracts on mainnet, (2) JSON data of transcoders (by address) with their campaign information (name, team, about), and (3) events from specific LPT exchanges (eg. Poloniex, Uniswap, IDEX) and wallets (eg. 0x6941627cba3518385e75de75d25a189185672bfe, which holds 6.5% of the network).

**Layer 2: Nodes and Smart Contracts**

Layer 2 will constitute the launch of full nodes running on both Mainnet and Ropsten with HTTP access. This will enable developers to immediately start building on a Livepeer node, without going through the potential roadblocks faced when launching a private node. In addition, this will enable broadcasters to use the Testnet nodes (and Mainnet nodes, if desired) as a way to quickly get up and running with the OBS integration.

Alongside the node integration, all major smart contract actions, including bonding and delegation functions, will be directly integrated into the API. To do so, the API will utilize the Livepeer Minter contract and other available contracts. This smart contract functionality will be integrated with web3 wallet support, initially with Metamask and, subsequently, with Fortmatic.
