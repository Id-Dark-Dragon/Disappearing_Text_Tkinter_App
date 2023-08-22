from customtkinter import CTkFrame, CTkButton, set_default_color_theme, set_appearance_mode, CTkLabel, CTkTextbox, \
    CTkCanvas, CTkProgressBar, END, IntVar
from CTkMessagebox import CTkMessagebox
from time import time
from ..configs import *


class InterFace(CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        self.parent = parent

        self.progressbar_1 = None
        self.final_countdown_duration = TIMER_DURATION
        self.sec_label = None
        self.textbox = None
        self.timer_text = None
        self.timer_canv = None
        self.top_label = None
        self.sec_label_text = "Type None Stop For 3 Minutes. If You Stop, Text Will Be Removed! " \
                              "\n___________________________________________________"

        set_appearance_mode(APPEARANCE_MODE)  
        set_default_color_theme(COLOR_THEME) 

        self.widgets()

    def widgets(self):
        # Widget initializing
        top_label = CTkLabel(master=self, text="The Most Dangerous Writing App", font=('one', 24, 'bold'),
                             text_color='red')
        self.sec_label = CTkLabel(master=self, text=self.sec_label_text, font=('one', 16),
                                  text_color='green')

        self.textbox = CTkTextbox(master=self, width=480, height=250, font=(None, 16))
        self.textbox.focus()


        self.progressbar_1 = CTkProgressBar(master=self, width=480)
        self.progressbar_1.set(0)


        self.timer_canv = CTkCanvas(master=self, width=150, height=75)
        self.timer_text = self.timer_canv.create_text(75, 35, text=f"00:0{self.final_countdown_duration}",
                                                      font=("Arial", 35, "bold"), fill="white")
        self.button = CTkButton(self, text="Start Again", width=150, height=75, font=("Arial", 16))
        # self.button.configure(state="disable")

        # Layout
        top_label.grid(row=0, column=0, columnspan=2, pady=10, padx=10)
        self.sec_label.grid(row=1, column=0, columnspan=2, padx=10)
        self.textbox.grid(row=2, column=0, columnspan=2, padx=10)
        self.progressbar_1.grid(row=3, column=0, columnspan=2, padx=10)
        self.timer_canv.grid(row=4, column=0, padx=10, pady=10)
        self.button.grid(row=4, column=1, padx=10, pady=10)

    def final_countdown_display(self, text, color):
        self.timer_canv.itemconfig(self.timer_text, text=text, font=("Arial", 35, "bold"),
                                   fill=color)

    def progressbar_display(self, val):
        self.progressbar_1.set(val/100)

    def popup_copy_to_clipboard(self):
        CTkMessagebox(title="Text Copied", message="Text Copied To Clipboard!")
