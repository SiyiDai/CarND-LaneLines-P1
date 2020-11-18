from PyQt5.QtWidgets import QFileDialog


def load_value_and_initialize_field(default_value, text_target, action, result_function):
    if default_value is not None:
        text_target.setText(default_value)

    action.connect(result_function)


def start_file_dialog(who, caption, default_value, loaded_default_value, file_types, text_line):
    file_path = QFileDialog.getOpenFileName(
        who, caption, default_value if not loaded_default_value else loaded_default_value, file_types,
    )
    text_line.setText(file_path[0])

def start_folder_dialog(who, caption, default_value, loaded_default_value, text_line):
    folder_path = QFileDialog.getExistingDirectory(
        who, caption, default_value if not loaded_default_value else loaded_default_value, QFileDialog.ShowDirsOnly
    )
    text_line.setText(folder_path)