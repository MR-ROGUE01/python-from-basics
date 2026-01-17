import tkinter as tk
from tkinter import messagebox

class GuessNumberPro:
    def __init__(self, root):
        self.root = root
        self.root.title("🤖 Guess My Number PRO")
        self.root.geometry("450x600")
        self.root.resizable(False, False)
        self.root.configure(bg="#0f172a")  # dark navy

        # ---------- Game State ----------
        self.start = 0
        self.end = 0
        self.mid = 0
        self.attempts = 0
        self.game_active = False

        # ---------- Title ----------
        tk.Label(
            root,
            text="🤖 Guess My Number",
            font=("Segoe UI", 22, "bold"),
            fg="#e5e7eb",
            bg="#0f172a"
        ).pack(pady=15)

        # ---------- Card ----------
        self.card = tk.Frame(root, bg="#111827", bd=0)
        self.card.pack(padx=20, pady=10, fill="both", expand=True)

        # ---------- Info ----------
        self.info = tk.Label(
            self.card,
            text="Set the range and start",
            font=("Segoe UI", 12),
            fg="#9ca3af",
            bg="#111827"
        )
        self.info.pack(pady=10)

        # ---------- Range Inputs ----------
        range_frame = tk.Frame(self.card, bg="#111827")
        range_frame.pack(pady=10)

        self.start_entry = self._entry(range_frame, "Start")
        self.end_entry = self._entry(range_frame, "End")

        # ---------- Start Button ----------
        self.start_btn = tk.Button(
            self.card,
            text="🚀 START GAME",
            font=("Segoe UI", 12, "bold"),
            bg="#22c55e",
            fg="black",
            padx=15,
            pady=8,
            command=self.start_game
        )
        self.start_btn.pack(pady=15)

        # ---------- Guess ----------
        self.guess_label = tk.Label(
            self.card,
            text="",
            font=("Segoe UI", 18, "bold"),
            fg="#facc15",
            bg="#111827"
        )
        self.guess_label.pack(pady=20)

        # ---------- Attempts ----------
        self.attempt_label = tk.Label(
            self.card,
            text="Attempts: 0",
            font=("Segoe UI", 11),
            fg="#38bdf8",
            bg="#111827"
        )
        self.attempt_label.pack(pady=5)

        # ---------- Buttons ----------
        btn_frame = tk.Frame(self.card, bg="#111827")
        btn_frame.pack(pady=15)

        self.yes_btn = self._action_button(btn_frame, "✅ YES", "#3b82f6", self.correct)
        self.high_btn = self._action_button(btn_frame, "⬆ HIGHER", "#f97316", self.higher)
        self.low_btn = self._action_button(btn_frame, "⬇ LOWER", "#ef4444", self.lower)

        # ---------- Restart ----------
        self.restart_btn = tk.Button(
            self.card,
            text="🔁 Restart",
            bg="#334155",
            fg="white",
            command=self.reset_game,
            state=tk.DISABLED
        )
        self.restart_btn.pack(pady=10)

        self.disable_actions()

    # ---------- UI Helpers ----------
    def _entry(self, parent, placeholder):
        frame = tk.Frame(parent, bg="#111827")
        frame.pack(side="left", padx=10)

        tk.Label(frame, text=placeholder, fg="#e5e7eb", bg="#111827").pack()
        e = tk.Entry(frame, width=10, justify="center")
        e.pack()
        return e

    def _action_button(self, parent, text, color, cmd):
        btn = tk.Button(
            parent, text=text, width=11,
            bg=color, fg="white",
            command=cmd, state=tk.DISABLED
        )
        btn.pack(side="left", padx=5)
        return btn

    # ---------- Game Logic ----------
    def start_game(self):
        try:
            self.start = int(self.start_entry.get())
            self.end = int(self.end_entry.get())
        except ValueError:
            messagebox.showerror("Invalid Input", "Enter valid integers!")
            return

        if self.start > self.end:
            messagebox.showerror("Invalid Range", "Start must be <= End")
            return

        self.attempts = 0
        self.game_active = True
        self.enable_actions()
        self.next_guess()

    def next_guess(self):
        if self.start > self.end:
            self.guess_label.config(text="🤨 Inconsistent answers!")
            self.end_game()
            return

        self.mid = (self.start + self.end) // 2
        self.attempts += 1
        self.guess_label.config(text=f"Is it {self.mid}?")
        self.attempt_label.config(text=f"Attempts: {self.attempts}")

    def correct(self):
        self.guess_label.config(text=f"🎉 Guessed it in {self.attempts} tries!")
        self.end_game()

    def higher(self):
        self.start = self.mid + 1
        self.next_guess()

    def lower(self):
        self.end = self.mid - 1
        self.next_guess()

    def end_game(self):
        self.disable_actions()
        self.restart_btn.config(state=tk.NORMAL)
        self.game_active = False

    def reset_game(self):
        self.start_entry.delete(0, tk.END)
        self.end_entry.delete(0, tk.END)
        self.guess_label.config(text="")
        self.attempt_label.config(text="Attempts: 0")
        self.info.config(text="Set the range and start")
        self.restart_btn.config(state=tk.DISABLED)

    def enable_actions(self):
        self.yes_btn.config(state=tk.NORMAL)
        self.high_btn.config(state=tk.NORMAL)
        self.low_btn.config(state=tk.NORMAL)

    def disable_actions(self):
        self.yes_btn.config(state=tk.DISABLED)
        self.high_btn.config(state=tk.DISABLED)
        self.low_btn.config(state=tk.DISABLED)


# ---------- Run ----------
root = tk.Tk()
GuessNumberPro(root)
root.mainloop()
