import tkinter as tk
from tkinter import messagebox, Frame, Button, Label
import webbrowser
import os
import subprocess
import threading # Use threading for non-blocking operations if needed, though not strictly necessary for simple launches.

class AppLauncherApp:
    def __init__(self, master):
        self.master = master
        master.title("B-Sigma | Launcher")
        master.geometry("700x550") # Set initial window size
        master.configure(bg="#2c3e50") # Dark background
        master.resizable(False, False) # Disable resizing for simplicity

        # --- Styling Constants ---
        self.font_title = ('Segoe UI', 24, 'bold')
        self.font_category = ('Segoe UI', 18, 'bold')
        self.font_item = ('Segoe UI', 14)
        self.fg_color_white = '#ecf0f1'
        self.bg_dark = '#2c3e50'
        self.button_bg_normal = '#34495e'
        self.button_fg_normal = '#ecf0f1'
        self.button_bg_hover = '#4a627a'
        self.back_button_bg = '#7f8c8d' # Gray for back button
        self.exit_button_bg = '#c0392b' # Red for exit button
        self.message_color_info = '#3498db' # Blue for info messages
        self.message_color_success = '#2ecc71' # Green for success messages
        self.message_color_error = '#e74c3c' # Red for error messages

        # --- Menu Data Structure ---
        # Defines the hierarchy of categories and items.
        # "type": "app" for local applications, "type": "url" for websites.
        # "path" for app executables, "url" for web addresses.
        self.menu_data = {
            "Programming": {
                "Visual Studio Code (VSC)": {"type": "app", "path": r"C:\Users\Réda\AppData\Local\Programs\Microsoft VS Code\Code.exe"},
                "GitHub": {"type": "url", "url": "https://github.com/mohamedredaou"},
                "Command Prompt (CMD)": {"type": "app", "path": r"C:\Windows\System32\cmd.exe"},
                # Add more programming tools as needed
            },
            "Design": {
                "Unblast": {"type": "url", "url": "https://unblast.com/"},
                "Unsplash": {"type": "url", "url": "https://unsplash.com/"},
                "Font Sites": { # Nested category
                    "Fontshare": {"type": "url", "url": "https://www.fontshare.com/"},
                    "Dafont": {"type": "url", "url": "https://www.dafont.com/"},
                    "Google Fonts": {"type": "url", "url": "https://fonts.google.com/"},
                    "Fonts CN": {"type": "url", "url": "https://www.fonts.net.cn/"},
                },
                "Freepik": {"type": "url", "url": "https://freepik.com/"},
                "Dribbble": {"type": "url", "url": "https://dribbble.com/"},
                "Behance": {"type": "url", "url": "https://behance.com/"},
                "Sketchfab": {"type": "url", "url": "https://sketchfab.com/"},
                "Free3D": {"type": "url", "url": "https://free3d.com/"},
                "UI/UX Design": { # Nested category
                    "Figma": {"type": "url", "url": "https://figma.com/"},
                },
                "Social Media Design": { # Nested category
                    "Photopea": {"type": "url", "url": "https://photopea.com/"},
                }
            },
            "Drawing": {
                "DeviantArt": {"type": "url", "url": "https://DeviantArt.com/"},
                "Artstation": {"type": "url", "url": "https://artstation.com/"},
                "Tumblr": {"type": "url", "url": "https://tumblr.com/"},
            },
            "Internet": {
                "Social Media": { # Nested category
                    "YouTube": {"type": "url", "url": "https://youTube.com/"},
                    "Tumblr": {"type": "url", "url": "https://tumblr.com/"},
                    "X (Twitter)": {"type": "url", "url": "https://x.com/"},
                    "Pinterest": {"type": "url", "url": "https://pinterest.com/"},
                    "Dribbble": {"type": "url", "url": "https://dribbble.com/"},
                },
                "Google Services": { # Nested category
                    "Google Search": {"type": "url", "url": "https://www.google.com/"},
                    "Gmail": {"type": "url", "url": "https://mail.google.com/mail/u/0/#inbox"},
                    "Google Drive": {"type": "url", "url": "https://drive.google.com/drive/home"},
                    "Google Docs": {"type": "url", "url": "https://docs.google.com/document/u/0/"},
                    "Google Sheets": {"type": "url", "url": "https://docs.google.com/spreadsheets/u/0/"},
                    "Google Slides": {"type": "url", "url": "https://docs.google.com/presentation/u/0/"},
                    "Google Calendar": {"type": "url", "url": "https://calendar.google.com/calendar/u/0/r?pli=1"},
                    "Google Keep": {"type": "url", "url": "https://keep.google.com/"},
                    "Google Maps": {"type": "url", "url": "https://www.google.com/maps"},
                    "Google Earth": {"type": "url", "url": "https://earth.google.com/web/"},
                    "Google Play Store": {"type": "url", "url": "https://play.google.com/store/games?hl=en"},
                    "Google Adsense": {"type": "url", "url": "https://adsense.google.com/start/"},
                    "Google Translate": {"type": "url", "url": "https://translate.google.com/?sl=ar&tl=en&op=translate"},
                    "Google Account": {"type": "url", "url": "https://myaccount.google.com/?utm_source=OGB&utm_medium=app"},
                    "Google Fonts": {"type": "url", "url": "https://fonts.google.com/"},
                }
            },
            "Freelance": {
                "Behance": {"type": "url", "url": "https://behance.com/"},
                "Freelancer": {"type": "url", "url": "https://freelancer.com/"},
                "Dribbble": {"type": "url", "url": "https://dribbble.com/"},
                "Kafiil": {"type": "url", "url": "https://kafiil.com/"},
                "Khamsat": {"type": "url", "url": "https://khamsat.com/"},
                "Mostaql": {"type": "url", "url": "https://mostaql.com/"},
            },
            "Games": {
                "Steam": {"type": "url", "url": "https://store.steampowered.com/"},
                "Web Games": { # Nested category
                    "Territorial.io": {"type": "url", "url": "https://territorial.io/"},
                    "Crazygames": {"type": "url", "url": "https://www.crazygames.com/"},
                    "Oskarstalberg Planet": {"type": "url", "url": "https://oskarstalberg.com/game/planet/planet.html"},
                    "Oskarstalberg Townscaper": {"type": "url", "url": "https://oskarstalberg.com/Townscaper/#GSB0RARueC6Snc9E0lO5B"},
                    "Slowroads": { # Nested category for Slowroads options
                        "Free Play": {"type": "url", "url": "https://slowroads.io/"},
                        "Race": {"type": "url", "url": "https://driftmas.slowroads.io/"},
                    }
                },
            },
            "Chine": {
                "Weibo": {"type": "url", "url": "https://m.weibo.cn/"},
                "Bilibili": {"type": "url", "url": "https://www.bilibili.com/"},
                "Baidu": {"type": "url", "url": "https://www.baidu.com/"},
                "Manga Sites": { # Nested category
                    "Webtoons": {"type": "url", "url": "https://webtoons.com/"},
                },
            }
            # Add "system" if you want to include system-level apps like calculator, notepad etc.
            # "system": {
            #     "Calculator": {"type": "app", "path": "calc.exe"},
            #     "Notepad": {"type": "app", "path": "notepad.exe"},
            # }
        }
        
        self.current_menu_level = self.menu_data # Start at the top level
        self.path_history = [] # To keep track of navigation for 'Back' button

        # --- GUI Elements ---
        self.title_label = Label(master, text="B-Sigma Launcher", font=self.font_title, fg=self.fg_color_white, bg=self.bg_dark)
        self.title_label.pack(pady=20)

        # Frame to hold dynamic content (buttons)
        self.content_frame = Frame(master, bg=self.bg_dark)
        self.content_frame.pack(expand=True, fill='both', padx=20, pady=10)

        # Message Label for status updates
        self.message_label = Label(master, text="Select a category to begin", font=self.font_item, fg=self.message_color_info, bg=self.bg_dark)
        self.message_label.pack(pady=10)

        # Back and Exit Buttons Frame
        self.bottom_buttons_frame = Frame(master, bg=self.bg_dark)
        self.bottom_buttons_frame.pack(pady=10)

        self.back_button = Button(self.bottom_buttons_frame, text="Back", font=self.font_item,
                                  bg=self.back_button_bg, fg=self.button_fg_normal,
                                  activebackground=self.button_bg_hover, activeforeground=self.button_fg_normal,
                                  relief='raised', bd=2, cursor='hand2',
                                  command=self.go_back)
        self.back_button.pack(side=tk.LEFT, padx=10)
        self.back_button.config(state=tk.DISABLED) # Disable initially

        self.exit_button = Button(self.bottom_buttons_frame, text="Exit", font=self.font_item,
                                 bg=self.exit_button_bg, fg=self.button_fg_normal,
                                 activebackground='#a93226', activeforeground=self.button_fg_normal,
                                 relief='raised', bd=2, cursor='hand2',
                                 command=master.quit)
        self.exit_button.pack(side=tk.RIGHT, padx=10)

        self.display_menu(self.menu_data) # Show initial main menu

    def clear_frame(self):
        """Clears all widgets from the content frame."""
        for widget in self.content_frame.winfo_children():
            widget.destroy()

    def display_menu(self, menu_dict):
        """
        Populates the content_frame with buttons based on the given dictionary.
        Handles both categories (nested dicts) and executable items (dicts with 'type').
        """
        self.clear_frame()
        self.current_menu_level = menu_dict
        
        # Enable/disable back button
        if len(self.path_history) > 0:
            self.back_button.config(state=tk.NORMAL)
        else:
            self.back_button.config(state=tk.DISABLED)

        row_num = 0
        col_num = 0
        max_cols = 3 # Number of columns for buttons

        for item_name, item_data in menu_dict.items():
            # Check if it's a nested category (a dictionary but not an action item with 'type')
            if isinstance(item_data, dict) and "type" not in item_data:
                button = Button(self.content_frame, text=item_name, font=self.font_category,
                                bg=self.button_bg_normal, fg=self.button_fg_normal,
                                activebackground=self.button_bg_hover, activeforeground=self.button_fg_normal,
                                relief='raised', bd=3, cursor='hand2',
                                command=lambda name=item_name, data=item_data: self.navigate_to_category(name, data))
                button.grid(row=row_num, column=col_num, padx=10, pady=10, sticky="ew")
            # It's an executable item (app or URL)
            else:
                button = Button(self.content_frame, text=item_name, font=self.font_item,
                                bg=self.button_bg_normal, fg=self.button_fg_normal,
                                activebackground=self.button_bg_hover, activeforeground=self.button_fg_normal,
                                relief='raised', bd=2, cursor='hand2',
                                command=lambda data=item_data: self.execute_item(data))
                button.grid(row=row_num, column=col_num, padx=10, pady=10, sticky="ew")
            
            col_num += 1
            if col_num >= max_cols:
                col_num = 0
                row_num += 1
        
        # Configure columns to expand evenly
        for i in range(max_cols):
            self.content_frame.grid_columnconfigure(i, weight=1)


    def navigate_to_category(self, category_name, category_data):
        """Navigates to a nested category menu."""
        self.path_history.append((self.current_menu_level, category_name)) # Store current level and chosen name
        self.display_menu(category_data)
        self.update_message(f"Selected: {category_name}", self.message_color_info)

    def go_back(self):
        """Goes back to the previous menu level."""
        if self.path_history:
            # Pop the last state to get the parent menu
            previous_menu, category_name = self.path_history.pop()
            # If the popped item was a sub-category, its parent is the one we want to display
            # If the popped item was a direct category from the main menu, its parent is the main menu data
            self.display_menu(previous_menu)
            self.update_message("Navigated back.", self.message_color_info)
        else:
            self.update_message("Already at the main menu.", self.message_color_info)
            self.back_button.config(state=tk.DISABLED) # Should already be disabled, but good to ensure

    def execute_item(self, item_data):
        """Executes the action (open app or URL) for the selected item."""
        item_type = item_data.get("type")
        
        if item_type == "url":
            url = item_data.get("url")
            if url:
                try:
                    webbrowser.open(url)
                    self.update_message(f"Opened URL: {url}", self.message_color_success)
                except Exception as e:
                    self.update_message(f"Error opening URL: {e}", self.message_color_error)
            else:
                self.update_message("URL not specified for this item.", self.message_color_error)

        elif item_type == "app":
            app_path = item_data.get("path")
            if app_path:
                try:
                    # Using subprocess.Popen to run the application
                    # This will open the application without blocking the GUI
                    subprocess.Popen([app_path])
                    self.update_message(f"Launched application: {os.path.basename(app_path)}", self.message_color_success)
                except FileNotFoundError:
                    self.update_message(f"Error: Application not found at path: {app_path}. Please check the path.", self.message_color_error)
                except Exception as e:
                    self.update_message(f"Error launching application: {e}", self.message_color_error)
            else:
                self.update_message("Application path not specified for this item.", self.message_color_error)
        else:
            self.update_message("Unknown item type.", self.message_color_error)

    def update_message(self, message, color):
        """Updates the status message label with specified text and color."""
        self.message_label.config(text=message, fg=color)


if __name__ == '__main__':
    root = tk.Tk()
    app = AppLauncherApp(root)
    root.mainloop()
