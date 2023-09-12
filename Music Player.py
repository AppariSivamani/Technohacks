import os
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from pygame import mixer  # You need to install pygame

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Music Player")
        self.root.geometry("400x200")

        mixer.init()  # Initialize the mixer for audio playback

        self.current_song = ""
        self.song_list = []

        self.create_widgets()
        self.update_song_list()

    def create_widgets(self):
        # Create buttons
        self.play_button = ttk.Button(self.root, text="Play", command=self.play_music)
        self.pause_button = ttk.Button(self.root, text="Pause", command=self.pause_music)
        self.stop_button = ttk.Button(self.root, text="Stop", command=self.stop_music)
        self.add_button = ttk.Button(self.root, text="Add Songs", command=self.add_songs)

        # Create song listbox
        self.song_listbox = tk.Listbox(self.root, selectmode=tk.SINGLE, height=10, width=40)

        # Pack widgets
        self.play_button.pack(pady=10)
        self.pause_button.pack(pady=10)
        self.stop_button.pack(pady=10)
        self.add_button.pack(pady=10)
        self.song_listbox.pack()

    def add_songs(self):
        songs = filedialog.askopenfilenames(filetypes=[("MP3 Files", "*.mp3")])
        for song in songs:
            self.song_list.append(song)
        self.update_song_list()

    def update_song_list(self):
        self.song_listbox.delete(0, tk.END)
        for song in self.song_list:
            song_name = os.path.basename(song)
            self.song_listbox.insert(tk.END, song_name)

    def play_music(self):
        selected_song_index = self.song_listbox.curselection()
        if selected_song_index:
            selected_song = self.song_list[selected_song_index[0]]
            if self.current_song != selected_song:
                mixer.music.load(selected_song)
                mixer.music.play()
                self.current_song = selected_song

    def pause_music(self):
        if mixer.music.get_busy():
            mixer.music.pause()

    def stop_music(self):
        if mixer.music.get_busy():
            mixer.music.stop()
            self.current_song = ""

if __name__ == "__main__":
    root = tk.Tk()
    app = MusicPlayer(root)
    root.mainloop()
