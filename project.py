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

auto_key = Key.f6

button1 = "Left"
clicktype = "Single"
repeattype = 1

class App(customtkinter.CTk):
    auto = False
    auto1 = False
    
    global resource
    def resource(relative_path):
        base_path = getattr(sys, "_MEIPASS", os.path.dirname(
            os.path.abspath(__file__)))
        return os.path.join(base_path, relative_path)
    
    def __init__(self):
        super().__init__()
        
        # configure window
        self.title("srch's Autoclicker")
        self.geometry(f"{768}x{256}")
        
        self.wm_iconbitmap("link.ico")

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4,pady=12,padx=10)
        
        # sidebar widgets
        # logo
        self.logo = customtkinter.CTkLabel(
            self.sidebar_frame, 
            text="srch's Autoclicker",
            font=("Segoe UI", 24))
        self.logo.grid(row=0,column=0,pady=12,padx=10)
        # start button
        self.start_on_button = customtkinter.CTkButton(
            self.sidebar_frame,
            text="Start (F6)",
            font=('Segoe UI', 16)
        )
        self.start_on_button.grid(row=1,column=0,pady=12,padx=10)
        # stop button
        self.stop_off_button = customtkinter.CTkButton(
            self.sidebar_frame,
            text="Stop (F6)",
            font=('Segoe UI', 16),
            state='disabled'
        )
        self.stop_off_button.grid(row=2,column=0,pady=12,padx=10)
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
            command=self.mousemenu_event,
            values=["Left","Right"]
        )
        self.mousemenu.grid(row=3,column=1,padx=12,pady=10)
        
        self.mousemenu.bind("<Return>", lambda e: self.custombutton())
        
        self.lis2 = keyboard.Listener(on_press=self.on_press1)
        self.lis2.start()
        
    def mousemenu_event(self, choice5):
        global button1
        self.choice5 = choice5

        if self.choice5 == "Left":
            button1 = "Left"
        elif self.choice5 == "Right":
            button1 = "Right"
            
    def custombutton(self):
        global button1
        button1 = self.mousemenu_var.get()
        self.frame.focus_set()
        
    def start_button(self):
        if (True and not self.pause):
            self.lis2.stop()
            self.pause = False

            self.autoclc = threading.Thread(target=self.autoClick)
            self.autoclc.start()

            self.mousemenu.configure(state="normal")
            self.mousemenu.configure(state="disabled")
            self.start_on_button.configure(state="disabled")
            self.stop_off_button.configure(state="enabled")
        else:
            if not self.pause:
                self.lis2.stop()
                self.pause = False

                self.autohol = threading.Thread(target=self.autoHold)
                self.autohol.start()

                self.mousemenu.configure(state="normal")
                self.mousemenu.configure(state="disabled")
                self.start_on_button.configure(state="disabled")
                self.stop_button.configure(state="enabled")    
        
    def on_press1(self, key):
        if not self.auto1 and key == auto_key:
            self.pause = False
            self.auto1 = True
            self.auto = False
            self.lis2.stop()
            self.start_button()
            
    def on_press(self, key):
        if self.auto1 and key == auto_key:
            self.pause = True
            self.auto1 = False
            self.stop_button()
            self.lis2 = keyboard.Listener(on_press=self.on_press1)
            self.lis2.start()
            
    def autoHold(self):
        self.auto = True
        self.auto1 = False
        self.pause = False
        
        lis = Listener(on_press=self.on_press)
        lis.start()
        
        while self.auto:
            if not self.pause:
                if button1 == "Left":
                    pydirectinput.mouseDown(button="left")
                elif button1 == "Right":
                    pydirectinput.mouseDown(button="right")
                else:
                    pydirectinput.keyDown(keys=self.mousemenu.get().lower())
                    pydirectinput.PAUSE = self.interval
                    
            if self.pause:
                self.autohol.join()
                break
        lis.stop()
        
    def autoClick(self):
        self.auto = False
        self.auto1 = True
        self.pause = False
        
        lis1 = Listener(on_press=self.on_press)
        lis1.start()
        # correct the decimal house
        self.interval = float(self.min_click.get()) * 60.0 + float(self.sec_click.get()) + float(self.mil_click.get()) * 0.001
        if repeattype == 1:
            while self.auto1:
                if not self.pause:
                    if self.mousemenu.get() == "Left":
                        pydirectinput.click(button="left")
                        pydirectinput.PAUSE = self.interval
                    elif self.mousemenu.get() == "Right":
                        pydirectinput.click(button="right")
                        pydirectinput.PAUSE = self.interval
                    else:
                        pydirectinput.press(keys=self.mousemenu.get().lower())
                        pydirectinput.PAUSE = self.interval
                if self.pause:
                    break
    def stop_button(self):
        self.pause = True
        
        if button1 == "Left":
            self.auto1 = False
            pydirectinput.mouseUp(button='left')
        elif button1 == "Right":
            self.auto1 = False
            pydirectinput.mouseUp(button="right")
        
        self.mousemenu.configure(state="normal")
        self.start_on_button.configure(state="enabled")
        self.stop_off_button.configure(state="disabled")
    
    def on_close(self, event=0):
        self.destroy()
        
    def start(self):
        self.mainloop()
    


if __name__ == "__main__":
    app = App()
    app.mainloop()