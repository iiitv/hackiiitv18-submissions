  <%@page import="java.sql.*" %>
<html>
 
 <head>
 <title> POST SIGNUP PAGE </TITLE>
 <center>
 <font style="algerian"  color="blue">
 
 <H1>  POST SIGNUP </H1>
 </font>
 </center>
 </HEAD>
 <BODY>
 <center>
 <% String Name=""; String password="";
			 boolean b1=false;
			 
		String s1=request.getParameter("username");
		String s2=request.getParameter("password");
		
		 try 
		  {
			  Class.forName("com.mysql.jdbc.Driver");
            String url = "jdbc:mysql://localhost:3306/akmproject";

            Connection conn = DriverManager.getConnection(url,"root","");  

            Statement stmt = conn.createStatement();   
			
			
           ResultSet rs;
		   
		   
		 
          rs = stmt.executeQuery("SELECT * FROM worker WHERE `USERNAME`='"+s1+"' AND `PASSWORD`='"+s2+"'");
			 
			  while ( rs.next() ) 
			  {             
                 Name = rs.getString("USERNAME");
                
				 password = rs.getString("PASSWORD");
				 b1=true;
			  }
			  
			   conn.close(); 	
		   }
		   
           catch (Exception e)
		   {
            System.out.println("Got an exception! ");
            System.out.println(e);
           } 
			  
		 
		 if(b1)
		 {  
	 
	     out.print("login successfull"); 
		 String site = new String("dashboard2.jsp");
         response.setStatus(response.SC_MOVED_TEMPORARILY);
         response.setHeader("Location", site); 
      
          }  
    else{  
        out.print("Sorry UserName or Password Error!"); 
        out.println("<br>");		
		out.println("<br>");	
		out.println("<br>");	
       
        }  
				
		  %>
		
		  
		  
 
 </center>
 </BODY>
 </HTML>
 