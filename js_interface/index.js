/*
 * @Author: YP
 * @Date:   2018-03-10 09:18:20
 * @Last Modified by:   YP
 * @Last Modified time: 2018-04-02 20:33:18
 */
//
var Web3 = require('web3'); //引包
web3 = new Web3(new Web3.providers.HttpProvider("http://localhost:9999"));
if (!web3.isConnected()) {

    console.log("failed");

} else {
    console.log("success");

}

ourAdress = "0x05A94caaCdb83e8B9E0b9a582988de448440ECc1";
ourPassword = "domore0325";
aim = "0xe3e755febbc288173293e0d2932ec57e288d4ed8";
sellerAddress = "0xe12fd247cd56347ece998784b013d060adc6ad69"; //你直接拿这个测试，不过得先导入，我发给你
sellerPassword = "domore0325";
newAccount = "0x7ddd721b11c9d939a6a711ff4d858c314c5ecfa5";

//买家地址你自己随便新建一个,
buyerAddress = "0x159475724cbe7ae7655c0d9d7b738cf2bcbe196c"; 
console.log(getContract());
console.log("卖家代币数量" + getBalance(newAccount));
console.log("买家代币数量" + getBalance(buyerAddress));
console.log("卖家eth数量" + getEthBalance(sellerAddress));
//下面这三个是我测试的时候用的，你可以试试
transfer(ourAdress,newAccount,100000,ourPassword);
//sendToUs(sellerAddress,sellerPassword,ourAdress,100);
//sendToBuyer(sellerAddress, buyerAddress, ourAdress, 90, ourPassword)
function estimateGasArguments(type, from, to, amount, other) //一个对象，估算手续费的时候用
{
    this.type = type;
    this.from = from; //规定手续费谁出
    this.to = to;
    this.amount = amount;
    this.other = other;
}
//普通转账预估手续费

//托管给平台预估手续费

function newUser(password) //传入一个密码，新建账户
{

    web3.personal.newAccount(password, function(error, data) {
        if (!error) {
            console.log("账户新建成功  地址是：" + data);
        } else {
            console.log("新建失败" + "原因是" + error);
        }
    });

}

function estimateGas(arguments) {
    var contract = getContract();
    var gasAmount;

    if (arguments.type == "commenTransfer" || arguments.type == "sendToUs") //用户之间转账
    {
        gasAmount = contract.transfer.estimateGas(arguments.to, arguments.amount, { from: arguments.from });
    }
    if (arguments.type == "sendToBuyer") {
        gasAmount = contract.transferFrom.estimateGas(arguments.other, arguments.to, arguments.amount, { from: arguments.from })
    }
    return gasAmount;
}

function importAccountByPrivateKey(key, callback) //通过私钥导入
{
    web3.personal.importRawKey(key, callback, function(error, data) {
        if (!error) {
            console.log("导入成功");
        } else {
            console.log("导入失败" + "原因是" + error);
        }
    });

}


function getBalance(address) //获得账户代币余额
{
    if (!isAddress(address)) {
        return;
    }

    return web3.toDecimal(getContract().balanceOf.call(address));
}


function getEthBalance(address) //获得eth余额
{
    if (!isAddress(address)) {
        return;
    }

    return web3.toDecimal(web3.eth.getBalance(address));
}




//卖家将币托管给平台
function sendToUs(sellerAddress, sellerPassword, ourAdress, coinAmount) {
    var gasAmount = estimateGas(new estimateGasArguments("sendToUs", "", ourAdress, coinAmount, ""));
    console.log("手续费是" + gasAmount);
    if (getEthBalance(sellerAddress) < gasAmount) {
        console.log("手续费不足");
        return;
    }

    if (isAddress(sellerAddress) && isAddress(ourAdress)) {
        web3.personal.unlockAccount(sellerAddress, sellerPassword, function(error, result) {
            if (!error) {
                console.log("解锁账户" + sellerAddress + "成功")
                sellerApprove(sellerAddress, ourAdress, coinAmount);
                return true;
            } else {
                console.log("解锁账户失败" + "原因是" + error);
            }
        });

    } else {
        return;
    }


}



//平台给买家转币
function sendToBuyer(sellerAddress, buyerAddress, ourAdress, coinAmount, ourPassword) {
    var gasAmount = estimateGas(new estimateGasArguments("sendToBuyer", ourAdress, buyerAddress, coinAmount, sellerAddress));
    if (getEthBalance(ourAdress) < gasAmount) {
        console.log("平台手续费不足");
        return;
    }
    console.log("手续费是" + gasAmount);
    if (!(isAddress(sellerAddress) && isAddress(ourAdress))) {
        console.log("无效地址");
        return;
    }
    web3.personal.unlockAccount(ourAdress, ourPassword, function(error, data) {
        if (!error) {
            getContract().transferFrom.sendTransaction(sellerAddress, buyerAddress, coinAmount, { from: ourAdress }, function(error, data) {
                if (!error) {
                    console.log("转给买家成功" + "  hash值是" + data);
                    lockAccount(ourAdress);
                } else {
                    console.log("转给买家失败" + "原因是" + error);
                }
            });
        }
    }); //from是一个对象声明手续费谁出

}

