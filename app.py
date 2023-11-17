from flask import Flask
from flask import render_template
from flask import Flask, render_template, request, jsonify
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

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.get_json()['message']  # 获取用户消息
    gpt4_response = new2_chat2gpt4(user_message)  # 将用户消息传给new2_chat2gpt4函数
    return gpt4_response  # 返回GPT-4的响应

if __name__ == "__main__":
    app.run(port=5000)
