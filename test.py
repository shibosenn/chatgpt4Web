import requests
import json
import openai

def new2_chat2gpt4(prompt):
    url = "https://openkey.cloud/v1/chat/completions"
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer sk-91OdInYu1FVFaOjIlZhp0gI1i7jkpaduiEvsKAtqOsQLctlB'
    }

    data = {
        "model": "gpt-3",
        "messages": [{"role": "user", "content": prompt}],

    }
    response = requests.post(url, headers=headers, json=data)  # ['choices'][0]['message']['content']
    # return response.json()['choices'][0]['message']['content']
    return response




def chat2gpt35_2(messages):
    openai.api_type = "azure"
    openai.api_base = "https://dptech.openai.azure.com/"
    openai.api_version = "2023-03-15-preview"
    openai.api_key = "2a2fbcf82115400e87d94056fecd91bd"
    gpt_name = "gpt-35"

    messages_dict = {"role": "user", "content": messages}

    answer = openai.ChatCompletion.create(
        engine=gpt_name,
        messages=[messages_dict],
        temperature=0.8,
        top_p=0.95
    )['choices'][0]['message']['content']
    return answer

if __name__ == "__main__":
    # print(new2_chat2gpt4("hello, can you hear me"))
    print(chat2gpt35_2("nihao"))