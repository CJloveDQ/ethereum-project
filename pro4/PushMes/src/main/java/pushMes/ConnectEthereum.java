package pushMes;

import java.io.IOException;
import java.util.ArrayList;

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
//import com.fasterxml.jackson.annotation.JsonSubTypes.Type;
import org.web3j.utils.Convert;

//import com.fasterxml.jackson.core.type.TypeReference;
public class ConnectEthereum {

	static Admin web3;
	static Web3ClientVersion web3ClientVersion;
	static Credentials credentials;
	static PushData contract;
	static ConnectDB db;
	static String fromAddress;
	static String contractAddress;
	static TransactionManager transactionManager;

	public static void main(String[] args) {
		db = new ConnectDB();
		init();
		toBlockChain("RUNOOB", "websites");
	}

	public static boolean init() {
		boolean result = false;
		fromAddress = "0x069ABcF74ecD05EA06CB56C4780CD60237082C25";
		contractAddress = "0xd8da54bc32a866eda0ab33e7d415fe0230a4cb13";
		System.out.println("开始连接...");
		web3 = Admin.build(new HttpService("http://127.0.0.1:8545"));
		transactionManager = new ClientTransactionManager(web3, fromAddress);
		contract = PushData.load(contractAddress, web3, transactionManager, ManagedTransaction.GAS_PRICE,org.web3j.tx.Contract.GAS_LIMIT);
		try {
			web3.personalUnlockAccount(fromAddress, "domore0325").send();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		try {
			web3ClientVersion = web3.web3ClientVersion().send();
			System.out.println(web3ClientVersion.getWeb3ClientVersion());
			System.out.println("连接成功");
			result = true;
		} catch (IOException e1) {
			// TODO Auto-generated catch block
			System.out.println("连接失败");
			e1.printStackTrace();
		}
		return result;
	}

	public void getTable(String databaseName, String tableName) {
		try {
			// 获取某个表
//			Tuple2<String, String> teString = contract.getTable(databaseName, tableName).send();
			System.out.println("获取结果是");
//			System.out.println(teString);
		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}

	public static boolean addMes(String databaseName, String tableName, String keys, String data) {
		boolean result = false;
		TransactionReceipt transactionReceipt;
		try {
			transactionReceipt = contract.addTable(databaseName, tableName, keys, data).send();
			System.out.println(transactionReceipt.getTransactionHash());
			result = true;
		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}

		return result;
	}

	public static void toBlockChain(String databaseName, String tableName) {

		ArrayList<String> result = new ArrayList<String>();
		System.out.println("从本地获取数据中...");
		result = db.connect(databaseName, tableName);

		if (result == null) {
			System.out.println("数据库名或表名错误");
		} else {
//			System.out.println(result.get(1));t
			System.out.println("本地数据获取完毕");
			String keys = result.get(0);

			// 以某个用户的身份调用合约
			// 数据上链
			System.out.println("数据上链...");
			ArrayList<PushPerData> list = new ArrayList<PushPerData>();
			for (int i = 1; i < result.size(); i++) {
				System.out.println("第　"+String.valueOf(i)+"　条数据上链中...　　　请稍后");
				list.add(new PushPerData());
				list.get(i-1).init(String.valueOf(i), contract, databaseName, tableName, keys,result.get(i));
				list.get(i-1).start();
//				addMes(databaseName, tableName, keys, result.get(i));
			}
		}
	}

}
