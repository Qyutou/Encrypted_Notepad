import importlib
import sys
import os
from pathlib import Path
from tkinter import Tk, ttk, Text, Menu, END
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter.messagebox import askyesno
import tkinter.font as tkinter_font

config_handler_module = importlib.import_module(".config_handler", "encrypted_notepad")
cryptography_handler_module = importlib.import_module(".cryptography_handler", "encrypted_notepad")

file = None


def menu_new_file(root, text_area):
    global file
    file = None
    root.title("Untitled - encrypted_notepad")
    text_area.delete("1.0", END)


def menu_open_file(root, text_area, certain_file=None):
    global file
    if certain_file is None:
        file = askopenfilename(defaultextension=".txt",
                               filetypes=[("All Files", "*.*"),
                                          ("Text Documents", "*.txt")])
    else:
        file = certain_file
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + " - Encrypted Notepad")
        f = open(file, "r")
        text_area.delete("1.0", END)
        text_area.insert(1.0, f.read())
        f.close()


def menu_open_file_encoded(root, text_area):
    global file
    file = askopenfilename(defaultextension=".bin",
                           filetypes=[("Binary files", "*.bin"), ("All Files", "*.*")], title="Open (Encoded)")
    if file == "":
        file = None
    else:
        text_area.delete("1.0", END)
        root.title(os.path.basename(file) + " - Encrypted Notepad")
        decoded_text = cryptography_handler_module.decode_text(file)
        text_area.insert(1.0, decoded_text)


def menu_save_file(root, text_area):
    global file

    if file is None:
        file = asksaveasfilename(defaultextension=".txt", filetypes=[("Text Documents", "*.txt"), ("All Files", "*.*")])
        if file == "":
            file = None
        else:
            f = open(file, "w")
            f.write(text_area.get(1.0, END))
            f.close()
            root.title(os.path.basename(file) + " - Encrypted Notepad")
    else:
        if os.path.splitext(file)[-1] == ".bin":
            message = text_area.get(1.0, END)
            file_out = file
            cryptography_handler_module.encode_text(message, file_out)
            root.title(os.path.basename(file) + " - Encrypted Notepad")
        else:

            f = open(file, "w")
            f.write(text_area.get(1.0, END))
            f.close()


def menu_save_file_as(root, text_area):
    global file

    file = asksaveasfilename(defaultextension=".txt", filetypes=[("Text Documents", "*.txt"), ("All Files", "*.*")])
    if file == "":
        file = None
    else:
        f = open(file, "w")
        f.write(text_area.get(1.0, END))
        f.close()
        root.title(os.path.basename(file) + " - Encrypted Notepad")


def menu_save_file_as_encoded(root, text_area):
    global file

    file = asksaveasfilename(defaultextension=".bin", filetypes=[("Binary files", "*.bin"), ("All Files", "*.*")],
                             title="Save as (Encoded)")
    if file == "":
        file = None
    else:
        message = text_area.get(1.0, END)
        file_out = file
        cryptography_handler_module.encode_text(message, file_out)
        root.title(os.path.basename(file) + " - Encrypted Notepad")


def menu_open_settings(root, text_area):
    config_file_path = Path("encrypted_notepad_rc.ini").absolute()

    global file
    file = config_file_path

    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + " - Encrypted Notepad")
        f = open(file, "r")
        text_area.delete("1.0", END)
        text_area.insert(1.0, f.read())
        f.close()


def menu_quit_app(root):
    answer = askyesno(title="Confirmation", message="Are you sure that you want to quit?")

    if answer:
        root.destroy()


def menu_undo(root, text_area):
    text_area.event_generate("<<Undo>>")


def menu_redo(root, text_area):
    text_area.event_generate("<<Redo>>")


def menu_copy(root, text_area):
    text_area.event_generate("<<Copy>>")


def menu_cut(root, text_area):
    text_area.event_generate("<<Cut>>")


def menu_paste(root, text_area):
    text_area.event_generate("<<Paste>>")


def read_argv():
    if len(sys.argv) > 1:
        expected_file = sys.argv[1]
        if os.path.isfile(expected_file):
            return expected_file
        else:
            raise FileNotFoundError
    return None


def add_text_area(root, colors, general):
    text_area_background_color = colors[0]
    text_area_foreground_color = colors[1]
    scrollbar_background_color = colors[2]
    scrollbar_foreground_color = colors[3]
    scrollbar_active_color = colors[4]

    vertical_scroll_bar_style = ttk.Style(root)
    vertical_scroll_bar_style.layout('custom.Vertical.TScrollbar',
                                     [('Vertical.Scrollbar.trough',
                                       {'children': [('Vertical.Scrollbar.thumb',
                                                      {'expand': '1', 'sticky': 'nswe'})],
                                        'sticky': 'ns'})])
    vertical_scroll_bar_style.configure('custom.Vertical.TScrollbar',
                                        borderwidth=0,
                                        background=scrollbar_foreground_color,
                                        troughcolor=scrollbar_background_color)
    vertical_scroll_bar_style.map('custom.Vertical.TScrollbar',
                                  background=[('disabled', scrollbar_background_color),
                                              ('pressed', scrollbar_active_color)])

    vertical_scroll_bar = ttk.Scrollbar(root, style="custom.Vertical.TScrollbar")

    text_area = Text(root, font=general[1], yscrollcommand=vertical_scroll_bar.set)
    text_area.config(borderwidth=0, highlightthickness=0,
                     background=text_area_background_color,
                     foreground=text_area_foreground_color,
                     insertbackground=text_area_foreground_color,
                     undo=True, autoseparators=True, maxundo=-1)

    font = tkinter_font.Font(font=text_area['font'])
    tab_size = font.measure(" " * int(general[0]))
    text_area.config(tabs=tab_size)

    vertical_scroll_bar.config(command=text_area.yview)

    vertical_scroll_bar.pack(side="right", fill="y")
    text_area.pack(expand=True, fill="both")

    return text_area


