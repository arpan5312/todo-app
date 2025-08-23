
tasks = []

def addtask():
    new_task = input("Enter new task: ")
    tasks.append(new_task)
    print(f"{new_task} is added.")


def removetask():
    remove_task = input("Enter the task to be removed: ")
    for task in tasks:
        if task in tasks:
            tasks.remove(remove_task)
            print(f"{remove_task} is removed.")
        else:
            print("Task not found")


def viewtask():
    if len(tasks)== 0:
        print("No tasks added yet")
    else:
        for index, task in enumerate (tasks, start=1):
            print(f"{index}. {task}")

def quit():
    print("Terminated.")
    exit
while True:
    ui = input("Choose an action: (add/rem/vie/qui)")
    if ui == 'add':
        addtask()
    elif ui == 'vie':
        viewtask()
    elif ui == 'rem':
        removetask()
    elif ui == 'qui':
        quit()
        exit
    else:
        print("Invalid Input")