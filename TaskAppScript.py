import sys
import json
# def addTask(task):
#     f=open("tasks.json", "w" )
f=open("tasks.json", "r")
print(json.loads(f))
    