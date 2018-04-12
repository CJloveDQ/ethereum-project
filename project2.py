from web3 import Web3, HTTPProvider
from web3.middleware import geth_poa_middleware
web3 = Web3(HTTPProvider('http://localhost:8545'))
web3.middleware_stack.inject(geth_poa_middleware, layer=0)
ourAddress = web3.toChecksumAddress("0x05A94caaCdb83e8B9E0b9a582988de448440ECc1")
ourPassword = "domore0325"
sellerAddress = web3.toChecksumAddress("0xe12fd247cd56347ece998784b013d060adc6ad69")
contractAddress = web3.toChecksumAddress('0x0008838B88CDFD659EA06cb51Cf32DA22eEd6518')
sellerPassword = "domore"
#下面这两个地址是用来测试的，你自己新建账户测试
transferTo="0xC74f777fad969f3e571f99fB6747418E4077A46C"
buyerAddress="0x624d40D9DE5bB3deb07E25f4B0dBba5e610d3569"
buyerPassword="domore0325"
#投资账户
investAccount="0xC9b9f95f36841Cd0f1568Cd1E7A4a425c853B56D"
maxInvestAmount={};
maxInvestAmount[buyerAddress]=10;
#获得合约
def getContract():
    abi='[ { "constant": false, "inputs": [ { "name": "newSellPrice", "type": "uint256" }, { "name": "newBuyPrice", "type": "uint256" } ], "name": "setPrices", "outputs": [], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": true, "inputs": [], "name": "name", "outputs": [ { "name": "", "type": "string", "value": "hash" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": false, "inputs": [ { "name": "_spender", "type": "address" }, { "name": "_value", "type": "uint256" } ], "name": "approve", "outputs": [ { "name": "success", "type": "bool" } ], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": true, "inputs": [], "name": "totalSupply", "outputs": [ { "name": "", "type": "uint256", "value": "1e+25" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": false, "inputs": [ { "name": "_to", "type": "address" }, { "name": "_value", "type": "uint256" } ], "name": "transferlockedAmount", "outputs": [], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": false, "inputs": [ { "name": "_from", "type": "address" }, { "name": "_to", "type": "address" }, { "name": "_value", "type": "uint256" } ], "name": "transferFrom", "outputs": [ { "name": "success", "type": "bool" } ], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": true, "inputs": [], "name": "decimals", "outputs": [ { "name": "", "type": "uint8", "value": "18" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": true, "inputs": [ { "name": "", "type": "address" }, { "name": "", "type": "uint256" } ], "name": "investDetails", "outputs": [ { "name": "investAmount", "type": "uint256", "value": "0" }, { "name": "lockTime", "type": "uint256", "value": "0" }, { "name": "investTime", "type": "uint256", "value": "0" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": false, "inputs": [ { "name": "target", "type": "address" }, { "name": "amount", "type": "uint256" } ], "name": "ownerUnlock", "outputs": [ { "name": "res", "type": "bool" } ], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": false, "inputs": [ { "name": "_value", "type": "uint256" } ], "name": "burn", "outputs": [ { "name": "success", "type": "bool" } ], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": true, "inputs": [], "name": "sellPrice", "outputs": [ { "name": "", "type": "uint256", "value": "0" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": false, "inputs": [ { "name": "user", "type": "address" }, { "name": "amount", "type": "uint256" } ], "name": "award", "outputs": [], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": true, "inputs": [ { "name": "", "type": "address" } ], "name": "balanceOf", "outputs": [ { "name": "", "type": "uint256", "value": "0" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": false, "inputs": [ { "name": "_recivers", "type": "address[]" }, { "name": "_values", "type": "uint256[]" } ], "name": "transferMultiAddress", "outputs": [], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": false, "inputs": [ { "name": "target", "type": "address" }, { "name": "mintedAmount", "type": "uint256" } ], "name": "mintToken", "outputs": [], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": false, "inputs": [ { "name": "_from", "type": "address" }, { "name": "_value", "type": "uint256" } ], "name": "burnFrom", "outputs": [ { "name": "success", "type": "bool" } ], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": true, "inputs": [], "name": "needLockPeriod", "outputs": [ { "name": "", "type": "uint256", "value": "7776000" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": true, "inputs": [ { "name": "", "type": "address" } ], "name": "investAccounts", "outputs": [ { "name": "", "type": "address", "value": "0x0000000000000000000000000000000000000000" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": false, "inputs": [ { "name": "target", "type": "address" }, { "name": "lockAmount", "type": "uint256" }, { "name": "lockPeriod", "type": "uint256" } ], "name": "lockToken", "outputs": [ { "name": "res", "type": "bool" } ], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": true, "inputs": [], "name": "buyPrice", "outputs": [ { "name": "", "type": "uint256", "value": "0" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": true, "inputs": [], "name": "owner", "outputs": [ { "name": "", "type": "address", "value": "0x05a94caacdb83e8b9e0b9a582988de448440ecc1" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": true, "inputs": [], "name": "symbol", "outputs": [ { "name": "", "type": "string", "value": "HsP" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": false, "inputs": [ { "name": "violator", "type": "address" }, { "name": "victim", "type": "address" }, { "name": "amount", "type": "uint256" } ], "name": "punish", "outputs": [], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": false, "inputs": [ { "name": "newTokenName", "type": "string" }, { "name": "newSymbolName", "type": "string" } ], "name": "rename", "outputs": [], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": true, "inputs": [ { "name": "", "type": "address" } ], "name": "lockedAmount", "outputs": [ { "name": "", "type": "uint256", "value": "0" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": false, "inputs": [], "name": "buy", "outputs": [], "payable": true, "stateMutability": "payable", "type": "function" }, { "constant": false, "inputs": [ { "name": "_to", "type": "address" }, { "name": "_value", "type": "uint256" } ], "name": "transfer", "outputs": [], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": true, "inputs": [ { "name": "", "type": "address" } ], "name": "frozenAccount", "outputs": [ { "name": "", "type": "bool", "value": false } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": false, "inputs": [ { "name": "newNeedLoackAmount", "type": "uint256" } ], "name": "changeLockPeriod", "outputs": [], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": false, "inputs": [ { "name": "_spender", "type": "address" }, { "name": "_value", "type": "uint256" }, { "name": "_extraData", "type": "bytes" } ], "name": "approveAndCall", "outputs": [ { "name": "success", "type": "bool" } ], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": false, "inputs": [ { "name": "activeAccount", "type": "address" }, { "name": "investAccount", "type": "address" } ], "name": "bind", "outputs": [], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": true, "inputs": [ { "name": "", "type": "address" } ], "name": "activeAccounts", "outputs": [ { "name": "", "type": "address", "value": "0x0000000000000000000000000000000000000000" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": true, "inputs": [ { "name": "", "type": "address" }, { "name": "", "type": "address" } ], "name": "allowance", "outputs": [ { "name": "", "type": "uint256", "value": "0" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": false, "inputs": [ { "name": "amount", "type": "uint256" } ], "name": "sell", "outputs": [], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": false, "inputs": [ { "name": "target", "type": "address" }, { "name": "freeze", "type": "bool" } ], "name": "freezeAccount", "outputs": [], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": false, "inputs": [ { "name": "newOwner", "type": "address" } ], "name": "transferOwnership", "outputs": [], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "name": "initialSupply", "type": "uint256", "index": 0, "typeShort": "uint", "bits": "256", "displayName": "initial Supply", "template": "elements_input_uint", "value": "10000000" }, { "name": "tokenName", "type": "string", "index": 1, "typeShort": "string", "bits": "", "displayName": "token Name", "template": "elements_input_string", "value": "hash" }, { "name": "tokenSymbol", "type": "string", "index": 2, "typeShort": "string", "bits": "", "displayName": "token Symbol", "template": "elements_input_string", "value": "HsP" } ], "payable": false, "stateMutability": "nonpayable", "type": "constructor" }, { "payable": true, "stateMutability": "payable", "type": "fallback" }, { "anonymous": false, "inputs": [ { "indexed": false, "name": "target", "type": "address" }, { "indexed": false, "name": "amount", "type": "uint256" }, { "indexed": false, "name": "lockPeriod", "type": "uint256" } ], "name": "LockToken", "type": "event" }, { "anonymous": false, "inputs": [ { "indexed": false, "name": "from", "type": "address" }, { "indexed": false, "name": "to", "type": "address" }, { "indexed": false, "name": "value", "type": "uint256" } ], "name": "TransferlockedAmount", "type": "event" }, { "anonymous": false, "inputs": [ { "indexed": false, "name": "from", "type": "address" }, { "indexed": false, "name": "to", "type": "address" }, { "indexed": false, "name": "amount", "type": "uint256" } ], "name": "OwnerUnlock", "type": "event" }, { "anonymous": false, "inputs": [ { "indexed": false, "name": "target", "type": "address" }, { "indexed": false, "name": "frozen", "type": "bool" } ], "name": "FrozenFunds", "type": "event" }, { "anonymous": false, "inputs": [ { "indexed": false, "name": "activeAccount", "type": "address" }, { "indexed": false, "name": "investAccount", "type": "address" } ], "name": "Bind", "type": "event" }, { "anonymous": false, "inputs": [ { "indexed": true, "name": "from", "type": "address" }, { "indexed": true, "name": "to", "type": "address" }, { "indexed": false, "name": "value", "type": "uint256" } ], "name": "Transfer", "type": "event" }, { "anonymous": false, "inputs": [ { "indexed": true, "name": "from", "type": "address" }, { "indexed": false, "name": "value", "type": "uint256" } ], "name": "Burn", "type": "event" } ]'
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
                print("转账成功 hash值是"+str(web3.toHex(transctresult)))
                return 1


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
                maxInvestAmount[sellerAddress]+=coinAmount


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