def add_top_menu(root, text_area, colors, general, key_binds):
    # parse inputs
    menu_background_color = colors[5]
    menu_foreground_color = colors[6]
    menu_active_color = colors[7]

    font = general[1]

    new_file_key_bind = key_binds[0]
    open_file_key_bind = key_binds[1]
    save_file_key_bind = key_binds[2]
    save_file_as_key_bind = key_binds[3]

    # create menu
    top_menu = Menu(root, tearoff=0, relief='flat', font=font, activeborderwidth=0,
                    background=menu_background_color, activebackground=menu_background_color,
                    foreground=menu_foreground_color, activeforeground=menu_active_color)

    # create file menu
    file_menu = Menu(top_menu, tearoff=0, relief='flat', font=font, activeborderwidth=0,
                     background=menu_background_color, activebackground=menu_background_color,
                     foreground=menu_foreground_color, activeforeground=menu_active_color)
    file_menu.add_command(label="New", command=lambda: menu_new_file(root, text_area),
                          accelerator=new_file_key_bind)
    file_menu.add_command(label="Open", command=lambda: menu_open_file(root, text_area),
                          accelerator=open_file_key_bind)
    file_menu.add_command(label="Open (Encoded)", command=lambda: menu_open_file_encoded(root, text_area))
    file_menu.add_command(label="Save", command=lambda: menu_save_file(root, text_area),
                          accelerator=save_file_key_bind)
    file_menu.add_command(label="Save As...", command=lambda: menu_save_file_as(root, text_area),
                          accelerator=save_file_as_key_bind)
    file_menu.add_command(label="Save As... (Encoded)", command=lambda: menu_save_file_as_encoded(root, text_area))
    file_menu.add_separator()
    file_menu.add_command(label="Settings", command=lambda: menu_open_settings(root, text_area))
    file_menu.add_separator()
    file_menu.add_command(label="Exit", command=lambda: menu_quit_app(root))

    # create edit menu
    edit_menu = Menu(top_menu, tearoff=0, relief='flat', font=font, activeborderwidth=0,
                     background=menu_background_color, activebackground=menu_background_color,
                     foreground=menu_foreground_color, activeforeground=menu_active_color)

    edit_menu.add_command(label="Undo", command=lambda: menu_undo(root, text_area), accelerator="<Control-z>")
    edit_menu.add_command(label="Redo", command=lambda: menu_redo(root, text_area), accelerator="<Control-Shift-Z>")
    edit_menu.add_separator()
    edit_menu.add_command(label="Copy", command=lambda: menu_copy(root, text_area), accelerator="<Control-c>")
    edit_menu.add_command(label="Cut", command=lambda: menu_cut(root, text_area), accelerator="<Control-x>")
    edit_menu.add_command(label="Paste", command=lambda: menu_paste(root, text_area), accelerator="<Control-v>")

    # add sub menu to menu
    top_menu.add_cascade(label="File", menu=file_menu)
    top_menu.add_cascade(label="Edit", menu=edit_menu)

    # add menu
    root.config(menu=top_menu)
    return top_menu


def calculate_geometry(root, resolution):
    # split resolution to width and height
    width, height = resolution.split("x")
    width = int(width)
    height = int(height)

    # get screen width and height
    screen_width = root.winfo_screenwidth()  # width of the screen
    screen_height = root.winfo_screenheight()  # height of the screen

    # calculate x and y coordinates for the Tk root window
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)

    # generate geometry
    return "%dx%d+%d+%d" % (width, height, x, y)


def initialize_key_binds(root, text_area, key_binds):
    key_binds_edited = ["<" + key_bind + ">" for key_bind in key_binds]
    root.bind(key_binds_edited[0], lambda key: menu_new_file(root, text_area))
    root.bind(key_binds_edited[1], lambda key: menu_open_file(root, text_area))
    root.bind(key_binds_edited[2], lambda key: menu_save_file(root, text_area))
    root.bind(key_binds_edited[3], lambda key: menu_save_file_as(root, text_area))


def main():
    # get data from config
    colors = config_handler_module.read_colors_section()
    startup_settings = config_handler_module.read_startup_settings_section()
    general = config_handler_module.read_general_section()
    key_binds = config_handler_module.read_key_binds_section()

    # create main window
    root = Tk()
    root.geometry(calculate_geometry(root, startup_settings[0]))
    root.title("Untiled - Encrypted Notepad")

    # add text area
    text_area = add_text_area(root, colors, general)

    # add top menu
    top_menu = add_top_menu(root, text_area, colors, general, key_binds)

    # initialize key binds
    initialize_key_binds(root, text_area, key_binds)

    # get file from arguments (not necessary)
    open_file = read_argv()
    if open_file is not None:
        menu_open_file(root, text_area, certain_file=open_file)

    # start application
    root.mainloop()


if __name__ == "__main__":
    main()
