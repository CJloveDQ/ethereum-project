package aa.bb;

import java.lang.invoke.VarHandle;
import java.sql.*;
import java.util.ArrayList;

import javax.xml.transform.Templates;

import org.bouncycastle.jcajce.provider.symmetric.DES.DESCFB8;
 
public class ConnectDB{
 
    // JDBC 驱动名及数据库 URL
    static final String JDBC_DRIVER = "com.mysql.jdbc.Driver";  
    static String DB_URL;
 
    // 数据库的用户名与密码，需要根据自己的设置
    static final String USER = "root";
    static final String PASS = "domore0325";
    
    public  void connect(String databaseName,String tableName) {
        Connection conn = null;
        Statement stmt = null;
        
        try{
            // 注册 JDBC 驱动
            Class.forName("com.mysql.jdbc.Driver");
        
            // 打开链接
            System.out.println("连接数据库...");
            DB_URL = "jdbc:mysql://localhost:3306/"+databaseName;
            conn = DriverManager.getConnection(DB_URL,USER,PASS);
        
            // 执行查询
            System.out.println(" 实例化Statement对象...");
            stmt = conn.createStatement();
            String sql;
//            sql = "desc "+tableName;
            sql = "SELECT * FROM "+tableName;
            ResultSet rs = stmt.executeQuery(sql);
            ResultSetMetaData data = rs.getMetaData();
            ArrayList<String> keys = new ArrayList<String>(); 
            ArrayList<String> values = new ArrayList<String>(); 
            //获得键
            for (int i = 1; i <= data.getColumnCount(); i++) {
    		 keys.add(data.getColumnName(i));
    		}
    		System.out.println(keys);
    		//获得值
    		
            while(rs.next()){
                // 通过字段检索
            	
            	for(int i = 1; i <= keys.size(); i++)
            	{
            		values.add(rs.getString(keys.get(i-1)));
      
            	}
            	
                
            
            }
        
            // 完成后关闭
            rs.close();
            stmt.close();
            conn.close();
        }catch(SQLException se){
            // 处理 JDBC 错误
            se.printStackTrace();
        }catch(Exception e){
            // 处理 Class.forName 错误
            e.printStackTrace();
        }finally{
            // 关闭资源
            try{
                if(stmt!=null) stmt.close();
            }catch(SQLException se2){
            }// 什么都不做
            try{
                if(conn!=null) conn.close();
            }catch(SQLException se){
                se.printStackTrace();
            }
        }
        System.out.println("Goodbye!");
    }
}