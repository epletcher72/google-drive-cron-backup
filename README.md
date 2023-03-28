Simple Utility for
Ensure filesystems setup with rclone
run using cron / flock
_/5 _ \* \* \* flock -n /tmp/google_drive_sync.lock /usr/bin/python3 path-to-sprypt.py
