# TextCraft-Text-Editor
TextCraft – A feature-rich text editor built with Python and Tkinter, offering powerful text editing, formatting, file handling, themes, font customization, color controls, zoom options, alignment, word wrap, and more.
# 📝 TextCraft – Text Editor

<p align="center">
  <strong>A Feature-Rich Desktop Text Editor Built with Python & Tkinter</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python">
  <img src="https://img.shields.io/badge/Tkinter-GUI-orange?style=for-the-badge">
  <img src="https://img.shields.io/badge/File%20Handling-Python-green?style=for-the-badge">
  <img src="https://img.shields.io/badge/Desktop%20Application-purple?style=for-the-badge">
</p>

---

## 📌 About the Project

**TextCraft – Text Editor** is a desktop-based text editing application developed using **Python and Tkinter**.

The application provides essential text-editing features such as creating, opening, saving, and editing text files, along with advanced formatting and customization options.

It includes features such as **Bold, Italic, Underline, Strikethrough, font selection, font size, text alignment, color customization, themes, zoom controls, word wrap, undo, redo, cut, copy, paste, and file handling**.

The project demonstrates practical knowledge of **Python programming, Object-Oriented Programming, Tkinter GUI development, event handling, file handling, and desktop application development**.

---

## ✨ Features

### 📁 File Operations

* 🆕 **New File** — Create a new blank document.
* 📂 **Open File** — Open and load an existing text file.
* 💾 **Save** — Save the current document.
* 💾 **Save As** — Save the document with a new filename or location.
* 🚪 **Exit** — Close TextCraft.

### ✏️ Text Editing

* ✂️ **Cut** — Remove selected text and copy it to the clipboard.
* 📋 **Copy** — Copy selected text.
* 📌 **Paste** — Paste clipboard content.
* ↩️ **Undo** — Undo the latest editing operation.
* ↪️ **Redo** — Redo a previously undone operation.
* 🧹 **Clear All** — Remove all text from the editor.

### 🎨 Text Formatting

<p align="center">
  <strong>Bold</strong> &nbsp; • &nbsp;
  <em>Italic</em> &nbsp; • &nbsp;
  <u>Underline</u> &nbsp; • &nbsp;
  <s>Strikethrough</s>
</p>

Additional formatting options include:

* **Bold**
* *Italic*
* <u>Underline</u>
* <s>Strikethrough</s>
* 🔤 Font Family
* 🔠 Font Size
* 🎨 Text Color
* 🖌️ Background Color
* ⬅️ Left Alignment
* ↔️ Center Alignment
* ➡️ Right Alignment

---

## 🖋️ Formatting Toolbar

The toolbar provides quick access to commonly used formatting features.

| Option   | Function                       |
| -------- | ------------------------------ |
| **B**    | Apply Bold formatting          |
| *I*      | Apply Italic formatting        |
| <u>U</u> | Apply Underline formatting     |
| <s>S</s> | Apply Strikethrough formatting |
| 🔤 Font  | Select font family             |
| 🔠 Size  | Change font size               |
| 🎨 Color | Change text color              |
| ⬅️       | Left alignment                 |
| ↔️       | Center alignment               |
| ➡️       | Right alignment                |

---

## 🌈 Theme Customization

TextCraft provides multiple themes to customize the editor's appearance.

### Available Themes

* ⚪ Light Default
* 🔵 Light Plus
* ⚫ Dark
* 🔴 Red
* 🟡 Monokai
* 🔵 Night Blue

---

## 🔍 View & Display Options

The **View** menu provides controls for improving the text viewing experience.

### Available Options

* 🔎 **Zoom In**
* 🔍 **Zoom Out**
* 🔄 **Restore Default Zoom**
* ↔️ **Word Wrap**

### ⌨️ Keyboard Shortcuts

| Shortcut       | Action               |
| -------------- | -------------------- |
| `Ctrl + Plus`  | Zoom In              |
| `Ctrl + Minus` | Zoom Out             |
| `Ctrl + 0`     | Restore Default Zoom |

---

## 🧰 Edit Menu

The **Edit** menu provides standard text editing operations.

### Available Operations

* 📋 Copy
* 📌 Paste
* ✂️ Cut
* 🧹 Clear All
* ↩️ Undo
* ↪️ Redo

### ⌨️ Keyboard Shortcuts

