import socket
import urllib.request
import os
import subprocess
import time
PING_HASH = "HEALTHCHECKS_PING_HASH"
HOME_DIRECTORY = "RCLONE_FS"
BACKUPS = ["RCLONE_FS"]

def sendHealthCheckPing(status = 0):
    parsedStatus = ""
    if status:
        parsedStatus = "/" + str(status)
    urllib.request.urlopen("https://hc-ping.com/" + PING_HASH + parsedStatus, timeout=10)

def healthCheck():
    returnCode = 0
    for backup in BACKUPS:
        result = subprocess.run(["rclone check " + HOME_DIRECTORY + " " +  backup], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, shell=True, capture_output=False, text=False)
        if result.returncode:
            returnCode = result.returncode
            break
    sendHealthCheckPing(returnCode)
    return returnCode

isUnhealthy = healthCheck()
if isUnhealthy:
    returnCode = 0
    sendHealthCheckPing("start")
    for backup in BACKUPS:
        ts = time.time()
        logFilePath = "/logs/log" + str(ts) + ".txt"
        result = subprocess.run(["rclone sync -P --create-empty-src-dirs " + HOME_DIRECTORY + " " + backup + " > " + logFilePath],stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, shell=True, capture_output=False, text=False)
        if result.returncode:
            returnCode = result.returncode
            break
    if returnCode:
        sendHealthCheckPing(returnCode)
    healthCheck()

