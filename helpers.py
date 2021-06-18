import subprocess
from toggl import api


def show_question_dialog(text=""):
    dialog_bash = [
        "zenity",
        "--question",
        f"--text='{text}'",
    ]
    reponse = subprocess.run(dialog_bash)
    return True if reponse.returncode == 0 else False


def show_select_project_dialog():
    all_projects = api.Project.objects.all()

    dialog_bash = [
        "zenity",
        "--list",
        "--title='Choose the project you want to work on'",
        "--column='Project Name'",
        "--column='Is Active'",
    ]

    for index, project in enumerate(all_projects):
        dialog_bash.extend([project.name, str(project.active)])

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
    return api.TimeEntry.objects.current()
