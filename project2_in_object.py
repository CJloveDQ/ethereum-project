# geth 操作工具
class GethUtil(object):
    def __init__(self):
        from web3 import Web3, HTTPProvider
        from web3.middleware import geth_poa_middleware
        self.web3 = Web3(HTTPProvider('http://localhost:8545'))
        self.web3.middleware_stack.inject(geth_poa_middleware, layer=0)
        assert self.web3.isConnected(),'connect fail'
        self.ourAddress = self.web3.toChecksumAddress("0x05A94caaCdb83e8B9E0b9a582988de448440ECc1")
        self.ourPassword = "domore0325"
        self.contractAddress = self.web3.toChecksumAddress('0xa35C16f796F0d7dd67fC80BE7E14A83Eb0942224')
        self.contract=self.getContract()

    # 获得合约(这个不用你掉)
    def getContract(self):
        abi ='[ { "constant": false, "inputs": [ { "name": "newSellPrice", "type": "uint256" }, { "name": "newBuyPrice", "type": "uint256" } ], "name": "setPrices", "outputs": [], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": true, "inputs": [], "name": "name", "outputs": [ { "name": "", "type": "string", "value": "yp" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": false, "inputs": [ { "name": "_spender", "type": "address" }, { "name": "_value", "type": "uint256" } ], "name": "approve", "outputs": [ { "name": "success", "type": "bool" } ], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": true, "inputs": [], "name": "totalSupply", "outputs": [ { "name": "", "type": "uint256", "value": "1e+25" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": false, "inputs": [ { "name": "_to", "type": "address" }, { "name": "_value", "type": "uint256" } ], "name": "transferlockedAmount", "outputs": [], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": false, "inputs": [ { "name": "_from", "type": "address" }, { "name": "_to", "type": "address" }, { "name": "_value", "type": "uint256" } ], "name": "transferFrom", "outputs": [ { "name": "success", "type": "bool" } ], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": true, "inputs": [], "name": "decimals", "outputs": [ { "name": "", "type": "uint8", "value": "18" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": true, "inputs": [ { "name": "", "type": "address" }, { "name": "", "type": "uint256" } ], "name": "investDetails", "outputs": [ { "name": "investAmount", "type": "uint256", "value": "0" }, { "name": "lockTime", "type": "uint256", "value": "0" }, { "name": "investTime", "type": "uint256", "value": "0" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": false, "inputs": [ { "name": "target", "type": "address" }, { "name": "amount", "type": "uint256" } ], "name": "ownerUnlock", "outputs": [ { "name": "res", "type": "bool" } ], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": false, "inputs": [ { "name": "_value", "type": "uint256" } ], "name": "burn", "outputs": [ { "name": "success", "type": "bool" } ], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": true, "inputs": [], "name": "sellPrice", "outputs": [ { "name": "", "type": "uint256", "value": "0" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": false, "inputs": [ { "name": "user", "type": "address" }, { "name": "amount", "type": "uint256" } ], "name": "award", "outputs": [], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": true, "inputs": [ { "name": "", "type": "address" } ], "name": "maxCanInvestAmount", "outputs": [ { "name": "", "type": "uint256", "value": "0" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": true, "inputs": [ { "name": "", "type": "address" } ], "name": "balanceOf", "outputs": [ { "name": "", "type": "uint256", "value": "9.7e+22" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": false, "inputs": [ { "name": "_recivers", "type": "address[]" }, { "name": "_values", "type": "uint256[]" } ], "name": "transferMultiAddress", "outputs": [], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": false, "inputs": [ { "name": "target", "type": "address" }, { "name": "mintedAmount", "type": "uint256" } ], "name": "mintToken", "outputs": [], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": false, "inputs": [ { "name": "_from", "type": "address" }, { "name": "_value", "type": "uint256" } ], "name": "burnFrom", "outputs": [ { "name": "success", "type": "bool" } ], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": true, "inputs": [], "name": "needLockPeriod", "outputs": [ { "name": "", "type": "uint256", "value": "7776000" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": true, "inputs": [ { "name": "", "type": "address" } ], "name": "investAccounts", "outputs": [ { "name": "", "type": "address", "value": "0x0000000000000000000000000000000000000000" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": false, "inputs": [ { "name": "target", "type": "address" }, { "name": "lockAmount", "type": "uint256" }, { "name": "lockPeriod", "type": "uint256" } ], "name": "lockToken", "outputs": [ { "name": "res", "type": "bool" } ], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": true, "inputs": [], "name": "buyPrice", "outputs": [ { "name": "", "type": "uint256", "value": "100000000000" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": true, "inputs": [], "name": "owner", "outputs": [ { "name": "", "type": "address", "value": "0x05a94caacdb83e8b9e0b9a582988de448440ecc1" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": true, "inputs": [], "name": "symbol", "outputs": [ { "name": "", "type": "string", "value": "HSPLAST" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": false, "inputs": [ { "name": "violator", "type": "address" }, { "name": "victim", "type": "address" }, { "name": "amount", "type": "uint256" } ], "name": "punish", "outputs": [], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": false, "inputs": [ { "name": "newTokenName", "type": "string" }, { "name": "newSymbolName", "type": "string" } ], "name": "rename", "outputs": [], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": true, "inputs": [ { "name": "", "type": "address" } ], "name": "lockedAmount", "outputs": [ { "name": "", "type": "uint256", "value": "0" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": false, "inputs": [], "name": "buy", "outputs": [], "payable": true, "stateMutability": "payable", "type": "function" }, { "constant": false, "inputs": [ { "name": "_to", "type": "address" }, { "name": "_value", "type": "uint256" } ], "name": "transfer", "outputs": [], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": true, "inputs": [ { "name": "", "type": "address" } ], "name": "frozenAccount", "outputs": [ { "name": "", "type": "bool", "value": false } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": false, "inputs": [ { "name": "newNeedLoackAmount", "type": "uint256" } ], "name": "changeLockPeriod", "outputs": [], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": false, "inputs": [ { "name": "_spender", "type": "address" }, { "name": "_value", "type": "uint256" }, { "name": "_extraData", "type": "bytes" } ], "name": "approveAndCall", "outputs": [ { "name": "success", "type": "bool" } ], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": false, "inputs": [ { "name": "activeAccount", "type": "address" }, { "name": "investAccount", "type": "address" } ], "name": "bind", "outputs": [], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": true, "inputs": [ { "name": "", "type": "address" } ], "name": "activeAccounts", "outputs": [ { "name": "", "type": "address", "value": "0x0000000000000000000000000000000000000000" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": true, "inputs": [ { "name": "", "type": "address" }, { "name": "", "type": "address" } ], "name": "allowance", "outputs": [ { "name": "", "type": "uint256", "value": "0" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": false, "inputs": [ { "name": "amount", "type": "uint256" } ], "name": "sell", "outputs": [], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": false, "inputs": [ { "name": "target", "type": "address" }, { "name": "freeze", "type": "bool" } ], "name": "freezeAccount", "outputs": [], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": false, "inputs": [ { "name": "newOwner", "type": "address" } ], "name": "transferOwnership", "outputs": [], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "name": "initialSupply", "type": "uint256", "index": 0, "typeShort": "uint", "bits": "256", "displayName": "initial Supply", "template": "elements_input_uint", "value": "10000000" }, { "name": "tokenName", "type": "string", "index": 1, "typeShort": "string", "bits": "", "displayName": "token Name", "template": "elements_input_string", "value": "yp" }, { "name": "tokenSymbol", "type": "string", "index": 2, "typeShort": "string", "bits": "", "displayName": "token Symbol", "template": "elements_input_string", "value": "HSPLAST" } ], "payable": false, "stateMutability": "nonpayable", "type": "constructor" }, { "payable": true, "stateMutability": "payable", "type": "fallback" }, { "anonymous": false, "inputs": [ { "indexed": false, "name": "target", "type": "address" }, { "indexed": false, "name": "amount", "type": "uint256" }, { "indexed": false, "name": "lockPeriod", "type": "uint256" } ], "name": "LockToken", "type": "event" }, { "anonymous": false, "inputs": [ { "indexed": false, "name": "from", "type": "address" }, { "indexed": false, "name": "to", "type": "address" }, { "indexed": false, "name": "value", "type": "uint256" } ], "name": "TransferlockedAmount", "type": "event" }, { "anonymous": false, "inputs": [ { "indexed": false, "name": "from", "type": "address" }, { "indexed": false, "name": "to", "type": "address" }, { "indexed": false, "name": "amount", "type": "uint256" } ], "name": "OwnerUnlock", "type": "event" }, { "anonymous": false, "inputs": [ { "indexed": false, "name": "target", "type": "address" }, { "indexed": false, "name": "frozen", "type": "bool" } ], "name": "FrozenFunds", "type": "event" }, { "anonymous": false, "inputs": [ { "indexed": false, "name": "activeAccount", "type": "address" }, { "indexed": false, "name": "investAccount", "type": "address" } ], "name": "Bind", "type": "event" }, { "anonymous": false, "inputs": [ { "indexed": true, "name": "from", "type": "address" }, { "indexed": true, "name": "to", "type": "address" }, { "indexed": false, "name": "value", "type": "uint256" } ], "name": "Transfer", "type": "event" }, { "anonymous": false, "inputs": [ { "indexed": true, "name": "from", "type": "address" }, { "indexed": false, "name": "value", "type": "uint256" } ], "name": "Burn", "type": "event" } ]'
        contract = self.web3.eth.contract(address=self.contractAddress, abi=abi)
        return contract

    # 卖家托管给平台预估手续费(这个不用你掉)
    def sendToUsEstimate(self,seller, amount):
        sellerAddress=self.web3.toChecksumAddress(seller)
        approveAmount = self.contract.functions.approve(self.ourAddress, amount).estimateGas({'from': sellerAddress})
        sendToBuyerAmount = int(3 * approveAmount / 2)
        sendToUsAmount = int(0.1 * (approveAmount + sendToBuyerAmount))
        sendToUsGasAmount = self.web3.eth.estimateGas({'from': sellerAddress, 'to': self.ourAddress, 'value': sendToUsAmount + sendToBuyerAmount})
        amountAll = approveAmount + sendToBuyerAmount + sendToUsAmount + sendToUsGasAmount
        return amountAll

    # 新建用户
    def newUser(self,password):
        return self.web3.personal.newAccount(password)

    # 获取代币余额
    def getBalance(self,rawAddress):
        address=self.web3.toChecksumAddress(rawAddress)
        if (self.web3.isAddress(address)):
            return self.contract.functions.balanceOf(address).call()
        else:
            print("地址无效")

    # 卖家托管币给平台
    def sendToUs(self,seller, sellerPassword,coinAmount):
        sellerAddress=self.web3.toChecksumAddress(seller)
        if (self.getBalance(sellerAddress) < coinAmount):
            print("卖家代币余额不足")
            return
        if (self.getEthBalance(sellerAddress) < self.sendToUsEstimate(sellerAddress, coinAmount)):
            print("卖家账户手续费不足")
            return
        unlockResult = self.web3.personal.unlockAccount(sellerAddress, sellerPassword)
        if (unlockResult):
            print("解锁卖家账户成功")
            sendResult = self.contract.functions.approve(self.ourAddress, coinAmount).transact({'from': sellerAddress})
            if (sendResult):
                print("托管给平台交易发起" + self.web3.toHex(sendResult))
                approveAmount = self.contract.functions.approve(self.ourAddress, coinAmount).estimateGas({'from': sellerAddress})
                sendToBuyerAmount = int(3 * approveAmount / 2)
                sendToUsAmount = int(0.1 * (approveAmount + sendToBuyerAmount))
                sendEthToUsResult = self.web3.eth.sendTransaction(
                    {'from': sellerAddress, 'to': self.ourAddress, 'value': sendToUsAmount + sendToBuyerAmount})
                if (sendEthToUsResult):
                    self.web3.personal.lockAccount(sellerAddress)
    #转给买家
    def sendToBuyer(self,seller, buyerAddress,coinAmount):
        sellerAddress=self.web3.toChecksumAddress(seller)
        if coinAmount>self.contract.functions.allowance(sellerAddress,self.ourAddress).call():
            print("卖家托管的币不足")
            return
        unlockResult = self.web3.personal.unlockAccount(self.ourAddress, self.ourPassword)
        if (unlockResult):
            sendToBuyerResult = self.contract.functions.transferFrom(sellerAddress, buyerAddress, coinAmount).transact({'from': self.ourAddress})
            self.web3.personal.lockAccount(self.ourAddress)
            if (sendToBuyerResult):
                print("转给买家交易发起 hash值是" + self.web3.toHex(sendToBuyerResult))
            else:
                print("转给买家交易发起失败，原因是" + sendToBuyerResult)
        else:
            print("解锁失败")

    # 获取账户的eth余额
    def getEthBalance(self,rawAddress):
        address=self.web3.toChecksumAddress(rawAddress)
        return self.web3.eth.getBalance(address)

    # 设置一个eth可以买多少个代币,一个eth买到的币等于10^18/buyprice
    def setPrice(self,sellPrice, buyPrice):
        unlockResult = self.web3.personal.unlockAccount(self.ourAddress, self.ourPassword)
        if (unlockResult):
            setPriceResult = self.contract.functions.setPrices(sellPrice, buyPrice).transact({'from': self.ourAddress})
            if (setPriceResult):
                print("价格设置成功 hash值是" + self.web3.toHex(setPriceResult))
                self.web3.personal.lockAccount(self.ourAddress)

    # 计算买amount数量的币需要支付的儿eth，返回的值是eth数量
    def needPayEthAmount(self,amount):
        sellPrice = self.contract.functions.buyPrice().call()
        return amount * sellPrice

    # 用户购买代币，也就是认购
    def buyCoin(self,rawUserAddress, userPassword, buyAmount):
        userAddress=self.web3.toChecksumAddress(rawUserAddress)
        needGiveEthAmount = self.needPayEthAmount(buyAmount)
        if (self.getEthBalance(userAddress) < self.needPayEthAmount(buyAmount) + self.buyOurCoinEstimate(userAddress, buyAmount)):
            print("账户eth不足")
        else:
            unlockResult = self.web3.personal.unlockAccount(userAddress, userPassword)
            if (unlockResult):
                buyResult = self.contract.functions.buy().transact({'from': userAddress, 'value': needGiveEthAmount})
                if (buyResult):
                    print("购买交易发起成功 hash值是" + self.web3.toHex(buyResult))

    # 投资,第一个参数是想投资的账户地址，第二个是活动账户的密码，第三个是投资数量
    def invest(self,rawActiveAccount,investAmount):
        activeAccount=self.web3.toChecksumAddress(rawActiveAccount)
        # 转账给投资账户
        investAccount = self.getBindInvestAccount(activeAccount)
        if (int(investAccount, 16) == 0):
            print("您还没有绑定投资账户")
            return
        if (self.getCanInvestMaxAmount(activeAccount) < investAmount):
            print("欲投资数量超出最大可投资数量，必须是私募来的hsp才可以投资")
            return
        else:
            unlockResult = self.web3.personal.unlockAccount(self.ourAddress, self.ourPassword)
            if (unlockResult):
                # 冻结投资账户，7776000是90天
                investResult = self.contract.functions.lockToken(activeAccount, investAmount, 7776000).transact({'from': self.ourAddress})
                if (investResult):
                    print("投资成功 hash值是" + str(self.web3.toHex(investResult)))
                    self.web3.personal.lockAccount(self.ourAddress)

    # 三级分销里面的推荐奖
    def award(self,userAddress, awardAmount):
        if(self.getEthBalance(self.contractAddress)<awardAmount):
            print("平台账户eth不足")
            return
        unlockResult = self.web3.personal.unlockAccount(self.ourAddress, self.ourPassword)
        if (unlockResult):
            awardResult = self.contract.functions.award(userAddress, awardAmount).transact({'from': self.ourAddress})
            if (awardResult):
                print("奖励交易发起 hash值是" + self.web3.toHex(awardResult))
                self.web3.personal.lockAccount(self.ourAddress)

    # 释放代币，参数是锁仓账户
    def releaseCoin(self,investAddress, amount):
        if(amount>self.contract.functions.lockedAmount(investAddress).call()):
            print("投资账户未被冻结如此多的数量")
            return
        unlockResult = self.web3.personal.unlockAccount(self.ourAddress, self.ourPassword)
        if (unlockResult):
            releaseResult = self.contract.functions.ownerUnlock(investAddress, amount).transact({'from': self.ourAddress})
            if (releaseResult):
                print("释放交易发起 hash值是" + self.web3.toHex(releaseResult))
                self.web3.personal.lockAccount(self.ourAddress)

    # 查看投资账户锁仓数量
    def getLockedAmount(self,investaddress):
        return self.contract.functions.lockedAmount(investaddress).call()


    # 绑定,重新绑定也可以
    def bind(self,activeAccount, investAccount):
        unlockResult = self.web3.personal.unlockAccount(self.ourAddress, self.ourPassword)
        if (unlockResult):
            bindResult = self.contract.functions.bind(activeAccount, investAccount).transact({'from': self.ourAddress})
            if (bindResult):
                print("绑定活动账户" + activeAccount + "和投资账户" + investAccount + "交易发起成功  hash值是" + str(self.web3.toHex(bindResult)))
                self.web3.personal.lockAccount(self.ourAddress)

    # 查看活动账户绑定的投资账户
    def getBindInvestAccount(self,activeAccount):
        return self.contract.functions.investAccounts(activeAccount).call()

    def getCanInvestMaxAmount(self,activeAccount):
        return self.contract.functions.maxCanInvestAmount(activeAccount).call()
    #认购计算手续费
    def buyOurCoinEstimate(self,rawBuyerAddress, buyAmount):
        buyerAddress=rawBuyerAddress
        return self.contract.functions.buy().estimateGas({'from': buyerAddress, 'value': self.needPayEthAmount(buyAmount)})
