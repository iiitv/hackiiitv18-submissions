  <% 
	
		out.println("<u>");
		out.println("REQUEST FROM " );
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
				
				
				
				%> 
				
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