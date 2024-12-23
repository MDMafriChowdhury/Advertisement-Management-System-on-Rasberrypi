# Advertisement Management System on Raspberry Pi

This project implements an advertisement management system on a Raspberry Pi. The system runs a Python script that automatically starts on boot, fetches video data from a server, retrieves videos from a database, and syncs them from Google Drive using `rclone`.

## Features
- **Automatic Startup**: The terminal opens automatically with the Python script on Raspberry Pi boot.
- **Data Fetching**: The system fetches data from a server to control the playback of advertisement videos.
- **Video Retrieval**: Videos are retrieved from a database.
- **Google Drive Syncing**: Videos are synced with a Google Drive folder using `rclone`.

## Prerequisites
1. **Raspberry Pi** running Raspberry Pi OS.
2. **Python 3** installed.
3. **rclone** installed and configured for Google Drive.

## Setup Instructions

### 1. Setting Up the Python Script to Run on Boot
To ensure the Python script runs automatically when the Raspberry Pi boots, add the following line to `~/.bashrc`:

```bash
nano ~/.bashrc
```

Add the line below at the end of the file:
```bash
python3 /path/to/your/script/Advertisement.py
```



### 2. Installing and Configuring `rclone` for Google Drive

## 2.1 Install `rclone`
Run the following commands to install `rclone`:

```bash
sudo apt update
sudo apt install rclone
```

## 2.2 Configure `rclone`
After installing `rclone`, configure it to access your Google Drive:

1. Run the configuration command:
    ```bash
    rclone config
    ```

2. Create a new remote for Google Drive:
    - Select `n` for a new remote.
    - Name the remote (e.g., `GoogleDrive`).
    - For the storage type, select `drive` (Google Drive).
    - Follow the prompts to authenticate with your Google account and authorize access for `rclone`.

3. Test the connection by listing your Google Drive files:
    ```bash
    rclone lsd GoogleDrive:
    ```

## 2.3 Syncing Google Drive with the Raspberry Pi
You can manually sync the Google Drive folder to a local folder (e.g., `/home/pi/Desktop/AddCasting/videos`) using the following command:

```bash
rclone sync GoogleDrive: /home/pi/Desktop/AddCasting/videos --drive-root-folder-id "GoogleDriveFolderID"
```

### 3. Autostart LXTerminal on Raspberry Pi
This guide explains how to set **LXTerminal** to open automatically at boot.

## Steps to Create the Autostart Entry

1. **Open the Terminal**.

2. **Navigate to the Autostart Directory**:
   ```bash
   cd ~/.config/autostart/
   ```

3. **Create a New Desktop Entry**:
    ```bash
    nano lxterminal.desktop
    ```

4. **Add the Following Content**:
    ```bash
    [Desktop Entry]
    Name=Terminal
    Exec=lxterminal
    Type=Application
    ```

### 4. Automating Google Drive Sync with `crontab`
To automatically sync the videos every 30 minutes, add a cron job using `crontab`:

1. Open the `crontab` editor:
    ```bash
    crontab -e
    ```


# Flask-Based Remote Raspberry Pi Management System

This project is a Flask web application for remotely managing a Raspberry Pi. The application provides functionalities such as rebooting the Raspberry Pi, connecting via VNC, closing terminal sessions, and redirecting users to specific URLs.

## Features

- **Reboot Remote Raspberry Pi:** Reboots a Raspberry Pi device remotely using SSH.
- **Connect via VNC Viewer:** Establishes a VNC connection to the Raspberry Pi.
- **Close Terminal Session:** Closes active terminal sessions on the Raspberry Pi.
- **Redirect to URL:** Redirects users to a specific Google Spreadsheet URL.
- **Status Check:** Checks the connection status to the Raspberry Pi.

## Technologies Used

- **Flask:** Web framework for building the application.
- **Paramiko:** Python library for SSH connections.
- **PyAutoGUI:** Automation of keyboard and mouse operations.
- **Subprocess:** Launching external applications (e.g., RealVNC Viewer).
- **Flask-CORS:** Enabling Cross-Origin Resource Sharing.

## Prerequisites

1. Python 3.x installed on your machine.
2. Required Python libraries:
   - Flask
   - Flask-CORS
   - Paramiko
   - PyAutoGUI
3. RealVNC Viewer installed on your system.
4. Raspberry Pi set up with SSH enabled.

## Installation

1. Clone this repository:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```
   
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Update the Raspberry Pi credentials and IP address in the script:
      ```bash
   hostname = "192.168.2.194"  # Update with your Raspberry Pi IP
   username = "pi"             # Update with your Raspberry Pi username
   password = "pi"             # Update with your Raspberry Pi password
   ```
   
   
