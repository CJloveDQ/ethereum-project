/*
 * @Author: YP
 * @Date:   2018-03-10 09:18:20
 * @Last Modified by:   YP
 * @Last Modified time: 2018-05-07 12:55:26
 */
//
var Web3 = require('web3'); //引包
myWeb3 = new Web3(window.web3.currentProvider); 
// web3 = new Web3(new Web3.providers.HttpProvider("http://localhost:8545"));
if (!myWeb3.isConnected()) {

    console.log("failed");

} else {
    console.log("success");

}

    // the default account doesn't seem to be persisted, copy it to our
    // new instance
   // myWeb3.eth.defaultAccount = window.web3.eth.defaultAccount;
    console.log(myWeb3.eth.accounts[0]);
// var hash = '0xe968db41771b91e0e074eb1c7915359be33206dd6ef1424df55f1f0dd9c0927c'
newAccount = "0x39ed115a902364d0de9cedf5877b2e359bdc9946"
contractAddress = "0xdb196650DB59F82ED2ea0d8D02e3b0C9493bF380"; //合约地址
// ourAdress = "0x05A94caaCdb83e8B9E0b9a582988de448440ECc1";
// ourPassword = "domore0325";

// getContract()
sellerAddress = "0xe12fd247cd56347ece998784b013d060adc6ad69"; //你直接拿这个测试，不过得先导入，我发给你
//transfer(sellerAddress, newAccount,1, "domore");
//console.log("新账户数量" + getBalance(newAccount) / 10 ** 18);
//newUser(ourPassword)
//console.log(getBalance(sellerAddress))
function transfer(from, to, _value, fromPassword) {
    web3.personal.unlockAccount(from, fromPassword, function(error, result) {
            if (!error) {
                console.log("解锁账户" + from + "成功")
                getContract().transfer.sendTransaction(to, _value, { from: from }, function(error, data) {
                        if (!error) {
                            hash = data
                            console.log(from + "  转账给  " + to + "  交易发起" + "交易hash值是" + data);
                            lockAccount(from);
                        }


                    else {
                        console.log(from + "  转账给  " + to + "  交易发起失败" + "原因是" + error);
                    }
                })
        } else {
            console.log("解锁账户失败" + "原因是" + error);
        }
    });

}

//sendToUs(sellerAddress,sellerPassword,ourAdress,100);
//sendToBuyer(sellerAddress, buyerAddress, ourAdress, 100, ourPassword)
//buyCoin(sellerAddress,sellerPassword);//假设seller要买hsb
//console.log(transferEstimateGas(ourAdress,contractAddress,100,ourPassword));
//console.log(sendToUsEstimateGas(sellerAddress,sellerPassword,ourAdress,100));
// console.log("平台代币数量" + getBalance(ourAdress));
// console.log("卖家的代币数量" + getBalance(aim2));
// var filter = web3.eth.filter({ address: contractAddress });

// filter.watch(function(error, log) {
//     console.log("1");
//     console.log(log); //
// });

// // get all past logs again.
// var myResults = filter.get(function(error, logs) {
//     console.log("2");
//     console.log(log);
// });

// var transaction = web3.eth.getTransaction(hash, function(error, data) {
//     if (!error) {
//         console.log("getTransaction")
//         console.log(data);
//     }
// });

// web3.eth.getTransactionReceipt(hash, function(error, data) {
//     if (!error) {
//         console.log("getTransactionReceipt status")
//         console.log(data.status)
//     }
// })

// function estimateGasArguments(type, from, to, amount, other) //一个对象，估算手续费的时候用
// {
//     this.type = type;
//     this.from = from; //规定手续费谁出
//     this.to = to;
//     this.amount = amount;
//     this.other = other;
// }

function lockCoin(target, lockAmount, lockPeriod) //锁仓
{
    if (!isAddress(target)) {
        return;
    } else {
        web3.personal.unlockAccount(ourAdress, ourPassword, function(error, data) {
            if (!error) {
                console.log("解锁账户成功");
                getContract().lockToken.sendTransaction(target, lockAmount, lockPeriod, { from: ourAdress }, function(error, data) {
                    if (!error) {
                        console.log("锁仓成功 hash值是" + data);
                        lockAccount(ourAdress);
                    } else {
                        console.log("锁仓失败 原因是" + error);
                    }
                });
            } else {
                console.log("解锁账户失败 原因是" + error);
            }
        });
    }
}


