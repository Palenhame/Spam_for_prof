import requests
import json


def ask_gpt(messages):
    """Запрос к Yandex GPT"""
    iam_token = ('t1.9euelZqKl4-JmI-Pl4mLicqWyc3Jmu3rnpWanJCVjYzKjpKdlczHjMrJipfl8_dNWXRP-e8QQSM0_t'
                 '3z9w0Ick_57xBBIzT-zef1656'
                 'VmpGMmIyZl5nOx5eUloqPzJac7_zF656VmpGMmIyZl5nOx5eUloqPzJacveuelZqcks'
                 '7NlsaKmc7PiZDIiomXirXehpzRnJCSj4qLmtGLmdKckJKPioua0pKai56bnoue0oye.1dTPmJY3I0Y'
                 'elE0rmLZQRmno41zWd9Pn-hTUaLb14NGZH3DPKeG3x3ZGwfadg6C6Skn0pv7lKOT6Y0UWCWIjBw')

    url = f"https://llm.api.cloud.yandex.net/foundationModels/v1/completion"
    headers = {
        'Authorization': f'Bearer {iam_token}',
        'Content-Type': 'application/json'
    }

    data = {
        "modelUri": f"gpt://b1gnr8vgjubhf0if6ft1/yandexgpt-lite/latest",
        "completionOptions": {
            "stream": False,
            "temperature": 0.7,
            "maxTokens": 100
        },
        "messages":  [
                    {"role": "system", "content": "Отвечай очень кратко"},
                    {"role": "user", "content": messages}
        ]
    }

    try:
        response = requests.post(url, headers=headers, json=data)

    except Exception as e:
        print("Произошла непредвиденная ошибка.", e)

    else:
        if response.status_code != 200:
            print("Ошибка при получении ответа:", response.status_code)
        else:
            with open('response.json', 'w') as f:
                f.write(response.json())
            print(response.json())
            result = response.json()['result']['alternatives'][0]['message']['text']
            return result


print(ask_gpt('Расскажи о себе'))
