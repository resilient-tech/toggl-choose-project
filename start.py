from helpers import *

current_time_entry = fetch_current_time_entry()

if current_time_entry:
    should_continue = show_question_dialog(
        f"Time tracking for <b>{current_time_entry.project.name}</b> is already running.\n\nAre you sure you want to continue?"
    )
    if not should_continue:
        exit(1)


selected_project_name = show_select_project_dialog()

if not selected_project_name:
    exit(1)

start_time_track(selected_project_name)
