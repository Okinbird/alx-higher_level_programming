##  0x11. Python - Network #1



#   0. What's my status? #0

Write a Python script that fetches `https://alx-intranet.hbtn.io/status`

*   You must use the package `urllib`
*   You are not allowed to import any packages other than `urllib`
*   The body of the response must be displayed like the following example (tabulation before `-`)
*   You must use a `with` statement

```
guillaume@ubuntu:~/0x11$ ./0-hbtn_status.py | cat -e
Body response:$
    - type: <class 'bytes'>$
    - content: b'OK'$
    - utf8 content: OK$
guillaume@ubuntu:~/0x11$ 
```



#   1. Response header value #0

Write a Python script that takes in a URL, sends a request to the URL and displays the value of the `X-Request-Id` variable found in the header of the response.

*   You must use the packages `urllib` and `sys`
*   You are not allow to import packages other than urllib and sys
*   The value of this variable is different for each request
*   You don’t need to check arguments passed to the script (number or type)
*   You must use a `with` statement

```
guillaume@ubuntu:~/0x11$ ./1-hbtn_header.py https://alx-intranet.hbtn.io
ade2627e-41dd-4c34-b9d9-a0fa0f47b237
guillaume@ubuntu:~/0x11$ 
guillaume@ubuntu:~/0x11$ ./1-hbtn_header.py https://alx-intranet.hbtn.io
6593e1f5-1b4b-4c9f-9c0e-72ab525b850f
guillaume@ubuntu:~/0x11$ 
```



#   2. POST an email #0

Write a Python script that takes in a URL and an email, sends a `POST` request to the passed URL with the email as a parameter, and displays the body of the response (decoded in `utf-8`)

*   The email must be sent in the `email` variable
*   You must use the packages `urllib` and `sys`
*   You are not allowed to import packages other than `urllib` and sys
*   You don’t need to check arguments passed to the script (number or type)
*   You must use the `with` statement

Please test your script in the sandbox provided, using the web server running on port 5000

```
guillaume@ubuntu:~/0x11$ ./2-post_email.py http://0.0.0.0:5000/post_email hr@holbertonschool.com
Your email is: hr@holbertonschool.com
guillaume@ubuntu:~/0x11$ 
```


#   3. Error code #0

Write a Python script that takes in a URL, sends a request to the URL and displays the body of the response (decoded in `utf-8`).

*   You have to manage `urllib.error.HTTPError` exceptions and print: `Error code:` followed by the HTTP status code
*   You must use the packages `urllib` and `sys`
*   You are not allowed to import other packages than `urllib` and `sys`
*   You don’t need to check arguments passed to the script (number or type)
*   You must use the `with` statement

Please test your script in the sandbox provided, using the web server running on port 5000

```
guillaume@ubuntu:~/0x11$ ./3-error_code.py http://0.0.0.0:5000
Index
guillaume@ubuntu:~/0x11$ ./3-error_code.py http://0.0.0.0:5000/status_401
Error code: 401
guillaume@ubuntu:~/0x11$ ./3-error_code.py http://0.0.0.0:5000/doesnt_exist
Error code: 404
guillaume@ubuntu:~/0x11$ ./3-error_code.py http://0.0.0.0:5000/status_500
Error code: 500
guillaume@ubuntu:~/0x11$ 
```