function releaseCoin(target, amount) //平台解锁
{
    if (!isAddress(target)) {
        return;
    } else {
        web3.personal.unlockAccount(ourAdress, ourPassword, function(error, data) {
            if (!error) {
                console.log("解锁账户成功");
                getContract().ownerUnlock.sendTransaction(target, amount, { from: ourAdress }, function(error, data) {
                    if (!error) {
                        console.log("释放" + target + "      " + amount + "数量的币成功 hash值是" + data);
                        lockAccount(ourAdress);
                    } else {
                        console.log("释放失败 原因是" + error);
                    }
                });
            } else {
                console.log("解锁账户失败 原因是" + error);
            }
        });
    }
}


function releaseCoinPersonal(target, amount, targetPassword) //个人解锁，在锁定时间够了之后自己可以解锁
{
    if (!isAddress(target)) {
        return;
    } else {
        web3.personal.unlockAccount(target, targetPassword, function(error, data) {
            if (!error) {
                console.log("解锁账户成功");
                getContract().ownerUnlock.sendTransaction(target, amount, { from: ourAdress }, function(error, data) {
                    if (!error) {
                        console.log("释放" + target + "      " + amount + "数量的币成功 hash值是" + data);
                        lockAccount(ourAdress);
                    } else {
                        console.log("释放失败 原因是" + error);
                    }
                });
            } else {
                console.log("解锁账户失败 原因是" + error);
            }
        });
    }
}


//发送eth的时候ethAmount要乘以10的18次方，比如说我想花一个eth买币，ethAmount就是10的18次方
function buyCoin(buyerAddress, buyerPassword, ethAmount) {

    web3.personal.unlockAccount(buyerAddress, buyerPassword, function(error, result) {
        if (!error) {
            console.log("解锁账户" + sellerAddress + "成功")
            getContract().buy.sendTransaction({ from: buyerAddress, value: ethAmount }, function(error, result) {
                if (!error) {
                    console.log("购买成功 hash值是" + result);
                    lockAccount(buyerAddress);
                } else {
                    console.log("购买失败 原因是" + error);
                }
            });
            return true;
        } else {
            console.log("解锁账户失败" + "原因是" + error);
        }
    });
}

function setPrices(buyPrice, sellPrice) {
    web3.personal.unlockAccount(ourAdress, ourPassword, function(error, result) {
        if (!error) {
            console.log("解锁账户" + ourAdress + "成功")
            getContract().setPrices.sendTransaction(buyPrice, sellPrice, { from: ourAdress }, function(error, result) {
                if (!error) {
                    console.log("价格设置成功" + result);
                    lockAccount(ourAdress);
                } else {
                    console.log("价格设置失败 原因是" + error);
                }
            });
            return true;
        } else {
            console.log("解锁账户失败" + "原因是" + error);
        }
    });
}

function getBuyPrice() {
    return getContract().buyPrice();
}

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
    console.log("平台需要出的手续费" + gasAmount);
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


function transferEstimateGas(from, to, _value, fromPassword) {
    var gasAmount = estimateGas(new estimateGasArguments("commenTransfer", from, to, _value, ""));
    return gasAmount;
}

function sendToUsEstimateGas(sellerAddress, sellerPassword, ourAdress, coinAmount) {
    var gasAmount = 3 * estimateGas(new estimateGasArguments("sendToUs", "", ourAdress, coinAmount, ""));
    return gasAmount;
}

