from helpers import fetch_current_time_entry, show_input_dialog, stop_current_time_entry

current_time_entry = fetch_current_time_entry()

if not current_time_entry:
    exit(0)

dialog_respose = show_input_dialog(
    "Add description",
    f"What task you have done for '{current_time_entry.project.name}'?",
)

if dialog_respose.returncode == 1:
    exit(0)

stop_current_time_entry(current_time_entry, dialog_respose.stdout)
