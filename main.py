import requests
import json
from GPT import gpt_request_completion,gpt_summarize, api_key 
from GoogleDrive import upload_audio_file
from TextToSpeech import get_speech_audio_data
#from GetArticle import get_article
from GetRedirect import get_redirect
from Diffbot import get_article_with_Diffbots

folder_id='1Am3cbHuKTu8lAdlXLvwPBx0K_l7cWXQ4' #GoogleDriveフォルダアドレス

url="https://nazology.net/archives/122877" #要約したいURL

redirect_url = get_redirect(url)
#article = get_article(reurl)
#print(text)
title,article = get_article_with_Diffbots(redirect_url)
print(f"タイトル: {title}")
print(f"本文: {article[:8000]}...")  # 本文の最初の8000文字を表示
summary = gpt_summarize(title, article)
#summary = article
contents = get_speech_audio_data(summary)
upload_audio_file(contents)
print(summary)
