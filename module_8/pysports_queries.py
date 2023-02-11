import mysql.connector  
# Connect to the database 
db = mysql.connector.connect(     host="localhost",     user="pysports_user",     passwd="MySQL8IsGreat!",     database="pysports" )  
# Create a cursor 
cursor = db.cursor()  
# Write the query 
query = "SELECT team_id, team_name, mascot FROM team"  
# Execute the query 
cursor.execute(query)  
# Iterate over the cursor 
for team in cursor:     print(team)  
# Close the cursor 
cursor.close()  
# Close the database 
db.close()
