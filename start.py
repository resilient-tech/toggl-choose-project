from helpers import *

current_time_entry = fetch_current_time_entry()

if current_time_entry:
    should_continue = show_question_dialog(
        f"Time tracking for project '{current_time_entry.project.name}'is already running, do you want to stop it?"
    )
    if not should_continue:
        exit(1)

selected_project_name = show_select_project_dialog()
print(f"starting timer for project '{selected_project_name}'...")
start_time_track(selected_project_name)
