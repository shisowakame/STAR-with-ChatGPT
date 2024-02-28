import requests
import json
from GPT import gpt_request_completion,gpt_summarize, api_key 
from GoogleDrive import upload_audio_file
from TextToSpeech import get_speech_audio_data
#from GetArticle import get_article
from GetRedirect import get_redirect
from Diffbot import get_article_with_Diffbots
from notion import fetch_unread_items_with_url, mark_items_as_read

folder_id='DrivefolderID' #GoogleDriveフォルダアドレス
database_id = 'Notion_databaseID' #Notionの読み上げたい記事が入っているデータベース
NOTION_TOKEN ="Notion_token" #Notionの内部インテグレーションシークレット

#url="https://target/URL" #要約したいURL
unread_items = fetch_unread_items_with_url(database_id, NOTION_TOKEN)
#print("未読項目（更新前）:")

for items in unread_items:
    # 未読項目の取得と表示
    #unread_items_with_ids = fetch_unread_items_with_url(database_id, NOTION_TOKEN)
    

    title = items['title']
    url = items['url']
    print(f'Title: {title}, URL: {url}')
    redirect_url = get_redirect(url)
    #article = get_article(reurl)
    #print(text)
    title,article = get_article_with_Diffbots(redirect_url)
    print(f"タイトル: {title}")
    print(f"本文: {article[:14500]}...")  # 本文の最初の14500文字を表示
    summary = gpt_summarize(title, article)
    #summary = article
    contents = get_speech_audio_data(summary)
    upload_audio_file(contents)
    print(summary)

# 未読項目を既読に更新するコードはこのままで問題ありません
mark_items_as_read(database_id, NOTION_TOKEN, unread_items)

#print("更新後の項目を既読にしました。")
