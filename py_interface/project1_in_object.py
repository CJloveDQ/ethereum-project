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
        self.contract=self.getContract()
    # 获得合约(这个不用你掉)
    def getContract(self):
        contractAddress = self.web3.toChecksumAddress('0xe8fd9a6399c96a5c213f01998f30357cc25d5a79')
        abi = '[{"constant":false,"inputs":[{"name":"_spender","type":"address"},{"name":"_value","type":"uint256"}],"name":"approve","outputs":[{"name":"success","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_from","type":"address"},{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transferFrom","outputs":[{"name":"success","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"}],"name":"balanceOf","outputs":[{"name":"balance","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transfer","outputs":[{"name":"success","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"},{"name":"_spender","type":"address"}],"name":"allowance","outputs":[{"name":"remaining","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_from","type":"address"},{"indexed":true,"name":"_to","type":"address"},{"indexed":false,"name":"_value","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_owner","type":"address"},{"indexed":true,"name":"_spender","type":"address"},{"indexed":false,"name":"_value","type":"uint256"}],"name":"Approval","type":"event"}]'
        contract = self.web3.eth.contract(address=contractAddress, abi=abi)
        return contract

    # 卖家托管给平台预估手续费(这个不用你掉)
    def sendToUsEstimate(self,seller,amount):
        print(amount)
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
        address=rawAddress
        if (self.web3.isAddress(address)):
            return self.contract.functions.balanceOf(address).call()/(10**6)
        else:
            print("地址无效")

    # 卖家托管币给平台
    def sendToUs(self,seller, sellerPassword,Amount):
        sellerAddress=self.web3.toChecksumAddress(seller)
        hadSentToUs=self.contract.functions.allowance(sellerAddress,geth.ourAddress).call()
        coinAmount=hadSentToUs+int(Amount*10**6)
        if (int(self.getBalance(sellerAddress)*10**6) < coinAmount):
            print("卖家代币余额不足")
            return
        if (int(self.getEthBalance(sellerAddress)*10**18) < self.sendToUsEstimate(sellerAddress, coinAmount)):
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
        else:
             print("密码错误")


    #转给买家
    def sendToBuyer(self,seller, buyer,Amount):
        coinAmount=int(Amount*10**6)
        buyerAddress=self.web3.toChecksumAddress(buyer)
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

    # 转到投资账户
    def transfer(self, From, _to,value, fromPassword):
        _value=int(value*10**6)
        _from=self.web3.toChecksumAddress(From)
        to=self.web3.toChecksumAddress(_to)
        if (self.getBalance(_from) < _value):
            print("数量不足，不能转")
        else:
            unlockResult = self.web3.personal.unlockAccount(_from, fromPassword)
            if (unlockResult):
                print("解锁成功")
                transctresult = self.contract.functions.transfer(to, _value).transact({'from': _from})
                self.web3.personal.lockAccount(_from)
                if (transctresult):
                    print(self.web3.toHex(transctresult))
            else:
                print("密码错误")

    # 获取账户的eth余额
    def getEthBalance(self,rawAddress):
        address=self.web3.toChecksumAddress(rawAddress)
        return self.web3.eth.getBalance(address)/(10**18)

    def getMaxCanSendTUs(self,address):
        sellerAddress = self.web3.toChecksumAddress(address)
        hadSentToUs = self.contract.functions.allowance(sellerAddress, geth.ourAddress).call()
        coinBalance=(int(self.getBalance(sellerAddress)*10**6)-hadSentToUs)/(10**6)
        return coinBalance


if __name__ =="__main__":
    geth = GethUtil()
    sellerAddress = geth.web3.toChecksumAddress("0xe12fd247cd56347ece998784b013d060adc6ad69")
    buyerAddress = "0xCFeE21Ebb1410F6664f5eB0b52E528b782b5dC28"
    sellerPassword = "domore"
    #新建账户
    #print(geth.newUser("1231312321"))
    #获取代币余额
    #print(geth.getBalance(geth.ourAddress))
    #获取eth余额
    #print(geth.getEthBalance(geth.ourAddress))
    #卖家托管1个nsrc给平台
    #geth.sendToUs(sellerAddress,sellerPassword,0.1)
    #转给买家（注意托管给平台成功后再调用发送给买家，看是否上一步成功在https://rinkeby.etherscan.io/tx/0x0b20860a25e7fbc30bbd2d33f30214e28c46c2d8e834640efe12e03827a7516c，右上角输入上个函数输出的的hash值）
    #geth.sendToBuyer(sellerAddress, buyerAddress,0.1)
    # print(geth.getBalance(buyerAddress))
    # #转一个币
    #geth.transfer(geth.ourAddress,"0xC08E04719ADCdA6594C58057dBcF2Cc6c9DcDBB7",0.1,geth.ourPassword)
    # contract=geth.getContract()
    # print(contract.functions.allowance(sellerAddress,geth.ourAddress).call())
    # print(geth.getMaxCanSendTUs(sellerAddress))
    # print(geth.getBalance(sellerAddress))