#设置一个eth可以买多少个代币,一个eth买到的币等于10^18/buyprice
def setPrice(sellPrice,buyPrice):
    unlockResult=web3.personal.unlockAccount(ourAddress,ourPassword)
    if(unlockResult):
        setPriceResult=contract.functions.setPrices(sellPrice,buyPrice).transact({'from':ourAddress})
        if(setPriceResult):
            print("价格设置成功 hash值是"+web3.toHex(setPriceResult))
            web3.personal.lockAccount(ourAddress)


#计算买amount数量的币需要支付的儿eth，返回的值是eth数量
def needPayEthAmount(amount):
    sellPrice=contract.functions.buyPrice().call()
    return amount*sellPrice
def callback(error,data):
    if(not(error)):
        print(data)
        print("jfidfji")



#用户购买代币，也就是私募
def buyCoin(userAddress,userPassword,buyAmount):
    needGiveEthAmount=needPayEthAmount(buyAmount)
    if(getEthBalance(userAddress)<needPayEthAmount(buyAmount)):
        print("账户eth不足")
    else:
        unlockResult=web3.personal.unlockAccount(userAddress,userPassword)
        if(unlockResult):
            buyResult = contract.functions.buy().transact({'from':userAddress,'value':needGiveEthAmount})
            if(buyResult):
                print("购买交易发起成功 hash值是"+web3.toHex(buyResult))






