import tkinter as tk
import subprocess

class speech():
    def __init__(self, root):
        self.root = root
        self.root.title("Text Speech Application")
        scrn_width = self.root.winfo_screenwidth()
        scrn_height = self.root.winfo_screenheight()

        self.root.geometry(f"{scrn_width}x{scrn_height}+0+0")

        mainTitle = tk.Label(self.root, text="Text to Speech", bg="blue", fg="white", bd=5, relief="groove", font=("Arial", 40, "bold"))
        mainTitle.pack(side="top", fill="x")

        mainFrame = tk.Frame(self.root, bg="lightblue",bd=5, relief="ridge")
        mainFrame.place(x=400, y=90, width=450, height=550)

        textLabel = tk.Label(mainFrame, text="Enter Your Text:", bg="lightblue", font=("Arial", 20, "bold"))
        textLabel.grid(row=0, column=0, padx=20, pady=30)

        self.text = tk.Text(mainFrame, bd=3, width=35, height=5, relief="sunken", font=("Arial", 15 ))
        self.text.grid(row=1, column=0, padx=20, pady=20)

        btn = tk.Button(mainFrame, bg="lightgray", command=self.speak, width=20, text="Speech", font=("Arial", 20, "bold"))
        btn.grid(row=2, column=0, padx=20, pady=20)

    def speak(self):
        value = self.text.get("1.0", tk.END)
        cmnd = f"PowerShell -Command \"Add-Type –AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('{value}');\""

        subprocess.run(cmnd)
        self.clear()


    def clear(self):
        self.text.delete("1.0", tk.END)


root = tk.Tk()
obj = speech(root)
root.mainloop()

