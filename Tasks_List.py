import time

# Tasks_Class
class Task:
  def __init__ (self, title, description, due_date, status):
    self.title = title
    self.description = description
    self.due_date = due_date
    self.status = status

  def print_info(self):
    print(f"Title: {self.title}")
    print(f"Description: {self.description}")
    print(f"Due Date: {self.due_date}")
    print(f"Status: {self.status}")

# User_Tasks_Input
user_task_title = input("Enter the title of the task: ")
while user_task_title == "":
  print("You didn't enter a title.")
  user_task_title = input("Enter the title of the task: ")

user_task_description = input("Enter the description of the task: ")
while user_task_description == "":
  print("You didn't enter a description.")
  user_task_description = input("Enter the description of the task: ")

user_task_due_date = input("Enter the due date of the task: ")
while user_task_due_date == "":
  print("You didn't enter a due date.")
  user_task_due_date = input("Enter the due date of the task: ")
  
user_task_status = input("Enter the status of the task: ")
while user_task_status == "":
  print("You didn't enter a status.")
  user_task_status = input("Enter the status of the task: ")


# Tasks_List
task1 = Task(user_task_title, user_task_description, user_task_due_date, user_task_status)
task1.print_info()

time.sleep(2)


