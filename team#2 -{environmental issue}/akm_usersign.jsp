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
 <% 
 
 
        String s0="kartikey"; 
		
		String s1=request.getParameter("NAME");
		
		String s2=request.getParameter("MOBILE");
		
		String s3=request.getParameter("adl1");
		
		String s4=request.getParameter("adl2");
		
		String s5=request.getParameter("PIN");
		
	    
		
	
        try 
		  {
			  Class.forName("com.mysql.jdbc.Driver");
            String url = "jdbc:mysql://localhost:3306/akmproject";

            Connection conn = DriverManager.getConnection(url,"root","");  

            Statement stmt = conn.createStatement();   
			
			
           ResultSet rs;
		   
		   
		  stmt.executeUpdate("INSERT INTO requests VALUES('"+s0+"','"+s1+"','"+s2+"','"+s3+"','"+s4+"','"+s5+"')");
		   
		      rs = stmt.executeQuery("SELECT * FROM requests");
			 
	        conn.close(); 	
			 	out.println("<p> REQUESTED SUCESSFULLY </p>");
		   }
		   
           catch (Exception e)
		   {
            
			System.out.println(e);
           }
             
              		 
		   %>
		<a href="index.html">
	  <input type="submit" name="signup" value="home" style="height:50px;width:200px;font-size:28pt;">
	
	</a>
		  
		  
 
 </center>
 </BODY>
 </HTML>
 