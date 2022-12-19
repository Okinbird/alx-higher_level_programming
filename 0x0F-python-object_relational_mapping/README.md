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
