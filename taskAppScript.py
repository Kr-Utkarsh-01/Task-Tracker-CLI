import sys
import json
def addTask(data, task):
    newTask={
                "task": task,
                "status": "To-do"
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
    f=open("tasks.json", "w")
    json.dump(data, f, indent=4)
    print(f"Status of task '{data[id]["task"]}' with id={id} changed to '{newStatus}'")
    
def listTask(data, arg="All"):
    if arg=="All":
        for i in data["currIds"]:
            print(f"Id: {i}\nTask: {data[i]["task"]}\nStatus: {data[i]["status"]}\n")
    elif arg=="done":
        for i in data["currIds"]:
            if data[i]["status"]=="Done":
                print(f"Id: {i}\nTask: {data[i]["task"]}\nStatus: {data[i]["status"]}\n")
    elif arg=="todo":
        for i in data["currIds"]:
            if data[i]["status"]=="To-do":
                print(f"Id: {i}\nTask: {data[i]["task"]}\nStatus: {data[i]["status"]}\n")
    elif arg=="in-progress":
        for i in data["currIds"]:
            if data[i]["status"]=="In-progress":
                print(f"Id: {i}\nTask: {data[i]["task"]}\nStatus: {data[i]["status"]}\n")

#main()
f=open("tasks.json", "r")
data=json.load(f)