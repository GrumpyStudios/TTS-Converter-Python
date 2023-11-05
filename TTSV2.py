import tkinter as tk
from tkinter import ttk
import pyttsx3
from tkinter import messagebox  # Import messagebox module

def convert_to_speech():
    text = text_entry.get("1.0", "end-1c")  # Get the text from the text box
    voice = voice_selector.get()  # Get the selected voice
    pitch = float(pitch_var.get())  # Get the selected pitch
    rate = float(rate_var.get())  # Get the selected rate
    output_file = output_entry.get()  # Get the output file name

    engine = pyttsx3.init()

    # Set voice
    voices = engine.getProperty("voices")
    if voice == "Male":
        engine.setProperty("voice", voices[0].id)  # Change to the desired male voice
    elif voice == "Female":
        engine.setProperty("voice", voices[1].id)  # Change to the desired female voice

    # Set pitch and rate
    engine.setProperty("pitch", pitch)
    engine.setProperty("rate", rate)

    # Convert text to speech
    engine.save_to_file(text, f"{output_file}.mp3")  # Use the specified file name
    engine.runAndWait()
    engine.stop()

    messagebox.showinfo("Conversion Complete", f"Speech saved as {output_file}.mp3")

root = tk.Tk()
root.title("Text to Speech Converter")

# Text Entry
text_label = tk.Label(root, text="Enter text:")
text_label.pack()
text_entry = tk.Text(root, height=10, width=40)
text_entry.pack()

# Voice Selection
voice_label = tk.Label(root, text="Select voice:")
voice_label.pack()
voice_selector = ttk.Combobox(root, values=("Male", "Female"), state="readonly")
voice_selector.set("Male")  # Default to Male voice
voice_selector.pack()

# Pitch Control
pitch_label = tk.Label(root, text="Pitch (default=1.0):")
pitch_label.pack()
pitch_var = tk.DoubleVar(value=1.0)
pitch_entry = tk.Entry(root, textvariable=pitch_var)
pitch_entry.pack()

# Rate Control
rate_label = tk.Label(root, text="Rate (default=200):")
rate_label.pack()
rate_var = tk.DoubleVar(value=200)
rate_entry = tk.Entry(root, textvariable=rate_var)
rate_entry.pack()

# Output File Name Entry
output_label = tk.Label(root, text="Output File Name:")
output_label.pack()
output_entry = tk.Entry(root)
output_entry.pack()

# Conversion Button
convert_button = tk.Button(root, text="Convert to Speech", command=convert_to_speech)
convert_button.pack()

root.mainloop()

