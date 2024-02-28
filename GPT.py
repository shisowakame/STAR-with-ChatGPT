import requests
import json

# 環境変数からAPIキーを取得するために追加
api_key = 'OpenAI-secret-key'

def gpt_request_completion(messages):
    api_url = 'https://api.openai.com/v1/chat/completions'
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }
    payload = {
        'model': 'gpt-3.5-turbo-0125',
        'messages': messages
    }

    response = requests.post(api_url, headers=headers, json=payload)
    if response.status_code == 200:
        try:
            response_data = response.json()
            if 'choices' in response_data and len(response_data['choices']) > 0:
                # 'text' から 'message' オブジェクトの 'content' に修正
                return response_data['choices'][0]['message']['content']
            else:
                return {'error': 'No choices found in the response.'}
        except Exception as error:
            print(f"Error processing the response: {error}")
            return {'error': str(error)}
    else:
        return {'error': f"API request failed with status code {response.status_code}: {response.text}"}

    api_url = 'https://api.openai.com/v1/chat/completions'
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }
    payload = {
        'model': 'gpt-3.5-turbo',
        'messages': messages
    }

    response = requests.post(api_url, headers=headers, json=payload)
    if response.status_code == 200:
        try:
            response_data = response.json()
            if 'choices' in response_data and len(response_data['choices']) > 0:
                # 応答からテキストを取得する修正
                return response_data['choices'][0]['text']
            else:
                return {'error': 'No choices found in the response.'}
        except Exception as error:
            print(f"Error processing the response: {error}")
            return {'error': str(error)}
    else:
        return {'error': f"API request failed with status code {response.status_code}: {response.text}"}

def gpt_summarize(title, article):
    system_prompt = (
        "与えられた文章の要約を,800字のですます調の日本語で出力してください。 \n"
        "レスポンスは必ず以下のJSONフォーマットで返します。\n"
        "{'title':'記事のタイトルの日本語訳', 'summary':'記事の要約'}"
    )
    user_prompt = f"title: {title}\nbody: {article[:14500]}"

    response = gpt_request_completion([
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ])
    return response

if __name__ == "__main__": 
    title = 'How To Avoid Burnout as a Designer'
    article = '''As a seasoned designer, I have had my fair share of burnouts over the years. I know firsthand how exhausting and demotivating it can be to constantly push yourself to meet deadlines and exceed client expectations. Burnout is a very real problem in the creative industry and it can happen to anyone, regardless of experience level.

    In this article, I will share my personal experiences with burnout and offer some advice on how to avoid it.

    Firstly, it’s important to understand what burnout is and how it can manifest. Burnout is a state of emotional, physical, and mental exhaustion caused by prolonged periods of stress. As a designer, you may experience burnout when you have to deal with tight deadlines, demanding clients, and repetitive tasks for a prolonged period. The warning signs of burnout can vary from person to person, but some of the most common ones include:

    Feeling emotionally drained and unable to cope with stress.
    Lack of motivation and interest in your work.
    Difficulty sleeping or staying focused.
    Chronic fatigue or physical exhaustion.
    Physical and emotional detachment from colleagues and clients.
    Increased irritability and short temper.
    Decreased productivity and creativity.
    If you notice any of these symptoms, it’s important to take action and address them before they worsen.

    Here are some tips on how to avoid burnout as a designer:

    1. Set realistic goals and manage expectations
    One of the main causes of burnout is the pressure to meet unrealistic goals and expectations. To avoid this, make sure you set achievable goals and communicate clearly with your clients and colleagues. If you are feeling overwhelmed, it’s important to speak up and ask for help. This can mean delegating tasks, pushing back on unrealistic deadlines, or re-negotiating the scope of a project.

    Something I found extremely useful in the past is to buddy up with somebody at work. Have weekly or bi-weekly check-ins with them. Talk about how you feel. Ideally, this would be someone who does not work directly with you or within the same project. Since it’s very useful to have an external point of view. The buddy should listen to the situation, and give advice. Knowing that sometimes having a rant is also all the other person would like to do. Externalising your emotions may be good enough to save you from stress.

    2. Take breaks and prioritize self-care
    Design work can be intense and demanding, but it’s important to take regular breaks and prioritize self-care. This means taking time to rest, exercise, and engage in activities that you enjoy outside of work. Try to establish a healthy work-life balance that allows you to recharge your batteries and prevent burnout.'''

    summary = gpt_summarize(title, article)
    print(summary)
