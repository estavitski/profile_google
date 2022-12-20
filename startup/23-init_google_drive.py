# SCOPES = ['https://www.googleapis.com/auth/drive']
#
# def get_service_drive():
#     creds = None
#     # The file token.pickle stores the user's access and refresh tokens, and is
#     # created automatically when the authorization flow completes for the first
#     # time.
#     if os.path.exists('token_gdrive.pickle'):
#         with open('token_gdrive.pickle', 'rb') as token:
#             creds = pickle.load(token)
#     # If there are no (valid) credentials available, let the user log in.
#     if not creds or not creds.valid:
#         if creds and creds.expired and creds.refresh_token:
#             creds.refresh(Request())
#         else:
#             flow = InstalledAppFlow.from_client_secrets_file(
#                 '/mnt/c/Users/Eli/gdrive_secret.json', SCOPES)
#             creds = flow.run_local_server(port=0)
#         # Save the credentials for the next run
#         with open('token_gdrive.pickle', 'wb') as token:
#             pickle.dump(creds, token)
#
#     service = build('drive', 'v3', credentials=creds)
#     print("Google Drive connected")
#     return service
#
# drive_service = get_service_drive()
#
# def gd_retrieve_files_from_folder(parent = ''):
#     _q = "mimeType != 'application/vnd.google-apps.file' and '{}' in parents".format(parent)
#     page_token = None
#     files = list()
#     while True:
#         results = drive_service.files().list(pageSize=100, q=_q, fields="nextPageToken, files(id, name)",
#                                          pageToken=page_token).execute()
#         page_token = results.get('nextPageToken', None)
#         items = results.get('files', [])
#         for item in items:
#             files.append(item)
#         if page_token is None:
#             break
#     return files
#
#
# def gd_folder_exists_in_root(folder_name = ''):
#     fid = 0
#     if folder_name:
#         results = drive_service.files().list(
#             pageSize=100, q=("mimeType = 'application/vnd.google-apps.folder' and 'root' in parents"),
#             fields="nextPageToken, files(id, name)").execute()
#         items = results.get('files',[])
#         for item in items:
#             if item['name'] == folder_name:
#                 fid = item['id']
#     return fid
#
#
#
# def current_folder():
#     #folder_name = '{}.{}.{}'.format(RE.md['year'], RE.md['cycle'], RE.md['proposal'])
#     working_folder = '2018.1.300000'
#
#
# def gd_create_folder(folder_name = ''):
#     if folder_name:
#         file_metadata = {
#             'name': folder_name,
#             'mimeType': 'application/vnd.google-apps.folder'
#         }
#
#         file = drive_service.files().create(body=file_metadata, fields='id').execute()
#         fid = file.get('id')
#         return fid
#
#
# def gd_upload_file_to_folder(folder_id = '', file_name='', from_local_file=''):
#     file_metadata = {
#         'name': file_name,
#         'parents': [folder_id]
#     }
#     media = MediaFileUpload(from_local_file,
#                             mimetype='text/html')
#
#     return drive_service.files().create(body=file_metadata, media_body=media).execute()
#
#
#
# def search_in_list(name, files):
#     return [item for item in files if item['name'] == name]
