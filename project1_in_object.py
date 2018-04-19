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

    # 获得合约(这个不用你掉)
    def getContract(self):
        contractAddress = self.web3.toChecksumAddress('0xe8fd9a6399c96a5c213f01998f30357cc25d5a79')
        abi = '[{"constant":false,"inputs":[{"name":"_spender","type":"address"},{"name":"_value","type":"uint256"}],"name":"approve","outputs":[{"name":"success","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_from","type":"address"},{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transferFrom","outputs":[{"name":"success","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"}],"name":"balanceOf","outputs":[{"name":"balance","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transfer","outputs":[{"name":"success","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"},{"name":"_spender","type":"address"}],"name":"allowance","outputs":[{"name":"remaining","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_from","type":"address"},{"indexed":true,"name":"_to","type":"address"},{"indexed":false,"name":"_value","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_owner","type":"address"},{"indexed":true,"name":"_spender","type":"address"},{"indexed":false,"name":"_value","type":"uint256"}],"name":"Approval","type":"event"}]'
        contract = self.web3.eth.contract(address=contractAddress, abi=abi)
        return contract

    # 卖家托管给平台预估手续费(这个不用你掉)
    def sendToUsEstimate(self,sellerAddress, amount):
        contract = self.getContract()
        approveAmount = contract.functions.approve(self.ourAddress, amount).estimateGas({'from': sellerAddress})
        sendToBuyerAmount = int(3 * approveAmount / 2)
        sendToUsAmount = int(0.1 * (approveAmount + sendToBuyerAmount))
        sendToUsGasAmount = self.web3.eth.estimateGas({'from': sellerAddress, 'to': self.ourAddress, 'value': sendToUsAmount + sendToBuyerAmount})
        amountAll = approveAmount + sendToBuyerAmount + sendToUsAmount + sendToUsGasAmount
        return amountAll

    # 新建用户
    def newUser(self,password):
        return self.web3.personal.newAccount(password)

    # 获取代币余额
    def getBalance(self,address):
        if (self.web3.isAddress(address)):
            contract = self.getContract()
            return contract.functions.balanceOf(address).call()
        else:
            print("地址无效")

    # 卖家托管币给平台
    def sendToUs(self,sellerAddress, sellerPassword,coinAmount):
        contract = self.getContract()
        if (self.getBalance(sellerAddress) < coinAmount):
            print("卖家代币余额不足")
        if (self.getEthBalance(sellerAddress) < self.sendToUsEstimate(sellerAddress, coinAmount)):
            print("卖家账户手续费不足")

        unlockResult = self.web3.personal.unlockAccount(sellerAddress, sellerPassword)
        if (unlockResult):
            print("解锁卖家账户成功")
            sendResult = contract.functions.approve(self.ourAddress, coinAmount).transact({'from': sellerAddress})
            if (sendResult):
                print("托管给平台交易发起" + self.web3.toHex(sendResult))
                approveAmount = contract.functions.approve(self.ourAddress, coinAmount).estimateGas({'from': sellerAddress})
                sendToBuyerAmount = int(3 * approveAmount / 2)
                sendToUsAmount = int(0.1 * (approveAmount + sendToBuyerAmount))
                sendEthToUsResult = self.web3.eth.sendTransaction(
                    {'from': sellerAddress, 'to': self.ourAddress, 'value': sendToUsAmount + sendToBuyerAmount})
                if (sendEthToUsResult):
                    self.web3.personal.lockAccount(sellerAddress)
    #转给买家
    def sendToBuyer(self,sellerAddress, buyerAddress,coinAmount):
        contract = self.getContract()
        if coinAmount>contract.functions.allowance(sellerAddress,self.ourAddress).call():
            print("卖家托管的币不足")
            return
        unlockResult = self.web3.personal.unlockAccount(self.ourAddress, self.ourPassword)
        if (unlockResult):
            sendToBuyerResult = contract.functions.transferFrom(sellerAddress, buyerAddress, coinAmount).transact({'from': self.ourAddress})
            self.web3.personal.lockAccount(self.ourAddress)
            if (sendToBuyerResult):
                print("转给买家交易发起 hash值是" + self.web3.toHex(sendToBuyerResult))
            else:
                print("转给买家交易发起失败，原因是" + sendToBuyerResult)
        else:
            print("解锁失败")

    # 获取账户的eth余额
    def getEthBalance(self,address):
        contract = self.getContract()
        return self.web3.eth.getBalance(address)

if __name__ =="__main__":
    geth = GethUtil()
    sellerAddress = geth.web3.toChecksumAddress("0xe12fd247cd56347ece998784b013d060adc6ad69")
    buyerAddress = "0xCFeE21Ebb1410F6664f5eB0b52E528b782b5dC28"
    sellerPassword = "domore"
    #新建账户
    #print(geth.newUser("1231312321"))
    #获取代币余额
    print(geth.getBalance(geth.ourAddress))
    #获取eth余额
    print(geth.getEthBalance(geth.ourAddress))
    #卖家托管1个nsrc给平台
    geth.sendToUs(sellerAddress, sellerPassword,1*10**6)
    #转给买家（注意托管给平台成功后再调用发送给买家，看是否上一步成功在https://rinkeby.etherscan.io/tx/0x0b20860a25e7fbc30bbd2d33f30214e28c46c2d8e834640efe12e03827a7516c，右上角输入上个函数输出的的hash值）
    geth.sendToBuyer(sellerAddress, buyerAddress,1*10**6)
