var Web3 = require('web3'); //引包
var app = app || {
    contract: {},
    init: function() {
        web3 = new Web3(new Web3.providers.HttpProvider("http://202.182.113.86:8545"));
        if (web3.isConnected()) {
            return true;
        } else {
            return false;
        }
    },
    getContract: function() {
        var abi = [{ "constant": false, "inputs": [{ "name": "newSellPrice", "type": "uint256" }, { "name": "newBuyPrice", "type": "uint256" }], "name": "setPrices", "outputs": [], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": true, "inputs": [], "name": "name", "outputs": [{ "name": "", "type": "string" }], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": false, "inputs": [{ "name": "_spender", "type": "address" }, { "name": "_value", "type": "uint256" }], "name": "approve", "outputs": [{ "name": "success", "type": "bool" }], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": true, "inputs": [], "name": "totalSupply", "outputs": [{ "name": "", "type": "uint256" }], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": false, "inputs": [{ "name": "_from", "type": "address" }, { "name": "_to", "type": "address" }, { "name": "_value", "type": "uint256" }], "name": "transferFrom", "outputs": [{ "name": "success", "type": "bool" }], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": true, "inputs": [], "name": "decimals", "outputs": [{ "name": "", "type": "uint8" }], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": false, "inputs": [{ "name": "_value", "type": "uint256" }], "name": "burn", "outputs": [{ "name": "success", "type": "bool" }], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": true, "inputs": [], "name": "sellPrice", "outputs": [{ "name": "", "type": "uint256" }], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": true, "inputs": [{ "name": "", "type": "address" }], "name": "balanceOf", "outputs": [{ "name": "", "type": "uint256" }], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": false, "inputs": [{ "name": "target", "type": "address" }, { "name": "mintedAmount", "type": "uint256" }], "name": "mintToken", "outputs": [], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": false, "inputs": [{ "name": "_from", "type": "address" }, { "name": "_value", "type": "uint256" }], "name": "burnFrom", "outputs": [{ "name": "success", "type": "bool" }], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": true, "inputs": [], "name": "buyPrice", "outputs": [{ "name": "", "type": "uint256" }], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": true, "inputs": [], "name": "owner", "outputs": [{ "name": "", "type": "address" }], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": true, "inputs": [], "name": "symbol", "outputs": [{ "name": "", "type": "string" }], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": false, "inputs": [], "name": "buy", "outputs": [], "payable": true, "stateMutability": "payable", "type": "function" }, { "constant": false, "inputs": [{ "name": "_to", "type": "address" }, { "name": "_value", "type": "uint256" }], "name": "transfer", "outputs": [{ "name": "success", "type": "bool" }], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": true, "inputs": [{ "name": "", "type": "address" }], "name": "frozenAccount", "outputs": [{ "name": "", "type": "bool" }], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": false, "inputs": [{ "name": "_spender", "type": "address" }, { "name": "_value", "type": "uint256" }, { "name": "_extraData", "type": "bytes" }], "name": "approveAndCall", "outputs": [{ "name": "success", "type": "bool" }], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": true, "inputs": [{ "name": "", "type": "address" }, { "name": "", "type": "address" }], "name": "allowance", "outputs": [{ "name": "", "type": "uint256" }], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": false, "inputs": [{ "name": "amount", "type": "uint256" }], "name": "sell", "outputs": [], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": false, "inputs": [{ "name": "target", "type": "address" }, { "name": "freeze", "type": "bool" }], "name": "freezeAccount", "outputs": [], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": false, "inputs": [{ "name": "newOwner", "type": "address" }], "name": "transferOwnership", "outputs": [], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "inputs": [{ "name": "initialSupply", "type": "uint256" }, { "name": "tokenName", "type": "string" }, { "name": "tokenSymbol", "type": "string" }], "payable": false, "stateMutability": "nonpayable", "type": "constructor" }, { "anonymous": false, "inputs": [{ "indexed": false, "name": "target", "type": "address" }, { "indexed": false, "name": "frozen", "type": "bool" }], "name": "FrozenFunds", "type": "event" }, { "anonymous": false, "inputs": [{ "indexed": true, "name": "from", "type": "address" }, { "indexed": true, "name": "to", "type": "address" }, { "indexed": false, "name": "value", "type": "uint256" }], "name": "Transfer", "type": "event" }, { "anonymous": false, "inputs": [{ "indexed": true, "name": "_owner", "type": "address" }, { "indexed": true, "name": "_spender", "type": "address" }, { "indexed": false, "name": "_value", "type": "uint256" }], "name": "Approval", "type": "event" }, { "anonymous": false, "inputs": [{ "indexed": true, "name": "from", "type": "address" }, { "indexed": false, "name": "value", "type": "uint256" }], "name": "Burn", "type": "event" }];
        //console.log(JSON.stringify(abi));
        var contract = web3.eth.contract(abi).at('0x5ED7eC1dE29954bf12052D69D63c8C67DfcEdB78');
        return contract;
    },
    importAccountByPrivateKey: function(key, newPassword) {
        web3.personal.importRawKey(key, callback, function(error, data) {
            if (!error) {
                return true;
            } else {
                return false;
            }
        });
    },
    transfer: function(from, to, _value, fromPassword) {
        web3.personal.unlockAccount(from, fromPassword, function(error, result) {
            if (!error) {
                app.getContract().transfer.sendTransaction(to, _value, { from: from }, function(error, data) {
                    if (!error) {
                        alert("交易发起成功，hash值是"+data);
                        app.lockAccount(from);
                        return true;
                    }
                    else
                    {
                        return false;
                    }
                })
            } else {
                return false;
            }
        });
    },
    getBalance: function(address) {
        if (!app.isAddress(address)) {
            console.log("地址无效");
            return false;
        }
        return web3.toDecimal(app.getContract().balanceOf.call(address));
    },
    lockAccount: function(account) {
        if (!app.isAddress(account)) {
            return;
        } else {
            web3.personal.lockAccount(account, function(error, data) {
                if (!error) {
                    console.log("锁定" + account + "成功");
                } else {
                    console.log("锁定" + account + "失败,原因是" + error);
                }
            })
        }
    },
    isAddress: function(address) {
        if (web3.isAddress(address)) {
            return true;
        } else {
            return false;
        }
    }
};


//控制代码

$(document).ready(
    function() {
        var from = "0x18f3a6fbdd28a0488230925c3d4390f8450b7ce5"; //账户地址
        var fromPassword = 'test'
        if (app.init()) {
            console.log("连接成功")
        } else {
            console.log("连接失败");
        }

        //监听提交按钮
        $('#button').click(function() {
            var to = $('#address').val();
            //判断to是不是合法地址
            if (!app.isAddress(to)) {
                alert("无效地址")
            } else {
                var amount = $('#amount').val();
                app.transfer(from, to, amount, fromPassword);
                //查询到交易成功之后调用这个方法查询余额
                console.log("收款账户余额是" + app.getBalance(to));
            }

            
        });
    }
);