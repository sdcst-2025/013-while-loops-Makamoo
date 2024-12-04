##### Problem 1
"""
Have the user enter a username and password.
Repeat this until both the username and password match the 
following:
username: admin
password: 12345
If they guess more than 3 times, they are not allowed to guess
any more and the program will end.
(2 marks)

inputs:
str username
str password

outputs:
Access granted
Access denied

example:
example:
Enter username: fred
Enter password: password
Access denied
Enter username: admin
Enter password: password
Access denied
Enter username: admin
Enter password: 1234
Access denied
Too many failed attempts. Access denied.
"""
doomclock = 0
username = ""
password = ""
while doomclock != 3:
    doomclock = doomclock + 1
    if username != "admin" or password != "12345":
        username = input("what is the username ")
        password = input("what is the password ")
        if username != "admin" or password != "12345":
            print("access denied")
        elif username == "admin" and password == "12345":
            print("access granted")
            exit()

print("Too many failed attempts. Access denied!")