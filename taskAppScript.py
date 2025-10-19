from datetime import datetime
import os
import sys
import json
def addTask(data, task, desc=""):
    newTask={
                "task": task,
                "status": "To-do",
                "desc" : desc,
                "created": str(datetime.now()),
                "modified": str(datetime.now())
            }
    id="1"
    while True:
        if id not in data["currIds"]:
            data[id]=newTask
            data["currIds"].append(id)
            break
        else:
            id=str(int(id)+1)
    f=open("tasks.json", "w")
    json.dump(data, f, indent=4)
    f.close()
    print(f"Added task: '{task}' | task id: {id}")

def updateTask(data, id, newTask):
    data[id]["task"]=newTask
    data[id]["modified"]=str(datetime.now())
    f=open("tasks.json", "w")
    json.dump(data, f, indent=4)
    print(f"Task with id={id} has been updated to: '{newTask}'")

def deleteTask(data, id):
    deleted=data.pop(id, None)
    if deleted is None:
        print(f"No task with id={id}!")
    else:
        print(f"Task '{deleted["task"]}' with id={id} deleted.")
        data["currIds"].remove(id)
    f=open("tasks.json", "w")
    json.dump(data, f, indent=4)

def deleteAll(data):
    data={"currIds": []}
    f=open("tasks.json", "w")
    json.dump(data, f, indent=4)
    print("All tasks deleted.")

def updateStatus(data, id, newStatus):
    data[id]["status"]=newStatus
    data[id]["modified"]=str(datetime.now())
    f=open("tasks.json", "w")
    json.dump(data, f, indent=4)
    print(f"Status of task '{data[id]["task"]}' with id={id} changed to '{newStatus}'")
    
def listTask(data, arg="All"):
    if arg=="All":
        for i in data["currIds"]:
            print(f"Id: {i}\nTask: {data[i]["task"]}\nStatus: {data[i]["status"]}\nDescription: {data[i]["desc"]}\nCreated: {data[i]["created"]}\nModified: {data[i]["modified"]}\n")
    elif arg=="done":
        for i in data["currIds"]:
            if data[i]["status"]=="Done":
                print(f"Id: {i}\nTask: {data[i]["task"]}\nStatus: {data[i]["status"]}\nDescription: {data[i]["desc"]}\nCreated: {data[i]["created"]}\nModified: {data[i]["modified"]}\n")
    elif arg=="todo":
        for i in data["currIds"]:
            if data[i]["status"]=="To-do":
                print(f"Id: {i}\nTask: {data[i]["task"]}\nStatus: {data[i]["status"]}\nDescription: {data[i]["desc"]}\nCreated: {data[i]["created"]}\nModified: {data[i]["modified"]}\n")
    elif arg=="inprogress":
        for i in data["currIds"]:
            if data[i]["status"]=="In-progress":
                print(f"Id: {i}\nTask: {data[i]["task"]}\nStatus: {data[i]["status"]}\nDescription: {data[i]["desc"]}\nCreated: {data[i]["created"]}\nModified: {data[i]["modified"]}\n")

def listCmds():
    print("""
Available Commands:

Task Management:
  add <task> [description]         - Add a new task with an optional description.
  update <id> <new_task>           - Update the task description for a given task ID.
  delete <id>                      - Delete a task with the specified ID.
  delete-all                       - Delete all tasks.

Status Updates:
  mark-to-do <id>                  - Mark the task status as 'To-do'.
  mark-in-progress <id>           - Mark the task status as 'In-progress'.
  mark-done <id>                   - Mark the task status as 'Done'.

Task Listing:
  list                             - List all tasks.
  list todo                        - List tasks marked as 'To-do'.
  list done                        - List tasks marked as 'Done'.
  list in-progress                 - List tasks marked as 'In-progress'.

Help:
  help                             - Show this help message.

Note: Task IDs are automatically assigned and are required for update, delete, or status change commands.
""")


#main()
if os.path.exists("tasks.json"):
    with open("tasks.json", "r") as f:
        data = json.load(f)
else:
    data = {"currIds": []}

#Trigger help
if len(sys.argv)==1 or sys.argv[1]=="help":
    listCmds()

#Adding tasks:
elif sys.argv[1]=="add":
    if len(sys.argv)<3 or len(sys.argv)>4:
        print("Invalid Arguments! Use 'help' to list commands.")
    elif len(sys.argv)==3:
        addTask(data, sys.argv[2])
    else:
        addTask(data, sys.argv[2], sys.argv[3])

#Updating tasks:
elif sys.argv[1]=="update":
    if len(sys.argv)!=4:
        print("Invalid Arguments! Use 'help' to list commands.")
    else:
        updateTask(data, sys.argv[2],sys.argv[3])

#Deleting tasks:
elif sys.argv[1]=="delete":
    if len(sys.argv)!=3:
        print("Invalid Arguments! Use 'help' to list commands.")
    else:
        deleteTask(data, sys.argv[2])

#Updating Status:
elif sys.argv[1]=="mark-in-progress":
    updateStatus(data, sys.argv[2], "In-progress")
elif sys.argv[1]=="mark-done":
    updateStatus(data, sys.argv[2], "Done")
elif sys.argv[1]=="mark-to-do":
    updateStatus(data, sys.argv[2], "To-do")

#List Tasks:
elif sys.argv[1]=="list":
    if len(sys.argv)==2:
        listTask(data)
    elif sys.argv[2]=="done":
        listTask(data, "done")
    elif sys.argv[2]=="todo":
        listTask(data, "todo")
    elif sys.argv[2]=="in-progress":
        listTask(data, "inprogress")

#Reset tasks.json
elif sys.argv[1] == "delete-all":
    deleteAll(data)
