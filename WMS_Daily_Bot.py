#!/opt/rh/rh-python36/root/usr/bin/python3
import datetime
import shutil
import WMSDao
from TelegramUtils import sendMessage


def initReportMessage():
    message_header = 'Daily report on: ' + str(datetime.datetime.now()) + '\n'
    part1 = 'Total of import trans: ' + str(WMSDao.getTotalTransByType(1)) + '\n'
    part2 = 'Total of export trans: ' + str(WMSDao.getTotalTransByType(2)) + '\n'
    part3 = WMSDao.getTotalTransByCusMessage()

    return message_header + part1 + part2 + part3


def initSystemInfoMessage():
    total, used, free = shutil.disk_usage("/")
    message = 'System information:\n'
    message += "Total: " + str((total // (2 ** 30))) + "GiB" + '\n'
    message += "Used: " + str((used // (2 ** 30))) + "GiB" + '\n'
    message += "Free: " + str((free // (2 ** 30))) + "GiB" + '\n'
    return message


sendMessage(initSystemInfoMessage())
sendMessage(initReportMessage())
