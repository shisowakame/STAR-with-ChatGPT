# STAR(Summarize Text and Automate Recitatioin)
Notionの記事DBから、記事の内容を要約してAIに読み上げさせた音声ファイルを、GoogleDriveに保存しPodcastとして配信します。  
増える一方のブックマークをpodcastにすることで効率的に消化します。<br>
podcastの詳細欄に元記事のURLを記載し、要約を聞き流して気になるものがあったら詳細から本文にとんで読み進めるといった流れを想定しています。<br>
毎朝定刻に記事を5個配信するスクリプトなどと組み合わせて使用すれば、さらなる機能性が期待できると思います。<br>
<br>
**必要なもの(APIによってはお金がかかります。)**  
・OpenAI-API-key  
・Diffbot-APIトークン  
・GoogleDriveのフォルダID  
・Notion-APIトークン  
・NotionデータベースID  
・token.json(GoogleDriveAPI)  
・credential.json(GoogleDriveAPI)  
<br>まずは必要なモジュールをインストールして下さい。
```
pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib --user
```
以下のコマンドで実行します。

```
python3 main.py
```
<br>

**成果物**<br>英語の文章も日本語で要約してくれます。<br>
https://podcasters.spotify.com/pod/show/shisowakame/episodes/TikTok--e2kftg6
<br>モデルをGPT-3.5-turboにすれば、contextの上限も踏まえて一回の音声ファイル生成にかかる金額は約1.5円です！<br>
安いモデルを使用して多少の読み間違えはこっちで修正する使い方もしやすいようにつくったので、読み上げ文を平仮名にするなどして教えてあげてください。<br>