#投资,第一个参数是想投资的账户地址，第二个是用户的投资账户，第三个是活动账户的密码，第四个是投资数量
def invest(activeAcount,activeAccountPassword,investAmount):
    #转账给投资账户
    investAccount=getBindInvestAccount(activeAcount)
    print(investAccount)
    if(int(investAccount,16)==0):
        print("您还没有绑定投资账户")
        return
    # if(getCanInvestMaxAmount(activeAcount)<investAmount):
    #     print("欲投资数量超出最大可投资数量，必须是私募来的hsp才可以投资")
    #     return
    else:
        unlockResult=web3.personal.unlockAccount(ourAddress,ourPassword)
        if(unlockResult):
            #冻结投资账户，7776000是90天
            investResult=contract.functions.lockToken(investAccount,investAmount,7776000).transact({'from':ourAddress})
            if(investResult):
                print("投资成功 hash值是"+str(web3.toHex(investResult)))
                web3.personal.lockAccount(ourAddress)


#三级分销里面的推荐奖，注意awardAmount是需要奖励的数量，以wei为单位
def award(userAddress,awardAmount):
    unlockResult=web3.personal.unlockAccount(ourAddress,ourPassword)
    if(unlockResult):
        awardResult=contract.functions.award(userAddress,awardAmount).transact({'from':ourAddress})
        if(awardResult):
            print("奖励交易发起 hash值是"+web3.toHex(awardResult))
            web3.personal.lockAccount(ourAddress)


#释放代币
def releaseCoin(investAddress,amount):
    unlockResult = web3.personal.unlockAccount(ourAddress, ourPassword)
    if (unlockResult):
        releaseResult=contract.functions.ownerUnlock(investAddress,amount).transact({'from':ourAddress})
        if(releaseResult):
            print("释放交易发起 hash值是"+web3.toHex(releaseResult))
            web3.personal.lockAccount(ourAddress)


#转移投资账户里面的代币给其他用户,必须判断to是一个投资账户
def transferInvestCoin(activeAccount,activeAccountPassword,to,transferAmount):
    investAccount=getBindInvestAccount(activeAccount)
    if(int(investAccount,16)==0):
        print("您的活动账户还没绑定投资账户，请先绑定")
        return
    if(getLockedAmount(investAccount)<transferAmount):
         print("投资账户代币余额不足")
         return
    if(getEthBalance(activeAccount)<transferlockCoinEstimateGas(activeAccount,to,transferAmount)):
        print("活动账户eth不足")
        return
    else:
         unlockResult = web3.personal.unlockAccount(activeAccount,activeAccountPassword)
         if (unlockResult):
            transferResult=contract.functions.transferlockedAmount(to,transferAmount).transact({'from':activeAccount})
            if(transferResult):
                 print("转移投资账户的币交易发起成功 hash值是"+web3.toHex(transferResult))
                 web3.personal.lockAccount(activeAccount)


