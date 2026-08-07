import customtkinter as ctk


class DashboardWindow(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("Personal Expense Tracker Pro")
        self.geometry("1200x700")
        self.resizable(False, False)

        ctk.set_appearance_mode("System")
        ctk.set_default_color_theme("green")

        title = ctk.CTkLabel(
            self,
            text="Personal Expense Tracker Pro",
            font=("Arial", 28, "bold")
        )

        title.pack(pady=30)

        welcome = ctk.CTkLabel(
            self,
            text="Welcome, Siraj 👋",
            font=("Arial", 22, "bold")
        )

        welcome.pack(pady=20)

            # Income Card
        income_card = ctk.CTkFrame(
            self,
            width=500,
            height=70,
            corner_radius=15
        )
        income_card.pack(pady=10)

        income_label = ctk.CTkLabel(
            income_card,
            text="💰 Total Income : ₹0.00",
            font=("Arial", 18, "bold")
        )
        income_label.place(relx=0.5, rely=0.5, anchor="center")


# Expense Card
        expense_card = ctk.CTkFrame(
            self,
            width=500,
            height=70,
            corner_radius=15
        )
        expense_card.pack(pady=10)

        expense_label = ctk.CTkLabel(
            expense_card,
            text="💸 Total Expense : ₹0.00",
            font=("Arial", 18, "bold")
        )
        expense_label.place(relx=0.5, rely=0.5, anchor="center")


# Balance Card
        balance_card = ctk.CTkFrame(
            self,
            width=500,
            height=70,
            corner_radius=15
        )   
        balance_card.pack(pady=10)

        balance_label = ctk.CTkLabel(
            balance_card,
            text="🏦 Current Balance : ₹0.00",
            font=("Arial", 18, "bold")
        )
        balance_label.place(relx=0.5, rely=0.5, anchor="center")