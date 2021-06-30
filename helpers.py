import subprocess
import json
from os import path
from toggl import api, exceptions
import pathlib

CACHE_FILE_PATH = path.join(str(pathlib.Path().resolve()), "projects.json")


def show_message_dialog(title, text, type):
    supported_dialog = ("error", "question", "warning", "info")

    dialog_bash = [
        "zenity",
        f"--{type}",
        f"--title={title}",
        f"--text={text}",
        "--icon-name=dialog-warning",
        "--width=300",
        "--height=200",
    ]
    reponse = subprocess.run(dialog_bash)
    return True if reponse.returncode == 0 else False


def cache_projects():
    print("Network Call")
    try:
        projects = api.Project.objects.all()
        projects = [project.name for project in projects if project.active]
        content = {"current_project": None, "projects": projects}
        with open(CACHE_FILE_PATH, "w+") as f:
            json.dump(content, f)

        return projects
    except exceptions.TogglConfigException as e:
        show_message_dialog(
            "ERROR!",
            "There is no authentication configuration found!\n\nRun 'toggl me' to configure the toggl.",
            "error",
        )

    return projects


def update_current_project(project):
    if not path.exists(CACHE_FILE_PATH):
        return
    try:
        with open(CACHE_FILE_PATH, "r+") as f:
            content = json.load(f)
            content["current_project"] = project
            f.seek(0)
            json.dump(content, f)
            f.truncate()
    except:
        pass


def get_cached_projects():
    try:
        with open(CACHE_FILE_PATH) as f:
            content = json.load(f)
            current_project, projects = content["current_project"], content["projects"]

            if current_project and current_project in projects:
                projects.remove(current_project)
                projects.insert(0, current_project)

            return projects
    except:
        return cache_projects()


def get_all_projects():
    return get_cached_projects() if path.exists(CACHE_FILE_PATH) else cache_projects()


def show_select_project_dialog():
    all_projects = get_all_projects()

    dialog_bash = [
        "zenity",
        "--list",
        "--title=Choose Project",
        "--column=Project Name",
        "--width=400",
        "--height=400",
    ]

    for project in all_projects:
        dialog_bash.append(project)

    reponse = subprocess.run(dialog_bash, capture_output=True, text=True)

    return reponse.stdout.replace("\n", "")


def show_notification(title="", description=""):
    notify_send_bash_command = [
        "notify-send",
        title,
        description,
    ]
    subprocess.run(notify_send_bash_command)


def start_time_track(project_name=""):
    start_time_bash_command = [
        "toggl",
        "start",
        "--project",
        project_name,
    ]
    response = subprocess.run(start_time_bash_command)
    if response.returncode != 0:
        show_notification(
            "ERROR!",
            f"Invalid project name!",
        )
        return

    show_notification(
        "Time tracking started",
        f"Time tracking started for the project: '{project_name}'",
    )


def fetch_current_time_entry():
    try:
        return api.TimeEntry.objects.current()
    except exceptions.TogglConfigException as e:
        show_message_dialog(
            "ERROR!",
            """There is no authentication configuration found!\n\nRun 'toggl me' to configure the toggl.""",
            "error",
        )
