import time
import os

print("""
██   ██  ██████  ████████ ███    ██  █████         ██████  ███████ 
██  ██  ██    ██    ██    ████   ██ ██   ██       ██    ██ ██      
█████   ██    ██    ██    ██ ██  ██ ███████ █████ ██    ██ ███████ 
██  ██  ██    ██    ██    ██  ██ ██ ██   ██       ██    ██      ██ 
██   ██  ██████     ██    ██   ████ ██   ██        ██████  ███████                                                                    
""")
print("""
[1] Continue With Setup
[2] I've Already Done Setup
""")
setup = input("[?]: ")
if setup == '1':
    name = input(str("Please enter your User Name To Be Displayed: "))
    pas = input(str("Please enter your Password to Login: "))
    lines = [name]
    with open('user/username.txt', 'w') as f:
        f.writelines(lines)

    lines2 = [pas]
    with open('user/password.txt', 'w') as f:
        f.writelines(lines2)