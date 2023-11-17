import requests

def new2_chat2gpt4(prompt):
    url = "https://openkey.cloud/v1/chat/completions"
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer sk-91OdInYu1FVFaOjIlZhp0gI1i7jkpaduiEvsKAtqOsQLctlB'
    }

    data = {
        "model": "gpt-4-0613",
        "messages": [{"role": "user", "content": prompt}],

    }
    response = requests.post(url, headers=headers, json=data)  # ['choices'][0]['message']['content']
    return response.json()['choices'][0]['message']['content']

if __name__ == "__main__":
    print(new2_chat2gpt4("hello, can you hear me"))