  <%@page import="java.sql.*" %>
<html>
 
 <head>
 <title> POST WORKERSEARCH </TITLE>
 <center>
 <font style="algerian"  color="blue">
 
 <H1>  POST WORKERSEARCH </H1>
 </font>
 </center>
 </HEAD>
 <BODY>
 <center>
 <% 
		String s1=request.getParameter("state");
		String s2=request.getParameter("district");
		
		
		out.println("<u>");
		out.println("recylator working in the selected location ");
		out.println("<br>");
		out.println("<br>");
		out.println("<br>");
		out.println("</u>");
		 try 
		  {
			  Class.forName("com.mysql.jdbc.Driver");
            String url = "jdbc:mysql://localhost:3306/akmproject";

            Connection conn = DriverManager.getConnection(url,"root","");  

            Statement stmt = conn.createStatement();   
			
			
           ResultSet rs;
		   
		   
		 
          rs = stmt.executeQuery("SELECT * FROM worker WHERE `STATE`='"+s1+"' AND `DISTRICT`='"+s2+"'");
			 
			  while ( rs.next() ) 
			  { String FIRSTNAME = rs.getString("FIRSTNAME");
                out.println("FIRSTNAME-- " + FIRSTNAME);
				out.println("<br>");
				
				String LASTNAME = rs.getString("LASTNAME");
                out.println("LASTNAME-- " + LASTNAME);
				out.println("<br>");
				
				String MOBILE = rs.getString("MOBILE");
                out.println("MOBILE-- " + MOBILE);
				out.println("<br>");
				
				String AADHAR = rs.getString("AADHAR");
                out.println("AADHAR NO. " + AADHAR);
				out.println("<br>");
				
				String GENDER = rs.getString("GENDER");
                out.println("GENDER " + GENDER);
				out.println("<br>");
				
				String USERNAME = rs.getString("USERNAME");
				
				%> <form>
			  <br>
			<a href="usersign.html">
			
			   <INPUT TYPE="BUTTON" name="confirm" value="confirm" >
			  </a>
			  </form>
				
			<%	System.out.println();
			System.out.println();
			System.out.println();
			  }
			  %>
			 
			  
			  
		<%	   conn.close(); 	
		   }
		   
           catch (Exception e)
		   {
            System.out.println("Got an exception! ");
            System.out.println(e);
           } 
			  
		  %>
		
 
 </center>
 </BODY>
 </HTML>
 