import tkinter as tk
from tkinter import messagebox
import time
import threading
from plyer import notification

class ReminderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Reminder App")

        # Set up UI elements
        self.frame = tk.Frame(root)
        self.frame.pack(pady=10)

        self.reminder_label = tk.Label(self.frame, text="Enter Reminder:")
        self.reminder_label.grid(row=0, column=0, padx=5, pady=5)

        self.reminder_entry = tk.Entry(self.frame, width=30)
        self.reminder_entry.grid(row=0, column=1, padx=5, pady=5)

        self.time_label = tk.Label(self.frame, text="Set Time (HH:MM):")
        self.time_label.grid(row=1, column=0, padx=5, pady=5)

        self.time_entry = tk.Entry(self.frame, width=10)
        self.time_entry.grid(row=1, column=1, padx=5, pady=5)

        self.add_button = tk.Button(self.frame, text="Add Reminder", command=self.add_reminder)
        self.add_button.grid(row=1, column=2, padx=5, pady=5)

        self.reminder_listbox = tk.Listbox(root, width=50, height=10)
        self.reminder_listbox.pack(pady=10)

        self.delete_button = tk.Button(root, text="Delete Selected", command=self.delete_reminder)
        self.delete_button.pack(pady=5)

        self.reminders = []

        # Start a background thread to check for reminders
        self.check_reminders_thread = threading.Thread(target=self.check_reminders, daemon=True)
        self.check_reminders_thread.start()

    def add_reminder(self):
        reminder = self.reminder_entry.get()
        time_str = self.time_entry.get()
        if reminder and time_str:
            try:
                reminder_time = time.strptime(time_str, "%H:%M")
                self.reminders.append((reminder, reminder_time))
                self.update_listbox()
                self.reminder_entry.delete(0, tk.END)
                self.time_entry.delete(0, tk.END)
            except ValueError:
                messagebox.showwarning("Input Error", "Please enter a valid time in HH:MM format.")
        else:
            messagebox.showwarning("Input Error", "Please enter a reminder and a time.")

    def delete_reminder(self):
        selected_indices = self.reminder_listbox.curselection()
        if selected_indices:
            for index in selected_indices[::-1]:
                del self.reminders[index]
            self.update_listbox()
        else:
            messagebox.showwarning("Selection Error", "Please select a reminder to delete.")

    def update_listbox(self):
        self.reminder_listbox.delete(0, tk.END)
        for reminder, reminder_time in self.reminders:
            self.reminder_listbox.insert(tk.END, f"{reminder} at {time.strftime('%H:%M', reminder_time)}")

    def check_reminders(self):
        while True:
            current_time = time.localtime()
            for reminder, reminder_time in self.reminders:
                if (current_time.tm_hour == reminder_time.tm_hour and
                        current_time.tm_min == reminder_time.tm_min):
                    self.show_notification(reminder)
                    self.reminders.remove((reminder, reminder_time))
                    self.update_listbox()
            time.sleep(30)  # Check every 30 seconds

    def show_notification(self, reminder):
        notification.notify(
            title="Reminder",
            message=reminder,
            timeout=10
        )

if __name__ == "__main__":
    root = tk.Tk()
    app = ReminderApp(root)
    root.mainloop()
