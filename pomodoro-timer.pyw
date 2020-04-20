# Credits
# https://medium.com/@fidel.esquivelestay/build-a-pomodoro-timer-using-python-d52509730f60
import time
import datetime as dt

import tkinter
from tkinter import messagebox
import winsound

### Main Script here
# Collection time information
t_now = dt.datetime.now()                           # Current time for reference
t_pom = 25*60                                       # Pomodoro time
t_delta = dt.timedelta(0,t_pom)                     # Time Delta in mins
t_fut = t_now + t_delta                             # Future time, ending pomodoro
delta_sec = 5*60                                    # Break time, after pomodoro
t_fin = t_now + dt.timedelta(0,t_pom+delta_sec)     # Final time (w/ 5 mins break)

# GUI Pomodoro  in motion!

# Hide tkinter's main window. We use only the alert message box
root = tkinter.Tk()
root.withdraw()

# Show alert message - Started
messagebox.showinfo("Pomodoro started!", "\nIt is now "+t_now.strftime("%H:%M") + " hrs. \nTimer set for 25 mins.")

# Initialize pomodoro counters
total_pomodoros = 0
breaks = 0

# Main Script loop
while True:
    # Pomodoro Time!
    if t_now < t_fut:
        print('Pomodoro')
    ## it is now past working pomodoro, whiting the break.
    elif t_fut <= t_now <= t_fin:
        # Check if is firts time, if so ring bell
        print('in break')
        if breaks == 0:
            print('if break')
            # Annoy !
            for i in range(5):
                winsound.Beep((i+100), 700)
            print('Break Time!')
            breaks += 1
    
    # Pomodoro and break finished. Check if ready for another pomodoro
    else:
        print('Finished!')
        #pomodoro finished. reset breaks
        breaks = 0
        # annoy ! -> Let user know that break is over :'(
        for i in range(10):
            winsound.Beep((i+100), 500)
        #ask if user wants to start again.
        usr_ans = messagebox.askyesno("Pomodoro Finished!", "Would you like to start another pomodoro?")
        total_pomodoros += 1
        if usr_ans == True:
            # User want another pomodoro! Update values to indicate new timeset.
            t_now = dt.datetime.now()
            t_fut = t_now + dt.timedelta(0, t_pom)
            t_fin = t_now + dt.timedelta(0, t_pom+delta_sec)
            continue
        elif usr_ans == False:
            # User is done, display achievments for now
            messagebox.showinfo("Pomodoro Finished!", "\nYou completed "+str(total_pomodoros)+" pomodoros today!")
            break
    # Check every 20 seconds and update current time
    print('Sleeping')
    time.sleep(20)
    t_now = dt.datetime.now()
    timenow = t_now.strftime("%H:%M")