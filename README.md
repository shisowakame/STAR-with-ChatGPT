# STAR(Summarize Text and Automate Recitatioin)
Notionの記事DBから、記事の内容を要約してAIに読み上げさせた音声ファイルを、GoogleDriveに保存しPodcastとして配信します。  
増える一方のブックマークをpodcastにすることで効率的に消化します。<br>
毎朝定刻に記事を5個配信するスクリプトなどと組み合わせて使用すれば、さらなる機能性が期待できると思います。 <br> 
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
**成果物**
