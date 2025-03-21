# 📌 Project Setup Guide

This guide provides step-by-step instructions to set up your project environment, including installing **FFmpeg** and **PortAudio** across macOS, Linux, and Windows, and setting up a Python virtual environment using **Pipenv**, **pip**, or **conda**.

---

## 📜 Table of Contents

1. [⚙️ Installing FFmpeg and PortAudio](#-installing-ffmpeg-and-portaudio)
   - [🍏 macOS](#-macos)
   - [🐧 Linux](#-linux)
   - [🪟 Windows](#-windows)
2. [🐍 Setting Up a Python Virtual Environment](#-setting-up-a-python-virtual-environment)
   - [📦 Using Pipenv](#-using-pipenv)
   - [📁 Using pip and venv](#-using-pip-and-venv)
   - [🔬 Using Conda](#-using-conda)
3. [🚀 Running the Application](#-running-the-application)

---

## ⚙️ Installing FFmpeg and PortAudio

### 🍏 macOS

1. **Install Homebrew** (if not already installed):
   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```
2. **Install FFmpeg and PortAudio:**
   ```bash
   brew install ffmpeg portaudio
   ```

### 🐧 Linux (Debian-based distributions, e.g., Ubuntu)

1. **Update the package list:**
   ```bash
   sudo apt update
   ```
2. **Install FFmpeg and PortAudio:**
   ```bash
   sudo apt install ffmpeg portaudio19-dev
   ```

### 🪟 Windows

#### 📥 Download FFmpeg
1. Visit the official **[FFmpeg Downloads](https://ffmpeg.org/download.html)** page.
2. Download the latest static build for Windows.

#### 📦 Extract and Set Up FFmpeg
1. Extract the downloaded ZIP file to a folder (e.g., `C:\ffmpeg`).
2. Add the `bin` directory to your system's PATH:
   - Search for **"Environment Variables"** in the Start menu.
   - Click **"Edit the system environment variables."**
   - Under **"System variables,"** select `Path` → Click **"Edit."**
   - Click **"New"** and add `C:\ffmpeg\bin`.
   - Click **"OK"** to save.

#### 🔧 Install PortAudio
1. Download **PortAudio** from the official **[PortAudio Downloads](http://www.portaudio.com/download.html)** page.
2. Follow the installation instructions.

---

## 🐍 Setting Up a Python Virtual Environment

### 📦 Using Pipenv
1. **Install Pipenv (if not already installed):**
   ```bash
   pip install pipenv
   ```
2. **Install dependencies with Pipenv:**
   ```bash
   pipenv install
   ```
3. **Activate the virtual environment:**
   ```bash
   pipenv shell
   ```

### 📁 Using pip and venv
1. **Create a virtual environment:**
   ```bash
   python -m venv venv
   ```
2. **Activate the virtual environment:**
   - **macOS/Linux:**
     ```bash
     source venv/bin/activate
     ```
   - **Windows:**
     ```bash
     venv\Scripts\activate
     ```
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

### 🔬 Using Conda
1. **Create a Conda environment:**
   ```bash
   conda create --name myenv python=3.11
   ```
2. **Activate the environment:**
   ```bash
   conda activate myenv
   ```
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

---

## 🚀 Running the Application

### 🏥 Phase 1: Brain of the Doctor
```bash
python brain_of_the_doctor.py
```

### 🎙️ Phase 2: Voice of the Patient
```bash
python voice_of_the_patient.py
```

### 🗣️ Phase 3: Voice of the Doctor
```bash
python voice_of_the_doctor.py
```

### 💻 Phase 4: Setup Gradio UI
```bash
python gradio_app.py
```

---

✅ **Your AI Medical Assistance is now ready!** 🚀
