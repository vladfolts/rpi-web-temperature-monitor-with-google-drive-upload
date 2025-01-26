import os
import sys

import googleapiclient.discovery
from google.oauth2.credentials import Credentials


def upload(path):
    token_file = os.path.expanduser("~/google_drive_token.json")
    creds = Credentials.from_authorized_user_file(token_file)
    service = googleapiclient.discovery.build('drive', 'v3', credentials=creds)
    files = service.files()
    
    file_name = os.path.basename(path)
    
    kwargs = {'body': {'name': file_name}, 
              'media_body': path, 
              'media_mime_type': 'application/octet-stream'
             }
    matching_files = files.list(q='name=\'%s\'' % file_name).execute()['files']
    if len(matching_files) == 0:
        create_or_update = files.create
    else:
        kwargs['fileId'] = matching_files[0]['id']
        create_or_update = files.update

    create_or_update(**kwargs).execute()


if __name__ == '__main__':
    upload(sys.argv[1])