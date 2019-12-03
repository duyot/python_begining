#!/opt/rh/rh-python36/root/usr/bin/python3
import logging
import re
import time
import os
from watchdog.events import LoggingEventHandler
from watchdog.observers import Observer
from TelegramUtils import sendMessage

logging.basicConfig(filename="bot.log", filemode="w", level=logging.INFO, format='%(asctime)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')
old = 0


def inspectFile(filePath):
    logging.info("Inspecting file: " + filePath)
    if "portal" in filePath:
        message = 'An error has occurs in portal, please check!'
    else:
        message = 'An error has occurs in service, please check!'
    for line in reversed(list(open(filePath))):
        is_error = re.findall(r'ERROR', line)
        if bool(is_error):
            message += '\n ' + line
            break
    sendMessage(message)


class Event(LoggingEventHandler):
    def on_modified(self, event):
        global old
        file_stat = os.stat(event.src_path)
        new = file_stat.st_mtime
        print(str(new) + " is new")
        print(str(old) + " is old")
        if (new - old) > 0.5:
            inspectFile(event.src_path)
        old = new


if __name__ == "__main__":
    paths = {'/WMS/logs/service/error/', '/WMS/logs/portal/error/'}
    observer = Observer()
    for path in paths:
        event_handler = Event()
        observer.schedule(event_handler, path, recursive=True)

    observer.start()
    try:
        while True:
            time.sleep(30)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
