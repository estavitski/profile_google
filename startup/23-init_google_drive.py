


SCOPES = 'https://www.googleapis.com/auth/drive'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Drive API Python Quickstart'



def get_credentials_drive():
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
                                   'drive-python-quickstart.json')

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



credentials = get_credentials_drive()
http = credentials.authorize(httplib2.Http())
drive_service = discovery.build('drive', 'v3', http=http)


def gd_retrieve_files_from_folder(parent = ''):
    _q = "mimeType != 'application/vnd.google-apps.folder' and '{}' in parents".format(parent)
    page_token = None
    files = list()
    while True:
        results = drive_service.files().list(pageSize=100, q=_q, fields="nextPageToken, files(id, name)",
                                         pageToken=page_token).execute()
        page_token = results.get('nextPageToken', None)
        items = results.get('files', [])
        for item in items:
            files.append(item)
        if page_token is None:
            break
    return files




def gd_folder_exists_in_root(folder_name = ''):
    fid = 0
    if folder_name:
        results = drive_service.files().list(
            pageSize=100, q=("mimeType = 'application/vnd.google-apps.folder' and 'root' in parents"),
            fields="nextPageToken, files(id, name)").execute()
        items = results.get('files',[])
        for item in items:
            if item['name'] == folder_name:
                fid = item['id']
    return fid


'''
      param = {}
      param['q'] = "mimeType = 'application/vnd.google-apps.folder'"
      if page_token:
          param['pageToken'] = page_toke
      children = drive_service.children().list(folderId, **param).execute()

      for child in children.get('items', []):
        print ('File Id: %s' % child['id'])
      page_token = children.get('nextPageToken')
      if not page_token:
        break

'''

def current_folder():
    #folder_name = '{}.{}.{}'.format(RE.md['year'], RE.md['cycle'], RE.md['proposal'])
    working_folder = '2018.1.300000'


def gd_create_folder(folder_name = ''):
    if folder_name:
        file_metadata = {
            'name': folder_name,
            'mimeType': 'application/vnd.google-apps.folder'
        }

        file = drive_service.files().create(body=file_metadata, fields='id').execute()
        fid = file.get('id')
        return fid



