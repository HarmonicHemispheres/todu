#!/usr/bin/env python3

import sys
import datetime as dt


# ========== GLOBALS FUNCS  ========== 

def tasklist(opt):
    if (opt == "r"):
        return open("data.txt", "r").read() 
    if (opt == "w"):
        return open("data.txt", "w") 

def main(arg=sys.argv):
    if(len(arg) == 1):
        show_task()
        return
    if (arg[1] == "add"):
        add_task(arg[2], arg[3])
    elif (arg[1] == "clear"):
        clear()
    elif (arg[1] == "rm"):
        rm_task(arg[2]) 

# ========== FUNCTIONS ========== 
def today():
    return dt.today().strftime("%m/%d/%Y")

def clear():
    tasks = tasklist("w")

def wl(L):
    TASKS = tasklist("w") 
    for i in L:
        TASKS.write(i + "\n")

def show_task():
    tasks = tasklist("r")
    for i in tasks.splitlines():
        print(i)

def gen_key():
    # generates a id for the new task based 
    # on the first open slot.

    return

def rm_task(ID):
    TASKS = tasklist("r") 
    tl = TASKS.splitlines()
    for i in tl:
        if (int(i.split()[0]) == int(ID) ):
            tl.remove(i)
            break
    wl(tl) 

def add_task(item, date):
    TASKS = tasklist("r") 
    tl = TASKS.splitlines()

    if (len(sys.argv) == 5):
        group = sys.argv[4]
    else:
        group = ""

    ID = 0
    for i in tl:
        ID += 1
    tl.append(str(ID) + " "  + item + " --- " + date + " " + group)    
    wl(tl)   
 
# ========== MAIN ========== 

main()

