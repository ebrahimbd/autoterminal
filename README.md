# Bash Script for Opening Multiple Terminals with Tmux

This script opens multiple terminals in a Tmux session and performs various actions, such as starting a Node.js server and monitoring system resource usage with htop.

## Prerequisites

* Python 3.x
* pyautogui module (pip install pyautogui)
* Tmux

## Usage

* Clone the repository to your local machine
* Navigate to the cloned directory and open a terminal 
* Run the command python bash.py


## The script will automatically open a Tmux session and create four terminals as shown below:

```python
| 1 | 2 |
| 3 | 4 |
```
On macOS and Linux, you need to run python3:

python3 -m pip install pyautogui
On Linux, additionally you need to install the scrot application, as well as Tkinter:

sudo apt-get install scrot

sudo apt-get install python3-tk

sudo apt-get install python3-dev
* Terminal 1: Changes the working directory to a Node.js project directory and starts the server using the command npm start.
*  Terminal 2: Creates a vertical split and moves the cursor to the right pane.
* Terminal 3: Creates a horizontal split below Terminal 2 and opens htop to monitor system resource usage.
*  Terminal 4: Moves the cursor to the right pane of Terminal 2 and opens nethogs to monitor network usage.

 ##### To customize the script for your use case, modify the commands passed to each terminal within the script.
