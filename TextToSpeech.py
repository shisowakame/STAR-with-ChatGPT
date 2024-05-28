import requests
import pathlib
from GoogleDrive import upload_audio_file 

gpt_api_key = 'OpenAI-secret-key'

def get_speech_audio_data(text):
    api_url = 'https://api.openai.com/v1/audio/speech'
    headers = {
        'Authorization': 'Bearer ' + gpt_api_key,
        'Content-Type': 'application/json',
    }

    payload = {
        'model': 'tts-1-hd',
        'voice': 'alloy',
        'input': text,
        'response_format': 'mp3',
        'speed': 1.2
    }

    try:
        response = requests.post(api_url, headers=headers, json=payload)
        # 成功した場合、レスポンスのバイナリコンテンツを返す
        if response.status_code == 200:
            return response.content  # MP3データのバイナリ
            """ローカルへの保存テスト
            if response.content:
                # 音声データをファイルに保存
                with open('output.mp3', 'wb') as audio_file:
                    audio_file.write(response.content)
                print('音声データをoutput.mp3に保存しました。')
            else:
                print('音声データの取得に失敗しました。')
            """
        else:
            # ステータスコードが200以外の場合は、エラーメッセージをログに出力
            print(f'Error: {response.status_code}, Message: {response.text}')
            return None
    except Exception as error:
        print(f'Exception: {error}')
        return None

if __name__ == "__main__":
    # 使用例
    text = '変換したいテキスト'
    audio_data = get_speech_audio_data(text)
    if audio_data:
        # 音声データをファイルに保存
        with open('output.mp3', 'wb') as audio_file:
            audio_file.write(audio_data)
        print('音声データをoutput.mp3に保存しました。')
        upload_audio_file(audio_data)
    else:
        print('音声データの取得に失敗しました。')

