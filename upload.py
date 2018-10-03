import googleapiclient.discovery
import httplib2
import oauth2client.file

import os
import sys

def upload(path):
    store = oauth2client.file.Storage(os.path.expanduser('~/google_drive_token.json'))
    creds = store.get()
    service = googleapiclient.discovery.build('drive', 'v3', http=creds.authorize(httplib2.Http()))
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