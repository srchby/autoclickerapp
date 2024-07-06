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

        self.logo = customtkinter.CTkLabel(
            self.sidebar_frame, 
            text="srch's Autoclicker",
            font=("Segoe UI", 32))
        self.logo.grid(row=0,column=0,pady=12,padx=10)
        
        self.start_button = customtkinter.CTkButton(
            self.sidebar_frame,
            text="Start",
            font=('Segoe UI', 16)
        )
        self.start_button.grid(row=1,column=0,pady=12,padx=10)
        
        self.stop_button = customtkinter.CTkButton(
            self.sidebar_frame,
            text="Stop",
            font=('Segoe UI', 16),
            state='disabled'
        )
        self.stop_button.grid(row=2,column=0,pady=12,padx=10)
        
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
        
        

if __name__ == "__main__":
    app = App()
    app.mainloop()

# buttonmenu_txt= customtkinter.CTkLabel(
#     master=frame,
#     text='Button Menu',
#     font=('Segoe UI', 16)
# )
# buttonmenu_txt.grid(row=0,column=1,pady=12,padx=10)
# buttonmenu_var = customtkinter.StringVar(value='Left')
# buttonmenu = customtkinter.CTkComboBox(
#     master=frame,
#     font=('Segoe UI', 16),
#     variable=buttonmenu_var,
#     values=['Left','Middle','Right']
# )
# clickinterval_var = customtkinter.StringVar(
#     master=frame,
#     value=str(0.01)
# )
# clickinterval = customtkinter.CTkEntry(
#     master=frame,
#     font=('Segoe UI', 16),
#     textvariable=clickinterval_var
# )
# clickinterval.grid(row=3,column=1,pady=12,padx=10)
# root.mainloop()