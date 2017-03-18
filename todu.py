#!/usr/bin/env python3

import sys
from time import gmtime, strftime
from operator import itemgetter

# ========== GLOBALS FUNCS  ========== 

def tasklist(opt):
    if (opt == "r"):
        return open("data.txt", "r").read() 
    if (opt == "w"):
        return open("data.txt", "w+") 

def main(arg=sys.argv):
    if(len(arg) == 1 or "-" in arg[1]):
        show_task(arg[1:])
        return
    if (arg[1] == "add"):
        add_task(arg[2], arg[3])
        show_task()
    elif (arg[1] == "clear"):
        clear()
    elif (arg[1] == "rm"):
        rm_task(arg[2]) 
    elif (arg[1] == "show"):
        show_task(arg[1:])

# ========== FUNCTIONS ========== 
def today():
    return dt.today().strftime("%Y-%m-%d")

def clear():
    tasks = tasklist("w")

def wl(L):
    TASKS = tasklist("w") 
    for i in L:
        TASKS.write(i + "\n")


# todays date = strftime("%Y-%m-%d", gmtime()) 
def show_task(cmdsList=[]):
    sh_id = 1
    sh_ordr = 0
    for i in cmdsList:
        if (i == "-id"):
            sh_id = 1
        if (i == "-ordr"):
            sh_ordr = 1
    tasks = tasklist("r")
    tl = [i.split("--") for i in tasks.splitlines()]
    sp = 0
    for i in tl:
        if (len(i[1])>sp):
            sp = len(i[1])
    if (sh_ordr):
        tl.sort(key=itemgetter(2))
    for i in tl:
        output = ""
        curlen = len(i[1])
        if(sh_id):
            output += i[0] + " "
            ID = i[0]
        output += i[1] + " "*(sp - curlen + 3) + i[2] + " "   # name + date
        
        print(output)

def gen_key():
    # generates an id for the new task based 
    # on the first open slot.

    tasks = tasklist("r")
    tl = tasks.splitlines()
    index = 0
    for ln in tl:
        if (int(ln.split("--")[0]) != index):
            return index
        index += 1
    return index

def rm_task(ID):
    TASKS = tasklist("r") 
    tl = TASKS.splitlines()
    for i in tl:
        if (int(i.split("--")[0]) == int(ID) ):
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
    ID = gen_key()
    tl.append(str(ID) + "--"  + item + "--" + date + "--" + group)    
    if (len(tl) > 1):
        tl = sorted(tl, key=lambda x: int(x.split("--")[0]))
    wl(tl)   
 
# ========== MAIN ========== 

main()

