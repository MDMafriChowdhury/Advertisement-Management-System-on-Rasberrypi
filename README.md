# Advertisement Management System on Raspberry Pi

This project implements an advertisement management system on a Raspberry Pi. The system runs a Python script that automatically starts on boot, fetches video data from a server, retrieves videos from a database, and syncs them from Google Drive using `rclone`.

## Features
- **Automatic Startup**: The Python script runs automatically when the Raspberry Pi boots.
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
python3 /path/to/your/script.py
```

## 2. Installing and Configuring `rclone` for Google Drive

### 2.1 Install `rclone`
Run the following commands to install `rclone`:

```bash
sudo apt update
sudo apt install rclone
```

### 2.2 Configure `rclone`
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

### 2.3 Syncing Google Drive with the Raspberry Pi
You can manually sync the Google Drive folder to a local folder (e.g., `/home/pi/Desktop/AddCasting/videos`) using the following command:

```bash
rclone sync GoogleDrive: /home/pi/Desktop/AddCasting/videos --drive-root-folder-id "1dzuIjwWJ1yTG3dZO2K6nNbvJTjg5DKlC"
```
