# Import the pyodbc module. 
#This module allows Python to connect to an ODBC database, like SQL Server.
import pyodbc

# The variables hold the server name, database name, username, and password. 
# This is necessary in order to connect to the SQL Server database.
server = 'ServerName'
database = 'DBName'
username = 'user'
password = 'password'

# Connection string:
# This is a formatted string that the ODBC driver uses to know who is connecting (username and password), 
# where they are connecting to (server and database), 
# and what driver they are using to make the connection (ODBC Driver 17 for SQL Server).
connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'

# DRIVER={{ODBC Driver 17 for SQL Server}}: Specifies the ODBC (Open Database Connectivity) 
# driver that's being used to connect to the SQL Server.
# The driver is software that enables the application (in this case, your Python program) to interact with the database system.
# ODBC Driver 17 is a version of Microsoft's ODBC driver for SQL Server.
# SERVER={server}: Server where the SQL Server database is hosted.
# DATABASE={database}: Database on the server that you want to connect to.
# UID={username} and PWD={password}: These specify the username and password used for authentication.

# Establish a connection to the database using the pyodbc.connect() function.
conn = pyodbc.connect(connection_string)

# From the Connection object, we create a new Cursor object. 
# This object is used to execute SQL commands.
cursor = conn.cursor()

# We define the SQL query that we want to execute.
query = 'SELECT * FROM [dbo].[TableName]'

# Use the execute() method of the Cursor object to execute the SQL query.
cursor.execute(query)

# Query executed - now we use fetchall() method of the Cursor object 
# to retrieve all rows of data returned from the query.
rows = cursor.fetchall()

# Finally, loop over each row in the rows list, printing it to the console.
for row in rows:
    print(row)