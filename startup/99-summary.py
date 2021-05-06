

'''
cd '/Users/elistavitski/Documents/Running Projects/ISS operations/2021-2 Cycle'
fid='2021-2 ISS Schedule list.xlsx'
schedule=read_excel(fid)


fil = open('/Users/elistavitski/Documents/Running Projects/ISS operations/letter COVID.html', 'r')
letter = fil.read().replace('\n', '')

events=create_events(schedule)
for event in events:
    print(event)
    ev = gcalendar_service.events().insert(calendarId='primary', body=event).execute()]



drafts = create_html_drafts(schedule,'2021-2')
for draft in drafts:
    upload_draft(draft)

'''


# In [5]: ev = gcalendar_service.events().insert(calendarId='primary', body=events[0]).execute()
#
# In [6]: ev = gcalendar_service.events().insert(calendarId='primary', body=events[1]).execute()
#
# In [7]: