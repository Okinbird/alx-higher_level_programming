##  0x10. Python - Network #0



#   0. cURL body size

Write a Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response

*    The size must be displayed in bytes
*    You have to use `curl`

Please test your script in the sandbox provided, using the web server running on port 5000

```
guillaume@ubuntu:~/0x10$ ./0-body_size.sh 0.0.0.0:5000
10
guillaume@ubuntu:~/0x10$ 
```


#   1. cURL to the end

Write a Bash script that takes in a URL, sends a `GET` request to the URL, and displays the body of the response

*   Display only body of a `200` status code response
*   You have to use `curl`

Please test your script in the sandbox provided, using the web server running on port 5000

```
guillaume@ubuntu:~/0x10$ ./1-body.sh 0.0.0.0:5000/route_1 ; echo ""
Route 2
guillaume@ubuntu:~/0x10$ 
```


#   2. cURL Method

Write a Bash script that sends a `DELETE` request to the URL passed as the first argument and displays the body of the response

*   You have to use `curl`

Please test your script in the sandbox provided, using the web server running on port 5000

```
guillaume@ubuntu:~/0x10$ ./2-delete.sh 0.0.0.0:5000/route_3 ; echo ""
I'm a DELETE request
guillaume@ubuntu:~/0x10$ 
```