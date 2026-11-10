#original list
tasks = ["Buy groceries", "Finish homework", "Call dentist"]

print("="*40)
print("My To-Do List")
print("="*40)
for i in range(len(tasks)):#That is for showing each task in a individual line 
     print(f"{i + 1}. {tasks[i]}")# +1 is to have each task numbered on a base 1
print(f"\nTotal tasks: {len(tasks)}")
print("\nWhat would you like to do?")
print("1. Add a task")
print("2. Remove a task\n")
choice = input("Choice: ")

if choice == "1":
   new_task = input("Enter new task: ")
   tasks.append(new_task)# that is to add the person answer as a new element in the list

elif choice == "2":#option if the person choose number 2
    while True:#to make sure the person can still try again
        try:
            task_number = int(input("Enter task number to remove: "))
            tasks.pop(task_number - 1)#it's to remove a task
            break

        except (ValueError, IndexError):# to avoid the program to crash if these error are made
            print("Invalid task number, please try again.")

else:
    print("Invalid choice. Please choose 1 or 2.")#else is to make sure that any other number the person type python can handle it without crashing.

print("\nUpdated List:")   # list with the new task
for i in range(len(tasks)):
    print(f"{i + 1}.{tasks[i]}")

print(f"\nTotal tasks: {len(tasks)}")


