import ast
import json
import requests

def g_drive_upload(file2upload):
    headers = {
        "Authorization": "Bearer ya29.a0AfH6SMDdhcPVuOh0QeNQfHStgxT0B42wfPKQTjwDLL8gJA5WkYMIaspSd7nxhkoy0H1jUWq-xjDDfSFS0yuRYFEfwgMttryaQCa6kuuqxzIuDIwthc7WptAq0oHIbdLLPI_CbRpqP1LABA0Sky9dCJOk9A6d"}
    para = {
        # "name": "sampleI.txt",
        "name": f"{file2upload}",
    }
    files = {
        'data': ('metadata', json.dumps(para), 'application/json; charset=UTF-8'),
        'file': open(f"{file2upload}", "rb")
    }
    r = requests.post(
        "https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart",
        headers=headers,
        files=files
    )
    # print(r.text)
    g_dict = ast.literal_eval(r.text)
    # print(g_dict)
    # print(f'https://drive.google.com/file/d/{g_dict["id"]}')
    gDrive_link = f'https://drive.google.com/file/d/{g_dict["id"]}'
    return gDrive_link