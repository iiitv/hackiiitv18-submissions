 <%@page import="java.sql.*" %>

<!DOCTYPE html>
<html lang="en">
<head>


<style>
* {
    box-sizing: border-box;
}

body {
    font-family: Arial, Helvetica, sans-serif;
}

/* Style the header */
header {
    background-color: #666;
    padding: 30px;
    text-align: center;
    font-size: 35px;
    color: white;
}

/* Container for flexboxes */
section {
    display: -webkit-flex;
    display: flex;
}

/* Style the navigation menu */
nav {
    -webkit-flex: 1;
    -ms-flex: 1;
    flex: 1;
    background: #ccc;
    padding: 20px;
}

/* Style the list inside the menu */
nav ul {
    list-style-type: none;
    padding: 0;
}

/* Style the content */
article {
    -webkit-flex: 3;
    -ms-flex: 3;
    flex: 3;
    background-color: #f1f1f1;
    padding: 10px;
}

/* Style the footer */
footer {
    background-color: #777;
    padding: 10px;
    text-align: center;
    color: white;
}

/* Responsive layout - makes the menu and the content (inside the section) sit on top of each other instead of next to each other */
@media (max-width: 600px) {
    section {
      -webkit-flex-direction: column;
      flex-direction: column;
    }
}

.avatar {
    vertical-align: middle;
    width: 171px;
    height: 190px;
    border-radius: 50%;
	padding:0px;
	
	opacity: 0.97;
}

</style>
</head>
<body>




<section>
  <nav>
    <img  align="left"  border="black" src="avatar3.png" alt="Avatar" class="avatar">
  </nav>
  
  <article>
  


<% 
	out.println("<u> WELCOME KARTIKEY </U> " );
	out.println("<br>");
		out.println("<br>");
		out.println("<br>");
		out.println("<br>");
		out.println("<br>");
		out.println("<br>");
		out.println("<u>");
		out.println("REQUESTS FROM " );
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
		   
		   
		 
          rs = stmt.executeQuery("SELECT * FROM requests ");
			 
			  while ( rs.next() ) 
			  
			  
			  { String USER = rs.getString("USER");
			 
				String MOBILE = rs.getString("MOBILE");
				
                
				String ADDRESS1 = rs.getString("ADDRESS1");
				
				String ADDRESS2 = rs.getString("ADDRESS2");
                
				String PIN = rs.getString("pin");
				
				String WORKER_REQUESTED = rs.getString("WORKER_REQUESTED");
				
				 
				 
				 out.println("NAME - " +USER );
               out.println("<br>");
				out.println("<u> CONTACT DETAILS </u> " );
				out.println("<br>");
				out.println("mobile - " +MOBILE );
				out.println("address - " + ADDRESS1 + ADDRESS2);
				out.println("PIN - " +PIN );
				
			out.println("<br>");
			out.println("<br>");
				
				
					
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

  </article>
</section>
<a href="index.html">
	  <input type="submit" name="signup" value="home" style="height:50px;width:200px;font-size:28pt;">
	
	</a>
<footer>
  <p>Footer</p>
</footer>

</body>
</html>
