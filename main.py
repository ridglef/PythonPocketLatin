import tkinter as tk
import requests


class CustomGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("PythonPocketLatin")

        self.label = tk.Label(self.master, text="Null")
        self.label.pack()

        self.textbox = tk.Entry(self.master)
        self.textbox.pack()

        self.button1 = tk.Button(self.master, text="Translate to English", command=lambda: self.translate_text("en"))
        self.button1.pack(side=tk.LEFT, padx=5)

        self.button2 = tk.Button(self.master, text="Translate to Latin", command=lambda: self.translate_text("la"))
        self.button2.pack(side=tk.RIGHT, padx=5)

    def translate_text(self, lang):
        text = self.textbox.get().replace(" ", "%20")
        if text != "":
            url = f"https://bw-trans.vercel.app/{lang}/{text}"
            response = requests.get(url).json()["text"]
            self.label.config(text=response)


if __name__ == "__main__":
    root = tk.Tk()

    custom_gui = CustomGUI(root)

    root.mainloop()
