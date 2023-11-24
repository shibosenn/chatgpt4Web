from flask import Flask
from flask import render_template
from flask import Flask, render_template, request, jsonify
import requests
import openai

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

app = Flask(__name__, template_folder='../templates/', static_folder='../static/')

@app.route('/')
def home():
    
    return render_template('index.html')

@app.route('/api/chat/', methods=['POST'])
def chat():
    # user_message = request.get_json()['message']  # 获取用户消息
    # # gpt4_response = new2_chat2gpt4(user_message)  # 将用户消息传给new2_chat2gpt4函数
    # gpt35_response = chat2gpt35_2('message')
    # # return gpt4_response  # 返回GPT-4的响应
    # return gpt35_response
    return "hello"

if __name__ == "__main__":
    app.run(port=5000)
