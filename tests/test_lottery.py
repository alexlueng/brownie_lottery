# 0.019
from brownie import Lottery, accounts, config, network, exceptions
from web3 import Web3
import pytest

def test_get_entrance_fee():
    account = accounts[0]
    lottery = Lottery.deploy(
        config["networks"][network.show_active()]["eth_usd_price_feed"], 
        {"from": account},
    )
    # print(lottery)
    # print(lottery.getPrice())
    # print(lottery.getEntranceFee())
    # with pytest.raises(exceptions.VirtualMachineError):
        # print(lottery.getEntranceFee())

    # assert lottery != None
    assert lottery.getEntranceFee() < Web3.toWei(0.022, "ether")