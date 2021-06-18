# Toggl Choose Project
Simple utility to select a project and start tracking it using Toggl Track

## Requirements
 * [toggl-cli](https://github.com/AuHau/toggl-cli)
 * [zenity](https://help.gnome.org/users/zenity/3.32/)
 * [notify-send](http://manpages.ubuntu.com/manpages/xenial/en/man1/notify-send.1.html)

## Installation

1. Clone this repo
   ```bash
   git clone https://github.com/resilient-tech/toggl-choose-project.git
   ```


1. Install toggl-cli
    ```bash
    pip install togglCli
    ```
1. Install gnome utilities: zenity and notify-send
    ```bash 
    sudo apt-get install zenity
    sudo apt-get install libnotify-bin
    ```

1. Run
    ```bash
    python3 toggle-choose-project/
    ```
