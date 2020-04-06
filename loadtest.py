import ws
import logging
import threading
import time
import concurrent.futures
from pprint import pprint

HOSTNAME = 'http://ubuntu.local/moodle37'
CMID = 89
BASEUSER = 'ftestuser'
PASSWORD = 'orange'



def doit(index):
    username = BASEUSER + str(index)
    print('Starting user ', username)

    token = ws.get_token(HOSTNAME, username, PASSWORD)
    instance = ws.core_course_get_course_module(HOSTNAME, token, CMID)
    filerecord = ws.webservice_upload(HOSTNAME, token)
    itemid = filerecord['itemid']
    ws.mod_assign_save_submission(HOSTNAME, token, instance, itemid)

    print('Completed user ', username)


with concurrent.futures.ThreadPoolExecutor(max_workers = 100) as executor:
    executor.map(doit, range(2, 450))