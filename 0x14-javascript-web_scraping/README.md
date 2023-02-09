##  0x14. JavaScript - Web scraping



#   0. Readme

Write a script that reads and prints the content of a file.

*   The first argument is the file path
*   The content of the file must be read in `utf-8`
*   If an error occurred during the reading, print the error object

```
guillaume@ubuntu:~/0x14$ cat cisfun
C is super fun!
guillaume@ubuntu:~/0x14$ ./0-readme.js cisfun
C is super fun!

guillaume@ubuntu:~/0x14$ ./0-readme.js doesntexist
{ Error: ENOENT: no such file or directory, open 'doesntexist'
    at Error (native)
  errno: -2,
  code: 'ENOENT',
  syscall: 'open',
  path: 'doesntexist' }
guillaume@ubuntu:~/0x14$ 
```
