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
        show_task()
    elif (arg[1] == "clear"):
        clear()
    elif (arg[1] == "rm"):
        rm_task(arg[2]) 

# ========== FUNCTIONS ========== 
def today():
    return dt.today().strftime("%Y-%m-%d")

def clear():
    tasks = tasklist("w")

def wl(L):
    TASKS = tasklist("w") 
    for i in L:
        TASKS.write(i + "\n")

def show_task():

    tasks = tasklist("r")
    tl = tasks.splitlines()
    sorted(tl)
    sp = max(tl, key=len)
    print(sp)
    sp = len(sp.split("--")[1])
    for i in tl:
        t = i.split("--")
        name = t[1]
        date = t[2]
        print(name + " "*sp + date )

def gen_key():
    # generates a id for the new task based 
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
    ID = gen_key()
    tl.append(str(ID) + "--"  + item + "--" + date + "--" + group)    
    if (len(tl) > 1):
        tl = sorted(tl, key=lambda x: int(x.split("--")[0]))
    wl(tl)   
 
# ========== MAIN ========== 

main()

