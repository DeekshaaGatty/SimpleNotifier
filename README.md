# SimpleNotifier
A Python desktop notification application with task scheduling and WhatsApp integration.

The code provided is a Python script that uses the Tkinter library to create a graphical user interface (GUI) for a notification application. Here's a breakdown of the code:

1. The necessary imports are made from the `tkinter`, `tkinter.ttk`, `plyer`, `datetime`, and `pywhatkit` libraries.

2. The `create_notification` function is defined, which takes the task description and the time (in hours, minutes, and seconds) as parameters. It calculates the total time in seconds, waits for that duration using `time.sleep`, and then displays a desktop notification using the `plyer.notification` module. It also uses `pywhatkit` to send a WhatsApp message with the task details.

3. The `submit_tasks` function is defined. It retrieves the task, hours, minutes, and seconds from the input fields in the GUI, and then calls the `create_notification` function for each task.

4. The Tkinter GUI window is created, titled "Notification Application," and set to a size of 500x400 pixels. The window is centered at the top of the screen.

5. A label is added to the GUI window to prompt the user to enter the task and time.

6. A loop is used to create five sets of input fields for entering tasks and times. Each set includes a task label, an entry field for the task description, labels for hours, minutes, and seconds, and combo boxes for selecting the corresponding values.

7. The input fields for each task are added to the `task_entries` list.

8. A submit button is added to the GUI window. When clicked, it calls the `submit_tasks` function.

9. The `mainloop` method is called on the Tkinter root object to start the GUI event loop and display the window.


Note : 
You need to replace `"+91YourNumber"` in the `pwt.sendwhatmsg` function call with your phone number to receive the WhatsApp message.
