from operator import ne
import sys
import json
from tkinter import NO
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
    data[id]=newTask
    f=open("tasks.json", "w")
    json.dump(data, f, indent=4)
    print(f"Task with id={id} has been updated to: '{newTask}'")

#main()
f=open("tasks.json", "r")
data=json.load(f)
