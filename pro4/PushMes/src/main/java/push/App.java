package push;

import java.util.ArrayList;

import org.bouncycastle.jcajce.provider.symmetric.Threefish;

import net.sf.json.JSONObject;
import okhttp3.Call;

interface Callback {
    void checkFinished(int index);
}


public class App {
	
	GetDBData dbData;
	Ethereum ethereum;
	static int haveFinished=0;
	static int tableLength;
	public App(String dbName,String dbPassword,String tableName,String coinbaseAddress,String coinbasePassword) {
		this.dbData=new GetDBData(dbName, dbPassword, tableName);
		this.ethereum=new Ethereum(coinbaseAddress,coinbasePassword);
	}
	
	
	public static void main(String[] args) {
		String dbPassword="domore0325";//mysql 数据库密码
		String dbName="videos";//需要上传的数据库名
		String tableName="requestQuanitity";//需要上传的数据库中的表名
		String  coinbaseAddress="0xec4f994157240ea2d245305f250ff12cd493cff8";//默认使用的交易发起账户地址
		String coinbasePassword="123456";//发起交易账户的密码
		App app=new App(dbName, dbPassword, tableName,coinbaseAddress,coinbasePassword);
		//实现接口回调用来判断是否全部上链完成
		Callback callback=new Callback() {
			@Override
			public void checkFinished(int index) {
				App.haveFinished++;
				if(App.haveFinished==App.tableLength)
				{
					System.out.println("表"+tableName+"上传全部完成");
					
				}
			}
		};
		//数据表上链
    	app.pushTable(callback,dbName, tableName);
    	//获取数据表信息
		//app.getTable(dbName, tableName);
	}
	
	
	//上传数据表
	public void pushTable(Callback callback,String databaseName,String tableName) 
	{
		ArrayList<String> result=this.dbData.getLocalData();//从数据库获取数据
		System.out.println("从数据库读取表　"+tableName+"  完成");
		String keys = result.get(0);//获得数据表的键
		System.out.println("在区块链创建表"+tableName+"....");
		this.createTable(databaseName, tableName, keys);//创建表用来存储数据
		System.out.println("创建表　"+tableName+"完成");
		System.out.println("开始上传数据...");
		App.tableLength=result.size()-1;
		//每条数据上链
		for (int i = 1; i < result.size(); i++) {
			System.out.println("第  "+String.valueOf(i)+" 条数据上链中...");
			new PushPerData(this.ethereum,callback,databaseName,tableName,result.get(i),i-1).start();//为每条数据开一个线程处理
		}
		
	}
	
	//读取数据表内容
	public void getTable(String databaseName, String tableName) {
		
		System.out.println("读取表"+tableName+"中 ...");
		if(!this.ethereum.exsitSuchTable(databaseName, tableName))//不存在这样的表
		{
			System.out.println("不存在这样的表,请上传后读取");
		}
		else     //存在的话直接读取 
		{
			int tableLength=this.ethereum.getTableLength(databaseName, tableName);
			for(int i=0;i<tableLength;i++)
			{
				System.out.println(this.ethereum.getTable(databaseName, tableName, i));	
			}
			System.out.println("读取完毕");
		}
		
	}
	//数据上链之前先创建数据表用来存储数据
	public void createTable(String databaseName,String tableName,String keys)
	{
		//判断是否之前上传过同名的数据表
		if(!this.ethereum.exsitSuchTable(databaseName, tableName))
		{
			this.ethereum.createTable(databaseName, tableName, keys);
		}
		else
		{
			//存在之前上传过的同名的，清空该数据表内容
			System.out.println("已存在名为"+tableName+"的表  清空该表内容中.....");
			this.ethereum.dropTable(databaseName, tableName);
		}
	}
	
	
}

class PushPerData implements Runnable {
       private Thread t;
	   Ethereum ethereum;
	   Callback callback;
	   String databaseName; //需要上传的数据库名
	   String tableName;//表名
	   String value;//传的值
	   int index;//此条数据在数据库的索引
	   
	   public PushPerData(Ethereum ethereum,Callback callback,String databaseName,String tableName,String value,int index) {
	      this.ethereum=ethereum;
	      this.databaseName=databaseName;
	      this.tableName=tableName;
	      this.value=value;
	      this.index=index;
	      this.callback=callback;
	   }
	   public void run() {
	      this.ethereum.pushData(databaseName, tableName, value, index);//上传
	      this.callback.checkFinished(index+1);//调用回调函数
	   }
	   public void start () {
		      if (t == null) {
		         t = new Thread (this);
		         t.start ();
		      }
		   }
	}

