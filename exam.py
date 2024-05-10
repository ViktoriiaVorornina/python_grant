import json
import os

class ProjectManager:
    def __init__(self, filename):
        self.filename = filename
        if not os.path.exists(self.filename):
            self.create_projects_file()
        self.projects = self.load_projects()

    def create_projects_file(self):
        with open(self.filename, "w") as file:
            json.dump([], file)

    def load_projects(self):
        with open(self.filename, 'r') as file:
            try:
                projects_data = json.load(file)
                projects = []
                for project_data in projects_data:
                    project = Project(project_data["name"])
                    for task_data in project_data["tasks"]:
                        task = Task(task_data["name"], task_data["assignee"], task_data["deadline"])
                        project.add_task(task)
                    projects.append(project)
                return projects
            except json.decoder.JSONDecodeError:
                print(f"Error loading projects from {self.filename}. File is empty or not valid JSON.")
                return []

    def save_projects(self):
        projects_to_save = [project.to_dict() for project in self.projects]
        with open(self.filename, 'w') as file:
            json.dump(projects_to_save, file, indent=4)

    def create_project(self, name):
        project = Project(name)
        self.projects.append(project)

    def delete_project(self, project_name):
        project = self.find_project(project_name)
        if project:
            self.projects.remove(project)
        else:
            print(f"Project '{project_name}' not found.")

    def find_project(self, project_name):
        for project in self.projects:
            if project.name == project_name:
                return project
        return None

class Project:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def delete_task(self, task_name):
        task = self.find_task(task_name)
        if task:
            self.tasks.remove(task)
        else:
            print(f"Task '{task_name}' not found.")

    def find_task(self, task_name):
        for task in self.tasks:
            if task.name == task_name:
                return task
        return None

    def to_dict(self):
        return {
            "name": self.name,
            "tasks": [task.to_dict() for task in self.tasks]
        }

class Task:
    def __init__(self, name, assignee, deadline):
        self.name = name
        self.assignee = assignee
        self.deadline = deadline

    def to_dict(self):
        return {
            "name": self.name,
            "assignee": self.assignee,
            "deadline": self.deadline
        }

pm = ProjectManager("projects.json")

pm.create_project("Project1")

pm.find_project("Project1").add_task(Task("Task1", "Viktoriia", "2024-04-14"))

pm.find_project("Project1").add_task(Task("Task2", "Alice", "2024-04-15"))

pm.save_projects()

project1 = pm.find_project("Project1")
print(f"Tasks in Project1:")
for task in project1.tasks:
    print(f"- {task.name} (Assigned to: {task.assignee}, Deadline: {task.deadline})")

project1.delete_task("Task1")
print("After deleting Task1:")
for task in project1.tasks:
    print(f"- {task.name} (Assigned to: {task.assignee}, Deadline: {task.deadline})")



