import unittest
import os
from exam import ProjectManager, Project, Task

class TestProjectManager(unittest.TestCase):
    def setUp(self):
        self.filename = "test_projects.json"
        self.pm = ProjectManager(self.filename)

    def tearDown(self):
        if os.path.exists(self.filename):
            os.remove(self.filename)

    def test_create_project(self):
        self.pm.create_project("TestProject")
        self.assertTrue(self.pm.find_project("TestProject"))

    def test_delete_project(self):
        self.pm.create_project("TestProject")
        self.pm.delete_project("TestProject")
        self.assertIsNone(self.pm.find_project("TestProject"))
class TestProject(unittest.TestCase):
    def test_add_task(self):
        project = Project("TestProject")
        task = Task("TestTask", "Viktor", "2024-04-14")
        project.add_task(task)
        self.assertTrue(project.find_task("TestTask"))


class TestTask(unittest.TestCase):
    def test_task_creation(self):
        task = Task("TestTask", "Viktor", "2024-04-14")
        self.assertEqual(task.name, "TestTask")
        self.assertEqual(task.assignee, "Viktor")
        self.assertEqual(task.deadline, "2024-04-14")


if __name__ == "__main__":
    unittest.main()