//从from转给to数量为value的币,fromPassword是from账户的密码
function transfer(from, to, _value, fromPassword) {
    var gasAmount = estimateGas(new estimateGasArguments("commenTransfer", from, to, _value, ""));
    console.log("手续费是" + gasAmount);
    if (getEthBalance(from) < gasAmount) {
        console.log("手续费不足");
        return;
    }
    if (!(isAddress(from) && isAddress(to))) {
        return;
    }
    if (getBalance(from) < _value) {
        return;
    }
    web3.personal.unlockAccount(from, fromPassword, function(error, result) {
        if (!error) {
            console.log("解锁账户" + from + "成功")
            sendTransaction(to, _value, from);
            return true;
        } else {
            console.log("解锁账户失败" + "原因是" + error);
        }
    });

}

function lockAccount(account) {
    if (!isAddress(account)) {
        return;
    } else {
        web3.personal.lockAccount(account, function(error, data) {
            if (!error) {
                console.log("锁定"+account+"成功");
            } else {
                console.log("锁定"+account+"失败,原因是" + error);
            }
        })
    }
}
//以下函数可以不看
function seeAmount(owner, user) //查看owner允许user使用的数量
{
    return web3.toDecimal(getContract().allowance.call(owner, user));
}




function sellerApprove(sellerAddress, ourAdress, coinAmount) {
    if (!(isAddress(sellerAddress) && isAddress(ourAdress))) {
        return;
    }
    getContract().approve.sendTransaction(ourAdress, coinAmount, { from: sellerAddress }, function(error, data) {
        if (!error) {
            console.log(error);
            console.log(sellerAddress + "将币托管给平台" + "hash值是" + data);
            lockAccount(sellerAddress);
        } else {
            console.log("托管失败" + "原因是" + error);
        }
    });
}

function sendTransaction(to, _value, from) //普通转账
{
    if (!(isAddress(to) && isAddress(from))) {
        return;
    }
    getContract().transfer.sendTransaction(to, _value, { from: from }, function(error, data) {
        if (!error) {
            console.log(from + "  转账给  " + to + "  交易发起" + "交易hash值是" + data);
            lockAccount(from);

        } else {
            console.log(from + "  转账给  " + to + "  交易发起失败" + "原因是" + error);
        }
    });
}


function unlockAccount(account, password) //account是发起交易的账户
{
    web3.personal.unlockAccount(account, password, function(error, result) {
        if (!error) {
            console.log("解锁账户" + account + "成功")
            return true;
        } else {
            console.log("解锁账户失败" + "原因是" + error);
        }
    });
}

function isAddress(address) {
    if (web3.isAddress(address)) {
        return true;
    } else {
        console.log("无效地址");
        return false;
    }
}

function getContract() {
    var abi = [{
            "constant": false,
            "inputs": [{
                    "name": "_spender",
                    "type": "address"
                },
                {
                    "name": "_value",
                    "type": "uint256"
                }
            ],
            "name": "approve",
            "outputs": [{
                "name": "success",
                "type": "bool"
            }],
            "payable": false,
            "stateMutability": "nonpayable",
            "type": "function"
        },
        {
            "constant": true,
            "inputs": [],
            "name": "totalSupply",
            "outputs": [{
                "name": "",
                "type": "uint256"
            }],
            "payable": false,
            "stateMutability": "view",
            "type": "function"
        },
        {
            "constant": false,
            "inputs": [{
                    "name": "_from",
                    "type": "address"
                },
                {
                    "name": "_to",
                    "type": "address"
                },
                {
                    "name": "_value",
                    "type": "uint256"
                }
            ],
            "name": "transferFrom",
            "outputs": [{
                "name": "success",
                "type": "bool"
            }],
            "payable": false,
            "stateMutability": "nonpayable",
            "type": "function"
        },
        {
            "constant": true,
            "inputs": [{
                "name": "_owner",
                "type": "address"
            }],
            "name": "balanceOf",
            "outputs": [{
                "name": "balance",
                "type": "uint256"
            }],
            "payable": false,
            "stateMutability": "view",
            "type": "function"
        },
        {
            "constant": false,
            "inputs": [{
                    "name": "_to",
                    "type": "address"
                },
                {
                    "name": "_value",
                    "type": "uint256"
                }
            ],
            "name": "transfer",
            "outputs": [{
                "name": "success",
                "type": "bool"
            }],
            "payable": false,
            "stateMutability": "nonpayable",
            "type": "function"
        },
        {
            "constant": true,
            "inputs": [{
                    "name": "_owner",
                    "type": "address"
                },
                {
                    "name": "_spender",
                    "type": "address"
                }
            ],
            "name": "allowance",
            "outputs": [{
                "name": "remaining",
                "type": "uint256"
            }],
            "payable": false,
            "stateMutability": "view",
            "type": "function"
        },
        {
            "anonymous": false,
            "inputs": [{
                    "indexed": true,
                    "name": "_from",
                    "type": "address"
                },
                {
                    "indexed": true,
                    "name": "_to",
                    "type": "address"
                },
                {
                    "indexed": false,
                    "name": "_value",
                    "type": "uint256"
                }
            ],
            "name": "Transfer",
            "type": "event"
        },
        {
            "anonymous": false,
            "inputs": [{
                    "indexed": true,
                    "name": "_owner",
                    "type": "address"
                },
                {
                    "indexed": true,
                    "name": "_spender",
                    "type": "address"
                },
                {
                    "indexed": false,
                    "name": "_value",
                    "type": "uint256"
                }
            ],
            "name": "Approval",
            "type": "event"
        }
    ];
    // var abik=JSON.stringify(abi);
    //  console.log(abik);
    var contractAddress = "0xe8fd9a6399c96a5c213f01998f30357cc25d5a79"; //合约地址
    var contract = web3.eth.contract(abi).at(contractAddress);
    return contract;
}