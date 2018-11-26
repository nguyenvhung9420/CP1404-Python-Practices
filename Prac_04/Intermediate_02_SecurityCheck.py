
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']


username_input = input("Please type your username, Attention: username is CASE SENSITIVE: ")
username_toprint = ""
passable = False

for username in usernames:
    if username_input == username:
        passable = True
        username_toprint = username
        break

if passable == True:
    print("Welcome {}!".format(username_toprint))
else:
    print("Access Denied.")