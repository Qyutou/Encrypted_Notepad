from configparser import ConfigParser

config_object = ConfigParser()


def create_config_file():
    config_object["STARTUP_SETTINGS"] = {
        "startup_resolution": "1200x800",
    }

    config_object["COLORS"] = {
        "text_area_background_color": "#282A36",
        "text_area_foreground_color": "#F8F8F2",
        "scrollbar_background_color": "#282A36",
        "scrollbar_foreground_color": "#7A7A7A",
        "scrollbar_active_color": "#6E46A4",
        "menu_background_color": "#1F1F29",
        "menu_foreground_color": "#F8F8F2",
        "menu_active_color": "#6E46A4",
    }

    config_object["GENERAL"] = {
        "tab_size": "4",
        "font": "ubuntu 14",
    }

    config_object["KEY_BINDS"] = {
        "new_file": "Control-n",
        "open_file": "Control-o",
        "save_file": "Control-s",
        "save_file_as": "Control-Shift-S"
    }

    with open("encrypted_notepad_rc.ini", "w") as config:
        config_object.write(config)


config_object.read("encrypted_notepad_rc.ini")

if len(config_object.sections()) == 0:
    create_config_file()


def read_colors_section():
    colors_section = [config_object["COLORS"]["text_area_background_color"],
                      config_object["COLORS"]["text_area_foreground_color"],
                      config_object["COLORS"]["scrollbar_background_color"],
                      config_object["COLORS"]["scrollbar_foreground_color"],
                      config_object["COLORS"]["scrollbar_active_color"],
                      config_object["COLORS"]["menu_background_color"],
                      config_object["COLORS"]["menu_foreground_color"],
                      config_object["COLORS"]["menu_active_color"]]

    return colors_section


def read_startup_settings_section():
    startup_section = [config_object["STARTUP_SETTINGS"]["startup_resolution"]]

    return startup_section


def read_general_section():
    general_section = [config_object["GENERAL"]["tab_size"],
                       config_object["GENERAL"]["font"]]

    return general_section


def read_key_binds_section():
    key_binds_section = [config_object["KEY_BINDS"]["new_file"],
                         config_object["KEY_BINDS"]["open_file"],
                         config_object["KEY_BINDS"]["save_file"],
                         config_object["KEY_BINDS"]["save_file_as"]]

    return key_binds_section
