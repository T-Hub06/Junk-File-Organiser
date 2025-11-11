
---

# 🧹 Junk File Organizer

A simple yet efficient Python-based tool that automatically organizes files in a selected folder into categorized subfolders (like Images, Videos, Documents, etc.).
This project helps you **clean messy directories**, **save time**, and **keep your system clutter-free** — all with just one click!

---

## 🚀 Features

✅ Automatically sorts files based on their type (extension)
✅ Creates categorized folders:

* 🖼️ **Images** (`.jpg`, `.png`, `.gif`, etc.)
* 🎥 **Videos** (`.mp4`, `.avi`, `.mkv`, etc.)
* 📄 **Documents** (`.pdf`, `.docx`, `.txt`, etc.)
* 🎵 **Music** (`.mp3`, `.wav`, etc.)
* 🗃️ **Others** (uncategorized or uncommon extensions)
  ✅ Lightweight and beginner-friendly
  ✅ Clean and simple code structure
  ✅ Runs directly inside **Jupyter Notebook**

---

## ⚙️ How It Works

1. The script scans the specified folder for all files.
2. It identifies each file type based on the extension.
3. It creates subfolders for each category (if not already existing).
4. Moves files into their respective folders automatically.

---

## 🧩 Technologies Used

* **Python 3.x**
* **Jupyter Notebook**
* **OS and Shutil modules** (for file management)

---

## 🧠 Learning Objectives

This project demonstrates:

* File handling in Python
* Working with OS-level commands
* Automation using Python scripting
* Organizing data efficiently

---

## 💻 How to Run

1. **Clone the repository**

   ```bash
   git clone https://github.com/T-Hub06/Junk-File-Organiser.git
   cd Junk-File-Organiser
   ```

2. **Open the notebook**
   Launch Jupyter Notebook and open the file:

   ```
   tj.ipynb
   ```

3. **Run all cells**
   Provide the path of the folder you want to organize when prompted.

---

## 🧾 Example Output

Before running:

```
Downloads/
 ├── photo.png
 ├── resume.pdf
 ├── song.mp3
 └── video.mp4
```

After running:

```
Downloads/
 ├── Images/photo.png
 ├── Documents/resume.pdf
 ├── Music/song.mp3
 └── Videos/video.mp4
```

---

## 🌟 Future Improvements

* Add GUI for user-friendly interaction
* Support for drag-and-drop folder selection
* File logging to track moved items
* Option to undo organization

---

## 🧑‍💻 Author

**Tushar Joshi**
📂 [GitHub Profile](https://github.com/T-Hub06)

If you like this project, ⭐ star the repo — it motivates me to build more automation tools!

---

Would you like me to make this **slightly shorter and recruiter-focused** (for GitHub main page readability) or keep it as this **detailed version**?

