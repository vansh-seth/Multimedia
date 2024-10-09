import tkinter as tk
import numpy as np
import sounddevice as sd

notes_freq = {
    "C4": 261.63,
    "C#4": 277.18,
    "D4": 293.66,
    "D#4": 311.13,
    "E4": 329.63,
    "F4": 349.23,
    "F#4": 369.99,
    "G4": 392.00,
    "G#4": 415.30,
    "A4": 440.00,
    "A#4": 466.16,
    "B4": 493.88,
    "C5": 523.25
}

def play_note(note):
    fs = 44100
    duration = 1.0 
    frequency = notes_freq[note]
    t = np.linspace(0, duration, int(fs * duration), endpoint=False)
    wave = 0.5 * np.sin(2 * np.pi * frequency * t)
    sd.play(wave, samplerate=fs)
    sd.wait()  

root = tk.Tk()
root.title("GUI Piano")

white_keys = ["C4", "D4", "E4", "F4", "G4", "A4", "B4", "C5"]
white_key_buttons = []

for note in white_keys:
    key = tk.Button(root, text=note, width=5, height=15, bg='white', fg='black', font=("arial", 14, "bold"))
    key.pack(side=tk.LEFT, padx=2, pady=2)
    white_key_buttons.append(key)

black_keys = {"C#4": 1, "D#4": 2, "F#4": 4, "G#4": 5, "A#4": 6}
black_key_buttons = []

for note, pos in black_keys.items():
    key = tk.Button(root, text=note, width=3, height=8, bg='black', fg='white', font=("arial", 10, "bold"))
    key.place(x=pos*55 + 35, y=2)
    black_key_buttons.append(key)

white_key_buttons[0].configure(command=lambda: play_note("C4"))
white_key_buttons[1].configure(command=lambda: play_note("D4"))
white_key_buttons[2].configure(command=lambda: play_note("E4"))
white_key_buttons[3].configure(command=lambda: play_note("F4"))
white_key_buttons[4].configure(command=lambda: play_note("G4"))
white_key_buttons[5].configure(command=lambda: play_note("A4"))
white_key_buttons[6].configure(command=lambda: play_note("B4"))
white_key_buttons[7].configure(command=lambda: play_note("C5"))

black_key_buttons[0].configure(command=lambda: play_note("C#4"))
black_key_buttons[1].configure(command=lambda: play_note("D#4"))
black_key_buttons[2].configure(command=lambda: play_note("F#4"))
black_key_buttons[3].configure(command=lambda: play_note("G#4"))
black_key_buttons[4].configure(command=lambda: play_note("A#4"))

root.mainloop()

