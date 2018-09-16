package aa.bb;

import java.io.IOException;


import org.web3j.protocol.admin.Admin;
import org.web3j.protocol.admin.methods.response.PersonalUnlockAccount;
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
//import com.fasterxml.jackson.annotation.JsonSubTypes.Type;
import org.web3j.utils.Convert;

//import com.fasterxml.jackson.core.type.TypeReference;
public class ConnectEthereum {

	static Admin web3;
	static Web3ClientVersion web3ClientVersion;
	static Credentials credentials;
	static PushData contract;
	static ConnectDB db;
	public static void main(String[] args) {
		db=new ConnectDB();
		toBlockChain("","");
//		// TODO Auto-generated method stub
//		String address = "0x069ABcF74ecD05EA06CB56C4780CD60237082C25";
//		System.out.println("开始连接");
//		
//		web3 = Admin.build(new HttpService("http://127.0.0.1:8545"));
//		
//		try {
//			web3ClientVersion = web3.web3ClientVersion().send();
//			System.out.println(web3ClientVersion.getWeb3ClientVersion());
//			System.out.println(web3.toString());
//			System.out.println("连接成功");
//			try {
//				
//				 // 第一个变量填入账户的密码，第二个变量填入账户文件的 path
//				credentials = WalletUtils.loadCredentials(
//						"domore0325",
//						"/home/yapie/qqDownload/keystore/UTC--2018-09-15T12-35-03.244887899Z--069abcf74ecd05ea06cb56c4780cd60237082c25");
//				
//				//获取合约
//				// 合约地址
//				String contractAddress = "0x81ec14d0cb1d073fd6bcdc8d3e463c314479eec6";
//				// 以某个用户的身份调用合约
//				PersonalUnlockAccount personalUnlockAccount = web3.personalUnlockAccount(address, "domore0325").send();
//				TransactionManager transactionManager = new ClientTransactionManager(web3,address);
//				contract = PushData.load(contractAddress, web3, transactionManager,ManagedTransaction.GAS_PRICE, org.web3j.tx.Contract.GAS_LIMIT);
//				//数据上链
//				System.out.println("数据上链");
//				try {
//					TransactionReceipt transactionReceipt = contract.addTable("test1", "student1", "name age", "yapie 11 liu 14").send();
//					System.out.println(transactionReceipt.getTransactionHash());			
//					
//				} catch (Exception e) {
//					// TODO Auto-generated catch block
//					e.printStackTrace();
//				}
//			} catch (CipherException e) {
//				// TODO Auto-generated catch block
//				e.printStackTrace();
//			}
//
//
//		} catch (IOException e) {
//			// TODO Auto-generated catch block
//			e.printStackTrace();
//		}
//		
		
	}
	
	public void getTable(String databaseName,String tableName) {
		
		try {
			//获取某个表
			Tuple2<String, String> teString=contract.getTable(databaseName,tableName).send();
			System.out.println("获取结果是");
			System.out.println(teString);
		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
	
	public static void toBlockChain(String databaseName,String tableName) {
		Tuple2<String, String> result;
		db.connect("RUNOOB","websites");
	}
}
