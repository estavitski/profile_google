def push_schedule(filename=None, no_email=False, no_cal=False):
    if filename is None:
        filename = '/Users/elistavitski/Documents/Running Projects /ISS operations/2018-2 Cycle/2018 2 ISS schedule list.xlsx'
    schedule = read_excel(filename)
    drafts = create_html_drafts(schedule)
    events = create_events(schedule)
    if not no_email:
        for draft in drafts:
            upload_draft(draft)
    if not no_cal:
        for event in events:
            cal=gcalendar_service.events().insert(calendarId='primary', body=event).execute()
            print(cal)


# In [5]: ev = gcalendar_service.events().insert(calendarId='primary', body=events[0]).execute()
#
# In [6]: ev = gcalendar_service.events().insert(calendarId='primary', body=events[1]).execute()
#
# In [7]: