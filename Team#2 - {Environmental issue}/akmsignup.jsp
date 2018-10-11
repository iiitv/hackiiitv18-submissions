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
 
		String s1=request.getParameter("FIRST");
		
		String s2=request.getParameter("LAST");
		
		String s3=request.getParameter("MOBILE");
		
		String s4=request.getParameter("AADHAR");
		
		String s5=request.getParameter("USERNAME");
		
		String s6=request.getParameter("PASSWORD");
		
		String s7=request.getParameter("CONFIRM");
		
		String s8=request.getParameter("GENDER");
	
		String s9=request.getParameter("state");
		
		String s10=request.getParameter("district");
		
		String s11=request.getParameter("agree");
		
		
		if(s6.compareTo(s7)==0)
		{
        try 
		  {
			  Class.forName("com.mysql.jdbc.Driver");
            String url = "jdbc:mysql://localhost:3306/akmproject";

            Connection conn = DriverManager.getConnection(url,"root","");  

            Statement stmt = conn.createStatement();   
			
			
           ResultSet rs;
		   
		   
		  stmt.executeUpdate("INSERT INTO worker VALUES('"+s1+"','"+s2+"','"+s3+"','"+s4+"','"+s5+"','"+s6+"','"+s7+"','"+s8+"','"+s9+"','"+s10+"','"+s11+"')");
		   
		      rs = stmt.executeQuery("SELECT * FROM worker");
			 
	        conn.close(); 	
			 	out.println("<p> SIGNED UP SUCESSFULLY </p>");
		   }
		   
           catch (Exception e)
		   {
            out.println("Got a PROBLEM! ");
            out.println("aadhar or mobile already registered");
			System.out.println(e);
           }
             
              		 
		  }
		  
		  else
		  {
		   out.println("<p>password mismatch </p>");
		   }
		 

		 
		  %>
		
		  <a href="index.html">
	  <input type="submit" name="signup" value="home" style="height:50px;width:200px;font-size:28pt;">
	
	</a>
		  
 
 </center>
 </BODY>
 </HTML>
 