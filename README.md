# 🗂️ Junk File Organizer Pro

A Python-based GUI application that automatically organizes cluttered 
directories by classifying files into categories based on their extensions.

## ⚡ Performance
- Organizes 100 files in ~1 second using multithreaded processing
- Supports 70+ file extensions across 9 categories
- Real-time progress tracking with millisecond-level operation logging

## ✨ Features

### Core
- **Auto Organization** — Classifies and moves files into category folders instantly
- **Drag & Drop** — Drop any folder directly onto the app to select it
- **Undo** — Full operation reversal via JSON-logged move history
- **Preview** — See exactly what will be organized before committing

### Safety
- **Collision-Safe Moving** — Automatic duplicate renaming ensures zero data loss
- **JSON Operation Logs** — Every move is logged with timestamp for full traceability
- **Confirmation Dialogs** — No accidental organization or undo operations

### UI
- **Dark/Light Theme** — Full theme switching with persistent styling
- **Real-time Status** — Live file-by-file progress in status panel
- **Performance Timer** — Shows exact time taken after every organization

## 📁 Supported Categories

| Category | Extensions |
|---|---|
| Images | .jpg .jpeg .png .gif .bmp .tiff .svg .ico .webp .heic .heif .raw .cr2 .nef |
| Documents | .pdf .doc .docx .txt .xls .xlsx .ppt .pptx .odt .rtf .csv .json .xml .md .epub |
| Videos | .mp4 .mov .avi .mkv .flv .wmv .webm |
| Music | .mp3 .wav .aac .flac .ogg .wma |
| Archives | .zip .rar .tar .gz .7z .bz2 .xz .iso |
| Scripts | .py .js .html .css .sh .bat .java .cpp .ts .jsx .tsx .php .rb .go .rs .ipynb |
| 3D & Design | .obj .fbx .stl .blend .ai .psd .xd .fig |
| Executables | .exe .msi .apk .dmg .deb .rpm |
| Others | Anything not in the above categories |

## 🛠️ Tech Stack
- **Python** — Core logic
- **Tkinter** — GUI framework
- **TkinterDnD2** — Drag and drop support
- **Threading** — Non-blocking file operations
- **JSON** — Operation logging for undo functionality

## 🚀 How to Run

### Prerequisites
```bash
pip install tkinterdnd2
```

### Run
```bash
python tj.py
```

## 📖 How to Use
1. Launch the app
2. Drag and drop a folder onto the app **or** click Browse
3. Click **Preview** to see what will be organized
4. Click **Organize Files** to sort everything automatically
5. Use **Undo Last** to reverse if needed

## ⚙️ Custom Categories
Go to the **Settings** tab to add, remove or modify file extensions 
for any category. Changes apply immediately to the next organization.
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
