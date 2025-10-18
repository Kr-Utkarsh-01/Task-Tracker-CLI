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

    

#main()
f=open("tasks.json", "r")
data=json.load(f)