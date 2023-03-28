Simple Utility for
Ensure filesystems setup with rclone
run using cron / flock
*/5 * * * * flock -n /tmp/google_drive_sync.lock /usr/bin/python3 /home/ubuntu/google-drive-cron-backup/script.py
