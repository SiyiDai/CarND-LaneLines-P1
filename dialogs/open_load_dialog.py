from PyQt5.QtWidgets import QDialog
from ui_py.ui_loaddialog import Ui_LoadDialog

from dialogs.saved_values_paths import SavedValuesConstants
from dialogs.settings_loader_and_saver import SettingsLoaderAndSaver
from dialogs.saving_dialogs_helper_functions import (
    load_value_and_initialize_field,
    start_file_dialog,
)
import os


class OpenLoadDialog(QDialog):
    def __init__(self):
        super(OpenLoadDialog, self).__init__()
        self.ui = Ui_LoadDialog()
        self.ui.setupUi(self)

        self.settings_loader = SettingsLoaderAndSaver(SavedValuesConstants.LoaderDialog.SETTING_NAME)

        self.__initialize_fields_and_values()

    def __initialize_fields_and_values(self):

        load_value_and_initialize_field(
            self.settings_loader.read(SavedValuesConstants.LoaderDialog.ORIGINAL_IMAGE_PATH),
            self.ui.original_image_line_edit,
            self.ui.select_original_image_button.pressed,
            self.on_select_original_image_button_down,
        )
        load_value_and_initialize_field(
            self.settings_loader.read(SavedValuesConstants.LoaderDialog.ORGINAL_VIDEO_PATH),
            self.ui.original_video_line_edit,
            self.ui.select_original_video_button.pressed,
            self.on_select_original_video_button_down,
        )

    def on_select_original_image_button_down(self):
        start_file_dialog(
            self,
            "Open original image file",
            "/home",
            self.original_image_file_path(),
            "Image Files (*.png *.jpg *.bmp)",
            self.ui.original_image_line_edit,
        )

    def on_select_original_video_button_down(self):
        start_file_dialog(
            self,
            "Open original video file",
            "/home",
            self.original_image_file_path(),
            "Video files (*.mp4 *.mwv *.mov)",
            self.ui.original_video_line_edit,
        )

    def original_image_file_path(self):
        return self.ui.original_image_line_edit.text()

    def original_video_file_path(self):
        return self.ui.original_video_line_edit.text()

    def save_values(self):
        self.settings_loader.write(
            SavedValuesConstants.LoaderDialog.ORIGINAL_IMAGE_PATH, self.original_image_file_path(),
        )
        self.settings_loader.write(
            SavedValuesConstants.LoaderDialog.ORGINAL_VIDEO_PATH, self.original_video_file_path(),
        )

    def exec_(self):
        if not super(OpenLoadDialog, self).exec_():
            return False

        self.save_values()
        return True
