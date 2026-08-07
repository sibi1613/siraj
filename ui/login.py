import customtkinter as ctk


class LoginWindow(ctk.CTk):
    def __init__(self):
        super().__init__()

        # ---------------- Window Settings ----------------
        self.title("Personal Expense Tracker Pro")
        self.geometry("900x600")
        self.resizable(False, False)

        ctk.set_appearance_mode("System")
        ctk.set_default_color_theme("green")

        # ---------------- Login Frame ----------------
        self.login_frame = ctk.CTkFrame(
            self,
            width=420,
            height=450,
            corner_radius=20
        )

        self.login_frame.place(relx=0.5, rely=0.5, anchor="center")

        # ---------------- Title ----------------
        self.title_label = ctk.CTkLabel(
            self.login_frame,
            text="💰 Personal Expense Tracker Pro",
            font=("Arial", 24, "bold")
        )
        self.title_label.pack(pady=(30, 10))

        # ---------------- Welcome ----------------
        self.welcome_label = ctk.CTkLabel(
            self.login_frame,
            text="Welcome Back!",
            font=("Arial", 18)
        )
        self.welcome_label.pack(pady=(0, 20))

        # ---------------- Username ----------------
        self.username_entry = ctk.CTkEntry(
            self.login_frame,
            width=300,
            height=40,
            placeholder_text="Enter Username"
        )
        self.username_entry.pack(pady=10)

        # ---------------- Password ----------------
        self.password_entry = ctk.CTkEntry(
            self.login_frame,
            width=300,
            height=40,
            placeholder_text="Enter Password",
            show="*"
        )
        self.password_entry.pack(pady=10)

        # ---------------- Login Button ----------------
        self.login_button = ctk.CTkButton(
            self.login_frame,
            text="Login",
            width=300,
            height=40,
            command=self.login
        )
        self.login_button.pack(pady=(20, 10))

        # ---------------- Register Button ----------------
        self.register_button = ctk.CTkButton(
            self.login_frame,
            text="Register",
            width=300,
            height=40,
            fg_color="gray",
            command=self.open_register
        )
        self.register_button.pack()

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        print("Username:", username)
        print("Password:", password)

    def open_register(self):
        from ui.register import RegisterWindow

        self.destroy()

        register_window = RegisterWindow()
        register_window.mainloop()