import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


class ExpenseTracker:
    def __init__(self, root):
        self.root = root
        self.root.title("Registro de Gastos")

        self.expenses_user1 = []
        self.expenses_user2 = []

        # Frame para la selección de usuario
        self.user_frame = ttk.Frame(self.root, padding="10")
        self.user_frame.grid(row=0, column=0, sticky=tk.W)

        self.user_label = ttk.Label(self.user_frame, text="Seleccionar Usuario:")
        self.user_label.grid(row=0, column=0, padx=5, pady=5)

        self.user_var = tk.StringVar()
        self.user_var.set("Usuario 1")
        self.user1_radio = ttk.Radiobutton(self.user_frame, text="Usuario 1", variable=self.user_var, value="Usuario 1")
        self.user1_radio.grid(row=0, column=1, padx=5, pady=5)
        self.user2_radio = ttk.Radiobutton(self.user_frame, text="Usuario 2", variable=self.user_var, value="Usuario 2")
        self.user2_radio.grid(row=0, column=2, padx=5, pady=5)

        # Frame para la entrada de datos
        self.entry_frame = ttk.Frame(self.root, padding="10")
        self.entry_frame.grid(row=1, column=0, sticky=tk.W)

        # Etiquetas y entradas
        self.desc_label = ttk.Label(self.entry_frame, text="Descripción del Gasto:")
        self.desc_label.grid(row=0, column=0, padx=5, pady=5)
        self.desc_entry = ttk.Entry(self.entry_frame, width=30)
        self.desc_entry.grid(row=0, column=1, padx=5, pady=5)

        self.amount_label = ttk.Label(self.entry_frame, text="Monto:")
        self.amount_label.grid(row=1, column=0, padx=5, pady=5)
        self.amount_entry = ttk.Entry(self.entry_frame, width=30)
        self.amount_entry.grid(row=1, column=1, padx=5, pady=5)

        # Botón para agregar gasto
        self.add_button = ttk.Button(self.entry_frame, text="Agregar Gasto", command=self.add_expense)
        self.add_button.grid(row=2, column=0, columnspan=2, pady=10)

        # Lista de gastos Usuario 1
        self.expense_list_user1 = tk.Listbox(self.root, width=50, height=10)
        self.expense_list_user1.grid(row=2, column=0, padx=10, pady=10)

        # Lista de gastos Usuario 2
        self.expense_list_user2 = tk.Listbox(self.root, width=50, height=10)
        self.expense_list_user2.grid(row=2, column=1, padx=10, pady=10)

        # Total de gastos Usuario 1
        self.total_label_user1 = ttk.Label(self.root, text="Total de Gastos Usuario 1: $0.00")
        self.total_label_user1.grid(row=3, column=0, padx=10, pady=10)

        # Total de gastos Usuario 2
        self.total_label_user2 = ttk.Label(self.root, text="Total de Gastos Usuario 2: $0.00")
        self.total_label_user2.grid(row=3, column=1, padx=10, pady=10)

        # Diferencia de pagos
        self.difference_label = ttk.Label(self.root, text="Diferencia de Pagos: $0.00")
        self.difference_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

    def add_expense(self):
        description = self.desc_entry.get()
        try:
            amount = float(self.amount_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Por favor ingrese un monto válido.")
            return

        user = self.user_var.get()

        if description and amount > 0:
            if user == "Usuario 1":
                self.expenses_user1.append((description, amount))
            else:
                self.expenses_user2.append((description, amount))

            self.update_expense_list()
            self.update_totals()
            self.update_difference()

            # Limpiar entradas
            self.desc_entry.delete(0, tk.END)
            self.amount_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Por favor ingrese una descripción y un monto válido.")

    def update_expense_list(self):
        self.expense_list_user1.delete(0, tk.END)
        for desc, amount in self.expenses_user1:
            self.expense_list_user1.insert(tk.END, f"{desc}: ${amount:.2f}")

        self.expense_list_user2.delete(0, tk.END)
        for desc, amount in self.expenses_user2:
            self.expense_list_user2.insert(tk.END, f"{desc}: ${amount:.2f}")

    def update_totals(self):
        total_user1 = sum(amount for desc, amount in self.expenses_user1)
        total_user2 = sum(amount for desc, amount in self.expenses_user2)

        self.total_label_user1.config(text=f"Total de Gastos Usuario 1: ${total_user1:.2f}")
        self.total_label_user2.config(text=f"Total de Gastos Usuario 2: ${total_user2:.2f}")

    def update_difference(self):
        total_user1 = sum(amount for desc, amount in self.expenses_user1)
        total_user2 = sum(amount for desc, amount in self.expenses_user2)
        #monto total de cada uno entre 2
        total_user1 = total_user1/2
        total_user2 = total_user2/2
        if total_user1 > total_user2:
            difference = total_user1 - total_user2
            self.difference_label.config(
                text=f"Diferencia de Pagos: Usuario 2 debe pagar ${difference:.2f} a Usuario 1")
        elif total_user2 > total_user1:
            difference = total_user2 - total_user1
            self.difference_label.config(
                text=f"Diferencia de Pagos: Usuario 1 debe pagar ${difference:.2f} a Usuario 2")
        else:
            self.difference_label.config(text="Diferencia de Pagos: Ambos han pagado lo mismo")


if __name__ == "__main__":
    root = tk.Tk()
    app = ExpenseTracker(root)
    root.mainloop()
