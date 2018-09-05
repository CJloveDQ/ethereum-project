pragma solidity ^0.4.16;    //声明使用的编译器版本
/**
 * The  test contract does this and that...
 */

/**
 * The contractName contract does this and that...
 */

/**
 * Tht students contract does this and that...
 */

 //contract类似java的class
contract students 
{
	mapping (uint => student)  public studentList ;  //一个映射，key是学生的id，值是student结构体
	mapping (uint => bool) public exists;  //一个映射，key是学生的id，值是true或者false，false表示学生列表不存在该id的学生，true的话表示存在
	struct   student   //定义一个student的结构体
	{      

	//这些数据都是public的
		uint id;  //学生id
		string  name;   //姓名
		uint icNum;  //身份证号
		string  gender; //性别
		uint8  age ;     //
    }


    //功能是往学生列表添加学生
	function addStudent (uint _id,string _name,uint _icNum,string _gender,uint8 _age) public   
	{
		//初始化一个学生并且存进学生列表
		studentList[_id]=student(_id,_name,_icNum,_gender,_age);
		//设置存在该id的学生
		exists[_id]=true;
	}
	
	//根据id修改学生信息
	function changeMes (uint _id,string _name,uint _icNum,string _gender,uint8 _age) public returns (bool res)   //修改信息
	{

		if(!existSuchStudent(_id))  //判断是不是存在这样的学生
		{
			addStudent(_id,_name,_icNum,_gender,_age);  //如果不存在则添加一个这样的学生
		}
		else   //存在，直接修改信息
		{
			studentList[_id].icNum=_icNum;  
			studentList[_id].gender=_gender;
			studentList[_id].age=_age;
			studentList[_id].name=_name;
			return true;
		}
 		
	}


	//根据id判断是不是学生表有没这样的学生
	function   existSuchStudent (uint _id) public view returns(bool res)     //public声明该函数是公开的，view声明是只对数据进行了读取，returns表示返回值，名字叫res，类型是布尔型
	{
		if(exists[_id])	  //如果记录存在与否的数组key为_id的值为true，返回true，否则返回false
		{
			return true;
		}
		else
		{
			return false;
		}
	}

	
}

