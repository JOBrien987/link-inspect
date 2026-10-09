"""Tkinter interface for offline suspicious URL checks."""
import tkinter as tk
from tkinter import ttk
from urlcheck import inspect as inspect_url


def main():
    root = tk.Tk()
    root.title("Suspicious Link Inspector")
    root.geometry("660x400")
    root.minsize(490, 340)
    frame = ttk.Frame(root, padding=22)
    frame.pack(fill="both", expand=True)
    frame.columnconfigure(0, weight=1)
    frame.rowconfigure(5, weight=1)
    ttk.Label(frame, text="Suspicious Link Inspector", font=("TkDefaultFont", 17, "bold")).grid(row=0, sticky="w")
    ttk.Label(frame, text="Inspect a URL without opening it or contacting its host.", wraplength=580).grid(row=1, sticky="w", pady=(7, 16))
    url = tk.StringVar()
    entry = ttk.Entry(frame, textvariable=url)
    entry.grid(row=2, sticky="ew")
    buttons = ttk.Frame(frame)
    buttons.grid(row=3, sticky="w", pady=10)
    output = tk.Text(frame, wrap="word", height=10, state="disabled")
    output.grid(row=5, sticky="nsew")
    def write(lines):
        output.configure(state="normal")
        output.delete("1.0", "end")
        output.insert("end", "\n\n".join("• " + s for s in lines))
        output.configure(state="disabled")
    def scan():
        write(inspect_url(url.get().strip()) if url.get().strip() else ["Paste a full HTTP or HTTPS URL first."])
    def clear():
        url.set("")
        write([])
        entry.focus_set()
    ttk.Button(buttons, text="Inspect link", command=scan).pack(side="left", padx=(0, 8))
    ttk.Button(buttons, text="Clear", command=clear).pack(side="left")
    ttk.Label(frame, text="A clean result does NOT establish that a link is safe.", wraplength=580).grid(row=4, sticky="w", pady=(1, 10))
    entry.bind("<Return>", lambda _event: scan())
    entry.focus_set()
    root.mainloop()


if __name__ == "__main__":
    main()
