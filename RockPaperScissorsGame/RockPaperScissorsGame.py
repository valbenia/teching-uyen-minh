import tkinter as tk
from tkinter import messagebox
import random
from PIL import Image, ImageTk
import os

class RockPaperScissorsGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock Paper Scissors Game")
        self.root.geometry("800x800")
        self.root.configure(bg="#f0f0f0")
        
        # Game variables
        self.player_score = 0
        self.computer_score = 0
        self.choices = ["rock", "paper", "scissors"]
        self.game_in_progress = False
        self.countdown_timer = None
        self.animation_timer = None
        self.countdown_value = 3
        self.final_computer_choice = None
        
        # Create images dictionary
        self.images = {}
        self.create_images()
        
        # Setup GUI
        self.setup_gui()
        
    def create_images(self):
        """Create or load images for rock, paper, scissors"""
        try:
            # Try to load actual images if they exist
            for choice in self.choices:
                img_path = f"images/{choice}.png"
                if os.path.exists(img_path):
                    img = Image.open(img_path)
                    img = img.resize((100, 100), Image.Resampling.LANCZOS)
                    self.images[choice] = ImageTk.PhotoImage(img)
                else:
                    # Create placeholder images
                    self.images[choice] = self.create_placeholder_image(choice)
        except Exception as e:
            # Fallback to placeholder images
            for choice in self.choices:
                self.images[choice] = self.create_placeholder_image(choice)
    
    def create_placeholder_image(self, choice):
        """Create placeholder images if actual images don't exist"""
        colors = {'rock': '#8B4513', 'paper': '#FFFFFF', 'scissors': '#C0C0C0'}
        img = Image.new('RGB', (100, 100), color=colors.get(choice, 'lightgray'))
        return ImageTk.PhotoImage(img)
    
    def setup_gui(self):
        """Setup the game interface"""
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
        
        # Choice buttons with images
        button_frame = tk.Frame(player_frame, bg="#f0f0f0")
        button_frame.pack(pady=10)
        
        self.choice_buttons = {}
        for i, choice in enumerate(self.choices):
            btn = tk.Button(
                button_frame,
                image=self.images[choice],
                text=choice.capitalize(),
                compound=tk.TOP,
                command=lambda c=choice: self.player_choice(c),
                font=("Arial", 10, "bold"),
                bg="white",
                relief="raised",
                borderwidth=2,
                padx=10,
                pady=5
            )
            btn.grid(row=0, column=i, padx=10)
            self.choice_buttons[choice] = btn
        
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
        
        self.player_choice_label = tk.Label(
            player_choice_frame,
            image=self.images["rock"],  # Default image
            bg="#f0f0f0"
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
        
        self.computer_choice_label = tk.Label(
            computer_choice_frame,
            image=self.images["rock"],  # Default image
            bg="#f0f0f0"
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
            command=self.reset_game,
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
    
    def disable_buttons(self):
        """Disable all choice buttons during countdown"""
        for button in self.choice_buttons.values():
            button.config(state="disabled")
    
    def enable_buttons(self):
        """Enable all choice buttons after countdown"""
        for button in self.choice_buttons.values():
            button.config(state="normal")
    
    def player_choice(self, choice):
        """Handle player's choice and start countdown with animation"""
        if self.game_in_progress:
            return  # Prevent multiple clicks during countdown
        
        self.game_in_progress = True
        self.disable_buttons()
        
        # Store player choice for later use
        self.current_player_choice = choice
        
        # Determine the final computer choice now (but don't show it yet)
        self.final_computer_choice = random.choice(self.choices)
        
        # Show player's choice immediately
        self.player_choice_label.config(image=self.images[choice])
        self.player_choice_text.config(text=choice.capitalize())
        
        # Start computer choice animation
        self.computer_choice_text.config(text="🎲 Deciding...")
        
        # Clear result and show countdown message
        self.result_label.config(text="🎰 Computer is deciding...", fg="orange")
        
        # Start both countdown and animation
        self.countdown_value = 3
        self.start_countdown()
        self.start_computer_animation()
    
    def start_countdown(self):
        """Start the 3-second countdown"""
        if self.countdown_value > 0:
            self.countdown_label.config(text=f"⏰ {self.countdown_value}")
            self.countdown_value -= 1
            # Schedule next countdown update in 1 second
            self.countdown_timer = self.root.after(1000, self.start_countdown)
        else:
            # Countdown finished, stop animation and show final result
            self.countdown_label.config(text="")
            self.stop_computer_animation()
            self.show_final_result()
    
    def start_computer_animation(self):
        """Start the computer choice animation (rapid random changes)"""
        if self.game_in_progress and self.countdown_value >= 0:
            # Show a random choice (not the final one)
            random_choice = random.choice(self.choices)
            self.computer_choice_label.config(image=self.images[random_choice])
            
            # Schedule next animation frame in 150ms for smooth animation
            self.animation_timer = self.root.after(150, self.start_computer_animation)
    
    def stop_computer_animation(self):
        """Stop the computer choice animation"""
        if self.animation_timer:
            self.root.after_cancel(self.animation_timer)
            self.animation_timer = None
    
    def show_final_result(self):
        """Show the final computer choice and determine the winner"""
        # Show the final computer choice
        self.computer_choice_label.config(image=self.images[self.final_computer_choice])
        self.computer_choice_text.config(text=self.final_computer_choice.capitalize())
        
        # Add a brief flash effect for the final choice
        self.flash_computer_choice()
        
        # Determine winner
        result = self.determine_winner(self.current_player_choice, self.final_computer_choice)
        
        # Update score and show result
        if result == "player":
            self.player_score += 1
            self.result_label.config(text="🎉 You Win! 🎉", fg="green")
        elif result == "computer":
            self.computer_score += 1
            self.result_label.config(text="😔 Computer Wins! 😔", fg="red")
        else:
            self.result_label.config(text="🤝 It's a Tie! 🤝", fg="orange")
        
        # Update score display
        self.score_label.config(
            text=f"Player: {self.player_score}  |  Computer: {self.computer_score}"
        )
        
        # Re-enable buttons and reset game state
        self.enable_buttons()
        self.game_in_progress = False
        
        # Check for game end (optional - first to 5 wins)
        if self.player_score >= 5:
            messagebox.showinfo("Game Over", "🏆 Congratulations! You won the game! 🏆")
            self.reset_game()
        elif self.computer_score >= 5:
            messagebox.showinfo("Game Over", "🤖 Computer won the game! Better luck next time! 🤖")
            self.reset_game()
    
    def flash_computer_choice(self):
        """Add a brief flash effect to highlight the final computer choice"""
        # Flash the computer choice label
        original_bg = self.computer_choice_label.cget("bg")
        self.computer_choice_label.config(bg="yellow")
        self.root.after(200, lambda: self.computer_choice_label.config(bg=original_bg))
    
    def determine_winner(self, player_choice, computer_choice):
        """Determine the winner of the round"""
        if player_choice == computer_choice:
            return "tie"
        elif (
            (player_choice == "rock" and computer_choice == "scissors") or
            (player_choice == "paper" and computer_choice == "rock") or
            (player_choice == "scissors" and computer_choice == "paper")
        ):
            return "player"
        else:
            return "computer"
    
    def reset_game(self):
        """Reset the game to initial state"""
        # Cancel any ongoing timers
        if self.countdown_timer:
            self.root.after_cancel(self.countdown_timer)
            self.countdown_timer = None
        
        if self.animation_timer:
            self.root.after_cancel(self.animation_timer)
            self.animation_timer = None
        
        # Reset game state
        self.game_in_progress = False
        self.countdown_value = 3
        self.final_computer_choice = None
        self.player_score = 0
        self.computer_score = 0
        
        # Reset UI
        self.enable_buttons()
        self.countdown_label.config(text="")
        
        self.score_label.config(
            text=f"Player: {self.player_score}  |  Computer: {self.computer_score}"
        )
        
        self.player_choice_label.config(image=self.images["rock"])
        self.player_choice_text.config(text="")
        
        self.computer_choice_label.config(image=self.images["rock"])
        self.computer_choice_text.config(text="")
        
        self.result_label.config(
            text="Make your choice to start!",
            fg="blue"
        )

def main():
    """Main function to run the game"""
    root = tk.Tk()
    game = RockPaperScissorsGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
