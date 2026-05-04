import tkinter as tk
from tkinter import font
import threading
import time

class FreezeScreen:
    def __init__(self, root):
        self.root = root
        self.root.attributes('-fullscreen', True)
        self.root.configure(bg='black')
        self.root.configure(cursor='arrow')
        
        # Disable all key and mouse events
        self.root.bind('<Key>', lambda e: 'break')
        self.root.bind('<Button-1>', lambda e: 'break')
        self.root.bind('<Motion>', lambda e: 'break')
        
        # Create main frame (overlay)
        self.overlay = tk.Frame(root, bg='black')
        self.overlay.pack(fill=tk.BOTH, expand=True)
        
        # Timer label
        self.timer_font = font.Font(family='Courier', size=50, weight='bold')
        self.timer_label = tk.Label(
            self.overlay,
            text='5',
            font=self.timer_font,
            fg='red',
            bg='black'
        )
        self.timer_label.pack(pady=20)
        
        # Status text
        self.text_font = font.Font(family='Courier', size=30)
        self.text_label = tk.Label(
            self.overlay,
            text='SYSTEM FREEZE...',
            font=self.text_font,
            fg='#00ff00',
            bg='black'
        )
        self.text_label.pack(pady=20)
        
        # Progress bar frame
        self.bar_frame = tk.Frame(self.overlay, width=600, height=20, bg='black')
        self.bar_frame.pack(pady=30)
        
        # Progress bar border
        self.bar = tk.Frame(
            self.bar_frame,
            width=600,
            height=20,
            bg='black',
            relief=tk.FLAT,
            bd=1,
            highlightthickness=1,
            highlightbackground='#00ff00'
        )
        self.bar.pack()
        
        # Progress bar fill
        self.progress = tk.Frame(self.bar, bg='#00ff00', height=20)
        self.progress.pack(side=tk.LEFT, fill=tk.Y)
        self.progress.pack_propagate(False)
        
        # Variables
        self.seconds = 150
        self.progress_width = 0
        self.total_width = 600
        
        # Start timers
        self.start_timers()
    
    def start_timers(self):
        """Start countdown and progress bar"""
        self.update_timer()
        self.update_progress()
    
    def update_timer(self):
        """Update countdown timer"""
        if self.seconds > 0:
            self.timer_label.config(text=str(self.seconds))
            self.seconds -= 1
            self.root.after(1000, self.update_timer)
        else:
            self.on_complete()
    
    def update_progress(self):
        """Update progress bar"""
        if self.progress_width < self.total_width:
            self.progress_width += 12  # Increment for smooth progress
            self.progress.config(width=self.progress_width)
            self.root.after(100, self.update_progress)
    
    def on_complete(self):
        """Called when countdown is complete"""
        self.overlay.pack_forget()
        # Alternatively, you can close the window:
        # self.root.quit()

def main():
    root = tk.Tk()
    root.title('Freeze Screen')
    app = FreezeScreen(root)
    root.mainloop()

if __name__ == '__main__':
    main()
