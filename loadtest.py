import ws
import logging
import threading
import time
from datetime import datetime
import concurrent.futures
from pprint import pprint

HOSTNAME = 'http://ubuntu.local/moodle37'
CMID = 89
BASEUSER = 'ftestuser'
PASSWORD = 'orange'
MAXWORKERS = 25

def printtime(message):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(message, current_time)

def doit(index):
    username = BASEUSER + str(index)
    print('Starting user ', username)

    token = ws.get_token(HOSTNAME, username, PASSWORD)
    instance = ws.core_course_get_course_module(HOSTNAME, token, CMID)
    filerecord = ws.webservice_upload(HOSTNAME, token)
    itemid = filerecord['itemid']
    ws.mod_assign_save_submission(HOSTNAME, token, instance, itemid)

    print('Completed user ', username)


printtime('Start time')
with concurrent.futures.ThreadPoolExecutor(max_workers = MAXWORKERS) as executor:
    executor.map(doit, range(2, 450))

printtime('End time')