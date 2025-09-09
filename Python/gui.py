import tkinter as tk
from tkinter import filedialog, messagebox
import sys
import io

class GUI:
    def __init__(self, root, theme):
        self.root = root
        self.root.title("Python IDE Challenge")

        self.editor = tk.Text(root, wrap="none", font=(theme["font"], theme["textsize"]))
        self.editor.pack(fill="both", expand=True)

        self.console = tk.Text(root, height=10, bg=theme["bg"], fg=theme["fg"], font=(theme["font"], theme["textsize"]))
        self.console.pack(fill="x")

        menubar = tk.Menu(root)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="New", command=self.new_file)
        filemenu.add_command(label="Open", command=self.open_file)
        filemenu.add_command(label="Save", command=self.save_file)
        menubar.add_cascade(label="File", menu=filemenu)
        menubar.add_command(label="Run", command=self.run_code)
        root.config(menu=menubar)


    def new_file(self):
        self.editor.delete("1.0", tk.END)
        self.current_file = None
        self.root.title("Python IDE Challenge - Untitled")


    def open_file(self):
        path = filedialog.askopenfilename(filetypes=[("Python Files", "*.py")])
        if path:
            with open(path, "r") as file:
                self.editor.delete("1.0", tk.END)
                self.editor.insert(tk.END, file.read())
            self.root.title(f"Python IDE Challenge - {path}")

    def save_file(self):
        path = filedialog.asksaveasfilename(defaultextension=".py", filetypes=[("Python Files", "*.py")])
        if path:
            with open(path, "w") as f:
                f.write(self.editor.get("1.0", tk.END))
            self.root.title(f"Mini Python IDE - {path}")

    def run_code(self):
        code = self.editor.get("1.0", tk.END)
        self.console.delete("1.0", tk.END)

        # Redirect stdout and stderr to console
        old_stdout, old_stderr = sys.stdout, sys.stderr
        sys.stdout = sys.stderr = io.StringIO()
        try:
            exec(code, {})
        except Exception as e:
            print(f"Error: {e}")
        output = sys.stdout.getvalue()
        self.console.insert(tk.END, output)
        # Reset stdout/stderr
        sys.stdout, sys.stderr = old_stdout, old_stderr

if __name__ == "__main__":
    root = tk.Tk()
    app = GUI(root, {"bg": "black", "fg": "white", "font": "Courier", "textsize": 25})
    root.mainloop()