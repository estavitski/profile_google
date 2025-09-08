import os
def goto():
    os.chdir('/mnt/c/Documents and Settings/Eli/OneDrive - Brookhaven National Laboratory/___Running projects/ISS operations/2025-2')

def read_letter():
    fil = open('/Users/elistavitski/.ipython/profile_google/letter.html', 'r')
    letter = fil.read().replace('\n', '')
    return letter



'''
Necessary Format
Proposal	PI	Start date	Start time	End date	End time	E-mail	cc


'''



'''
excel_file = '/Users/elistavitski/OneDrive - Brookhaven National Laboratory/___Running projects/ISS operations/2025-2/schedule.xlsx'
schedule = read_excel(excel_file)
letter = read_letter()
cycle = '2025-2'
drafts = create_html_drafts(schedule, cycle, letter)
'''