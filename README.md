# [Google Drive Cron Backup](https://ethanpletcher.com/) &middot; [![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/epletcher72/google-drive-cron-backup/blob/master/LICENSE) [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/epletcher72/google-drive-cron-backup/tree/master#Contributing)

Google Drive Cron Backup is a Python program for syncing data between two hosted databases, regardless of provider.

* **Universal:** This project is built on [rclone](https://rclone.org/), which allows for universal file transfer between many data providers (Google, Box, etc...) See this [full list](https://rclone.org/#providers) of compatible platforms.
* **Portable:** Can be used anywhere with minimal external technology setup.
* **Worry Free:** We support integration with [healthchecks.io](https://healthchecks.io/) so you never have to remember to check that the service is working.

[How to use this project](#Installation)

[How You can contribute :)](#Contributing)

## System Design

This program is built as a simple Python script, intended to be run as a cron job by an external tool.

Every time it runs, it performs the following sequence:

* Use [rclone check](https://rclone.org/commands/rclone_check/) to see whether the contents of the two drives match.
* If they are already in sync, send a SUCCESS ping to [healthchecks.io](https://healthchecks.io/) and exit.
* if they are not in sync, send a FAILURE ping to healthchecks.
* While the drives are out of sync, send a START ping to healthchecks then attempt to sync the contents of the two drives. if it fails, it will try again, otherwise, it will send a SUCCESS ping to [healthchecks.io](https://healthchecks.io/) and exit.

Healthchecks will inform you by email or using whatever contact method you set up if it does not receive confirmation within a designated period that the drives are in sync.

## System Requirements

It is recommended to run this on a Linux server instance, but any computer with Python installed and a cron system that can be relied upon to stay on will do the trick.

## Installation

* Clone [this repository](https://github.com/epletcher72/google-drive-cron-backup/) on your machine.
* Install rclone on your machine. A guide can be found [here](https://rclone.org/install/).
* Set up the two drives for the sync using rclone config command.
* Create a Check on [healthchecks.io](https://healthchecks.io/). Signup may be necessary
* Edit script.py with the appropriate drive directories from rclone and check hash in lines 4-6.
* Set up a cron job to run as often as you like.
* Example using crontab and flock */5 * * * * flock -n /tmp/google_drive_sync.lock </path/to/python3> /path/to/google-drive-cron-backup/script.py

## Documentation

Documentation is extremely limited for this project. It consists basically of the info contained in this file. 
You can improve it by sending pull requests to [this repository](https://github.com/epletcher72/google-drive-cron-backup/).

## Example Use Cases

* **Sync local NAS to remote archive** If one maintains a Network Attached Storage device, one could use this service to automatically back up stored data to Google Drive.
* **Many to one:** If one has two data sources, each with different access rules and purposes, but wants to be able to view both in the same store, this service could be used to copy data from each source into multiple folders in one destination source.

## Contributing

I appreciate your interest in improving this project.

I am no longer actively working on this project. However, if you have any ideas for improvements to make the repository more robust or easier to use, feel free to open a pull request.

Please keep PRs streamlined and minimal and avoid making breaking changes wherever practical.

New to GitHub? Read this [Contributing Guide]([https://reactjs.org/docs/how-to-contribute.html](https://docs.github.com/en/get-started/quickstart/contributing-to-projects)) as a jumping-off point.

## Bug Reports

Feel free to submit an issue [here](https://github.com/epletcher72/google-drive-cron-backup/issues).

Maintaining this project is not a high priority for me, but I will try to address any issues as they come up.

### Code of Conduct

This repository exists for the benefit of myself and future developers. Please be respectful.

### License

Google Drive Cron Backup is [MIT licensed](./LICENSE).
