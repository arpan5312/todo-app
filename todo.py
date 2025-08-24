tasks = []
tasks_done = []

def add_task():
    new_task = input("Enter new task: ")
    tasks.append(new_task)
    print(f"✅ {new_task} added.")

def remove_task():
    remove_task = input("Enter the task to remove: ")
    if remove_task in tasks:
        tasks.remove(remove_task)
        print(f"🗑️ {remove_task} removed.")
    else:
        print("⚠️ Task not found.")

def view_tasks():
    if not tasks:
        print("📭 No tasks added yet.")
    else:
        print("\nYour tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
        print()

def quit_app():
    print("👋 Exiting To-Do App. Goodbye!")
    exit()

def log():
    completed_task = input("Enter the task to be checked off: ")
    if completed_task in tasks:
        tasks.remove(completed_task)
        tasks_done.append(completed_task)
        print(f"{completed_task} checked off")
    else:
        print("Task not found")

def prog():
    print("\n✅ Tasks done:")
    if tasks_done:
        for index, task in enumerate(tasks_done, start=1):
            print(f"{index}. {task}")
    else:
        print("None yet")

    print("\n⬜ Tasks not done:")
    if tasks:
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
    else:
        print("All caught up!")

    completed = len(tasks_done)
    not_completed = len(tasks)
    total = completed + not_completed

    if total == 0:
        progress = 0
    else:
        progress = (completed / total) * 100

    print(f"\nSummary:")
    print(f"   ✅ Completed: {completed}")
    print(f"   ⬜ Remaining: {not_completed}")
    print(f"   📊 Progress: {progress:.1f}%")

        # Progress bar
    bar_length = 20  
    filled_length = int(bar_length * progress / 100)
    bar = "█" * filled_length + "-" * (bar_length - filled_length)

    print(f"   📈 [{bar}] {progress:.1f}%")



while True:
    ui = input("\nChoose action: add / rem / view / quit / log / prog: ").strip().lower()
    if ui == 'add':
        add_task()
    elif ui == 'rem':
        remove_task()
    elif ui == 'view':
        view_tasks()
    elif ui == 'quit':
        quit_app()
    elif ui == 'log':
        log()
    elif ui == 'prog':
        prog()
    else:
        print("Invalid input. Try again.")
