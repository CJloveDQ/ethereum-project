pragma solidity ^0.4.16;

contract pushMes
{
	struct table {
		string [] keys;
		string [] values;
	}
	
	struct database {
		mapping (string tableName => table) tables;
	}

	//定义数据库
	database databases;

	function addTable (string databaseName,string tableName,string [] keys,string [] values) returns(bool res) public {
		if(!existSuchTable(databaseName,tableName))
		{
			return false;
		}
		else
		{
			databases[databaseName][tableName].keys = keys;
			databases[databaseName][tableName].values = values;
		}
	}
	
	function getTable (string databaseName,string tableName) returns(string [] keys,string [] values) public {
		if(!existSuchTable(databaseName,tableName))
		{
			return false;
		}
		else
		{
			keys = databases[databaseName][tableName].keys;
			values = databases[databaseName][tableName].values;
		}
	}
	
	function existSuchTable (string databaseName,string tableName) returns(bool res) internal {
		if(tables[databaseName])
		{
			return true;
		}
		else
		{
			return false;
		}
	}
	
	
}