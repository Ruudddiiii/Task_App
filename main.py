import json
import base64
import requests
from requests.auth import HTTPBasicAuth
from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.pickers import MDDatePicker
from kivymd.uix.list import TwoLineAvatarIconListItem, ILeftBodyTouch
from kivymd.uix.selectioncontrol import MDCheckbox
from datetime import datetime

# GitHub settings
GITHUB_USERNAME = 'Ruudddiiii'
REPO_NAME = 'TaskTravelTime'
GITHUB_TOKEN = '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'
TASK_FILE = 'task1.json'

# GitHub API URLs
REPO_API_URL = f'https://api.github.com/repos/{GITHUB_USERNAME}/{REPO_NAME}/contents/{TASK_FILE}'

# Function to load tasks from GitHub
def load_tasks_from_github():
    try:
        response = requests.get(REPO_API_URL, auth=HTTPBasicAuth(GITHUB_USERNAME, GITHUB_TOKEN))
        response.raise_for_status()
        file_data = response.json()
        file_content_base64 = file_data['content']
        file_content = base64.b64decode(file_content_base64).decode('utf-8')
        data = json.loads(file_content)
        return data.get('tasks', [])
    except Exception as e:
        print(f"Error loading tasks from GitHub: {e}")
        return []

# Function to update and push tasks.json to GitHub
def save_tasks_to_github(tasks):
    try:
        response = requests.get(REPO_API_URL, auth=HTTPBasicAuth(GITHUB_USERNAME, GITHUB_TOKEN))
        response.raise_for_status()
        file_data = response.json()
        sha = file_data['sha']

        json_data = json.dumps({"tasks": tasks}).encode('utf-8')
        base64_content = base64.b64encode(json_data).decode('utf-8')

        payload = {
            "message": "Update tasks.json",
            "content": base64_content,
            "sha": sha
        }

        response = requests.put(REPO_API_URL, json=payload, auth=HTTPBasicAuth(GITHUB_USERNAME, GITHUB_TOKEN))
        response.raise_for_status()
        print("Tasks successfully updated on GitHub")
    except Exception as e:
        print(f"Error saving tasks to GitHub: {e}")

class DialogContent(MDBoxLayout):
    """OPENS A DIALOG BOX THAT GETS THE TASK FROM THE USER"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ids.date_text.text = str(datetime.now().strftime('%A %d %B %Y'))

    def show_date_picker(self):
        """Opens the date picker"""
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.on_save)
        date_dialog.open()

    def on_save(self, instance, value, date_range):
        date = value.strftime('%A %d %B %Y')
        self.ids.date_text.text = str(date)

class ListItemWithCheckbox(TwoLineAvatarIconListItem):
    '''Custom list item'''

    def __init__(self, pk=None, **kwargs):
        super().__init__(**kwargs)
        self.pk = pk

    def mark(self, check, the_list_item):
        '''Mark the task as complete or incomplete'''
        tasks = load_tasks_from_github()
        if check.active:
            the_list_item.text = '[s]' + the_list_item.text + '[/s]'
            tasks[self.pk]['completed'] = True
        else:
            the_list_item.text = tasks[self.pk]['name']
            tasks[self.pk]['completed'] = False
        save_tasks_to_github(tasks)

    def delete_item(self, the_list_item):
        '''Delete the task'''
        tasks = load_tasks_from_github()
        tasks.pop(self.pk)
        save_tasks_to_github(tasks)
        self.parent.remove_widget(the_list_item)

class LeftCheckbox(ILeftBodyTouch, MDCheckbox):
    '''Custom left container'''

class MainApp(MDApp):
    task_list_dialog = None

    def build(self):
        self.theme_cls.primary_palette = "Orange"

    def show_task_dialog(self):
        if not self.task_list_dialog:
            self.task_list_dialog = MDDialog(
                title="Create Task",
                type="custom",
                content_cls=DialogContent(),
            )
        self.task_list_dialog.open()

    def on_start(self):
        try:
            tasks = load_tasks_from_github()
            for idx, task in enumerate(tasks):
                add_task = ListItemWithCheckbox(pk=idx, text=str(task['name']), secondary_text="Due Date: None")
                if task.get('completed'):
                    add_task.text = '[s]' + task['name'] + '[/s]'
                    add_task.ids.check.active = True
                self.root.ids.container.add_widget(add_task)
        except Exception as e:
            print(e)

    def close_dialog(self, *args):
        self.task_list_dialog.dismiss()

    def add_task(self, task, task_date):
        '''Add task to the list of tasks'''
        tasks = load_tasks_from_github()
        new_task = {"name": task.text, "completed": False}
        tasks.append(new_task)
        save_tasks_to_github(tasks)

        self.root.ids['container'].add_widget(
            ListItemWithCheckbox(pk=len(tasks)-1, text=f'[b]{task.text}[/b]', secondary_text="Due Date: None")
        )
        task.text = ''

if __name__ == '__main__':
    app = MainApp()
    app.run()