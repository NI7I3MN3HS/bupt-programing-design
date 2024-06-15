# 导入正确的模块
from openai import OpenAI

# 设置您的 OpenAI API 密钥
api_key = "sk-a8hPyfbHzmCNpRIk6894D0Fb64Fc4299A0C87eBe56F7606f"

# 实例化 OpenAI 客户端
client = OpenAI(api_key=api_key,base_url="https://apikeyplus.com/v1")

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

def academic_paper_refinement(text):
    # 定义对话上下文，说明需要翻译和润色学术论文
    conversation = [
        {"role": "system", "content": "You are provided with a sentence from an academic paper in Chinese. Your task is to translate it into English and polish it."},
        {"role": "user", "content": text}  # 这里是需要翻译和润色的中文文本
    ]

    # 调用 ChatGPT API 进行翻译和润色
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=conversation,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    # 提取助手的回复，这将包含翻译和润色建议
    assistant_reply = response.choices[0].message.content

    return assistant_reply

def writing_guidance_and_refinement(text):
    # 定义对话上下文，请求写作指导和润色
    conversation = [
        {"role": "system", "content": "You are provided with a piece of writing. Your task is to provide suggestions for vocabulary enhancement, sentence structure optimization, and overall composition improvement."},
        {"role": "user", "content": text}  # 这里是需要润色的文本
    ]

    # 调用 ChatGPT API 获取写作指导和润色建议
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=conversation,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    # 提取助手的回复，这将包含写作指导和润色建议
    assistant_reply = response.choices[0].message.content

    return assistant_reply

def generate_sentences(word):
    # 定义对话上下文，请求生成基于特定单词的例句
    conversation = [
        {"role": "system", "content": "You are provided with a word. Your task is to generate sentences that use the word in context to help with memorization."},
        {"role": "user", "content": word}  # 这里是需要生成例句的单词
    ]

    # 调用 ChatGPT API 获取基于单词的例句
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=conversation,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    # 提取助手的回复，这将包含生成的例句
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

