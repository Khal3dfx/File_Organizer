# 📁 File Organizer (Python)

A command-line Python tool that organizes files inside a selected folder into categorized subfolders such as **Images**, **Documents**, and **Videos**.  
It includes a **dry-run mode** so you can preview changes safely before moving files.

---

## 🚀 Features
- Organizes files by type (Images, Documents, Videos)
- Detects files automatically based on extensions
- Ignores subfolders
- Dry-run mode to preview file movements
- Cross-platform (Windows, macOS, Linux)
- Simple and beginner-friendly CLI interface

---

## ▶️ How to Run

### 1️⃣ Clone the repository
```bash
git clone https://github.com/Khal3dfx/File_Organizer.git
cd File_Organizer
```

### 2️⃣ Run the program
```bash
python3 File_Organizer.py
```

### 🧭 How It Works
1. Enter the full path of the folder you want to organize
2. The program scans only files (ignores folders)
3. Files are categorized by extension
4. You can preview the mapping
5. Choose:
  - Dry-run → no files moved
  - Actual move → files organized into folders

### 📂 Categories Used
- Images: .jpg, .jpeg, .png, .gif
- Documents: .pdf, .docx, .txt, .xlsx
- Videos: .mp4, .mkv, .mov
- Others: Files that don’t match the above

### 2️⃣ Run the program
```bash
File_Organizer/
│
├── File_Organizer.py   # Main script
├── README.md           # Documentation
├── .gitignore          # Git ignored files
```

### 🛠 Requirements
- Python 3.x
- No external libraries required

### 🔮 Future Improvements
- Add more file categories
- Custom category configuration
- Recursive folder support
- Undo feature
- Logging moved files

### 👤 Author
Khaled Fahad Al-Hamad
