# 🧹 Junk File Organizer Pro

A powerful and modern Python-based GUI application that automatically organizes files in a selected folder into categorized subfolders. This enhanced version features a sleek interface with dark mode, drag-and-drop support, progress tracking, and much more — helping you clean messy directories with ease and style!

---

## 🚀 Features

### ✨ Core Functionality
- ✅ **Automatic File Organization** - Sorts files based on their extensions into categorized folders
- ✅ **Smart Categorization** - Pre-configured categories for Images, Videos, Documents, Music, Archives, Scripts, and Others
- ✅ **Duplicate Handling** - Automatically renames duplicate files to prevent overwrites
- ✅ **Undo Functionality** - Revert any organization operation with one click
- ✅ **Preview Mode** - See what will be organized before making changes

### 🎨 Modern UI Features
- ✅ **Drag & Drop Support** - Simply drag a folder onto the interface
- ✅ **Dark Mode** - Toggle between beautiful light and dark themes
- ✅ **Tabbed Interface** - Organized layout with Organize, Settings, and Logs tabs
- ✅ **Progress Bar** - Real-time visual feedback during file operations
- ✅ **Confirmation Dialogs** - Safety confirmations before organizing or undoing
- ✅ **Responsive Design** - Clean, modern interface that adapts to your theme

### 🛠️ Advanced Features
- ✅ **Customizable Categories** - Edit file extensions for each category
- ✅ **Organization History** - View all past organization operations with timestamps
- ✅ **File Size Display** - See file sizes in preview mode
- ✅ **Multi-threaded Operations** - UI remains responsive during file operations
- ✅ **Detailed Logging** - Track all file movements in the status panel

---
---
## 🗂️ Default File Categories

The organizer automatically categorizes files into these folders:

| Category | Extensions |
|----------|-----------|
| 🖼️ **Images** | `.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp`, `.tiff`, `.svg`, `.ico` |
| 📄 **Documents** | `.pdf`, `.doc`, `.docx`, `.txt`, `.xls`, `.xlsx`, `.ppt`, `.pptx`, `.odt`, `.rtf` |
| 🎥 **Videos** | `.mp4`, `.mov`, `.avi`, `.mkv`, `.flv`, `.wmv`, `.webm` |
| 🎵 **Music** | `.mp3`, `.wav`, `.aac`, `.flac`, `.ogg`, `.wma` |
| 🗃️ **Archives** | `.zip`, `.rar`, `.tar`, `.gz`, `.7z`, `.bz2` |
| 💻 **Scripts** | `.py`, `.js`, `.html`, `.css`, `.sh`, `.bat`, `.java`, `.cpp`, `.c` |
| 📦 **Others** | Any file type not matching above categories |

---

---

## 💻 Installation & Setup

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

### Step 1: Clone the Repository
```bash
git clone https://github.com/T-Hub06/Junk-File-Organiser.git
cd Junk-File-Organiser
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

Or install manually:
```bash
pip install tkinterdnd2
```

### Step 3: Run the Application
```bash
python junk_organizer_enhanced.py
```

---

---

## 🧩 Technologies Used

- **Python 3.x** - Core programming language
- **Tkinter** - GUI framework for the interface
- **TkinterDnD2** - Drag-and-drop functionality
- **Threading** - For responsive UI during operations
- **JSON** - For storing operation logs and configurations
- **OS & Shutil** - File system operations

---

---

## 🔧 Troubleshooting

### Issue: "No module named 'tkinterdnd2'"
Solution: Run `pip install tkinterdnd2`

### Issue: Drag and drop not working
Solutions:
- Ensure tkinterdnd2 is properly installed
- Try restarting the application
- Use the "Browse Folder" button as an alternative

### Issue: Files not organizing
Check:
- The selected folder contains files (not just subfolders)
- File extensions match configured categories
- Check the Logs tab for error messages
- Ensure you have write permissions for the folder

### Issue: Application not starting
Solutions:
- Verify Python 3.7+ is installed: `python --version`
- Reinstall dependencies: `pip install -r requirements.txt`
- Try running with: `python3 junk_organizer_enhanced.py`

---

---
## 🎯 Future Enhancements

- [ ] Recursive folder organization (organize subfolders)
- [ ] Duplicate file detection
- [ ] File size filtering options
- [ ] Scheduled automatic organization
- [ ] Cloud storage integration
- [ ] Custom naming patterns
- [ ] Statistics dashboard
- [ ] Multi-language support

---

---
## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

---
## ⭐ Show Your Support

If you find this project helpful:
- ⭐ **Star this repository** - It motivates me to build more tools!
- 🐛 **Report bugs** - Help improve the project
- 💡 **Suggest features** - Share your ideas
- 🔀 **Fork and contribute** - Make it even better!

---
<div align="center">



[Report Bug](https://github.com/T-Hub06/Junk-File-Organiser/issues) · [Request Feature](https://github.com/T-Hub06/Junk-File-Organiser/issues)

</div>
