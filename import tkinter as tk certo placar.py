import tkinter as tk
from tkinter import messagebox

class ValueCounterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Value Counter")

        self.value = 0

        self.label = tk.Label(root, text=f"Valor: {self.value}", font=("Helvetica", 32))
        self.label.pack(pady=20)

        self.instructions = tk.Label(root, text="Use os botões abaixo para interagir.", font=("Helvetica", 16))
        self.instructions.pack(pady=10)

        self.create_buttons()
        self.create_entry()

    def create_buttons(self):
        frame = tk.Frame(self.root)
        frame.pack(pady=10)

        increment_button = tk.Button(frame, text="Incrementar", command=self.increment, font=("Helvetica", 14))
        increment_button.grid(row=0, column=0, padx=10)

        decrement_button = tk.Button(frame, text="Decrementar", command=self.decrement, font=("Helvetica", 14))
        decrement_button.grid(row=0, column=1, padx=10)

        reset_button = tk.Button(frame, text="Zerar", command=self.reset, font=("Helvetica", 14))
        reset_button.grid(row=0, column=2, padx=10)

        exit_button = tk.Button(frame, text="Sair", command=self.exit, font=("Helvetica", 14))
        exit_button.grid(row=0, column=3, padx=10)

    def create_entry(self):
        self.entry_label = tk.Label(self.root, text="Digite um valor:", font=("Helvetica", 16))
        self.entry_label.pack(pady=5)

        self.entry = tk.Entry(self.root, font=("Helvetica", 16))
        self.entry.pack(pady=5)

        self.set_value_button = tk.Button(self.root, text="Definir Valor", command=self.set_value_from_entry, font=("Helvetica", 14))
        self.set_value_button.pack(pady=10)

    def increment(self):
        self.value += 1
        self.update_label()

    def decrement(self):
        self.value -= 1
        self.update_label()

    def reset(self):
        self.value = 0
        self.update_label()

    def exit(self):
        self.root.quit()

    def set_value_from_entry(self):
        try:
            new_value = int(self.entry.get())
            self.value = new_value
            self.update_label()
        except ValueError:
            messagebox.showerror("Erro de entrada", "Por favor, insira um valor numérico válido.")

    def update_label(self):
        self.label.config(text=f"Valor: {self.value}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ValueCounterApp(root)
    root.mainloop()