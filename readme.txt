
OVERVIEW:
    DO is a todo list manager with lots of capabilities as well as
    a simple method to implement. its about DOing things on the list
    instead of having things toDO.

    This python script is a management file for a todo.data
    file which allows the user to easily manage a todo list from the
    command line. 

FILES:
    readme.txt          -This readme file
    todu.sh             -manager script to run program and echo results
    todu-core.py        -source script to parse data from tasks.dat
    tasks.txt           -data file with all of tasks and information
    .todu-conf          -settings for how update should function when called

FUNCTIONS:
    todu add "task" "date"      -adds the task to the todolist
        -sub=id                   -adds this task as a sub task of id
        -days=X                   -adds this task to X days from now
        -weeks=X                  -adds task to X weeks from now
    todu update                 -follows settings in .todo-conf
    todu edit id type "new"     -changes the the task desc to Y 
        type=desc                 -changes the desc for the task
        type=note                 -changes the note for the task
        type=flag                 -replaces all flags with "new" flag
        type=date                 -changes the due date for the task
        -a                        -appends changes instead of replaces
    todu note id                -shows note for the task
        -e "X"                    -note = X
        -a "X"                    -append X to the note
    todu flag id X              -adds the flag X to the id
    todu                        -displays all tasks and due dates
    todu sh                     -displays all tasks and due dates
        -id                       -shows id#s for tasks
        -day-X                    -only show X days tasks from now
        -mon-X                    -only show X months from now tasks
        -subs                     -shows sub tasks
        -left                     -shows time left on tasks
        -flag                     -shows flags for each task    
        -flag-X                   -only show tasks X flag 
    todu flags                  -shows all the flags you have on tasks
    todu late                   -shows all tasks past their due date
    
CONFIGURATION FILE:
.todo-conf Options
    remove-flagged=X            -will remove flagged tasks with X tag
        X=                        -removes all flagged tasks
        X=whatever                -tags can be anything defined by the user
    remove-past                 -will remove tasks with dates before today
    
