from playsound import playsound
import time as q
import colorama
from colorama import Fore, Style 
import os
x="Sayar Thurain "


b=len(x)
def cake(): 
    print(Fore.WHITE+" "*23,"i  i  i  i")
    y=q.sleep(.1)
    print(Fore.YELLOW+" "*23,"i  i  i  i")
    y=q.sleep(.1)
    print(Fore.YELLOW+" "*23,"i  i  i  i")
    y=q.sleep(.1)
    print(Fore.CYAN+" "*21,"__i__i__i__i__")
    y=q.sleep(.1)
    print(Fore.CYAN+" "*20,"|"," "*12,"|")
    y=q.sleep(0.5)
    print(Fore.CYAN+" "*20,"|"," "*12,"|")
    y=q.sleep(.5)
    print(Fore.CYAN+" "*20,"|"," "*12,"|")
    y=q.sleep(.5)
    print(Fore.CYAN+" "*16,"-"*24)
    y=q.sleep(.5)
    print(Fore.CYAN+" "*16,"|"," "*20,"|")
    y=q.sleep(.5)
    print(Fore.CYAN+" "*16,"|"," "*int((20-b)/2),x," "*int((20-b)/2-2),"|")
    y=q.sleep(.5)
    print(Fore.CYAN+" "*16,"|"," "*20,"|")
    y=q.sleep(.5)
    print(Fore.CYAN+" "*16,"-"*24)
 
 
def menu():
    print()
    
    for i in range(4):
        if i==3:
            print(Fore.RED+" "*13,"HAPPY HAPPY BIRTHDAY TO YOU")
        elif i==0 or i==1:
            print(Fore.RED+" "*15,"HAPPY BIRTHDAY TO YOU")
        elif i==2:
            print(Fore.YELLOW+" "*15,"HAPPY BIRTHDAY","*",x.upper(),"*","\n")
        q.sleep(.8)
            
        print()
    
def heart():
    playsound('welcome.mp3')
    for row in range(6):
        for col in range(7):
            if (row==0 and col %3 != 0)or(row==1 and col %3==0) or(row-col==2) or(row+col==8):
                print("💙",end=" ")
            else:
                print(end="  ")
        print() 
print(Fore.MAGENTA+"#"*9,"BIRTHDAY WISHES FOR MY UNCLE👫","*"+x.upper()+"*","#"*9)
q.sleep(1.5)
menu()
cake()
 
print(Fore.RED+" "*14,"Many Many Returns Of The Day\n \n\n".upper())
q.sleep(2)
x="Happy, healthy, exceptional, rocking birthday to you my uncle!"
a=x.split()
for i in a:
    print("\t\t",i.title())
    q.sleep(1)
print(Fore.RED+"")
q.sleep(2)

heart()
os.system('python z.py	')
