import tkinter as tk
from tkinter import ttk
import tkinter.font as font


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Clicker')
        self.geometry('300x200')

        self.count = 0

        self.font_style = font.Font(family='Lucida Grande', size=40)
        self.label = ttk.Label(self, text='0', font=self.font_style)
        self.label.pack(side=tk.TOP, expand=True, fill=tk.BOTH, pady=20)
        self.label.config(anchor='center')

        self.btn = ttk.Button(self, text='Click!', command=self.handle_click_btn)
        self.btn.pack(side=tk.TOP, pady=20)

    def handle_click_btn(self):
        self.count += 1
        self.label.config(text=f'{self.count}')


def main():
    app = App()
    app.mainloop()


main()
