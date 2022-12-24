# Library-
	LIBRARY MANAGEMENT SYSTEM

This is a library management system built with Python and the MySQL database. 
Your data is gathered and stored in a database that was made using other files in the repository.



necessary information to run code.
---------------------------------

1. Your device needs to be configured with SQL Workbench.
2. You should be comfortable with using SQL to conduct queries.
3. Install the 'pymysql' attachment on the device that connects your IDE to your SQL workbench.
	if pymysql attatchment is not installed in your device then type 'pip install pymysql' on your 
	command prompt and then it will start installing, after that it will be enabled in your system.


Information about files.
-----------------------

createDatabaseLibrary.py --> this file of code will create a Database in your SQL workbench. 

createTableBook --> this will create a table named as book in your database (library), this will store the 
			name of book and quantity.

createTableUser --> this will create a table named as user in your dtabase (library), this will store the 
			users details (name,rollno,semester,year,branch)...etc.

createTableLibrarian --> this will create a table as librarian in your database (library), this will 
			store the details of faculty.

mainLibrary.py --> this will fetch the data from datbase whenever needed and use it, and it will also used to 
			store the data taken from user in database. 
			
NOTE:-
------

The 4 files (createDatabase , and 3 createTable files) needs to be executed only once otherwise mainLibrary will 
show error.
			 
