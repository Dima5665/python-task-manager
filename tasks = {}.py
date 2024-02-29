import tkinter as tk
from tkinter import messagebox
import json
from datetime import datetime
 
class TaskManagementApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Task Management App")
 
        self.tasks = {}
        self.load_tasks()
 
        self.setup_ui()
 
    def load_tasks(self):
        try:
            with open("tasks.json", "r") as file:
                self.tasks = json.load(file)
        except FileNotFoundError:
            self.tasks = {}
 
    def save_tasks(self):
        with open("tasks.json", "w") as file:
            json.dump(self.tasks, file)
 
    def add_task(self):
        task_name = self.input_task_name.get()
        task_description = self.input_task_description.get("1.0", tk.END)
        task_date = self.input_task_date.get()
 
        if not task_name or not task_date:
            messagebox.showwarning("Missing Information", "Please enter both task name and date.")
            return
 
        self.tasks[task_name] = {"description": task_description, "date": task_date}
        self.save_tasks()
        messagebox.showinfo("Task Added", "Task added successfully!")
        self.clear_entry_fields()
 
    def view_tasks(self):
        if self.tasks:
            task_list = "\n".join([f"Task: {name}\nDescription: {desc.get('description', 'No description')}\nDate: {desc.get('date', 'No date')}\n" if isinstance(desc, dict) else f"Task: {name}\nDescription: {desc}\n" for name, desc in self.tasks.items()])
            messagebox.showinfo("View Tasks", f"Task List:\n{task_list}")
        else:
            messagebox.showinfo("View Tasks", "No tasks found.")
 
    def delete_task(self):
        task_name = self.input_task_name.get()
        if task_name in self.tasks:
            del self.tasks[task_name]
            self.save_tasks()
            messagebox.showinfo("Task Deleted", f"{task_name} has been deleted.")
            self.clear_entry_fields()
        else:
            messagebox.showinfo("Task Not Found", f"{task_name} not found in the task list.")
 
    def clear_entry_fields(self):
        self.input_task_name.delete(0, tk.END)
        self.input_task_description.delete("1.0", tk.END)
        self.input_task_date.delete(0, tk.END)
 
    def setup_ui(self):
        label_task_name = tk.Label(self.root, text="Task Name:")
        label_task_name.pack()
        self.input_task_name = tk.Entry(self.root)
        self.input_task_name.pack()
 
        label_task_description = tk.Label(self.root, text="Task Description:")
        label_task_description.pack()
        self.input_task_description = tk.Text(self.root, height=10, width=30)
        self.input_task_description.pack()
 
        label_task_date = tk.Label(self.root, text="Task Date (YYYY-MM-DD):")
        label_task_date.pack()
        self.input_task_date = tk.Entry(self.root)
        self.input_task_date.pack()
 
        add_button = tk.Button(self.root, text="Add Task", command=self.add_task)
        add_button.pack()
 
        view_button = tk.Button(self.root, text="View Tasks", command=self.view_tasks)
        view_button.pack()
 
        delete_button = tk.Button(self.root, text="Delete Task", command=self.delete_task)
        delete_button.pack()
 
        exit_button = tk.Button(self.root, text="Exit", command=lambda: [self.save_tasks(), self.root.destroy()])
        exit_button.pack()
 
if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManagementApp(root)
    root.mainloop()