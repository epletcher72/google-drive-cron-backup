import urllib.request
import subprocess
PING_HASH = "HEALTHCHECKS_PING_HASH"
HOME_DIRECTORY = "RCLONE_FS"
BACKUPS = ["RCLONE_FS"]
WITH_OUTPUT = False

def sysrun(args):
    return subprocess.run(args, shell=True, capture_output=WITH_OUTPUT)


def sendHealthCheckPing(status = 0):
    parsedStatus = ""
    if status:
        parsedStatus = "/" + str(status)
    urllib.request.urlopen("https://hc-ping.com/" + PING_HASH + parsedStatus, timeout=10)

def healthCheck():
    returnCode = 0
    for backup in BACKUPS:
        result = sysrun(["rclone check " + HOME_DIRECTORY + " " +  backup])
        if result.returncode:
            returnCode = result.returncode
            break
    if not returnCode:
        sendHealthCheckPing(returnCode)
    return returnCode

isUnhealthy = healthCheck()
if isUnhealthy:
    returnCode = 0
    sendHealthCheckPing("start")
    for backup in BACKUPS:
        result = sysrun(["rclone sync -P --create-empty-src-dirs " + HOME_DIRECTORY + " " + backup])
        if result.returncode:
            returnCode = result.returncode
            break
    if returnCode:
        sendHealthCheckPing(returnCode)
    healthCheck()

