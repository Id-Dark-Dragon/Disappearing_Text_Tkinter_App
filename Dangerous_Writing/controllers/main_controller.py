from customtkinter import END
from ..views import InterFace
from time import time
from ..utilities import play_sound
from ..configs import *
import pyperclip


class MainController:
    def __init__(self, root):

        self.progressbar_start_num = 0
        self.progressbar_duration = WRITING_DUR
        self.progressbar_after_func = None
        self.final_countdown_duration = TIMER_DURATION
        self.final_countdown_after_func = None
        self.final_countdown_is_on = None
        self.progressbar_is_on = None
        self.stop_typing_care_after_func = None
        self.text_len_last_check = None
        self.time_last_check = None

        self.root = root

        self.view = InterFace(self.root)
        self.view.pack(fill="both", expand=True)

        self.view.button.configure(command=self.start_again)
        self.view.textbox.bind("<Key>", self.typing_start_detection)

#   Core Functions
    def typing_start_detection(self, event):
        if len(self.view.textbox.get("0.0", END)) >= 5:
            # Typing has started
            self.view.textbox.unbind("<Key>")
            self.time_last_check = time()
            self.text_len_last_check = len(self.view.textbox.get("0.0", END))

            self.progressbar()
            self.stop_typing_care()

    def stop_typing_care(self):
        if time() - self.time_last_check > 1:

            if len(self.view.textbox.get("0.0", END)) == self.text_len_last_check:
                # Typing Stopped
                self.stop_typing_care_after_func = self.root.after(250, self.stop_typing_care)
                if self.final_countdown_is_on is False:
                    self.final_countdown(self.final_countdown_duration)

            else:
                # Ongoing typing
                self.time_last_check = time()
                self.text_len_last_check = len(self.view.textbox.get("0.0", END))
                try:
                    self.final_countdown_is_on = False
                    self.root.after_cancel(self.final_countdown_after_func)
                    self.view.final_countdown_display(text=f"00:0{self.final_countdown_duration}", color="white")

                except ValueError:
                    pass
                self.stop_typing_care_after_func = self.root.after(250, self.stop_typing_care)

        else:
            self.stop_typing_care_after_func = self.root.after(250, self.stop_typing_care)

    def final_countdown_stops(self):
        if self.final_countdown_is_on is True:
            self.root.after_cancel(self.final_countdown_after_func)
        self.final_countdown_is_on = False

        self.progressbar_start_num = 0
        self.view.progressbar_display(self.progressbar_start_num)

        self.view.textbox.delete('0.0', END)
        self.root.after_cancel(self.stop_typing_care_after_func)
        self.root.after_cancel(self.progressbar_after_func)

        self.text_len_last_check = None
        self.time_last_check = None

        self.view.final_countdown_display(text=f"00:0{self.final_countdown_duration}", color="white")

        self.view.textbox.bind("<Key>", self.typing_start_detection)

#   Count-Down Mechanisms
    def final_countdown(self, counter):
        self.final_countdown_is_on = True
        # Counting down mechanism
        if counter < 0:
            self.final_countdown_stops()
        else:
            play_sound()
            self.view.final_countdown_display(text=f'00:0{counter}', color="red")
            counter -= 1
            self.final_countdown_after_func = self.root.after(1000, self.final_countdown, counter)

    def progressbar(self):
        self.progressbar_start_num = self.progressbar_start_num + 100 / self.progressbar_duration

        self.view.progressbar_display(self.progressbar_start_num)

        if self.progressbar_start_num > 100:
            self.root.after_cancel(self.progressbar_after_func)
            self.copy_to_clipboard()
            self.start_again()

        else:
            self.progressbar_after_func = self.root.after(1000, self.progressbar)

#   Additional Functions
    def copy_to_clipboard(self):
        pyperclip.copy(self.view.textbox.get("0.0", END))
        self.view.popup_copy_to_clipboard()

    def start_again(self):
        self.final_countdown_stops()
        self.view.textbox.bind("<Key>")

