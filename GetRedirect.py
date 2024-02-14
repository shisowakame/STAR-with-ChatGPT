import requests
import re

def get_redirect(url):
    print(['getRedirect', url])
    try:
        response = requests.get(url, allow_redirects=False)
        # HTTPステータスコードを取得
        response_code = response.status_code

        if 300 <= response_code < 400:
            # レスポンスヘッダーからリダイレクトURLを取得
            redirect_url = response.headers.get('Location')
            if redirect_url and redirect_url != url:
                # リダイレクトがあれば再帰的に処理
                return get_redirect(redirect_url)
            else:
                return url
        else:
            return url
    except requests.RequestException as e:
        print(e)
        return None
