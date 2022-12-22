##  0x0F. Python - Object-relational mapping



#   0. Get all states

Write a script that lists all `states` from the database `hbtn_0e_0_usa`:

*   Your script should take 3 arguments: `mysql username`, `mysql password` and `database name` (no argument validation needed)
*   You must use the module `MySQLdb` (`import MySQLdb`)
*   Your script should connect to a MySQL server running on `localhost` at port `3306`
*   Results must be sorted in ascending order by `states.id`
*   Results must be displayed as they are in the example below
*   Your code should not be executed when imported



#   1. Filter states

Write a script that lists all `states` with a `name` starting with `N` (upper N) from the database `hbtn_0e_0_usa`:

*   Your script should take 3 arguments: `mysql username`, `mysql password` and `database name` (no argument validation needed)
*   You must use the module `MySQLdb` (`import MySQLdb`)
*   Your script should connect to a MySQL server running on `localhost` at port `3306`
*   Results must be sorted in ascending order by `states.id`
*   Results must be displayed as they are in the example below
*   Your code should not be executed when imported



#   2. Filter states by user input

Write a script that takes in an argument and displays all values in the `states` table of `hbtn_0e_0_usa` where `name` matches the argument.

*   Your script should take 4 arguments: `mysql username`, `mysql password`, `database name` and `state name searched` (no argument validation needed)
*   You must use the module `MySQLdb` (`import MySQLdb`)
*   Your script should connect to a MySQL server running on `localhost` at port `3306`
*   You must use `format` to create the SQL query with the user input
*   Results must be sorted in ascending order by `states.id`
*   Results must be displayed as they are in the example below
*   Your code should not be executed when imported



#   3. SQL Injection...

Wait, do you remember the previous task? Did you test `"Arizona'; TRUNCATE TABLE states ; SELECT * FROM states WHERE name = '"` as an input?

```
guillaume@ubuntu:~/0x0F$ ./2-my_filter_states.py root root hbtn_0e_0_usa "Arizona'; TRUNCATE TABLE states ; SELECT * FROM states WHERE name = '"
(2, 'Arizona')
guillaume@ubuntu:~/0x0F$ ./0-select_states.py root root hbtn_0e_0_usa
guillaume@ubuntu:~/0x0F$ 
```

What? Empty?

