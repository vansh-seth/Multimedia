```markdown
# GUI Piano

This project is a simple GUI-based piano application built using Python's `tkinter` library for the graphical user interface and `sounddevice` for sound playback. The piano can play musical notes corresponding to keys on a keyboard, providing a basic interactive tool for creating music.

## Features

- **Graphical Piano Interface**: A simple graphical representation of a piano with both white and black keys.
- **Sound Playback**: Plays the sound of the corresponding note when a key is pressed.
- **Octave**: The piano includes notes from C4 to C5, covering a full octave with both sharp and natural notes.

## Prerequisites

Before running the application, ensure you have the following Python packages installed:

- `tkinter` (usually comes pre-installed with Python)
- `numpy`
- `sounddevice`

You can install the required packages using pip:

```bash
pip install numpy sounddevice
```

## How to Run

1. **Clone or Download** the repository containing this file.

2. **Navigate** to the directory containing the Python script.

3. **Run the script** using Python:

    ```bash
    python piano.py
    ```

4. **Play Notes** by clicking on the keys in the GUI. The white and black keys correspond to natural and sharp notes, respectively.

## Code Overview

- **Note Frequencies**: A dictionary `notes_freq` maps musical note names to their corresponding frequencies in Hertz.

- **play_note(note)**: A function that generates and plays a sine wave of the given note's frequency for 1 second.

- **GUI Setup**: The main window is created using `tkinter.Tk()`. Buttons representing piano keys are created and configured for both white and black keys.

- **Key Binding**: Each button is bound to its corresponding note, so clicking the button will play the note.

## Screenshot

A basic piano interface with labeled keys, ready to be played!

## License

This project is open-source and available under the MIT License.

## Acknowledgements

- Python `tkinter` documentation for GUI creation.
- `sounddevice` and `numpy` libraries for sound generation.
```

This README provides a comprehensive overview of the project, guiding users on installation, running, and understanding the code.
