import urllib.request
import subprocess
PING_HASH = "HEALTHCHECKS_PING_HASH"
HOME_DIRECTORY = "RCLONE_FS"
BACKUP = "RCLONE_FS"
WITH_OUTPUT = False

def sysrun(args):
    return subprocess.run(args, shell=True, capture_output=WITH_OUTPUT)


def sendHealthCheckPing(status = 0):
    parsedStatus = ""
    if status:
        parsedStatus = "/" + str(status)
    urllib.request.urlopen("https://hc-ping.com/" + PING_HASH + parsedStatus, timeout=10)

def healthCheck():
    result = sysrun(["rclone check " + HOME_DIRECTORY + " " + BACKUP])
    if not result.returncode:
        sendHealthCheckPing(result.returncode)
    return result.returncode

isUnhealthy = healthCheck()
while isUnhealthy:
    sendHealthCheckPing("start")
    result = sysrun(["rclone sync -P --create-empty-src-dirs " + HOME_DIRECTORY + " " + BACKUP])
    if result.returncode:
        sendHealthCheckPing("fail")
    isUnhealthy = healthCheck()

