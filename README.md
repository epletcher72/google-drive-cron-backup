# [Google Drive Cron Backup](https://ethanpletcher.com/) &middot; [![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/epletcher72/google-drive-cron-backup/blob/master/LICENSE) [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/epletcher72/google-drive-cron-backup/tree/master#Contributing)

Google Drive Cron Backup is a Python program for syncing data between two hosted databases, regardless of provider.

* **Universal:** This project is built on [Rclone](https://rclone.org/), which allows for universal file transfer between many data providers (Google, Box, etc...) See this [full list](https://rclone.org/#providers) of compatible platforms.
* **Portable:** Can be used anywhere with minimal external technology setup.
* **Worry Free:** We support integration with [healthchecks.io](https://healthchecks.io/) so you never have to remember to check that the service is working.

[How to use this project](#Installation)
[How You can contribute :)](#Contributing)

## System Design

This program is built as a simple Python script, intended to be run as a cron job by an external tool.

Every time it runs, it performs the following sequence:

* Use [rclone check](https://rclone.org/commands/rclone_check/) to see whether the contents of the two drives match.
* If they are already in sync, send a <span style='color: red;'>long</span> ping to [healthchecks.io](https://healthchecks.io/) and exit.
* if they are not in sync, send a FAILURE ping to [healthchecks.io](https://healthchecks.io/).
* While the drives are out of sync, send a START ping to [healthchecks.io](https://healthchecks.io/) then attempt to sync the contents of the two drives. if it fails, it will try again, otherwise, it will send a SUCCESS ping to [healthchecks.io](https://healthchecks.io/) and exit.

[healthchecks.io](https://healthchecks.io/) will inform you by email or using whatever contact method you set up if it does not receive confirmation within a designated period that the drives are in sync.

## Installation

React has been designed for gradual adoption from the start, and **you can use as little or as much React as you need**:

* Use [Online Playgrounds](https://reactjs.org/docs/getting-started.html#online-playgrounds) to get a taste of React.
* [Add React to a Website](https://reactjs.org/docs/add-react-to-a-website.html) as a `<script>` tag in one minute.
* [Create a New React App](https://reactjs.org/docs/create-a-new-react-app.html) if you're looking for a powerful JavaScript toolchain.

You can use React as a `<script>` tag from a [CDN](https://reactjs.org/docs/cdn-links.html), or as a `react` package on [npm](https://www.npmjs.com/package/react).

## Documentation

Documentation is basically limited to basic in-code comments and the info contained here. 
You can improve it by sending pull requests to [this repository](https://github.com/epletcher72/google-drive-cron-backup/).

## Examples

* **Sync local NAS to remote archive** If one maintains a Network Attached Storage device, one could use this service to automattically back up stored data to Google Drive.
* **Many to one:** If one has two data sources, each with different access rules and purposes, but wants to be able to view both in on the same store, this service could be used to copy data from each source into multiple folders in one destination source.

## Contributing

I am no longer actively working on this project. However, if you have any ideas for improvements that would make the repository easier to use, feel free to open a pull request. Please refer to [this guide](https://github.com/epletcher72/google-drive-cron-backup/tree/master#Contributing_Guide)

### [Contributing Guide](https://reactjs.org/docs/how-to-contribute.html)

Read our [contributing guide](https://reactjs.org/docs/how-to-contribute.html) to learn about our development process, how to propose bugfixes and improvements, and how to build and test your changes to React.

### Good First Issues

To help you get your feet wet and get you familiar with our contribution process, we have a list of [good first issues](https://github.com/facebook/react/labels/good%20first%20issue) that contain bugs that have a relatively limited scope. This is a great place to get started.

### [Code of Conduct](https://code.fb.com/codeofconduct)

This repository exists for the benefit of myself and future developers. Please be respectful.

### License

Google Drive Cron Backup is [MIT licensed](./LICENSE).

Simple Utility for
Ensure filesystems setup with rclone
run using cron / flock

*/5 * * * * flock -n /tmp/google_drive_sync.lock /usr/bin/python3 /home/ubuntu/google-drive-cron-backup/script.py
