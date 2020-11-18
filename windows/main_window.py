from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QPixmap, QColor, QImage
from PyQt5.QtWidgets import QMainWindow, QColorDialog
import os
import cv2
import numpy as np
from PIL import Image

from ui_py.ui_mainwindow import Ui_MainWindow
from utils.saved_values_paths import SavedValuesConstants

from utils.saved_values_paths import SavedValuesConstants
from utils.settings_loader_and_saver import SettingsLoaderAndSaver
from utils.saving_dialogs_helper_functions import (
    load_value_and_initialize_field,
    start_file_dialog,
    start_folder_dialog
)
import os

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # setup ui layout
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # register event handlers
        self.ui.mode_selection_comboBox.currentTextChanged.connect(self.__refresh_ui)
        self.ui.load_path_lineEdit.textChanged.connect(self.__refresh_ui)

        # initialize load and save dialogs
        self.settings_loader = SettingsLoaderAndSaver(SavedValuesConstants.LoaderDialog.SETTING_NAME)
        self.__initialize_fields_and_values()

    def __initialize_fields_and_values(self):
        load_value_and_initialize_field(
            self.settings_loader.read(SavedValuesConstants.LoaderDialog.LOAD_PATH),
            self.ui.load_path_lineEdit,
            self.ui.load_path_pushButton.pressed,
            self.on_select_load_path_button_down,
        )
        load_value_and_initialize_field(
            self.settings_loader.read(SavedValuesConstants.LoaderDialog.SAVE_PATH),
            self.ui.save_path_lineEdit,
            self.ui.save_path_pushButton.pressed,
            self.on_select_save_path_button_down,
        )

    def on_select_load_path_button_down(self):
        start_file_dialog(
            self,
            "Open any files",
            "/home",
            self.load_file_path(),
            "Image Files (*.png *.jpg *.bmp);; Video files (*.mp4 *.mwv *.mov)",
            self.ui.load_path_lineEdit,
        )
        self.set_default_save_file_path(self.load_file_path())
        self.save_values(path=SavedValuesConstants.LoaderDialog.LOAD_PATH, value= self.load_file_path())

    def on_select_save_path_button_down(self):
        start_folder_dialog(
            self,
            "Create/choose any folder",
            "/home",
            self.save_file_path(),
            self.ui.save_path_lineEdit,
        )
        self.save_values(path=SavedValuesConstants.LoaderDialog.SAVE_PATH, value=self.save_file_path())

    def load_file_path(self):
        return self.ui.load_path_lineEdit.text()

    def save_file_path(self):
        return self.ui.save_path_lineEdit.text()

    def set_default_save_file_path(self, path):
        self.ui.save_path_lineEdit.setText(os.path.dirname(path))

    def save_values(self, path, value):
        self.settings_loader.write(path, value)

    def on_image_button_is_checked(self, path):
        self.__refresh_original_image(path)
        # self.detection_frame = self.show_result_image(self.original_image_path, detection_img)
        # self.__refresh_detection_result(self.detection_frame)

    def on_video_button_is_checked(self, path):
        pass
        # self.__refresh_original_video(path)
        # self.cap = cv2.VideoCapture(self.original_video_path)
        # self.detection_img = detection_img
        # self.timer_video = QTimer(self)
        # self.timer_video.timeout.connect(self.show_result_video)
        # self.timer_video.start(50)

    def on_camera_button_is_checked(self, detection_img):
        pass
        # self.cap = cv2.VideoCapture(0)
        # self.detection_img = detection_img
        # self.timer_camera = QTimer(self)
        # self.timer_camera.timeout.connect(self.show_result_camera_stream)
        # self.timer_camera.start(5)

    def show_result_image(self, pic_path, detection_img):
        pass
        # image, change the post-it part in pic
        # frame = self.__convert_rgb_to_bgr(pic_path)
        # detection_result = self.detect_and_detection(frame.copy(), detection_img)
        # return detection_result

    def show_result_video(self):
        pass
        # Video, change the post-it part in video
        # detection_img = self.detection_img
        # ret, frame = self.cap.read()
