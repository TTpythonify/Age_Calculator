# pip install customtkinter

import customtkinter as ctk
from datetime import datetime
from tkinter import messagebox

# Initialize the customtkinter application
ctk.set_appearance_mode("system") 
ctk.set_default_color_theme("blue")  

class AgeCalculator(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Age Calculator")
        self.geometry("300x400")

        # Labels Entries for Day/Month/Year
        self.day_label = ctk.CTkLabel(self, text="Day:")
        self.day_label.pack(pady=10)
        self.day_entry = ctk.CTkEntry(self)
        self.day_entry.pack(pady=5)

        self.month_label = ctk.CTkLabel(self, text="Month:")
        self.month_label.pack(pady=10)
        self.month_entry = ctk.CTkEntry(self)
        self.month_entry.pack(pady=5)

        self.year_label = ctk.CTkLabel(self, text="Year:")
        self.year_label.pack(pady=10)
        self.year_entry = ctk.CTkEntry(self)
        self.year_entry.pack(pady=5)

        # Button to calculate age
        self.button_calculate = ctk.CTkButton(self, text="Calculate Age", command=self.calculate_age)
        self.button_calculate.pack(pady=20)

        # Label to display the result
        self.label_result = ctk.CTkLabel(self, text="")
        self.label_result.pack(pady=10)

    # Function to calculate age
    def calculate_age(self):
        try:
            # Get the day, month and year
            day = int(self.day_entry.get())
            month = int(self.month_entry.get())
            year = int(self.year_entry.get())

            # Create a datetime object
            birth_date = datetime(year, month, day)

            # Get current date
            today = datetime.now()

            # Calculate the age
            age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))

            # Display the age
            self.label_result.configure(text=f"You are {age} years old.")

        # Errors
        except ValueError:
            messagebox.showerror("Error", "Please enter valid day, month, and year.")
        except Exception as e:
            messagebox.showerror("Error", str(e))


if __name__ == "__main__":
    app = AgeCalculator()
    app.mainloop()
