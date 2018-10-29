package push;

//import java.lang.invoke.VarHandle;
import java.sql.*;
import java.util.ArrayList;

import com.fasterxml.jackson.core.Versioned;

import net.sf.json.JSONArray;
import net.sf.json.JSONObject;

public class GetDBData {

	// JDBC 驱动名及数据库 URL
	static final String JDBC_DRIVER = "com.mysql.jdbc.Driver";
	static String DB_URL;

	// 数据库的用户名与密码，需要根据自己的设置
	static final String USER = "root";
	static String dbName;
	static String dbPassword;
	static Connection con;
	static String tableName;
	public GetDBData(String dbName,String dbPassword,String tableName)
	{
		this.dbName=dbName;
		this.dbPassword=dbPassword;
		this.tableName=tableName;
	}
	public ArrayList<String> getLocalData() {
		ArrayList<String> result = new ArrayList<String>();
		Statement stmt = null;
		try {
			// 注册 JDBC 驱动
			Class.forName("com.mysql.jdbc.Driver");

			// 打开链接
			System.out.println("连接数据库...");
			DB_URL = "jdbc:mysql://localhost:3306/" + this.dbName;
			con = DriverManager.getConnection(DB_URL, USER, dbPassword);

			// 执行查询
			stmt = con.createStatement();
			String sql = "SELECT * FROM " + this.tableName;
			ResultSet rs = stmt.executeQuery(sql);
			ResultSetMetaData data = rs.getMetaData();
			ArrayList<String> keys = new ArrayList<String>();
			ArrayList<String> values = new ArrayList<String>();
			// 获得键
			JSONObject keyTemp = new JSONObject();
			for (int i = 1; i <= data.getColumnCount(); i++) {
				keys.add(data.getColumnName(i));
			}

			//获得值
			while (rs.next()) {
				JSONObject temp = new JSONObject();

				for (int i = 1; i <= keys.size(); i++) {
					String teString = rs.getString(i);
					temp.put(keys.get(i-1),teString);
	
				}
				values.add(temp.toString());
			}
			ArrayList<String> keysInJSON = new ArrayList<String>();
			JSONObject temp = new JSONObject();
			for (int i = 1; i <= keys.size(); i++) {
				
				temp.put(i,keys.get(i-1));
			}
			//返回json形式的字符串
			keysInJSON.add(temp.toString());
			result.addAll(keysInJSON);
			result.addAll(values);
			// 完成后关闭
			rs.close();
			stmt.close();
			con.close();
			return result;
		} catch (SQLException se) {
			// 处理 JDBC 错误
			se.printStackTrace();
			return null;
		} catch (Exception e) {
			// 处理 Class.forName 错误
			e.printStackTrace();
			return null;
		} finally {
			// 关闭资源
			try {
				if (stmt != null)
					stmt.close();
			} catch (SQLException se2) {
			} // 什么都不做
			try {
				if (con != null)
					con.close();
			} catch (SQLException se) {
				se.printStackTrace();
			}
		}
	}
}