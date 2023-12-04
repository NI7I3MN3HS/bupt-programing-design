# 导入正确的模块
from openai import OpenAI

# 设置您的 OpenAI API 密钥
api_key = "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"

# 实例化 OpenAI 客户端
client = OpenAI(api_key=api_key)

def get_english(text):
    # 定义对话
    conversation = [
        {"role": "system", "content": "You will be provided with a sentence in English, and your task is to translate it into Chinese."},
        {"role": "user", "content": "My name is Jane. What is yours?"},
        {"role": "assistant", "content": "我的名字是简。你的呢？"},
        {"role": "user", "content": text},
    ]

    # 调用 ChatGPT API
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=conversation,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    # 提取助手的回复
    assistant_reply = response.choices[0].message.content

    return assistant_reply

def get_chinese(text):
    # 定义对话
    conversation = [
        {"role": "system", "content": "You will be provided with a sentence in Chinese, and your task is to translate it into English."},
        {"role": "user", "content": "我的名字是简。你的呢？"},
        {"role": "assistant", "content": "My name is Jane. What is yours?"},
        {"role": "user", "content": text},
    ]

    # 调用 ChatGPT API
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=conversation,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    # 提取助手的回复
    assistant_reply = response.choices[0].message.content

    return assistant_reply


'''
text = "Hello"

# 定义对话
conversation = [
    {"role": "system", "content": "You will be provided with a sentence in English, and your task is to translate it into Chinese."},
    {"role": "user", "content": text},
]

# 调用 ChatGPT API
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=conversation,
    temperature=0.7,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
)

# 提取助手的回复
assistant_reply = response.choices[0].message.content

print(assistant_reply)
'''