Yes, it’s an [SQL injection](https://alx-intranet.hbtn.io/rltoken/qzLjdkHPTue2U1isMj5fJA) to delete all records of a table…

Once again, write a script that takes in arguments and displays all values in the `states` table of `hbtn_0e_0_usa` where `name` matches the argument. But this time, write one that is safe from MySQL injections!

*   Your script should take 4 arguments: `mysql username`, `mysql password`, `database name` and `state name searched` (safe from MySQL injection)
*   You must use the module `MySQLdb` (`import MySQLdb`)
*   Your script should connect to a MySQL server running on `localhost` at port `3306`
*   Results must be sorted in ascending order by `states.id`
*   Results must be displayed as they are in the example below
*   Your code should not be executed when imported



#   4. Cities by states

Write a script that lists all `cities` from the database `hbtn_0e_4_usa`

*   Your script should take 3 arguments: `mysql username`, `mysql password` and `database name`
*   You must use the module `MySQLdb` (`import MySQLdb`)
*   Your script should connect to a MySQL server running on `localhost` at port `3306`
*   Results must be sorted in ascending order by `cities.id`
*   You can use only execute`()` once
*   Results must be displayed as they are in the example below
*   Your code should not be executed when imported

```
guillaume@ubuntu:~/0x0F$ cat 4-cities_by_state.sql | mysql -uroot -p
Enter password: 
guillaume@ubuntu:~/0x0F$ ./4-cities_by_state.py root root hbtn_0e_4_usa
(1, 'San Francisco', 'California')
(2, 'San Jose', 'California')
(3, 'Los Angeles', 'California')
(4, 'Fremont', 'California')
(5, 'Livermore', 'California')
(6, 'Page', 'Arizona')
(7, 'Phoenix', 'Arizona')
(8, 'Dallas', 'Texas')
(9, 'Houston', 'Texas')
(10, 'Austin', 'Texas')
(11, 'New York', 'New York')
(12, 'Las Vegas', 'Nevada')
(13, 'Reno', 'Nevada')
(14, 'Henderson', 'Nevada')
(15, 'Carson City', 'Nevada')
guillaume@ubuntu:~/0x0F$
```


#   5. All cities by state

Write a script that takes in the name of a state as an argument and lists all `cities` of that state, using the database `hbtn_0e_4_usa`

*   Your script should take 4 arguments: `mysql username`, `mysql password`, `database name` and `state name` (SQL injection free!)
*   You must use the module `MySQLdb` (`import MySQLdb`)
*   Your script should connect to a MySQL server running on `localhost` at port `3306`
*   Results must be sorted in ascending order by `cities.id`
*   You can use only `execute()` once
*   The results must be displayed as they are in the example below
*   Your code should not be executed when imported

```
guillaume@ubuntu:~/0x0F$ ./5-filter_cities.py root root hbtn_0e_4_usa Texas

guillaume@ubuntu:~/0x0F$ cat 4-cities_by_state.sql | mysql -uroot -p
Enter password: 
guillaume@ubuntu:~/0x0F$ ./5-filter_cities.py root root hbtn_0e_4_usa Texas
Dallas, Houston, Austin
guillaume@ubuntu:~/0x0F$ ./5-filter_cities.py root root hbtn_0e_4_usa Hawaii

guillaume@ubuntu:~/0x0F$
```


#   6. First state model

Write a python file that contains the class definition of a `State` and an instance `Base = declarative_base()`:

*   `State` class:
    -   inherits from `Base` [Tips]
    -   links to the MySQL table `states`
    -   class attribute `id` that represents a column of an auto-generated, unique integer, can’t be null and is a primary key
    -   class attribute `name` that represents a column of a string with maximum 128 characters and can’t be null
*   You must use the module `SQLAlchemy`
*   Your script should connect to a MySQL server running on `localhost` at port `3306`
*   **WARNING:** all classes who inherit from `Base` **must** be imported before calling `Base.metadata.create_all(engine)`

```
guillaume@ubuntu:~/0x0F$ cat 6-model_state.sql | mysql -uroot -p
Enter password: 
ERROR 1146 (42S02) at line 4: Table 'hbtn_0e_6_usa.states' doesn't exist

guillaume@ubuntu:~/0x0F$ ./6-model_state.py root root hbtn_0e_6_usa
guillaume@ubuntu:~/0x0F$ cat 6-model_state.sql | mysql -uroot -p
Enter password: 
Table   Create Table
states  CREATE TABLE `states` (\n  `id` int(11) NOT NULL AUTO_INCREMENT,\n  `name` varchar(128) NOT NULL,\n  PRIMARY KEY (`id`)\n) ENGINE=InnoDB DEFAULT CHARSET=latin1
guillaume@ubuntu:~/0x0F$
```


#   7. All states via SQLAlchemy

Write a script that lists all `State` objects from the database `hbtn_0e_6_usa`

*   Your script should take 3 arguments: `mysql username`, `mysql password` and `database name`
*   You must use the module `SQLAlchemy`
*   You must import `State` and `Base` from `model_state` - `from model_state import Base, State`
*   Your script should connect to a MySQL server running on `localhost` at port `3306`
*   Results must be sorted in ascending order by `states.id`
*   The results must be displayed as they are in the example below
*   Your code should not be executed when imported

```
guillaume@ubuntu:~/0x0F$ cat 7-model_state_fetch_all.sql | mysql -uroot -p hbtn_0e_6_usa
Enter password: 
guillaume@ubuntu:~/0x0F$ ./7-model_state_fetch_all.py root root hbtn_0e_6_usa
1: California
2: Arizona
3: Texas
4: New York
5: Nevada
guillaume@ubuntu:~/0x0F$
```



