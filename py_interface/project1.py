from web3 import Web3, HTTPProvider
from web3.middleware import geth_poa_middleware
web3 = Web3(HTTPProvider('http://localhost:8545'))
web3.middleware_stack.inject(geth_poa_middleware, layer=0)
ourAddress = web3.toChecksumAddress("0x05A94caaCdb83e8B9E0b9a582988de448440ECc1")
ourPassword = "domore0325"
sellerAddress = web3.toChecksumAddress("0xe12fd247cd56347ece998784b013d060adc6ad69")
sellerPassword = "domore"
#下面这两个地址是用来测试的，你自己新建账户测试
transferTo="0xC74f777fad969f3e571f99fB6747418E4077A46C"
buyerAddress="0xCFeE21Ebb1410F6664f5eB0b52E528b782b5dC28"


#获得合约
def getContract():
    contractAddress = web3.toChecksumAddress('0xe8fd9a6399c96a5c213f01998f30357cc25d5a79')
    abi = '[{"constant":false,"inputs":[{"name":"_spender","type":"address"},{"name":"_value","type":"uint256"}],"name":"approve","outputs":[{"name":"success","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_from","type":"address"},{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transferFrom","outputs":[{"name":"success","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"}],"name":"balanceOf","outputs":[{"name":"balance","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transfer","outputs":[{"name":"success","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"},{"name":"_spender","type":"address"}],"name":"allowance","outputs":[{"name":"remaining","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_from","type":"address"},{"indexed":true,"name":"_to","type":"address"},{"indexed":false,"name":"_value","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_owner","type":"address"},{"indexed":true,"name":"_spender","type":"address"},{"indexed":false,"name":"_value","type":"uint256"}],"name":"Approval","type":"event"}]'
    contract = web3.eth.contract(address=contractAddress, abi=abi)
    return contract
contract=getContract()


#新建用户
def newUser(password):
    return web3.personal.newAccount(password)


#获取代币余额
def getBalance(address):
    if(web3.isAddress(address)):
        return  contract.functions.balanceOf(address).call()
    else:
        print("地址无效")


#普通转账
def transfer(_from, to, _value, fromPassword):
    if(getBalance(_from)<_value):
        print("数量不足，不能转")
    else:
        unlockResult=web3.personal.unlockAccount(_from, fromPassword)
        if(unlockResult):
            print("解锁成功")
            transctresult=contract.functions.transfer(to, _value).transact({'from':_from})
            web3.personal.lockAccount(_from)
            if(transctresult):
                print(web3.toHex(transctresult))


#卖家托管币给平台
def sendToUs(sellerAddress, sellerPassword, ourAddress, coinAmount):
    if(getBalance(sellerAddress)<coinAmount):
        print("您的代币余额不足")
    if(getEthBalance(sellerAddress)<sendToUsEstimate(sellerAddress,coinAmount)):
        print("账户手续费不足")

    unlockResult = web3.personal.unlockAccount(sellerAddress, sellerPassword)
    if (unlockResult):
        print("解锁成功")
        sendResult=contract.functions.approve(ourAddress,coinAmount).transact({'from':sellerAddress})
        if(sendResult):
            print("托管结果" + web3.toHex(sendResult))
            approveAmount = contract.functions.approve(ourAddress, coinAmount).estimateGas({'from': sellerAddress})
            sendToBuyerAmount = int(3 * approveAmount / 2)
            sendToUsAmount = int(0.1 * (approveAmount + sendToBuyerAmount))
            sendEthToUsResult=web3.eth.sendTransaction({'from':sellerAddress,'to':ourAddress,'value':sendToUsAmount+sendToBuyerAmount})
            if(sendEthToUsResult):
                print("卖家发送eth给平台成功"+web3.toHex(sendEthToUsResult))
                web3.personal.lockAccount(sellerAddress)


def sendToBuyer(sellerAddress, buyerAddress, ourAddress, coinAmount, ourPassword):
    unlockResult = web3.personal.unlockAccount(ourAddress,ourPassword)
    if(unlockResult):
        sendToBuyerResult=contract.functions.transferFrom(sellerAddress, buyerAddress, coinAmount).transact({'from':ourAddress})
        web3.personal.lockAccount(ourAddress)
        if(sendToBuyerResult):
            print("转给买家交易发起 hash值是"+web3.toHex(sendToBuyerResult))
        else:
            print("转给买家交易发起失败，原因是"+sendToBuyerResult)
    else:
        print("解锁失败")


#获取账户的eth余额
def getEthBalance(address):
    return web3.eth.getBalance(address)


#卖家托管给平台预估手续费
def sendToUsEstimate(sellerAddress,amount):
    approveAmount=contract.functions.approve(ourAddress,amount).estimateGas({'from':sellerAddress})
    sendToBuyerAmount=int(3*approveAmount/2)
    sendToUsAmount = int(0.1 * (approveAmount + sendToBuyerAmount))
    sendToUsGasAmount=web3.eth.estimateGas({'from':sellerAddress,'to':ourAddress,'value':sendToUsAmount+sendToBuyerAmount})
    amountAll = approveAmount + sendToBuyerAmount + sendToUsAmount + sendToUsGasAmount
    return amountAll



def seeAmount(owner, user): # 查看owner允许user使用的数量
    return contract.functions.allowance(owner, user).call()


def importAccountByPrivateKey(privateKey,passphrase):
    importResult=web3.personal.importRawKey(privateKey, passphrase)
    if(importResult):
        print("导入成功，地址是"+str(importResult))
    else:
        print(importResult)

#普通转币需要的手续费
def transferCoinGas(_from,to,amount):
    gas=contract.functions.transfer(to,amount).estimateGas({'from':_from})
    return gas


#托管
#sendToUs(sellerAddress,sellerPassword,ourAddress,1000000)

#转给买家
#sendToBuyer(sellerAddress, buyerAddress, ourAddress, 1000000, ourPassword)

#查询买家代币余额
#print(getBalance(buyerAddress))

#查询卖家代币余额
#print(getBalance(buyerAddress))

#查询卖家账户以太币余额
#print(getEthBalance(sellerAddress))

#卖家需要支付的手续费,参数和卖家托管的一样
#print(sendToUsEstimate(sellerAddress,820))

#通过私钥导入,相当于修改密码了，新密码是后面输入的domore,导入的前提是该账户的keyJosn不在本地,下面这个私钥是seller的，密码随便写，不过以后就是这个密码了
#importAccountByPrivateKey("c5010a3b675f9385f7dffb27678f1c61a34c931b3b7c16c00a6fab49f04871f8","domore")

#普通转币需要的手续费
#print(transferCoinGas(sellerAddress,buyerAddress,1000))

#print(sendToUsEstimate(sellerAddress,1000000))

