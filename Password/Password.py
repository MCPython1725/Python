import sys
import time

pwd1="MCPython17"#Type Your Password Inside The Double Inverted Comma.

for i in range(4,-1,-1):
    pwd=input("Password:")
    time.sleep(0.6)
    if pwd==pwd1:
        break
    elif i!=0:
        print("Wrong Password:Try Again:Chance Left =",i)
    else:
        print("Wrong Password:Access is Denied")
        sys.exit()

print("Correct Password")
time.sleep(1)
#Write Your Program Below This Comment.
