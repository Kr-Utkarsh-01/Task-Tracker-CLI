import sys
import json
def addTask(task):
    f=open("tasks.json", "r")
    data=json.load(f)
    count=data["count"]
    newTask={
                "task": task,
                "status": "To-do"
            }
    data[count+1]=newTask
    data["count"]+=1
    f.close()
    f=open("tasks.json", "w")
    json.dump(data, f, indent=4)
    f.close()
