
SCOPES = ['https://www.googleapis.com/auth/gmail.modify']

def get_service_gmail():
    system = platform.system()
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token_gmail.pickle'):
        with open('token_gmail.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            system = platform.system()
            if system == "Darwin":
                json_file = '/Users/elistavitski/gmail_secret.json'
            elif system == "Windows":
                json_file = '/mnt/c/Users/Eli/gmail_secret.json'

            flow = InstalledAppFlow.from_client_secrets_file(
                json_file, SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token_gmail.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('gmail', 'v1', credentials=creds)
    print("Gmail connected")
    return service

gmail_service = get_service_gmail()



def create_message(sender, to, subject, message_text):
    message = MIMEText(message_text)
    message['to'] = to
    message['from'] = sender
    message['subject'] = subject
    #return message
    return {'raw': base64.urlsafe_b64encode(message.as_string().encode()).decode()}


def create_html_message(sender, to, cc, subject, message_text):
    message = MIMEText(message_text,'html')
    message['to'] = to
    message['cc'] = cc
    message['from'] = sender
    message['subject'] = subject
    return {'raw': base64.urlsafe_b64encode(message.as_string().encode()).decode()}

def upload_draft(message_body, user_id="me"):
    message = {'message': message_body}
    draft = gmail_service.users().drafts().create(userId=user_id, body=message).execute()
    print( 'Draft id: %s\nDraft message: %s' % (draft['id'], draft['message']))
    return draft