| Shortcut         | Action    |
| ---------------- | --------- |
| `Ctrl + C`       | Copy      |
| `Ctrl + V`       | Paste     |
| `Ctrl + X`       | Cut       |
| `Ctrl + Z`       | Undo      |
| `Ctrl + Y`       | Redo      |
| `Ctrl + Alt + X` | Clear All |

---

## 🎨 Color Customization

TextCraft supports color customization to provide a personalized writing experience.

Users can customize:

* 🖌️ Text Color
* 🎨 Background Color
* 🌗 Editor Theme

---

## 📄 File Handling

The application uses Python file handling to manage text documents.

It supports:

* Creating new documents
* Opening existing text files
* Reading file content
* Writing content to files
* Saving documents
* Save As functionality

---

## 🪟 Dialog Boxes

Tkinter dialog boxes are used for user interaction and file management.

They are used for:

* 📂 Selecting files to open
* 💾 Selecting save locations
* 🎨 Selecting colors
* ⚠️ Displaying user messages
* ❓ Confirming user actions

---

## 🛠️ Technologies Used

### 🐍 Python

Used for application logic, event handling, text processing, file handling, and implementing editor functionality.

### 🖥️ Tkinter

Used to develop the graphical user interface, menus, toolbar, text editor, buttons, dialogs, and interactive components.

### 📄 File Handling

Used to create, open, read, write, and save text documents.

---

## 🏗️ How It Works

```text
                    👤 User
                       │
                       ▼
              ┌─────────────────┐
              │   Tkinter GUI   │
              └────────┬────────┘
                       │
                       ▼
              ┌─────────────────┐
              │   Text Editor   │
              │ & Formatting    │
              └────────┬────────┘
                       │
                ┌──────┴──────┐
                ▼             ▼
        ┌──────────────┐ ┌──────────────┐
        │ Python Logic │ │ File Dialogs │
        └───────┬──────┘ └──────────────┘
                │
                ▼
        ┌──────────────────┐
        │    Text Files    │
        └──────────────────┘
```

The user interacts with the Tkinter-based interface. Python processes the selected operation and performs the required text editing, formatting, customization, or file-handling operation.

---

## 🔄 Application Workflow

```text
Launch TextCraft
       ↓
Create / Open Document
       ↓
Enter or Edit Text
       ↓
Select Text
       ↓
Apply Formatting
       ↓
Customize Font / Color / Theme
       ↓
Save / Save As
       ↓
Continue Editing
       ↓
Exit Application
```

---

## 💡 Key Concepts Demonstrated

* 🐍 Python Programming
* 🖥️ Tkinter GUI Development
* ⚡ Event Handling
* 📄 File Handling
* ✏️ Text Processing
* 🧰 Menu & Toolbar Implementation
* 🎨 Text Formatting
* 🔤 Font Management
* 🌈 Color Management
* 🌗 Theme Customization
* 🪟 Dialog Box Handling
* ⌨️ Keyboard Shortcuts
* 👤 User Interaction
* 💻 Desktop Application Development

---

## 📂 Project Structure

```text
TextCraft-Text-Editor/
│
├── homepage.py
└── README.md
```

---

## 🚀 Setup & Installation

### 1. Clone the Repository

```bash
git clone https://github.com/shivangisahu-dev/TextCraft-Text-Editor.git
```

### 2. Navigate to the Project Directory

```bash
cd TextCraft-Text-Editor
```

### 3. Run the Application

```bash
python homepage.py
```

---

## 🎯 Project Highlights

<p align="center">
  <strong>Python</strong> •
  <strong>Tkinter</strong> •
  <strong>File Handling</strong> •
  <strong>Text Formatting</strong> •
  <strong>Theme Customization</strong> •
  <strong>GUI Development</strong> •
  <strong>Desktop Application</strong>
</p>

---

## 📌 What This Project Demonstrates

TextCraft demonstrates the ability to build a complete desktop application from scratch using Python.

It combines:

**GUI Development + File Handling + Text Editing + Formatting + Event Handling + User Interaction**

into a single functional application.

---

## 👩‍💻 Conclusion

**TextCraft – Text Editor** demonstrates the practical implementation of a feature-rich desktop text editor using **Python and Tkinter**.

The project combines **file handling, text editing, formatting, font management, color customization, themes, zoom controls, menus, keyboard shortcuts, and GUI development** to provide a complete desktop editing experience.

It demonstrates how Python can be used to develop interactive and user-friendly desktop applications.

---

<p align="center">
  ⭐ <strong>If you find this project useful, consider giving it a star!</strong>
</p>
