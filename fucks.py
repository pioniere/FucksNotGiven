#
# fucks.py
# 
# Tracks the number of times a fuck is not given. 
# Set the location below for the file holding the totalfucks
#
# For my dear friend Beth, who would have appreciated the utility of this.
# August 13, 2021
#


import PySimpleGUI as sg
from pyscreeze import center

ver = '0.1'
fnt = 'Arial 18'
bigfnt = 'Arial 24'
sg.theme("SystemDefault")

# Full file path for tracking alltime fucks not given
# Change this as needed
# ----------------------------------------
fuckslocation = 'D:/Dev/Fucks/totalfucks.txt'
# ----------------------------------------

# Opens alltime fucks file, and creates it if it doesn't exist
while True:
    try:
        fucksfile = open(fuckslocation, 'r')
    except FileNotFoundError:
        fucksfile = open(fuckslocation, 'w')
        fucksfile.write(str(0))
        fucksfile.close()
        continue
    break

# Get alltime fucks not given and get ready to count today's
alltimeFucks = fucksfile.read()
alltimeFucks = int(alltimeFucks)
fucksfile.close()
todayFucks = 0

# Screen layout
layout = [
    [sg.Text('Fucks Not Given', font = bigfnt, justification='center')],
    [sg.Text('Today: ', font = fnt), sg.Text(todayFucks, size=(2,1), key='tFucks', font = fnt), sg.Text('Alltime: ', font = fnt), sg.Text(alltimeFucks, size=(3,1), key='aFucks', font = fnt)],
    [sg.Button(' Don\'t Give A Fuck ', font = fnt), sg.Button(' Quit ', font = fnt)]

]

window = sg.Window('Don\'t Give A Fuck ' + ver, layout=layout, margins=(20,10), return_keyboard_events=True, finalize=True, keep_on_top=True)

while True:
    event, values = window.read()

    # Write alltimefucks and Exit
    if event in (' Fuck It ', None):
        fucksfile = open(fuckslocation, 'w')
        fucksfile.write(str(alltimeFucks))
        fucksfile.close()
        break

    # Increment fucks not given totals
    if event == ' Don\'t Give A Fuck ':    
        todayFucks = todayFucks + 1
        alltimeFucks = int(alltimeFucks) + 1
        window.FindElement('tFucks').update(todayFucks) 
        window.FindElement('aFucks').update(alltimeFucks)

window.close()
