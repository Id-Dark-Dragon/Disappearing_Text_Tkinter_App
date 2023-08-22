# this brief test just provides test for 2 core functions.
import time
import unittest
from tkinter import Tk
from unittest.mock import patch, MagicMock

from Dangerous_Writing.controllers import MainController
from Dangerous_Writing.views import InterFace


class TestMainApp(unittest.TestCase):
    def setUp(self):
        self.root = Tk()
        self.controller = MainController(self.root)

    def tearDown(self):
        self.root.destroy()

    def test_typing_detection_typing_started(self):
        # Simulate typing event and test typing detection logic
        self.controller.view.textbox.insert(0.0, "Some text")
        self.controller.typing_start_detection(None)

        self.assertAlmostEquals(self.controller.time_last_check, time.time(), delta=0.1)
        self.assertEquals(self.controller.text_len_last_check, len("Some text") + 1)

    @patch("Dangerous_Writing.controllers.MainController.progressbar")
    def test_typing_start_detection_typing_not_started(self, mock_unbind_function):
        self.controller.view.textbox.insert(0.0, "tex")
        self.controller.typing_start_detection(None)

        mock_unbind_function.assert_not_called()

    @patch("time.time")
    def test_stop_typing_care_typing_stopped(self, mock_time):
        mock_time.return_value = 12
        self.controller.time_last_check = 10
        self.controller.text_len_last_check = 10
        self.controller.view.textbox.insert(0.0, "Some text")
        self.controller.final_countdown_is_on = False

        mock_countdown_function = MagicMock()
        with patch("Dangerous_Writing.controllers.MainController.final_countdown", mock_countdown_function):
            self.controller.stop_typing_care()
            mock_countdown_function.assert_called()

    @patch("time.time")
    def test_stop_typing_care_typing_ongoing(self, mock_time):
        mock_time.return_value = 12
        self.controller.time_last_check = 10
        self.controller.text_len_last_check = 11
        self.controller.view.textbox.insert(0.0, "Some text")
        self.controller.final_countdown_is_on = True

        self.controller.stop_typing_care()
        self.assertFalse(self.controller.final_countdown_is_on)

    def test_final_countdown_stops(self):
        self.final_countdown_is_on = True
        mock_after_cancel_func = MagicMock()

        with patch.object(self.controller.root, "after_cancel", mock_after_cancel_func):
            self.controller.final_countdown_stops()
            mock_after_cancel_func.assert_called()



if __name__ == "__main__":
    unittest.main()
