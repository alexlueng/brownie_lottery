1. Users can enter lottery with ETH based on a USD fee
2. An admin will choose when the lottery is over
3. The lottery will select a random winner

How do we test the contract?
`mainnet-fork`
`development` with mocks
`testnet`



brownie networks add development mainnet-fork cmd=ganache-cli host=http://127.0.0.1 fork=https://eth-mainnet.alchemyapi.io/v2/L9mpEMRyQCQTHSJ_Ycrg5qY0QC3uts3t accounts=10 mnemonic=brownie port=8545 evm_version=istanbul

https://eth-mainnet.alchemyapi.io/v2/L9mpEMRyQCQTHSJ_Ycrg5qY0QC3uts3t
https://eth-mainnet.alchemyapi.io/v2/L9mpEMRyQCQTHSJ_Ycrg5qY0QC3uts3t


test smart contract is a very import step,
you should test every line in the smart contract

What should I do now?
- figure out so many questions
- test文件夹下的sol文件如何编译，不同版本的sol文件
- 测试网络与本地网络的区别，分别是如何部署的
- brownie account
- vrf1 与 vrf2
  