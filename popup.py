import tkinter as tk
from tkinter import messagebox
import time
import winsound


def play_error_sound():
    winsound.MessageBeep(winsound.MB_ICONHAND)


def show_popup():
    root = tk.Tk()
    root.withdraw()
    
    result = messagebox.askyesno("Question", "Will you be my valentine? 💕")
    
    root.destroy()
    return result


def show_message(title, message):
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo(title, message)
    root.destroy()
    

def main():
    while True:
        user_response = show_popup()
        
        if user_response:
            show_message("Yay!", "WOOHOO!!! Love always wins. 😍")
            break
        else:
            play_error_sound()
            time.sleep(1)


if __name__ == "__main__":
    main()