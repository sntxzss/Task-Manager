import database as data

def good_looking():
    print(f"Task Number: {data.ID}| Task Name: {data.Name}")

def task_load(tasks):
    for tasks in data.task_list:
        print(tasks)