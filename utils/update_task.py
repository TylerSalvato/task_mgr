import requests

import json 

# Mini Challenge 1
# Create a script that allows you to interactively
# update a task via its ID.

# Acceptance criteria
# 1. Prompt the user for an ID
# 2. Issue a get request for the specific task
# 3. Display the task in question
# 4. Allow the user to update all of the fields (via prompts)

# Bonus:
# 1. If there is no task received (404) display an error message.
# Note: the methods in requests for PUT and GET are "requests.put(URL, json=something)"
# and requests.get(URL)

BACKEND_URL = "http://127.0.0.1:5000/tasks"

def get_task(id):
    response = requests.get(BACKEND_URL + "/" + id)
    if response.status_code == 200:
        print("Get succeeded, data: ")
        print(json.dumps(response.json(), indent=4))
        return 1
    elif response.status_code  == 404:
        print("Get failed")   
        return 0

def update_task(id, summary, description, is_done):
    task = {
        "summary": summary,
        "description": description,
        "is_done": is_done 
    }
    response = requests.put(BACKEND_URL + "/" + id, json=task)
    if response.status_code == 204:
        print("Update succeeded")
    else:
        print("Update failed")     

if __name__ == "__main__":
    print("Fill out the prompts below to update task:")
    
    id = str(input("Task id: ") )
    
    if get_task(id):
        summary = str(input("New task summary: "))
        description = str(input("New task description: "))
        is_done = str(input("New status: "))
        
        update_task(id, summary, description, is_done)