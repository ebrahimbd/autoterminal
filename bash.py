import pyautogui
import time


# terminal
#     | 1 | 2 |
#     | 3 | 4 |

# t=0
# while t<2:
#     time.sleep(1)
#     screenHeight = pyautogui.position() 
#     print(screenHeight)
#     t+=1
# pyautogui.moveTo(2430, 1140) 
# pyautogui.click(2430, 1140) 
 
def move(to):
    pyautogui.hotkey('ctrl', 'b')
    pyautogui.hotkey(to)

pyautogui.hotkey('ctrl', 'alt', 't')
time.sleep(0.1)
# for vs code
# pyautogui.hotkey('ctrl', 'shift', '`')
pyautogui.hotkey('F11')
time.sleep(0.5)
pyautogui.write('tmux') 
pyautogui.typewrite(['enter'])

# corser in 1no turmux
pyautogui.write('cd "/mnt/Importent file/full stack development/Website build/Project/ReactjsApi"') 
pyautogui.typewrite(['enter'])
pyautogui.write('js') #js is alies who are npm start command
pyautogui.typewrite(['enter'])

# vertical turmux create curser in right side 2no
pyautogui.hotkey('ctrl', 'b', '%')
time.sleep(0.1)

# horizantal turmux create 4no
pyautogui.hotkey('ctrl', 'b', '"')
time.sleep(0.1)
# move 1 no 
move('left')
# create horizental terminal 3no
pyautogui.hotkey('ctrl', 'b', '"')
# show htop
time.sleep(0.1)
pyautogui.write('htop') 
pyautogui.typewrite(['enter'])
# move 4 no
move('right')
time.sleep(0.1)
# opennethogh right terminal and asking a admin password
pyautogui.write('sudo nethogs') 
pyautogui.typewrite(['enter'])
pyautogui.write('sdsdsdsdsd') 
pyautogui.typewrite(['enter'])

# go to 2no terminal
time.sleep(0.1)
move('up')
pyautogui.write('cd "/mnt/Importent file/full stack development/Website build/Project/ReactjsApi"') 
pyautogui.typewrite(['enter'])
pyautogui.write('ok') 
# pyautogui.typewrite(['enter'])
# pyautogui.write('code .') 