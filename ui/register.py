import customtkinter as ctk


class RegisterWindow(ctk.CTk):

    def __init__(self):
        super().__init__()

        # Window Settings
        self.title("Register - Personal Expense Tracker Pro")
        self.geometry("900x600")
        self.resizable(False, False)

        ctk.set_appearance_mode("System")
        ctk.set_default_color_theme("green")

        # Main Frame
        self.register_frame = ctk.CTkFrame(
            self,
            width=420,
            height=500,
            corner_radius=20
        )

        self.register_frame.place(
            relx=0.5,
            rely=0.5,
            anchor="center"
        )

        # Title
        title = ctk.CTkLabel(
            self.register_frame,
            text="Create New Account",
            font=("Arial", 24, "bold")
        )

        title.pack(pady=(30,20))

            # Username Entry
        self.username_entry = ctk.CTkEntry(
            self.register_frame,
            width=300,
            height=40,
            placeholder_text="Enter Username"
        )
        self.username_entry.pack(pady=10)

# Password Entry
        self.password_entry = ctk.CTkEntry(
            self.register_frame,
            width=300,
            height=40,
            placeholder_text="Enter Password",
            show="*"
        )
        self.password_entry.pack(pady=10)

# Confirm Password Entry
        self.confirm_password_entry = ctk.CTkEntry(
            self.register_frame,
            width=300,
            height=40,
            placeholder_text="Confirm Password",
            show="*"
        )
        self.confirm_password_entry.pack(pady=10)

# Register Button
        self.register_button = ctk.CTkButton(
            self.register_frame,
            text="Register",
            width=300,
            height=40
        )
        self.register_button.pack(pady=(20,10))

# Back Button
        self.back_button = ctk.CTkButton(
            self.register_frame,
            text="Back to Login",
            width=300,
            height=40,
            fg_color="gray",
            command=self.back_to_login
        )
        self.back_button.pack()

    def back_to_login(self):
        from ui.login import LoginWindow

        self.destroy()

        login_window = LoginWindow()
        login_window.mainloop()