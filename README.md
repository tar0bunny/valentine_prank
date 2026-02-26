# 💕 Valentine's Day Popup

A persistent Python script that asks someone to be your valentine... and won't take no for an answer!

<img width="250" height="163" alt="image" src="https://github.com/user-attachments/assets/0fc9d22f-4fef-4401-bfe6-6c97bb26cb6f" />
<img width="275" height="165" alt="image" src="https://github.com/user-attachments/assets/a93818eb-dd42-4539-abc1-fbc4de2563f1" />

![Python](https://img.shields.io/badge/python-3.6+-blue.svg)
![Platform](https://img.shields.io/badge/platform-Windows-blue.svg)

## ✨ Features

* **Persistent Popups** - Keeps asking until they say yes
* **Sound Effects** - Plays error sound on "No" answer
* **Simple GUI** - Clean tkinter popup window
* **Victory Message** - Celebrates when they finally say yes!

## 🛠️ Tech Stack

* **Language**: Python
* **GUI**: tkinter (built-in)
* **Audio**: winsound (Windows only)

## 🚀 Installation

**Requirements:**
- Python 3.6 or higher
- Windows OS (for sound effects)

**Run it:**

```bash
python valentine.py
```

## 📝 How It Works

1. Shows a popup asking "Will you be my valentine? 💕"
2. If they click **Yes**: Shows "WOOHOO!!! Love always wins. 😍" and exits
3. If they click **No**: Plays error sound, waits 1 second, asks again
4. Repeats until they say yes!

## 💡 Usage Ideas

* Send to your crush on Valentine's Day
* Prank your friends
* Learn basic Python GUI programming
* Customize the messages for any occasion

## 🎨 Customization

**Change the question:**
```python
result = messagebox.askyesno("Question", "Your custom message here")
```

**Change the victory message:**
```python
show_message("Title", "Your celebration message here")
```

**Change the wait time:**
```python
time.sleep(1)  # Change 1 to any number of seconds
```

## ⚠️ Notes

* **Windows Only** - `winsound` module only works on Windows
* **Persistent** - Only way to exit is clicking "Yes" or force-closing
* **Use Responsibly** - Don't actually trap someone in a loop forever! 😅

## 🐛 Troubleshooting

**"No module named 'tkinter'"**
- tkinter comes with Python, try reinstalling Python with "tcl/tk" option checked

**No sound playing**
- Make sure you're on Windows
- Check system volume is on