if __name__ =="__main__":
    geth = GethUtil()
    sellerAddress = geth.web3.toChecksumAddress("0xe12fd247cd56347ece998784b013d060adc6ad69")
    buyerAddress = "0xCFeE21Ebb1410F6664f5eB0b52E528b782b5dC28"
    sellerPassword = "domore"
    # 新建账户
    # print(geth.newUser("1231312321"))

    # 获取卖家余额
    #print(geth.getBalance(sellerAddress))

    # 获取eth余额
    #print(geth.getEthBalance(geth.ourAddress))

    # 卖家托管1个nsrc给平台
    #geth.sendToUs(sellerAddress, sellerPassword, 1 * 10 ** 18)

    # 转给买家（注意托管给平台成功后再调用发送给买家，看是否上一步成功在https://rinkeby.etherscan.io/tx/0x0b20860a25e7fbc30bbd2d33f30214e28c46c2d8e834640efe12e03827a7516c，右上角输入上个函数输出的的hash值）
    #geth.sendToBuyer(sellerAddress, buyerAddress, 1 * 10 ** 18)


    #======================================================================下面是第二个新加的==================
    # 投资账户，随便写的
    investAccount = "0xC9b9f95f36841Cd0f1568Cd1E7A4a425c853B56D"

    print("活动账户余额为" + str(geth.getBalance(sellerAddress) / (10 ** 18)) + "hsp")
    print("平台账户余额为" + str(geth.getBalance(geth.ourAddress) / (10 ** 18)) + "hsp")
    print("投资账户被锁定余额是" + str(geth.getLockedAmount(investAccount) / (10 ** 18)) + "hsp")
    print("最大可投资数量是" + str(geth.getCanInvestMaxAmount(sellerAddress) / 10 ** 18) + "hsp")
    # 买1000个币需要支付的eth数量(包括手续费),把这个的呈现到前端界面
    print("买1000个币需要支付的eth" + str((geth.needPayEthAmount(1000) + geth.buyOurCoinEstimate(buyerAddress, 1000)) / (10 ** 18)) + "eth")
    # 绑定
    #geth.bind(sellerAddress, investAccount)


    #设置一个eth买10000000个币,0是卖给平台的价格，设置成0就好(后台有个设置价格的按钮，按了之后把管理员输入的数量当作第二个参数传入就可以)
    #geth.setPrice(0,10000000)

    # 一期认购.认购1000个,认购最大可投资数量会增加
    geth.buyCoin(sellerAddress,sellerPassword,1000)


    # 投资10个(账户和密码是想参与认购的人的账户的)
    geth.invest(sellerAddress,10 * 10 ** 18)


    # 奖励,我这里奖励investAccount 100wei个以太币，为了方便看余额，第一个参数最好放一个以太币余额为0的账户,第一个参数是活动账户
    #geth.award(sellerAddress,100)


    # 释放投资账户的10个币
    geth.releaseCoin(investAccount,10*10**18)


    # 投资账户之间互转，得确认第三个参数是一个投资账户(这个先别急着加)
    # geth.transferInvestCoin(buyerAddress,buyerPassword,ourAddress,10*10**18)




