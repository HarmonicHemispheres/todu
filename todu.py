#!/usr/bin/env python3

import sys
import datetime as dtm
from time import gmtime, strftime
from operator import itemgetter

# ========== GLOBALS FUNCS  ========== 

def tasklist(opt):
    data_path = "/Users/themusicman/bin/todu_data.txt"
    help_path = "/Users/themusicman/bin/todu_help.txt"
    if (opt == "r"):
        return open(data_path, "r").read() 
    if (opt == "w"):
        return open(data_path, "w+") 

def main(arg=sys.argv):
    if(len(arg) == 1 or "-" in arg[1]):
        show_task(arg[1:])
        return
    if (arg[1] == "add"):
        add_task(arg[2], arg[3])
        show_task()
    elif (arg[1] == "flag"):
       add_flag(arg[1:]) 
    elif (arg[1] == "etask"):
        edit_task(arg[2], arg[3])
    elif (arg[1] == "edate"):
        edit_dt(arg[2], arg[3])
    elif (arg[1] == "clear"):
        clear()
    elif (arg[1] == "rm"):
        rm_task(arg[2], arg[2:]) 
    elif (arg[1] == "help"):
        show_funcs(help_path)

# ========== FUNCTIONS ========== 

"""
This function prints the contents of todu_help.txt
to stdout. this provides a useful function for seeing
what commands are available for todu.
"""
def show_funcs(help_path):
    output = open(help_path, "r").read()
    for i in output.splitlines():
        print(i)
"""
This function returns the date of today, or if "wk"
then it returns the date of 7 days from today.
"""
def today(wk=0):
    today = strftime("%Y-%m-%d", gmtime())
    if (wk):
        today = today.split("-")
        today[2] = str( int(today[2]) + 7 )
        today = "-".join(today)
        return today
    else:
        return today

# this function clears all tasks in todu_data.txt
def clear():
    tasks = tasklist("w")

"""
This function takes the list of lines of tasks and
writes them to todu_data.txt
"""
def wl(L):
    TASKS = tasklist("w") 
    for i in L:
        TASKS.write(i + "\n")

def time_left(date):
    dt = date.split("-")
    tday = today().split("-")
    d0 = dtm.date(int(tday[0]), int(tday[1]), int(tday[2]))
    d1 = dtm.date(int(dt[0]), int(dt[1]), int(dt[2]))
    dlta = d1 - d0
    # dtm.datetime.strptime(date, '%Y-%m-%d')
    return str(dlta.days + 1)

"""
This function prints the contents of todu_data.txt
to stdout. extra parameters may be passed to this
function in order to print out specific information.
SEE: todu_help.txt for a complete list of extra commands
"""
def show_task(cmdsList=[]):
    sh_id = 1
    sh_ordr = 0
    sh_thisweek = 0
    sh_lft = 0
    sh_fl = 0
    for i in cmdsList:
        if (i == "-id"):
            sh_id = 0
        elif (i == "-ordr"):
            sh_ordr = 1
        elif (i == "-wk"):
            sh_thisweek = 1
        elif (i == "-lft"):
            sh_lft = 1
        elif (i == "-fl"):
            sh_fl = 1

    tasks = tasklist("r")
    tl = [i.split("--") for i in tasks.splitlines()]
    sp = 0
    sp_id = 0
    for i in tl:
        if (len(i[1]) > sp):
            sp = len(i[1])
        if (len(i[0]) > sp_id):
            sp_id = len(i[0])

    if (sh_ordr):
        tl.sort(key=itemgetter(2))
    for i in tl:
        # check if this line should be printed
        prt = 1
        if (sh_thisweek):
            onewk = today(wk=1)
            if (i[2] > onewk):
               # print("---->", i[2], "---->", onewk)
                prt = 0
        if (prt):
            output = ""
            curlen = len(i[0])
            if(sh_id):
                output += i[0] + " "*(sp_id - curlen + 2)
                ID = i[0]
            curlen = len(i[1])
            output += i[1] + " "*(sp - curlen + 3) + i[2] + ",  "            
            output += dtm.datetime.strptime(i[2], '%Y-%m-%d').strftime("%a") + "  "
            if (sh_lft):
                output += time_left(i[2]) + "  " 
            if (sh_fl):
                output += i[3] + " "
            print(output)

"""
Generates an id for the new task based 
on the first open slot.
"""
def gen_key():
    tasks = tasklist("r")
    tl = tasks.splitlines()
    index = 0
    for ln in tl:
        if (int(ln.split("--")[0]) != index):
            return index
        index += 1
    return index

def rm_task(ID, arg):
    rm_fl = 0
    for i in arg:
        if (i == "-fl"):
            rm_fl = 1

    TASKS = tasklist("r") 
    tl = TASKS.splitlines()
    for i in range(len(tl)):
        if (int(tl[i].split("--")[0]) == int(ID) ):
            if (rm_fl):
                newline = tl[i].split("--")
                newline[3] = " "
                newline = "--".join(newline)
                tl[i] = newline
            else:
                tl.remove(tl[i])
            break
    wl(tl) 

def add_task(item, date):
    TASKS = tasklist("r") 
    tl = TASKS.splitlines()

    if (len(sys.argv) >= 5):
        group = sys.argv[4]
    else:
        group = " "
    ID = gen_key()
    tl.append(str(ID) + "--"  + item + "--" + date + "--" + group + "--")    
    if (len(tl) > 1):
        tl = sorted(tl, key=lambda x: int(x.split("--")[0]))
    wl(tl)   

def add_flag(arg):
    ID = arg[1]
    flag = arg[2]
    tasks = tasklist("r")
    tl = tasks.splitlines()
    for i in range(len(tl)):
        lnsplit = tl[i].split("--")
        if (lnsplit[0] == ID):
            new = tl[i].split("--")[3] + " " + flag 
            tl[i] = "--".join( tl[i].split("--")[:3] + [new]) + "--"
    wl(tl)

def edit_task(task_id, newts):
    tasks = tasklist("r")
    tl = tasks.splitlines()

    for i in range(len(tl)):
        i_spl = tl[i].split("--")
        if (i_spl[0] == task_id):
            i_spl[1] = newts
            tl[i] = "--".join(i_spl)
            break
    wl(tl)

def edit_dt(task_id, newdt):
    tasks = tasklist("r")
    tl = tasks.splitlines()

    for i in range(len(tl)):
        i_spl = tl[i].split("--")
        if (i_spl[0] == task_id):
            i_spl[2] = newdt
            tl[i] = "--".join(i_spl)
            break
    wl(tl)

# ========== MAIN ========== 

main()