#查看锁仓数量
def getLockedAmount(address):
    return contract.functions.lockedAmount(address).call()

def transferlockCoinEstimateGas(_from,to,amount):
    return contract.functions.transferlockedAmount(to,amount).estimateGas({'from':_from})

def bind(activeAccount,investAccount):
    if(not(activeAccount in maxInvestAmount)):#最大可投资数量设置为0
        print("没在")
        maxInvestAmount[activeAccount]=0
    unlockResult = web3.personal.unlockAccount(ourAddress, ourPassword)
    if (unlockResult):
        bindResult=contract.functions.bind(activeAccount,investAccount).transact({'from':ourAddress})
        if(bindResult):
            print("绑定活动账户"+activeAccount+"和投资账户"+investAccount+"交易发起成功  hash值是"+str(web3.toHex(bindResult)))
            web3.personal.lockAccount(ourAddress)

#查看活动账户绑定的投资账户
def getBindInvestAccount(activeAccount):
    return contract.functions.investAccounts(activeAccount).call()
    #return int(contract.functions.investAccounts(activeAccount).call(),16)

#查看投资账户绑定的活动账户
def getBindActiveAccount(investAccount):
    return contract.functions.activeAccounts(investAccount).call()

def getCanInvestMaxAmount(activeAccount):
    return maxInvestAmount[activeAccount]

#新建账户
#print(newUser("domore0325"))

#托管
#sendToUs(sellerAddress,sellerPassword,ourAddress,1000000)

#转给买家
#sendToBuyer(sellerAddress, buyerAddress, ourAddress, 1000000, ourPassword)
#print(getEthBalance(ourAddress))
#查询买家代币余额
#print(getBalance(buyerAddress))

#查询卖家代币余额
#print(getBalance(sellerAddress))

#查询卖家账户以太币余额
#print(getEthBalance(sellerAddress))

#卖家需要支付的手续费,参数和卖家托管的一
#print(sendToUsEstimate(sellerAddress,1000000))

#通过私钥导入,相当于修改密码了，新密码是后面输入的domore,导入的前提是该账户的keyJosn不在本地,下面这个私钥是seller的，密码随便写，不过以后就是这个密码了
#importAccountByPrivateKey("c5010a3b675f9385f7dffb27678f1c61a34c931b3b7c16c00a6fab49f04871f8","domore")

#普通转币需要的手续费
#print(transferCoinGas(sellerAddress,buyerAddress,1000))

#普通转币,转了1000给卖家，参数乘以十的十八次方
#transfer(ourAddress,sellerAddress,10*10**18,ourPassword)

#设置一个eth买10000000个币,0是卖给平台的价格，设置成0就好
#setPrice(0,100000000000)

#买1000个币需要支付的eth数量,把这个的呈现到前端界面
#print(str(needPayEthAmount(1000)/(10**18))+"eth")

#买币，首先用户得有足够的eth,而且合约得有这么多的数量
#print("合约代币数量是"+str(getBalance(contractAddress)/(10**18))+" hsp")
#合约币不够的话这样转，转10个给合约
transfer(ourAddress,contractAddress,100000*10**18,ourPassword)
#print("最大数量是"+str(maxInvestAmount[buyerAddress]))
#buyCoin(buyerAddress,buyerPassword,1000)


#投资10个
#invest(buyerAddress,buyerPassword,10*10**18)
print("活动账户余额为"+str(getBalance(buyerAddress)/(10**18))+"hsp")
print("平台账户余额为"+str(getBalance(ourAddress)/(10**18))+"hsp")
print("投资账户被锁定余额是"+str(getLockedAmount(investAccount)/(10**18))+"hsp")
#奖励,我这里奖励investAccount 100wei个以太币，为了方便看余额，这里最好放一个以太币余额为0的账户
#award(investAccount,100)
#print("我获得的奖励是"+str(getEthBalance(investAccount))+"wei")

#释放投资账户的10个币，需要注意的是.是释放到投资账户的余额里面
#releaseCoin(investAccount,10*10**18)

#投资账户之间互转，注意得判断下接受的那个人的地址是不是一个投资账户,还得
#transferInvestCoin(buyerAddress,buyerPassword,ourAddress,10*10**18)


#绑定
#bind(buyerAddress,investAccount)
print(getEthBalance(investAccount))

