from tkinter import *
from tkinter import ttk
from plyer import notification
from datetime import datetime
import pywhatkit as pwt
import time


def create_notification(task, hours, minutes, seconds):
    total_seconds = hours * 3600 + minutes * 60 + seconds
    if total_seconds > 0:
        time.sleep(total_seconds)
        notification.notify(
            title="Desktop Notifier",
            message="Your task: " + task,
            app_icon=None,
            timeout=3
        )
        current_time = datetime.now()
        pwt.sendwhatmsg("+91YourNumber", "You have a task now: " + task, current_time.hour, current_time.minute + 1)


def submit_tasks():
    tasks = [(task_entry.get(), hour_combo.get(), minute_combo.get(), second_combo.get()) for task_entry, hour_combo, minute_combo, second_combo in task_entries]
    for task, hours, minutes, seconds in tasks:
        create_notification(task, int(hours), int(minutes), int(seconds))


root = Tk()
root.title("Notification Application")
root.geometry("500x400")
root.configure(bg="cyan")

# Calculate the window position to center it at the top
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
window_width = 500
window_height = 400
x = (screen_width // 2) - (window_width // 2)
y = 0
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

task_entries = []

label = Label(root, text="Enter the task and time", background='cyan', foreground='purple', font=("Arial", 35), borderwidth=2)
label.place(relx=0.5, y=50, anchor=CENTER)

for i in range(5):
    task_label = Label(root, text="Task " + str(i+1), background='lightcyan', foreground='blue', font=("Arial", 20), borderwidth=3)
    task_label.place(relx=0.2, y=110 + i * 50, anchor=W)

    task_entry = Entry(root, font=("Arial", 12), bd=5)
    task_entry.place(relx=0.30, y=110 + i * 50, anchor=W)

    hour_label = Label(root, text="Hour", background='lightcyan', foreground='blue', font=("Arial", 20))
    hour_label.place(relx=0.50, y=110 + i * 50, anchor=CENTER)

    hour_combo = ttk.Combobox(root, width=5, font=("Arial", 12), values=list(range(25)))
    hour_combo.place(relx=0.55, y=110 + i * 50, anchor=CENTER)
    hour_combo.current(0)

    minute_label = Label(root, text="Minute", background='lightcyan', foreground='blue', font=("Arial", 20))
    minute_label.place(relx=0.63, y=110 + i * 50, anchor=W)

    minute_combo = ttk.Combobox(root, width=5, font=("Arial", 12), values=list(range(61)))
    minute_combo.place(relx=0.70, y=110 + i * 50, anchor=W)
    minute_combo.current(0)

    second_label = Label(root, text="Second", background='lightcyan', foreground='blue', font=("Arial", 20))
    second_label.place(relx=0.78, y=110 + i * 50, anchor=W)

    second_combo = ttk.Combobox(root, width=5, font=("Arial", 12), values=list(range(61)))
    second_combo.place(relx=0.85, y=110 + i * 50, anchor=W)
    second_combo.current(0)

    task_entries.append((task_entry, hour_combo, minute_combo, second_combo))

submit_button = Button(root, text="Submit", background='yellow', foreground='green', font=("Arial", 20), borderwidth=2, bd=5, command=submit_tasks)
submit_button.place(relx=0.5, y=400, anchor=CENTER)

root.mainloop()
