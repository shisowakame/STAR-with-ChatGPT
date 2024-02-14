import requests
import json

def get_article_with_Diffbots(target_url):
    api_url = "https://api.diffbot.com/v3/analyze"
    #target_url = "http://nazology.net/archives/145043"  # 解析対象の URL
    token = "e7e6672af6419c2fe9a35e11503113f1"  # Diffbot API トークン

    url = f"{api_url}?token={token}&url={target_url}"

    headers = {"Accept": "application/json"}

    # API リクエストを送信し、レスポンスを取得
    response = requests.get(url, headers=headers)

    # レスポンスの内容を表示
    #print(response.text)

    # レスポンスの JSON データを辞書として取得
    data = response.json()
    """
    # レスポンスを JSON ファイルとして保存
    file_name = "response.json"  # 保存するファイル名
    with open(file_name, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    print(f"レスポンスが {file_name} として保存されました。")
    # JSON文字列をPythonの辞書に変換
    json_data = '''    '''
    data = json.loads(json_data)
    """
    # titleとtextの値を取得
    title = data['title']
    text = data['objects'][0]['text']

    #print(f"タイトル: {title}")
    #print(f"本文: {text[:8000]}...")  # 本文の最初の8000文字を表示
    return title,text

if __name__ == "__main__":
    target_url = "http://nazology.net/archives/145043"
    title,text = get_article_with_Diffbots(target_url)
    print(f"タイトル: {title}")
    print(f"本文: {text[:8000]}...")  # 本文の最初の8000文字を表示