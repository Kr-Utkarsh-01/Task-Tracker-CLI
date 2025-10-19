import sys
import json
def addTask(data, task):
    count=data["count"]
    newTask={
                "task": task,
                "status": "To-do"
            }
    data[count+1]=newTask
    data["count"]+=1
    f=open("tasks.json", "w")
    json.dump(data, f, indent=4)
    f.close()
    print(f"Added task: '{task}' | task id: {count+1}")

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
        data["count"]-=1
    f=open("tasks.json", "w")
    json.dump(data, f, indent=4)

def deleteAll(data):
    data={"count": 0}
    f=open("tasks.json", "w")
    json.dump(data, f, indent=4)
    print("All tasks deleted.")

def updateStatus(data, id, newStatus):
    data[id]["status"]=newStatus
    f=open("tasks.json", "w")
    json.dump(data, f, indent=4)
    print(f"Status of task '{data[id]["task"]}' with id={id} changed to '{newStatus}'")
    

#listing left
#main()
f=open("tasks.json", "r")
data=json.load(f)
deleteAll(data)
