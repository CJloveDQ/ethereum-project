package pushMes;

import org.web3j.protocol.core.methods.response.TransactionReceipt;

public class PushPerData extends Thread {
	private Thread t;
	private  String threadName;
	private static PushData contract;
	static String databaseName;
	static String tableName;
	static String keys;
	static String data;

	public void PushData(String _data) {

	}

	public void init(String _threadName, PushData _contract, String _databaseName, String _tableName, String _keys,String _data) {
		contract = _contract;
		databaseName = _databaseName;
		tableName = _tableName;
		keys = _keys;
		threadName = _threadName;
		data=_data;
	}

	public void run() {
		addMes(threadName);
	}

	public void start() {
	      if (t == null) {
	         t = new Thread (this, threadName);
	         t.start ();
	      }
	 
	}

	public static boolean addMes(String threadName) {
		boolean result = false;
		TransactionReceipt transactionReceipt;
		try {
			transactionReceipt = contract.addTable(databaseName, tableName, keys, data).send();
			System.out.println("第"+threadName+"条数据上链交易发起　hash值是");
			System.out.println(transactionReceipt.getTransactionHash());
			result = true;
		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		return result;
	}

}