# 
        # if frame is not None:
            # detection_result = self.detect_and_detection(frame.copy(), detection_img)
# 
            # detection_result = self.__convert_bgr_to_rgb(detection_result)
            # frame = self.__convert_bgr_to_rgb(frame)
# 
            # self.__refresh_original_video(frame)
            # self.__refresh_detection_video(detection_result)
# 
            # if self.ui.pushButton_pause.isChecked():
                # self.timer_video.stop()
                # return
# 
        # else:
            # self.timer_video.stop()
            # return

    def show_result_camera_stream(self):
        pass
        # webcam, change the post-it part in camera stream
        # detection_img = self.detection_img
        # ret, frame = self.cap.read()
# 
        # if frame is not None:
            # detection_result = self.detect_and_detection(frame.copy(), detection_img)
# 
            # detection_result = self.__convert_bgr_to_rgb(detection_result)
            # frame = self.__convert_bgr_to_rgb(frame)
# 
            # self.__refresh_original_video(frame)
            # self.__refresh_detection_video(detection_result)
# 
        # else:
            # self.timer_camera.stop()
            # return

    def detect_and_detection(self, frame, detection_img):
        pass
        # contours, hierarchy = self.find_contours(frame)
        # try:
        #     # find biggest bounding box
        #     biggest, index = 0, 0
        #     rect = list()
        #     for i in range(len(contours)):
        #         x, y, w, h = cv2.boundingRect(contours[i])
        #         rect.append(((x, y), (x + w, y + h), (w, h)))
        #         if w * h > biggest:
        #             biggest = w * h
        #             index = i

        #     # draw bounding box in captured image
        #     height = rect[index][1][1] - rect[index][0][1]
        #     width = rect[index][1][0] - rect[index][0][0]
        #     trans_pt1 = (int(rect[index][0][0] + width / 4), int(rect[index][0][1] + height / 4))
        #     trans_pt2 = (int(rect[index][1][0] - width / 4), int(rect[index][1][1] - height / 4))

        #     # frame = cv2.rectangle(frame, trans_pt1, trans_pt2, (0, 0, 255), 2)
        #     temp_detection = np.array(
        #         detection_img.resize((int(trans_pt2[0] - trans_pt1[0]), int(trans_pt2[1] - trans_pt1[1])))
        #     )
        #     frame[trans_pt1[1] : trans_pt2[1], trans_pt1[0] : trans_pt2[0]] = temp_detection

        # except:
        #     pass
        # return frame

    def __refresh_ui(self):
        if self.ui.mode_selection_comboBox.currentText() == "Image":
            self.on_image_button_is_checked(self.load_file_path())
        if self.ui.mode_selection_comboBox.currentText() == "Video":
            self.on_video_button_is_checked(self.load_file_path())
        if self.ui.mode_selection_comboBox.currentText() == "Webcam":
            # self.on_camera_button_is_checked()
            pass

    def __refresh_original_image(self, original_image_path):
        pix_map = QPixmap(original_image_path)
        self.ui.original_source_label.setPixmap(pix_map)

    def __refresh_detection_result(self, frame):
        frame = self.__convert_bgr_to_rgb(frame)
        source_image = QImage(frame.data, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
        self.ui.detection_result_label.setPixmap(QPixmap.fromImage(source_image))

    def __refresh_original_video(self, frame):
        source_image = QImage(frame.data, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
        self.ui.original_source_label.setPixmap(QPixmap.fromImage(source_image))

    def __refresh_detection_video(self, detection_result):
        show_image = QImage(detection_result.data, detection_result.shape[1], detection_result.shape[0], QImage.Format_RGB888)
        self.ui.detection_result_label.setPixmap(QPixmap.fromImage(show_image))

