import customtkinter
import tkinter
from pynput.keyboard import Key, Listener
from pynput import keyboard
import pydirectinput
import sys
import os
import pydirectinput
import customtkinter
import threading

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        
        self.iconbitmap(r'C:\Users\srchby\Documents\Code\autoclickerapp\link.ico')

        # configure window
        self.title("srch's Autoclicker")
        self.geometry(f"{1024}x{512}")

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4,pady=12,padx=10)
        
        # sidebar widgets
        # logo
        self.logo = customtkinter.CTkLabel(
            self.sidebar_frame, 
            text="srch's Autoclicker",
            font=("Segoe UI", 32))
        self.logo.grid(row=0,column=0,pady=12,padx=10)
        # start button
        self.start_button = customtkinter.CTkButton(
            self.sidebar_frame,
            text="Start",
            font=('Segoe UI', 16)
        )
        self.start_button.grid(row=1,column=0,pady=12,padx=10)
        # stop button
        self.stop_button = customtkinter.CTkButton(
            self.sidebar_frame,
            text="Stop",
            font=('Segoe UI', 16),
            state='disabled'
        )
        self.stop_button.grid(row=2,column=0,pady=12,padx=10)
        # author
        self.author_label = customtkinter.CTkLabel(
            self.sidebar_frame,
            text='Made by srchby',
            font=('Segoe UI', 12)
        )
        self.author_label.grid(row=4,column=0,padx=12,pady=10)
        
        # frame widgets
        # minutes
        self.min_label = customtkinter.CTkLabel(
            self,
            text="Minutes",
            font=('Segoe UI', 12),
        )
        self.min_label.grid(row=0,column=1,padx=12, pady=10,sticky='nw')
        self.min_click_var = customtkinter.StringVar(
            self,
            value=str(0)
        )
        self.min_click = customtkinter.CTkEntry(
            self,
            font=("Segoe UI", 12),
            textvariable=self.min_click_var
        )
        self.min_click.grid(row=1,column=1,padx=12,pady=10,sticky='nw')
        # seconds box
        self.sec_label = customtkinter.CTkLabel(
            self,
            text="Seconds",
            font=('Segoe UI', 12),
        )
        self.sec_label.grid(row=0,column=2,padx=12, pady=10,sticky='nw')
        self.sec_click_var = customtkinter.StringVar(
            self,
            value=str(0)
        )
        self.sec_click = customtkinter.CTkEntry(
            self,
            font=("Segoe UI", 12),
            textvariable=self.sec_click_var
        )
        self.sec_click.grid(row=1,column=2,padx=12,pady=10,sticky='nw')
        # milliseconds box
        self.mil_label = customtkinter.CTkLabel(
            self,
            text="Milliseconds",
            font=('Segoe UI', 12),
        )
        self.mil_label.grid(row=0,column=3,padx=12, pady=10,sticky='nw')
        self.mil_click_var = customtkinter.StringVar(
            self,
            value=str(0)
        )
        self.mil_click = customtkinter.CTkEntry(
            self,
            font=("Segoe UI", 12),
            textvariable=self.mil_click_var
        )
        self.mil_click.grid(row=1,column=3,padx=12,pady=10,sticky='nw')
        # mouse buttons box
        self.mousemenu_label = customtkinter.CTkLabel(
            self,
            text='Mouse button',
            font=('Segoe UI', 12)
        )
        self.mousemenu_label.grid(row=2,column=1,padx=12,pady=10)
        self.mousemenu_var = customtkinter.StringVar(value="Left")
        self.mousemenu = customtkinter.CTkComboBox(
            self,
            font=("Segoe UI", 12),
            variable=self.mousemenu_var,
            values=["Left","Right"]
        )
        self.mousemenu.grid(row=3,column=1,padx=12,pady=10)

if __name__ == "__main__":
    app = App()
    app.mainloop()