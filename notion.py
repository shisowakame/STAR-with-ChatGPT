import os
from pprint import pprint
from notion_client import Client


def fetch_unread_items_with_url(database_id, NOTION_TOKEN):
    notion = Client(auth=NOTION_TOKEN)
    db = notion.databases.query(database_id=database_id)
    
    unread_items_with_url_and_id = []
    
    for result in db['results']:
        properties = result['properties']
        page_id = result['id']
        
        # '記事名' と 'URL' プロパティが存在し、かつ 'read' チェックボックスが未読の場合のみ処理
        if ('記事名' in properties and len(properties['記事名']['title']) > 0 and
            'URL' in properties and properties['URL']['url'] is not None and
            properties['URL']['url'] != "" and  # URLが空でないことを確認
            'read' in properties and not properties['read']['checkbox']):
            
            name = properties['記事名']['title'][0]['text']['content']
            url = properties['URL']['url']
            
            # URLが存在する場合のみ項目をリストに追加
            unread_items_with_url_and_id.append({
                'id': page_id,
                'title': name,
                'url': url
            })
            
            # 最大5つの未読項目をリストに追加
            if len(unread_items_with_url_and_id) == 1:
                break
    
    return unread_items_with_url_and_id

def mark_items_as_read(database_id, NOTION_TOKEN, items):
    notion = Client(auth=NOTION_TOKEN)
    
    for item in items:
        page_id = item['id']
        notion.pages.update(
            page_id=page_id,
            properties={
                'read': {
                    'checkbox': True
                }
            }
        )
if __name__ == "__main__":
    database_id = 'Notion_database'
    NOTION_TOKEN = "Notion_token"
    
    # 未読項目の取得と表示
    unread_items_with_ids = fetch_unread_items_with_url(database_id, NOTION_TOKEN)
    print("未読項目（更新前）:")
    for item in unread_items_with_ids:
        print(f'Title: {item["title"]}, URL: {item["url"]}')
    
    # 未読項目を既読に更新
    mark_items_as_read(database_id, NOTION_TOKEN, unread_items_with_ids)
    
    print("更新後の項目を既読にしました。")
