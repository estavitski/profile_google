import os
import uuid
import pandas as pd
import numpy as np



def create_events(schedule):
    events=[]
    location = 'NSLS II, Brookhaven National Laboratory, Upton, NY, 11973 USA'

    for i in range(len(schedule)):
        d = schedule.iloc[i]
        start='{}T{}'.format(str(d['Start date'])[:10], d['Start time'])
        end = '{}T{}'.format(str(d['End date'])[:10], d['End time'])
        event = {
          'summary': 'NSLS-II ISS Beamtime GUP {}'.format(d['Proposal']),
          'location': location,
          'description': 'NSLS-II ISS Beamtime GUP {}'.format(d['Proposal']),
          'start': {
            'dateTime': start,
            'timeZone': 'America/New_York',
          },
          'end': {
            'dateTime': end,
            'timeZone': 'America/New_York',
          },
          'attendees': [
            {'email': d['E-mail']}
          ],
          'reminders': {
            'useDefault': False,
            'overrides': [
              {'method': 'email', 'minutes': 24 * 60 * 10},
              {'method': 'email', 'minutes': 24 * 60 * 20},
              {'method': 'email', 'minutes': 24 * 60 * 30}
            ],
          },
        }
        print(event)
        events.append(event)

    return(events)
from datetime import datetime

def prettify_date(timestamp):
    return  timestamp.strftime("%A, %B %-d, %Y")


def prettify_time(time_obj):
    return time_obj.strftime("%I:%M %p").lstrip("0")

def create_html_drafts(schedule, cycle, letter):
    drafts = []
    for _, experiment in schedule.iterrows():
        email = experiment['E-mail'].strip()
        start=f"{prettify_date(experiment['Start date'])}, {prettify_time(experiment['Start time'])}"
        end = f"{prettify_date(experiment['End date'])}, {prettify_time(experiment['End time'])}"
        message_body = letter.format(experiment['PI'],experiment['Proposal'],cycle,start,end)
        subject = f"NSLS-II 8-ID ISS {cycle} Beamtime scheduling notification for Proposal {experiment['Proposal']}"
        cc = f"{experiment['cc'].strip()}, istavitski@bnl.gov, atayal@bnl.gov, jmoncadav@bnl.gov"
        draft = create_html_message('staff8id@gmail.com', email, cc, subject,message_body)
        drafts.append(draft)
    return drafts




'''
excel_file = '/Users/elistavitski/OneDrive - Brookhaven National Laboratory/___Running projects/ISS operations/2025-2/schedule.xlsx'
schedule = read_excel(excel_file)
schedule
excel_file = '/Users/elistavitski/OneDrive - Brookhaven National Laboratory/___Running projects/ISS operations/2025-2/schedule.xlsx'
schedule = read_excel(excel_file)
letter = read_let
letter = read_letter()
letter
excel_file = '/Users/elistavitski/OneDrive - Brookhaven National Laboratory/___Running projects/ISS operations/2025-2/schedule.xlsx'
schedule = read_excel(excel_file)
letter = read_letter()
cycle = '2025-3'
drafts =create_html_drafts(schedule, cycle, letter)
drafts
upload_draft(drafts[0])
excel_file = '/Users/elistavitski/OneDrive - Brookhaven National Laboratory/___Running projects/ISS operations/2025-2/schedule.xlsx'
schedule = read_excel(excel_file)
letter = read_letter()
cycle = '2025-3'
drafts =create_html_drafts(schedule, cycle, letter)
%history
In [8]: for draft in drafts:
     upload_draft(draft)
Draft id: r-8178430995140916645
Draft message: {'id': '1991a60b12917889', 'threadId': '1991a60b12917889', 'labelIds': ['DRAFT']}
Out[8]:
{'id': 'r-8178430995140916645',
 'message': {'id': '1991a60b12917889',
  'threadId': '1991a60b12917889',
  'labelIds': ['DRAFT']}}
'''


