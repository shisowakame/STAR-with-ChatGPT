# STAR(Summarize Text and Automate Recitatioin)
Notionの記事DBから、記事の内容を要約してAIに読み上げさせた音声ファイルを、GoogleDriveに保存しPodcastとして配信します。  
自分のpodcastでブックマークを消化します。毎朝定刻に記事を5個配信するスクリプトなどと組み合わせて使用する予定  
必要なもの(APIによってはお金がかかります。)  
・OpenAI-API-key  
・Diffbot-APIトークン  
・GoogleDriveのフォルダID  
・Notion-APIトークン  
・NotionデータベースID  
・token.json(GoogleDriveAPI)  
・credential.json(GoogleDriveAPI)  
```
pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib --user
```

成果物は以下のようになります。
