pragma solidity ^0.4.24;
contract pushMes
{
	
	//定义数据库
  	struct table {
		string  keys;
		string[]  values;
	}
    struct database {
		mapping (string  => table) tables;
	}
    mapping(string => database) databases;
    mapping(string => bool) exsitDB;
    
   
	function addTable (string databaseName,string tableName,string keys,string value) public returns(bool res)  {
		
			
		if(!existSuchDatabase(databaseName))
		{
			//新建一个数据库
			databases[databaseName]=database();
            exsitDB[databaseName]=true;
			//新建表

		}
        
		//添加数据
		databases[databaseName].tables[tableName].keys =keys;
		databases[databaseName].tables[tableName].values.push(value);
	}

	function existSuchDatabase (string databaseName) internal returns(bool res)  {
		if(exsitDB[databaseName])
		{
			return true;
		}
		else
		{
			return false;
		}
	}
	
	function getTable(string databaseName,string tableName,uint index)public returns(string)
	{
		return databases[databaseName].tables[tableName].values[index];
	}
}