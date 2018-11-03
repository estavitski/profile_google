# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/gmail-python-quickstart.json


from email.mime.text import MIMEText
import base64

SCOPES = 'https://www.googleapis.com/auth/gmail.modify'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Gmail API Python Quickstart'



def get_credentials_gmail():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'gmail-python-quickstart.json')

    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials



credentials = get_credentials_gmail()
http = credentials.authorize(httplib2.Http())
gmail_service = discovery.build('gmail', 'v1', http=http)



def create_message(sender, to, subject, message_text):
    message = MIMEText(message_text)
    message['to'] = to
    message['from'] = sender
    message['subject'] = subject
    #return message
    return {'raw': base64.urlsafe_b64encode(message.as_string().encode()).decode()}


def create_html_message(sender, to, subject, message_text):
    message = MIMEText(message_text,'html')
    message['to'] = to
    message['from'] = sender
    message['subject'] = subject
    #return message
    return {'raw': base64.urlsafe_b64encode(message.as_string().encode()).decode()}

def upload_draft(message_body, user_id="me"):
    message = {'message': message_body}
    draft = gmail_service.users().drafts().create(userId=user_id, body=message).execute()
    print( 'Draft id: %s\nDraft message: %s' % (draft['id'], draft['message']))
    return draft