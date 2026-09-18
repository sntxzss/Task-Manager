import database as data

def good_looking(task):
    print(f"Task Number: {task.get('ID')} | Task Name: {task.get('Name')} | Desc: {task.get('Desc')} | Priority: {task.get('Priority')}")

def task_load(tasks):
    for task in tasks:
        good_looking(task)

def add_task():
          new_task = {
           "ID": len(data.task_list) + 1,
           "Name": input("Enter task name: ").strip(),
           "Desc": input("Enter description: ").strip(),
           "Priority": input("Enter priority (Low/Medium/High): ").strip()
          }
          data.task_list.append(new_task)

def remove_task():
    task_id = int(input("Enter task number: "))
    for task in data.task_list:
        if task["ID"] == task_id:
            data.task_list.remove(task)
            break

def show_menu():
    while True:
        print("1. View All Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")
        choice = input("Select an option (1-3): ").strip()

        if choice == "1":
            task_load(data.task_list)
        elif choice == "2":
          add_task()
        elif choice == "3":
          remove_task()
        elif choice == "4":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    show_menu()