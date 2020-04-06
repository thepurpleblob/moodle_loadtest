import requests
import json
from pprint import pprint

def get_token(host, username, password):
    r = requests.get(host + '/login/token.php?username=' + username + '&password=' + password + '&service=FLT')
    tokens = json.loads(r.text)
    return tokens['token']

def core_course_get_course_module(host, token, cmid):
    pd = {
        'wstoken': token,
        'wsfunction': 'core_course_get_course_module',
        'moodlewsrestformat': 'json',
        'cmid': cmid
    }
    r = requests.post(host + '/webservice/rest/server.php', data = pd)
    response = json.loads(r.text)
    cm = response['cm']
    if (cm['modname'] != 'assign'):
        print('cmid is not an assignment')
        exit()
    instance = cm['instance']
    return instance

def webservice_upload(host, token):
    pd = {
        'token': token,
    }
    files = {'file': open('testfile.pdf', 'rb')}
    r = requests.post(host + '/webservice/upload.php', data = pd, files = files)
    response = json.loads(r.text)
    return response[0]

def mod_assign_save_submission(host, token, assignid, files_filemanager):
    pd = {
        'wstoken': token,
        'wsfunction': 'mod_assign_save_submission',
        'moodlewsrestformat': 'json',
        'assignmentid': assignid,
        'plugindata[files_filemanager]': files_filemanager
    } 
    r = requests.post(host + '/webservice/rest/server.php', data = pd)
    response = json.loads(r.text)
    return  

def mod_assign_view_submission_status(host, token, assignid):
    pd = {
        'wstoken': token,
        'wsfunction': 'mod_assign_view_submission_status',
        'moodlewsrestformat': 'json',
        'assignid': assignid
    }
    r = requests.post(host + '/webservice/rest/server.php', data = pd)
    response = json.loads(r.text)
    pprint(response)

def mod_assign_get_submission_status(host, token, assignid):
    pd = {
        'wstoken': token,
        'wsfunction': 'mod_assign_get_submission_status',
        'moodlewsrestformat': 'json',
        'assignid': assignid
    }
    r = requests.post(host + '/webservice/rest/server.php', data = pd)
    response = json.loads(r.text)
    lastattempt = response['lastattempt']
    return lastattempt
