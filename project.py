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

root = customtkinter.CTk()
root.geometry("500x500")
root.title('Autoclicker')

root.iconbitmap(r'C:\Users\srchby\Documents\Code\autoclickerapp\link.ico')

customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('dark-blue')

frame = customtkinter.CTkFrame(master=root)
frame.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
frame.grid_columnconfigure(0, weight=1)
frame.grid_columnconfigure(1, weight=1)
frame.grid_columnconfigure(5, weight=1)

frame.pack(pady=12,padx=10)

title = customtkinter.CTkLabel(master=frame, text='Autoclicker', font= ("Segoe UI", 24))
title.pack(pady=12,padx=10)

start_auto_button = customtkinter.CTkButton(
    master=frame,
    text="Start",
    font=('Segoe UI', 16)
)
start_auto_button.pack(pady=12,padx=10)

stop_auto_button = customtkinter.CTkButton(
    master=frame,
    text='Stop',
    font=("Segoe UI", 16),
    state='disabled'
)
stop_auto_button.pack(pady=12,padx=10)

buttonmenu_txt= customtkinter.CTkLabel(
    master=frame,
    text='Button Menu',
    font=('Segoe UI', 16)
)
buttonmenu_txt.pack(pady=12,padx=10)

buttonmenu_var = customtkinter.StringVar(value='Left')

buttonmenu = customtkinter.CTkComboBox(
    master=frame,
    font=('Segoe UI', 16),
    variable=buttonmenu_var,
    values=['Left','Middle','Right']
)
buttonmenu.pack(pady=12,padx=10)

clickinterval_txt= customtkinter.CTkLabel(
    master=frame,
    text='Click Interval',
    font=('Segoe UI', 16)
)
clickinterval_txt.pack(pady=12,padx=10)

clickinterval_var = customtkinter.StringVar(
    master=frame,
    value=str(0.01)
)

clickinterval = customtkinter.CTkEntry(
    master=frame,
    font=('Segoe UI', 16),
    textvariable=clickinterval_var
)
clickinterval.pack(pady=12,padx=10)

root.mainloop()