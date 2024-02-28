import os.path
import datetime
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaIoBaseUpload
from io import BytesIO

# スコープを設定
SCOPES = ['https://www.googleapis.com/auth/drive']

# フォルダーIDを設定
folder_id = 'DriveFolderID'

def upload_audio_file(file_path, mime_type='audio/mpeg'):
    creds = None
    # トークンファイルが存在するか確認
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    # トークンが無効な場合は更新または新規認証を行う
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "credentials.json", SCOPES)
            creds = flow.run_local_server(port=0)
        with open("token.json", "w") as token_file:
            token_file.write(creds.to_json())

    try:
        service = build("drive", "v3", credentials=creds)

        # ファイル名を現在の日時から生成
        file_name = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '.mp3'

        # ファイルのメタデータを設定
        file_metadata = {
            'name': file_name,
            'parents': [folder_id]
        }

        # メディアアップロードオブジェクトを作成
        media = MediaIoBaseUpload(BytesIO(file_path), mimetype=mime_type)

        # ファイルをアップロード
        file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()

        print(f"File ID: {file.get('id')}")

    except HttpError as error:
        print(f"An error occurred: {error}")
