package push;

import java.io.IOException;
import java.math.BigInteger;
import java.util.ArrayList;
import java.util.concurrent.TimeUnit;
import org.web3j.protocol.admin.Admin;
import org.web3j.protocol.admin.methods.response.PersonalUnlockAccount;
import org.objectweb.asm.tree.IntInsnNode;
import org.web3j.crypto.CipherException;
import org.web3j.crypto.Credentials;
import org.web3j.crypto.WalletUtils;
import org.web3j.protocol.Web3j;

import org.web3j.protocol.core.DefaultBlockParameterName;

import org.web3j.protocol.core.methods.response.EthGetBalance;
import org.web3j.protocol.core.methods.response.TransactionReceipt;
import org.web3j.protocol.core.methods.response.Web3ClientVersion;
import org.web3j.protocol.http.HttpService;
import org.web3j.tuples.generated.Tuple2;
import org.web3j.tx.ClientTransactionManager;

import org.web3j.tx.ManagedTransaction;
import org.web3j.tx.TransactionManager;
import org.web3j.tx.exceptions.TxHashMismatchException;
//import com.fasterxml.jackson.annotation.JsonSubTypes.Type;
import org.web3j.utils.Convert;
//import com.fasterxml.jackson.core.type.TypeReference;
public class Ethereum {

	static Admin web3;
	static Web3ClientVersion web3ClientVersion;
	static Credentials credentials;
	static PushMes contract;
	static String fromAddress;
	static String contractAddress;
	static TransactionManager transactionManager;
	//连接以太坊网络
	public  Ethereum(String coinbaseAddress,String coninbasePassword) {
		fromAddress = coinbaseAddress;
		contractAddress = "0x030cb64A7e45361E5Ba8FF6E1E22b7341bd87E0B";
		System.out.println("开始连接...");
		web3 = Admin.build(new HttpService("http://127.0.0.1:8545"));
		transactionManager = new ClientTransactionManager(web3, fromAddress);
		//获得合约
		contract = PushMes.load(contractAddress, web3, transactionManager, ManagedTransaction.GAS_PRICE,org.web3j.tx.Contract.GAS_LIMIT);
		try {
			//解锁账户
			web3.personalUnlockAccount(fromAddress, coninbasePassword).send();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			System.out.println("以太坊账户密码不匹配");
			e.printStackTrace();
		}
		try {
			web3ClientVersion = web3.web3ClientVersion().send();
			System.out.println(web3ClientVersion.getWeb3ClientVersion());
			System.out.println("连接以太坊网络成功");

		} catch (IOException e1) {
			// TODO Auto-generated catch block
			System.out.println("连接以太坊网络失败");
			e1.printStackTrace();
		}
	}
	
	//创建表
	public void createTable(String databaseName,String tableName,String keys)
	{
		TransactionReceipt transactionReceipt;
		try {
			transactionReceipt = contract.createTable(databaseName, tableName, keys).send();//调用合约
			String hash=transactionReceipt.getTransactionHash();
			System.out.println("创建表"+tableName+"交易确认完成　hash值是"+hash);

		} catch (Exception e) {
			// TODO Auto-generated catch block
			//e.printStackTrace();
			System.out.println("无其他节点可用，请添加静态节点或重启以太坊网络");
			System.exit(1);
		}
	}
	
	//删除表
	public void dropTable(String databaseName,String tableName)
	{
		TransactionReceipt transactionReceipt;
		try {
			transactionReceipt = contract.dropTable(databaseName, tableName).send();
			String hash=transactionReceipt.getTransactionHash();
			System.out.println("清空表"+tableName+"内容的交易完成　hash值是"+hash);
		} catch (Exception e) {
			// TODO Auto-generated catch block
			//e.printStackTrace();
			System.out.println("无其他节点可用，请添加静态节点或重启以太坊网络");
			System.exit(1);
		}
	}
	
	//上传数据
	public void pushData(String databaseName,String tableName,String value,int index)
	{
		TransactionReceipt transactionReceipt;
		try {
			transactionReceipt = contract.pushData(databaseName, tableName, value, BigInteger.valueOf(index)).send();
			String hash=transactionReceipt.getTransactionHash();
			System.out.println("上传数据第"+(index+1)+"条数据交易完成　hash值是"+hash);
		} catch (Exception e) {
			// TODO Auto-generated catch block
			//e.printStackTrace();
			System.out.println("无其他节点可用，请添加静态节点或重启以太坊网络");
			System.exit(1);
		}
	}
	
//	public void  waitingForFinish(String hash) throws IOException, InterruptedException
//	{
//		int needWaitTime=3;
//		System.out.println(web3.ethGetTransactionReceipt(hash));
//		while(web3.ethGetTransactionReceipt(hash)==null)
//		{
//			TimeUnit.SECONDS.sleep(needWaitTime);
//		}
//		System.out.println("交易  "+hash+"  打包完成");	
//	}
	
	//获得表的长度
	public int getTableLength(String databaseName,String tableName) 
	{
        try {
			return contract.getTableLength(databaseName, tableName).send().intValue();
		} catch (Exception e) {
			// TODO Auto-generated catch block
			//e.printStackTrace();
			System.out.println("无其他节点可用，请添加静态节点或重启以太坊网络");
			System.exit(1);
			return 0;
		}
        
	}
	
	//获得表的某一项
	public String getTable(String databaseName,String tableName,int index)
	{
		String result="";
        try {
			result=contract.getTable(databaseName, tableName, BigInteger.valueOf(index)).send();
		} catch (Exception e) {
			// TODO Auto-generated catch block
			//e.printStackTrace();
			System.out.println("无其他节点可用，请添加静态节点或重启以太坊网络");
			System.exit(1);
		}
        return result;
	}
	
	//判断是否存在该表
	public boolean exsitSuchTable(String databaseName,String tableName)
	{
		boolean result = false;
		try {
			result=contract.exsitSuchTable(databaseName, tableName).send();
			
		} catch (Exception e) {
			// TODO Auto-generated catch block
			//e.printStackTrace();
			System.out.println("无其他节点可用，请添加静态节点或重启以太坊网络");
			System.exit(1);
		}
		return result;
	}
	
}
