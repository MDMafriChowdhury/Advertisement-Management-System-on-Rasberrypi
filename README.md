# Advertisement Management System on Raspberry Pi

This project implements an advertisement management system on a Raspberry Pi. The system runs a Python script that automatically starts on boot, fetches video data from a server, retrieves videos from a database, and syncs them from Google Drive using `rclone`.

## Features
- **Automatic startup**: The Python script runs automatically when the Raspberry Pi boots.
- **Data fetching**: The system fetches data from a server to control the playback of advertisement videos.
- **Video retrieval**: The videos are retrieved from a database.
- **Google Drive syncing**: Videos are synced with a Google Drive folder using `rclone`.

## Prerequisites

1. **Raspberry Pi** running Raspberry Pi OS.
2. **Python 3** installed.
3. **rclone** installed and configured for Google Drive.

## 1. Setting up the Python Script to Run on Boot

To ensure the Python script runs automatically when the Raspberry Pi boots, add the following line to `~/.bashrc`:

```bash
nano ~/.bashrc
python3 /path/to/your/script.py

## 2. Installing and Configuring `rclone` for Google Drive

Follow the instructions below to install and configure `rclone` for syncing videos from Google Drive.

### 2.1 Install `rclone`

Run the following commands to install `rclone`:

```bash
sudo apt update
sudo apt install rclone

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

## 3. Automating Google Drive Sync with `crontab`

To automatically sync the videos every 30 minutes, add a cron job using `crontab`:

1. Open the `crontab` editor:
    ```bash
    crontab -e
    ```

2. Add the following line to the crontab file:

    ```bash
    */30 * * * * /usr/bin/rclone sync "GoogleDrive:" "/home/pi/Desktop/AddCasting/videos" --drive-root-folder-id "1dzuIjwWJ1yTG3dZO2K6nNbvJTjg5DKlC" >/dev/null 2>&1
    ```

This will sync the videos from Google Drive to the local folder every 30 minutes.

