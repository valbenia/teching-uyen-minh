import tkinter as tk
import random
from PIL import Image, ImageTk

class RockPaperScissorsGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock Paper Scissors Game")
        self.root.geometry("600x550")
        self.root.configure(bg="#f0f0f0")
        
        # Game variables
        self.player_score = 0
        self.computer_score = 0
        self.choices = ["rock", "paper", "scissors"]
        
        # Setup the complete layout
        self.setup_gui()
        
    def setup_gui(self):
        """Setup the complete game interface"""
        # Title
        title_label = tk.Label(
            self.root,
            text="🎮 Rock Paper Scissors Game 🎮",
            font=("Arial", 20, "bold"),
            bg="#f0f0f0",
            fg="#333"
        )
        title_label.pack(pady=20)
        
        # Score display
        self.score_frame = tk.Frame(self.root, bg="#f0f0f0")
        self.score_frame.pack(pady=10)
        
        self.score_label = tk.Label(
            self.score_frame,
            text=f"Player: {self.player_score}  |  Computer: {self.computer_score}",
            font=("Arial", 14, "bold"),
            bg="#f0f0f0",
            fg="#333"
        )
        self.score_label.pack()
        
        # Player choice section
        player_frame = tk.Frame(self.root, bg="#f0f0f0")
        player_frame.pack(pady=20)
        
        tk.Label(
            player_frame,
            text="Choose Your Move:",
            font=("Arial", 14, "bold"),
            bg="#f0f0f0"
        ).pack()
        
        # Placeholder for choice buttons (we'll add these in step 3)
        button_frame = tk.Frame(player_frame, bg="#f0f0f0")
        button_frame.pack(pady=10)
        
        # Temporary buttons for testing layout
        for i, choice in enumerate(self.choices):
            btn = tk.Button(
                button_frame,
                text=choice.capitalize(),
                font=("Arial", 10, "bold"),
                bg="white",
                padx=20,
                pady=10
            )
            btn.grid(row=0, column=i, padx=10)
        
        # Countdown display
        self.countdown_frame = tk.Frame(self.root, bg="#f0f0f0")
        self.countdown_frame.pack(pady=10)
        
        self.countdown_label = tk.Label(
            self.countdown_frame,
            text="",
            font=("Arial", 18, "bold"),
            bg="#f0f0f0",
            fg="red"
        )
        self.countdown_label.pack()
        
        # Result display area
        self.result_frame = tk.Frame(self.root, bg="#f0f0f0")
        self.result_frame.pack(pady=20)
        
        # Player and Computer choice display
        choice_display_frame = tk.Frame(self.result_frame, bg="#f0f0f0")
        choice_display_frame.pack()
        
        # Player choice display
        player_choice_frame = tk.Frame(choice_display_frame, bg="#f0f0f0")
        player_choice_frame.pack(side=tk.LEFT, padx=20)
        
        tk.Label(
            player_choice_frame,
            text="Your Choice:",
            font=("Arial", 12, "bold"),
            bg="#f0f0f0"
        ).pack()
        
        # Placeholder for player choice image
        self.player_choice_label = tk.Label(
            player_choice_frame,
            text="[Player Image]",
            bg="lightblue",
            width=15,
            height=5
        )
        self.player_choice_label.pack(pady=5)
        
        self.player_choice_text = tk.Label(
            player_choice_frame,
            text="",
            font=("Arial", 10, "bold"),
            bg="#f0f0f0"
        )
        self.player_choice_text.pack()
        
        # VS label
        tk.Label(
            choice_display_frame,
            text="VS",
            font=("Arial", 16, "bold"),
            bg="#f0f0f0",
            fg="red"
        ).pack(side=tk.LEFT, padx=10)
        
        # Computer choice display
        computer_choice_frame = tk.Frame(choice_display_frame, bg="#f0f0f0")
        computer_choice_frame.pack(side=tk.LEFT, padx=20)
        
        tk.Label(
            computer_choice_frame,
            text="Computer Choice:",
            font=("Arial", 12, "bold"),
            bg="#f0f0f0"
        ).pack()
        
        # Placeholder for computer choice image
        self.computer_choice_label = tk.Label(
            computer_choice_frame,
            text="[Computer Image]",
            bg="lightcoral",
            width=15,
            height=5
        )
        self.computer_choice_label.pack(pady=5)
        
        self.computer_choice_text = tk.Label(
            computer_choice_frame,
            text="",
            font=("Arial", 10, "bold"),
            bg="#f0f0f0"
        )
        self.computer_choice_text.pack()
        
        # Result message
        self.result_label = tk.Label(
            self.result_frame,
            text="Make your choice to start!",
            font=("Arial", 14, "bold"),
            bg="#f0f0f0",
            fg="blue"
        )
        self.result_label.pack(pady=20)
        
        # Control buttons
        control_frame = tk.Frame(self.root, bg="#f0f0f0")
        control_frame.pack(pady=20)
        
        reset_btn = tk.Button(
            control_frame,
            text="Reset Game",
            font=("Arial", 12, "bold"),
            bg="#ff6b6b",
            fg="white",
            padx=20,
            pady=5
        )
        reset_btn.pack(side=tk.LEFT, padx=10)
        
        quit_btn = tk.Button(
            control_frame,
            text="Quit",
            command=self.root.quit,
            font=("Arial", 12, "bold"),
            bg="#6c757d",
            fg="white",
            padx=20,
            pady=5
        )
        quit_btn.pack(side=tk.LEFT, padx=10)

def main():
    root = tk.Tk()
    game = RockPaperScissorsGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()