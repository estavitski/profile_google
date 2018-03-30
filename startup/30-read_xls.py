import os
import uuid
import pandas as pd
import numpy as np



def read_excel(fname):
    return pd.read_excel(fname)

def create_events(schedule):
    events=[]
    location = 'NSLS II, Brookhaven National Laboratory, Upton, NY, 11973 USA'

    for i in range(len(schedule)):
        d = schedule.iloc[i]
        start='{}T{}'.format(str(d['Start date'])[:10], d['Start time'])
        end = '{}T{}'.format(str(d['End date'])[:10], d['End time'])
        event = {
          'summary': 'NSLS-II ISS Beamtime GUP Proposal {}'.format(d['Proposal']),
          'location': location,
          'description': 'NSLS-II ISS Beamtime GUP Proposal {}'.format(d['Proposal']),
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


# In [1]: cd '/Users/elistavitski/Documents/Running Projects /ISS operations/2018-2 Cycle'
# /Users/elistavitski/Documents/Running Projects /ISS operations/2018-2 Cycle
#
# In [2]: fid='2018 2 ISS schedule list.xlsx'
#
# In [3]: a=read_excel(fid)
#
# In [4]: events=create_events(a)
# {'summary': 'NSLS-II ISS Beamtime GUP Proposal 303179', 'location': 'NSLS II, Brookhaven National Laboratory, Upton, NY, 11973 USA', 'description': 'NSLS-II ISS Beamtime GUP Proposal 303179', 'start': {'dateTime': '2018-06-05T08:00:00', 'timeZone': 'America/New_York'}, 'end': {'dateTime': '2018-06-07T08:00:00', 'timeZone': 'America/New_York'}, 'attendees': [{'email': 'qjia@hawk.iit.edu'}], 'reminders': {'useDefault': False, 'overrides': [{'method': 'email', 'minutes': 14400}, {'method': 'email', 'minutes': 28800}, {'method': 'email', 'minutes': 43200}]}}
# {'summary': 'NSLS-II ISS Beamtime GUP Proposal 302325', 'location': 'NSLS II, Brookhaven National Laboratory, Upton, NY, 11973 USA', 'description': 'NSLS-II ISS Beamtime GUP Proposal 302325', 'start': {'dateTime': '2018-06-08T12:00:00', 'timeZone': 'America/New_York'}, 'end': {'dateTime': '2018-06-09T12:00:00', 'timeZone': 'America/New_York'}, 'attendees': [{'email': 'smbak@bnl.gov'}], 'reminders': {'useDefault': False, 'overrides': [{'method': 'email', 'minutes': 14400}, {'method': 'email', 'minutes': 28800}, {'method': 'email', 'minutes': 43200}]}}
#
# In [5]: ev = serviceCalendar.events().insert(calendarId='primary', body=events[0]).execute()
#
# In [6]: ev = serviceCalendar.events().insert(calendarId='primary', body=events[1]).execute()
#
# In [7]: