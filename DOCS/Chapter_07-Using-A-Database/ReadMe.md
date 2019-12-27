# Chapter 07 | Using a Database | Putting Python's DB-API to Use #

* We have stored the visitor data into text file, though the information is saved, but it is not in a helpful state to give certain other information.
* We need to store it in a RDBMS, to use SQL like language to retrieve data.
* 4 Steps are involved in achieving this.
    - Install MySQL Server
    - Install a MySQL database driver for Python.
    - Create our WebApp's database and tables
    - Create Code to work with our webapp's database and tables.
* Installing MySql Server is pretty straight forward. We can use any package manager available for the OS, or install directly from the MYSQL webpage.

## DataBase Connector for Python ##

* Python interpreter comes with the support to work with database.
* A standard APIs called DB-APIs are provide by Python.
* For the above DB-APIs to work with database like MySQL, we need to install MySQL Connector/Driver program.
* The biggest advantage of DB-APIs is that we can change the underlying Database technology completely still the application code will still work.
* Download the MySQL DB driver from the MySQL Website.
* Installing the DB Driver in a Virtual env can be challenging.
    - Activate your Virtual ENV.
    - Go to the Untared directory of the DB Driver.
    - `python setup.py install`
    - This will require some dependency.
        + `python -m pip uninstall dnspython` : Un-install `dnspython` first
        + `python -m pip install dnspython` : Install `dnspython`
        + `python -m pip install protobuf==3.6.1` : Install a particular version of `protobuf`

## Create Database and Tables ##
* We can login to MySQL prompt by using the below command.
    - `mysql -u root -p` : username is root, and it will ask for password, which we might have given during the installation of MySQL.
* `create database vsearchlogDB;` : Create the database.
* `GRANT ALL PRIVILEGES ON * . * TO 'vsearch'@'localhost';` grants `vsearch` user all access to the database.
* Till now everything was happening with `root` user, now we will use the `vsearch` user to create database.
* `mysql -u vsearch -p vsearchlogDB` : login as `vsearch` user for the `vsearchlogDB`.
* We need to create table called **log**.

````sql
create table log(id int auto_increment primary key,
    ts timestamp default current_timestamp,
    phrase varchar(128) not null,
    letters varchar(32) not null,
    ip varchar(16) not null,
    browser_string varchar(256) not null,
    results varchar(64) not null);
````

* `describe log` : show the table information.

## DB-API connection to Database ##

### DB-API - Define Connection ###
* These 4 information is required while connecting toe the MySql DB.
    - The IP address/name of the computer running the MySql Server.
    - The user ID to use.
    - The password associated with the user ID.
    - The name of the database the user ID wants to interact.
* These 4 information can be stored in a dictionary and passed onto while creating connection.

````python
dbconfig = {
    "host": "127.0.0.1",
    "user": "vsearch",
    "password": "hello",
    "database": "vsearchlogDB",
}
````

### DB-API - Establish Connection ###
* We have to import the MySql Connector.
    - `import mysql.connector`
* We should establish connection with the DB Server.
    - `conn = mysql.connector.connect(**dbconfig)`
* We also need a `cursor` to execute SQL commands on DB.
    - `cursor = conn.cursor()`

### DB-API - SQL ###
* SQL queries are often passed in a `""" """` triple quotes, as the SQL can run into multiple line.
* `_SQL = """select * from log"""` : the SQL statement is stored.
* `cursor.execute(_SQL)` : Send the SQL query to the server
    - The result is not immediately returned, we have request them
* `.fetchone()` : retrieves a single row of results.
* `.fetchmany()` : retrieve the number of row that make up the results.
* `.fetchall()` : retrieve all the row that make up the results.
  
