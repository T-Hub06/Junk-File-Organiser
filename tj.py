import os
import shutil
import json
import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog, ttk
from tkinterdnd2 import DND_FILES, TkinterDnD
import datetime
import threading

default_file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".svg", ".ico",".webp", ".heic", ".heif", ".raw", ".cr2", ".nef"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".xls", ".xlsx", ".ppt", ".pptx", ".odt", ".rtf",".csv", ".json", ".xml", ".md", ".epub", ".pages", ".keynote"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv", ".flv", ".wmv", ".webm"],
    "Music": [".mp3", ".wav", ".aac", ".flac", ".ogg", ".wma"],
    "Archives": [".zip", ".rar", ".tar", ".gz", ".7z", ".bz2",".xz", ".iso"],
    "Scripts": [".py", ".js", ".html", ".css", ".sh", ".bat", ".java", ".cpp", ".c",".ts", ".jsx", ".tsx", ".php", ".rb", ".go", ".rs",".swift", ".kt", ".r", ".m", ".sql", ".yaml", ".yml",".toml", ".ini", ".env", ".ipynb"],
    "3D & Design":[".obj", ".fbx", ".stl", ".blend", ".ai", ".psd", ".xd", ".fig"],
    "Executables":[".exe", ".msi", ".apk", ".dmg", ".deb", ".rpm"],
    "Others": []
}

class JunkFileOrganizerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Junk File Organizer Pro")
        self.root.geometry("900x650")

        self.source_dir = ""
        self.log_dir = ""
        self.move_logs = []
        self.file_types = default_file_types.copy()
        self.dark_mode = False

        self.light_theme = {
            'bg': '#f0f0f0',
            'fg': '#000000',
            'button_bg': '#e0e0e0',
            'button_fg': '#000000',
            'text_bg': '#ffffff',
            'text_fg': '#000000',
            'frame_bg': '#ffffff',
            'accent': '#0078d4'
        }

        self.dark_theme = {
            'bg': '#2b2b2b',
            'fg': '#ffffff',
            'button_bg': '#3c3c3c',
            'button_fg': '#ffffff',
            'text_bg': '#1e1e1e',
            'text_fg': '#ffffff',
            'frame_bg': '#363636',
            'accent': '#0078d4'
        }

        self.current_theme = self.light_theme

        self.setup_gui()
        self.apply_theme()

    def setup_gui(self):
        main_frame = tk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        top_frame = tk.Frame(main_frame)
        top_frame.pack(fill=tk.X, pady=(0, 10))

        title_label = tk.Label(top_frame, text="🗂️ Junk File Organizer Pro", 
                               font=("Arial", 18, "bold"))
        title_label.pack(side=tk.LEFT, padx=5)

        self.dark_mode_btn = tk.Button(top_frame, text="🌙 Dark Mode", 
                                       command=self.toggle_dark_mode, 
                                       width=12)
        self.dark_mode_btn.pack(side=tk.RIGHT, padx=5)

        folder_frame = tk.LabelFrame(main_frame, text="Folder Selection", 
                                     font=("Arial", 10, "bold"), 
                                     padx=10, pady=10)
        folder_frame.pack(fill=tk.X, pady=(0, 10))

        self.drop_label = tk.Label(folder_frame, 
                                   text="📁 Drag & Drop a folder here or click 'Browse'",
                                   font=("Arial", 11), 
                                   relief=tk.SUNKEN, 
                                   height=3,
                                   cursor="hand2")
        self.drop_label.pack(fill=tk.X, pady=5)

        self.drop_label.drop_target_register(DND_FILES)
        self.drop_label.dnd_bind('<<Drop>>', self.drop_folder)

        browse_btn = tk.Button(folder_frame, text="📂 Browse Folder", 
                              command=self.select_folder, 
                              font=("Arial", 10))
        browse_btn.pack(pady=5)

        self.folder_label = tk.Label(folder_frame, text="No folder selected", 
                                     fg="gray", font=("Arial", 9, "italic"))
        self.folder_label.pack(pady=5)

        self.notebook = ttk.Notebook(main_frame)
        self.notebook.pack(fill=tk.BOTH, expand=True, pady=(0, 10))

        organize_tab = tk.Frame(self.notebook)
        self.notebook.add(organize_tab, text="  Organize  ")
        self.setup_organize_tab(organize_tab)

        settings_tab = tk.Frame(self.notebook)
        self.notebook.add(settings_tab, text="  Settings  ")
        self.setup_settings_tab(settings_tab)

        logs_tab = tk.Frame(self.notebook)
        self.notebook.add(logs_tab, text="  Logs  ")
        self.setup_logs_tab(logs_tab)

        progress_frame = tk.Frame(main_frame)
        progress_frame.pack(fill=tk.X, pady=(0, 5))

        self.progress_label = tk.Label(progress_frame, text="Ready", 
                                       font=("Arial", 9))
        self.progress_label.pack(side=tk.LEFT, padx=5)

        self.progress_bar = ttk.Progressbar(progress_frame, mode='determinate')
        self.progress_bar.pack(fill=tk.X, expand=True, padx=5)

    def setup_organize_tab(self, parent):
        btn_frame = tk.Frame(parent)
        btn_frame.pack(fill=tk.X, padx=10, pady=10)

        self.preview_btn = tk.Button(btn_frame, text="👁️ Preview Files", 
                                     command=self.preview_files, 
                                     state=tk.DISABLED,
                                     font=("Arial", 10),
                                     width=15)
        self.preview_btn.pack(side=tk.LEFT, padx=5)

        self.organize_btn = tk.Button(btn_frame, text="✨ Organize Files", 
                                      command=self.confirm_organize, 
                                      state=tk.DISABLED,
                                      font=("Arial", 10, "bold"),
                                      width=15)
        self.organize_btn.pack(side=tk.LEFT, padx=5)

        self.undo_btn = tk.Button(btn_frame, text="↶ Undo Last", 
                                  command=self.confirm_undo, 
                                  state=tk.DISABLED,
                                  font=("Arial", 10),
                                  width=15)
        self.undo_btn.pack(side=tk.LEFT, padx=5)

        status_frame = tk.LabelFrame(parent, text="Status", 
                                     font=("Arial", 10, "bold"))
        status_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        scrollbar = tk.Scrollbar(status_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.status_text = tk.Text(status_frame, height=15, 
                                   state=tk.DISABLED,
                                   yscrollcommand=scrollbar.set,
                                   font=("Consolas", 9))
        self.status_text.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        scrollbar.config(command=self.status_text.yview)

    def setup_settings_tab(self, parent):
        settings_frame = tk.Frame(parent)
        settings_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        tk.Label(settings_frame, text="File Categories Configuration", 
                font=("Arial", 12, "bold")).pack(pady=10)

        tk.Label(settings_frame, 
                text="Edit file extensions for each category (comma-separated, include the dot)",
                font=("Arial", 9),
                fg="gray").pack(pady=5)

        canvas = tk.Canvas(settings_frame, height=300)
        scrollbar = tk.Scrollbar(settings_frame, orient="vertical", 
                                command=canvas.yview)
        scrollable_frame = tk.Frame(canvas)

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.category_entries = {}

        for i, (category, extensions) in enumerate(self.file_types.items()):
            cat_frame = tk.Frame(scrollable_frame)
            cat_frame.pack(fill=tk.X, padx=10, pady=5)

            tk.Label(cat_frame, text=category + ":", 
                    font=("Arial", 10, "bold"), 
                    width=15, anchor="w").pack(side=tk.LEFT, padx=5)

            ext_entry = tk.Entry(cat_frame, width=50, font=("Arial", 9))
            ext_entry.insert(0, ", ".join(extensions))
            ext_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)
            self.category_entries[category] = ext_entry

        save_btn = tk.Button(settings_frame, text="💾 Save Categories", 
                            command=self.save_categories,
                            font=("Arial", 10, "bold"))
        save_btn.pack(pady=10)

        reset_btn = tk.Button(settings_frame, text="🔄 Reset to Defaults", 
                             command=self.reset_categories,
                             font=("Arial", 10))
        reset_btn.pack(pady=5)

    def setup_logs_tab(self, parent):
        logs_frame = tk.Frame(parent)
        logs_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        tk.Label(logs_frame, text="Organization History", 
                font=("Arial", 12, "bold")).pack(pady=10)

        scrollbar = tk.Scrollbar(logs_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.logs_text = tk.Text(logs_frame, height=20, 
                                state=tk.DISABLED,
                                yscrollcommand=scrollbar.set,
                                font=("Consolas", 9))
        self.logs_text.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        scrollbar.config(command=self.logs_text.yview)

        refresh_btn = tk.Button(logs_frame, text="🔄 Refresh History", 
                               command=self.refresh_logs,
                               font=("Arial", 10))
        refresh_btn.pack(pady=5)

    def toggle_dark_mode(self):
        self.dark_mode = not self.dark_mode
        self.current_theme = self.dark_theme if self.dark_mode else self.light_theme
        self.dark_mode_btn.config(text="☀️ Light Mode" if self.dark_mode else "🌙 Dark Mode")
        self.apply_theme()

    def apply_theme(self):
        theme = self.current_theme

        self.root.config(bg=theme['bg'])

        def apply_to_widget(widget):
            widget_class = widget.winfo_class()

            try:
                if widget_class in ['Frame', 'Labelframe']:
                    widget.config(bg=theme['frame_bg'])
                elif widget_class == 'Label':
                    widget.config(bg=theme['frame_bg'], fg=theme['fg'])
                elif widget_class == 'Button':
                    widget.config(bg=theme['button_bg'], fg=theme['button_fg'],
                                 activebackground=theme['accent'],
                                 activeforeground='white')
                elif widget_class == 'Text':
                    widget.config(bg=theme['text_bg'], fg=theme['text_fg'],
                                 insertbackground=theme['fg'])
                elif widget_class == 'Entry':
                    widget.config(bg=theme['text_bg'], fg=theme['text_fg'],
                                 insertbackground=theme['fg'])
            except:
                pass

            for child in widget.winfo_children():
                apply_to_widget(child)

        apply_to_widget(self.root)

    def drop_folder(self, event):
        folder_path = event.data
        folder_path = folder_path.strip('{}')

        if os.path.isdir(folder_path):
            self.source_dir = folder_path
            self.setup_log_dir()
            self.log(f"✓ Folder selected via drag & drop: {self.source_dir}")
        else:
            messagebox.showerror("Error", "Please drop a valid folder")

    def select_folder(self):
        folder = filedialog.askdirectory(title="Select Folder to Organize")
        if folder:
            self.source_dir = folder
            self.setup_log_dir()
            self.log(f"✓ Folder selected: {self.source_dir}")

    def setup_log_dir(self):
        self.log_dir = os.path.join(self.source_dir, ".junk_organizer_logs")
        if not os.path.exists(self.log_dir):
            os.makedirs(self.log_dir)

        self.folder_label.config(text=f"📂 {self.source_dir}", 
                                fg=self.current_theme['accent'])
        self.preview_btn.config(state=tk.NORMAL)
        self.organize_btn.config(state=tk.NORMAL)
        self.update_undo_button()
        self.refresh_logs()

    def update_undo_button(self):
        if not self.log_dir or not os.path.exists(self.log_dir):
            self.undo_btn.config(state=tk.DISABLED)
            return

        logs = sorted(
            [f for f in os.listdir(self.log_dir) 
             if f.startswith("file_move_log_") and f.endswith(".json")],
            reverse=True
        )
        self.move_logs = [os.path.join(self.log_dir, f) for f in logs]

        if self.move_logs:
            self.undo_btn.config(state=tk.NORMAL)
        else:
            self.undo_btn.config(state=tk.DISABLED)

    def get_category_for_extension(self, ext):
        ext = ext.lower()
        for category, extensions in self.file_types.items():
            if ext in extensions:
                return category
        return "Others"

    def preview_files(self):
        if not self.source_dir:
            messagebox.showwarning("Warning", "Please select a folder first.")
            return

        files = []
        for filename in os.listdir(self.source_dir):
            file_path = os.path.join(self.source_dir, filename)
            if os.path.isfile(file_path):
                _, ext = os.path.splitext(filename)
                category = self.get_category_for_extension(ext)
                size = os.path.getsize(file_path)
                files.append((filename, category, size))

        preview_window = tk.Toplevel(self.root)
        preview_window.title("Preview Files")
        preview_window.geometry("700x500")

        preview_window.config(bg=self.current_theme['bg'])

        header_frame = tk.Frame(preview_window, bg=self.current_theme['frame_bg'])
        header_frame.pack(fill=tk.X, padx=10, pady=10)

        tk.Label(header_frame, text=f"Found {len(files)} files to organize",
                font=("Arial", 12, "bold"),
                bg=self.current_theme['frame_bg'],
                fg=self.current_theme['fg']).pack()

        tree_frame = tk.Frame(preview_window)
        tree_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        scrollbar = tk.Scrollbar(tree_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        tree = ttk.Treeview(tree_frame, columns=("File", "Category", "Size"),
                           show="headings", yscrollcommand=scrollbar.set)
        tree.heading("File", text="File Name")
        tree.heading("Category", text="Category")
        tree.heading("Size", text="Size")

        tree.column("File", width=300)
        tree.column("Category", width=150)
        tree.column("Size", width=100)

        tree.pack(fill=tk.BOTH, expand=True)
        scrollbar.config(command=tree.yview)

        for fname, cat, size in files:
            size_str = self.format_size(size)
            tree.insert("", tk.END, values=(fname, cat, size_str))

        close_btn = tk.Button(preview_window, text="Close", 
                             command=preview_window.destroy,
                             bg=self.current_theme['button_bg'],
                             fg=self.current_theme['button_fg'])
        close_btn.pack(pady=10)

    def format_size(self, size):
        for unit in ['B', 'KB', 'MB', 'GB']:
            if size < 1024.0:
                return f"{size:.1f} {unit}"
            size /= 1024.0
        return f"{size:.1f} TB"

    def confirm_organize(self):
        if not self.source_dir:
            messagebox.showwarning("Warning", "Please select a folder first.")
            return

        file_count = sum(1 for f in os.listdir(self.source_dir) 
                        if os.path.isfile(os.path.join(self.source_dir, f)))

        response = messagebox.askyesno(
            "Confirm Organization",
            f"Are you sure you want to organize {file_count} files?\n\n"
            f"Files will be moved into category folders.\n"
            f"This action can be undone using 'Undo Last' button.",
            icon='question'
        )

        if response:
            self.organize_files()

    def organize_files(self):
        if not self.source_dir:
            return
        self.organize_btn.config(state=tk.DISABLED)
        self.preview_btn.config(state=tk.DISABLED)
        self.undo_btn.config(state=tk.DISABLED)

        thread = threading.Thread(target=self._organize_files_thread)
        thread.daemon = True
        thread.start()

    def _organize_files_thread(self):
        import time
        self.start_time = time.time()
        for folder in self.file_types.keys():
            folder_path = os.path.join(self.source_dir, folder)
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)

        move_log = {}
        files = [f for f in os.listdir(self.source_dir) 
                if os.path.isfile(os.path.join(self.source_dir, f))]

        total_files = len(files)

        try:
            for i, filename in enumerate(files):
                file_path = os.path.join(self.source_dir, filename)

                _, ext = os.path.splitext(filename)
                category = self.get_category_for_extension(ext)

                dest_folder = os.path.join(self.source_dir, category)
                dest_path = os.path.join(dest_folder, filename)

                new_dest_path = self.safe_move(file_path, dest_path)

                progress = ((i + 1) / total_files) * 100
                self.root.after(0, self.update_progress, progress, 
                               f"Moving {filename}...")

                self.log(f"✓ Moved {filename} → {category}")
                move_log[new_dest_path] = file_path

            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            log_path = os.path.join(self.log_dir, f"file_move_log_{timestamp}.json")
            with open(log_path, "w") as f:
                json.dump(move_log, f, indent=4)

            self.root.after(0, self.organization_complete)

        except Exception as e:
            self.root.after(0, lambda: messagebox.showerror("Error", 
                           f"An error occurred: {e}"))
            self.root.after(0, self.reset_buttons)

    def update_progress(self, value, text):
        self.progress_bar['value'] = value
        self.progress_label.config(text=text)
        self.root.update_idletasks()

    def organization_complete(self):
        import time
        elapsed = time.time() - self.start_time
        self.update_progress(100, "✓ Organization complete!")
        self.log("\n" + "="*50)
        self.log("✓ ORGANIZATION COMPLETE!")
        self.log(f"⏱️ Time taken: {elapsed:.2f} seconds")
        self.log("="*50 + "\n")
        self.update_undo_button()
        self.refresh_logs()

        messagebox.showinfo("Success", 
                           "Files organized successfully!\n\n"
                           "You can undo this operation if needed.")

        self.root.after(2000, lambda: self.update_progress(0, "Ready"))
        self.reset_buttons()

    def reset_buttons(self):
        self.organize_btn.config(state=tk.NORMAL)
        self.preview_btn.config(state=tk.NORMAL)
        self.update_undo_button()

    def safe_move(self, src, dest):
        base, ext = os.path.splitext(dest)
        counter = 1
        new_dest = dest
        while os.path.exists(new_dest):
            new_dest = f"{base}({counter}){ext}"
            counter += 1
        shutil.move(src, new_dest)
        return new_dest

    def confirm_undo(self):
        response = messagebox.askyesno(
            "Confirm Undo",
            "Are you sure you want to undo the last organization?\n\n"
            "All files will be moved back to their original locations.",
            icon='question'
        )

        if response:
            self.undo_organize()

    def undo_organize(self):
        if not self.move_logs:
            messagebox.showwarning("Warning", "No organization log found to undo.")
            return

        log_path = self.move_logs[0]

        self.undo_btn.config(state=tk.DISABLED)
        self.organize_btn.config(state=tk.DISABLED)

        try:
            with open(log_path, "r") as f:
                move_log = json.load(f)

            total = len(move_log)
            for i, (new_path, original_path) in enumerate(move_log.items()):
                if os.path.exists(new_path):
                    original_dir = os.path.dirname(original_path)
                    if not os.path.exists(original_dir):
                        os.makedirs(original_dir)
                    shutil.move(new_path, original_path)

                    progress = ((i + 1) / total) * 100
                    self.update_progress(progress, f"Restoring files...")

                    self.log(f"↶ Restored {os.path.basename(new_path)}")

            os.remove(log_path)
            self.log("\n" + "="*50)
            self.log("↶ UNDO COMPLETE!")
            self.log("="*50 + "\n")

            messagebox.showinfo("Success", "Undo completed successfully!")

            self.update_undo_button()
            self.refresh_logs()

            self.root.after(2000, lambda: self.update_progress(0, "Ready"))

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

        finally:
            self.organize_btn.config(state=tk.NORMAL)
            self.update_undo_button()

    def save_categories(self):
        new_file_types = {}

        for category, entry in self.category_entries.items():
            ext_text = entry.get().strip()
            if ext_text:
                exts = []
                for e in ext_text.split(","):
                    e = e.strip().lower()
                    if e and not e.startswith('.'):
                        e = '.' + e
                    if e:
                        exts.append(e)
            else:
                exts = []
            new_file_types[category] = exts

        if "Others" not in new_file_types:
            new_file_types["Others"] = []

        self.file_types = new_file_types
        self.log("✓ File categories updated successfully!")

        messagebox.showinfo("Success", "File categories have been updated!")

    def reset_categories(self):
        response = messagebox.askyesno(
            "Confirm Reset",
            "Are you sure you want to reset all categories to default values?",
            icon='warning'
        )

        if response:
            self.file_types = default_file_types.copy()

            for category, entry in self.category_entries.items():
                if category in self.file_types:
                    entry.delete(0, tk.END)
                    entry.insert(0, ", ".join(self.file_types[category]))

            self.log("✓ Categories reset to defaults!")
            messagebox.showinfo("Success", "Categories have been reset to defaults!")

    def refresh_logs(self):
        if not self.log_dir or not os.path.exists(self.log_dir):
            return

        self.logs_text.config(state=tk.NORMAL)
        self.logs_text.delete(1.0, tk.END)

        logs = sorted(
            [f for f in os.listdir(self.log_dir) 
             if f.startswith("file_move_log_") and f.endswith(".json")],
            reverse=True
        )

        if not logs:
            self.logs_text.insert(tk.END, "No organization history found.\n")
        else:
            self.logs_text.insert(tk.END, f"Found {len(logs)} organization(s):\n\n")

            for log_file in logs:
                log_path = os.path.join(self.log_dir, log_file)
                timestamp = log_file.replace("file_move_log_", "").replace(".json", "")

                try:
                    dt = datetime.datetime.strptime(timestamp, "%Y%m%d_%H%M%S")
                    formatted_time = dt.strftime("%Y-%m-%d %H:%M:%S")
                except:
                    formatted_time = timestamp

                with open(log_path, "r") as f:
                    log_data = json.load(f)

                self.logs_text.insert(tk.END, f"📅 {formatted_time}\n")
                self.logs_text.insert(tk.END, f"   Files moved: {len(log_data)}\n\n")

        self.logs_text.config(state=tk.DISABLED)

    def log(self, message):
        self.status_text.config(state=tk.NORMAL)
        self.status_text.insert(tk.END, message + "\n")
        self.status_text.see(tk.END)
        self.status_text.config(state=tk.DISABLED)

def main():
    root = TkinterDnD.Tk()
    app = JunkFileOrganizerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()