function lockAccount(account) {
    if (!isAddress(account)) {
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
    var abi = [{ "constant": true, "inputs": [], "name": "name", "outputs": [{ "name": "", "type": "string" }], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": false, "inputs": [{ "name": "_spender", "type": "address" }, { "name": "_value", "type": "uint256" }], "name": "approve", "outputs": [{ "name": "success", "type": "bool" }], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": true, "inputs": [], "name": "totalSupply", "outputs": [{ "name": "", "type": "uint256" }], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": false, "inputs": [{ "name": "_from", "type": "address" }, { "name": "_to", "type": "address" }, { "name": "_amount", "type": "uint256" }], "name": "transferFrom", "outputs": [{ "name": "success", "type": "bool" }], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": true, "inputs": [], "name": "decimals", "outputs": [{ "name": "", "type": "uint256" }], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": false, "inputs": [], "name": "withdraw", "outputs": [], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": true, "inputs": [], "name": "value", "outputs": [{ "name": "", "type": "uint256" }], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": false, "inputs": [{ "name": "_value", "type": "uint256" }], "name": "burn", "outputs": [], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": false, "inputs": [{ "name": "addresses", "type": "address[]" }], "name": "disableWhitelist", "outputs": [], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": true, "inputs": [{ "name": "_owner", "type": "address" }], "name": "balanceOf", "outputs": [{ "name": "", "type": "uint256" }], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": false, "inputs": [{ "name": "addresses", "type": "address[]" }], "name": "airdrop", "outputs": [], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": true, "inputs": [], "name": "symbol", "outputs": [{ "name": "", "type": "string" }], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": false, "inputs": [], "name": "finishDistribution", "outputs": [{ "name": "", "type": "bool" }], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": false, "inputs": [{ "name": "addresses", "type": "address[]" }], "name": "enableWhitelist", "outputs": [], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": false, "inputs": [{ "name": "addresses", "type": "address[]" }, { "name": "amounts", "type": "uint256[]" }], "name": "distributeAmounts", "outputs": [], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": false, "inputs": [{ "name": "_to", "type": "address" }, { "name": "_amount", "type": "uint256" }], "name": "transfer", "outputs": [{ "name": "success", "type": "bool" }], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": false, "inputs": [], "name": "getTokens", "outputs": [], "payable": true, "stateMutability": "payable", "type": "function" }, { "constant": true, "inputs": [], "name": "distributionFinished", "outputs": [{ "name": "", "type": "bool" }], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": true, "inputs": [{ "name": "tokenAddress", "type": "address" }, { "name": "who", "type": "address" }], "name": "getTokenBalance", "outputs": [{ "name": "", "type": "uint256" }], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": true, "inputs": [], "name": "totalRemaining", "outputs": [{ "name": "", "type": "uint256" }], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": true, "inputs": [{ "name": "_owner", "type": "address" }, { "name": "_spender", "type": "address" }], "name": "allowance", "outputs": [{ "name": "", "type": "uint256" }], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": false, "inputs": [{ "name": "_tokenContract", "type": "address" }], "name": "withdrawForeignTokens", "outputs": [{ "name": "", "type": "bool" }], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": true, "inputs": [], "name": "totalDistributed", "outputs": [{ "name": "", "type": "uint256" }], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": false, "inputs": [{ "name": "newOwner", "type": "address" }], "name": "transferOwnership", "outputs": [], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": false, "inputs": [{ "name": "addresses", "type": "address[]" }, { "name": "amount", "type": "uint256" }], "name": "distribution", "outputs": [], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": true, "inputs": [{ "name": "", "type": "address" }], "name": "blacklist", "outputs": [{ "name": "", "type": "bool" }], "payable": false, "stateMutability": "view", "type": "function" }, { "inputs": [], "payable": false, "stateMutability": "nonpayable", "type": "constructor" }, { "payable": true, "stateMutability": "payable", "type": "fallback" }, { "anonymous": false, "inputs": [{ "indexed": true, "name": "_from", "type": "address" }, { "indexed": true, "name": "_to", "type": "address" }, { "indexed": false, "name": "_value", "type": "uint256" }], "name": "Transfer", "type": "event" }, { "anonymous": false, "inputs": [{ "indexed": true, "name": "_owner", "type": "address" }, { "indexed": true, "name": "_spender", "type": "address" }, { "indexed": false, "name": "_value", "type": "uint256" }], "name": "Approval", "type": "event" }, { "anonymous": false, "inputs": [{ "indexed": true, "name": "to", "type": "address" }, { "indexed": false, "name": "amount", "type": "uint256" }], "name": "Distr", "type": "event" }, { "anonymous": false, "inputs": [], "name": "DistrFinished", "type": "event" }, { "anonymous": false, "inputs": [{ "indexed": true, "name": "burner", "type": "address" }, { "indexed": false, "name": "value", "type": "uint256" }], "name": "Burn", "type": "event" }];
    console.log(JSON.stringify(abi));
    var contract = web3.eth.contract(abi).at(contractAddress);
    return contract;
}