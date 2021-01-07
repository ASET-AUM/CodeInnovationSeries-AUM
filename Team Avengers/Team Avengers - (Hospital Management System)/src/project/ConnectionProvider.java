package project;
import java.sql.*;
import java.io.*;
public class ConnectionProvider
{
	public static void main(String arrgs[])
	{
           getCon();     
	}
        
    public static Connection getCon(){
        try{
            Class.forName("com.mysql.jdbc.Driver");
            Connection con=DriverManager.getConnection("jdbc:mysql://localhost:3306/project","root","7977166687");
            return con;
        }
        catch(Exception e){
            return null;
        }
    }
}

