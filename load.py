import tkinter as tk
import webbrowser

def plugin_start3(plugin_dir):
  pass

def plugin_stop():
  pass

def plugin_app(parent):
  label = tk.Label(parent, text="Aaaaaaaaaaaaaaaaardvark", fg="blue",
      cursor="hand2")
  label.bind("<Button-1>", lambda e: callback("https://youtu.be/dQw4w9WgXcQ"))
  return label

def callback(url):
  webbrowser.open(url)
