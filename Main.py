import customtkinter as ctk
from tkinter import messagebox

ctk.set_appearance_mode("dark")  
ctk.set_default_color_theme("green")

class ToDoApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("✅ To-Do List (Modern)")
        self.geometry("450x580")
        self.resizable(False, False)

        self.tasks = []

        self.title_label = ctk.CTkLabel(self, text="🧠 My To-Do List", font=ctk.CTkFont(size=22, weight="bold"))
        self.title_label.pack(pady=20)

        self.entry_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.entry_frame.pack(pady=10)

        self.task_entry = ctk.CTkEntry(self.entry_frame, placeholder_text="Enter new task...", width=260)
        self.task_entry.pack(side="left", padx=(0, 10))

        self.add_button = ctk.CTkButton(self.entry_frame, text="➕", width=40, command=self.add_task)
        self.add_button.pack(side="left")

        self.task_frame = ctk.CTkFrame(self)
        self.task_frame.pack(pady=20, fill="both", expand=True)

        self.task_listbox = ctk.CTkTextbox(self.task_frame, height=300, width=380, activate_scrollbars=True)
        self.task_listbox.pack(padx=10, pady=10)
        self.task_listbox.configure(state="disabled")

        self.button_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.button_frame.pack(pady=10)

        self.complete_button = ctk.CTkButton(self.button_frame, text="✔️ Complete", width=120, command=self.mark_completed)
        self.complete_button.grid(row=0, column=0, padx=5, pady=5)

        self.edit_button = ctk.CTkButton(self.button_frame, text="✏️ Edit", width=120, command=self.edit_task)
        self.edit_button.grid(row=0, column=1, padx=5, pady=5)

        self.delete_button = ctk.CTkButton(self.button_frame, text="🗑️ Delete", width=120, command=self.delete_task)
        self.delete_button.grid(row=0, column=2, padx=5, pady=5)

    def update_task_listbox(self):
        self.task_listbox.configure(state="normal")
        self.task_listbox.delete("1.0", "end")
        for i, task in enumerate(self.tasks, start=1):
            self.task_listbox.insert("end", f"{i}. {task}\n")
        self.task_listbox.configure(state="disabled")

    def add_task(self):
        task = self.task_entry.get().strip()
        if task:
            self.tasks.append(task)
            self.task_entry.delete(0, "end")
            self.update_task_listbox()
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def delete_task(self):
        if not self.tasks:
            messagebox.showwarning("Warning", "No tasks to delete.")
            return

        task_number = self.ask_task_number("delete")
        if task_number is not None and 0 < task_number <= len(self.tasks):
            del self.tasks[task_number - 1]
            self.update_task_listbox()

    def mark_completed(self):
        if not self.tasks:
            messagebox.showwarning("Warning", "No tasks to mark.")
            return

        task_number = self.ask_task_number("mark complete")
        if task_number is not None and 0 < task_number <= len(self.tasks):
            self.tasks[task_number - 1] = f"✔️ {self.tasks[task_number - 1]}"
            self.update_task_listbox()

    def edit_task(self):
        if not self.tasks:
            messagebox.showwarning("Warning", "No tasks to edit.")
            return

        task_number = self.ask_task_number("edit")
        if task_number is not None and 0 < task_number <= len(self.tasks):
            new_task = self.task_entry.get().strip()
            if new_task:
                self.tasks[task_number - 1] = new_task
                self.task_entry.delete(0, "end")
                self.update_task_listbox()
            else:
                messagebox.showwarning("Warning", "Please enter new task text.")

    def ask_task_number(self, action):
        try:
            number = ctk.CTkInputDialog(title="Task Number", text=f"Enter task number to {action}:")
            num = int(number.get_input())
            return num
        except:
            return None

if __name__ == "__main__":
    app = ToDoApp()
    app.mainloop()
