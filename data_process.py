# -*- coding: utf-8 -*-
# @Time    : 2023/12/22 
# @Author  : lkj
# @description :
import json
import pandas as pd

data_path = 'riddle'
df = pd.read_json(f'{data_path}/original.json', lines=True, encoding='utf-8')
df = df.rename(columns={'question': 'user', 'answer': 'assistant'})
print(df.tail())
chat_input = df["user"].tolist()
chat_output = df["assistant"].tolist()

all_chat = []
for i in range(len(chat_input)):
    user = str(chat_input[i])
    assistant = str(chat_output[i])
    conversations = [{"from": "user", "value": user}, {"from": "assistant", "value": assistant}]
    chat_id = "identity_" + str(i)
    chat = {"id": chat_id, "conversations": conversations}
    all_chat.append(chat)

# 指定要保存的文件路径
file_path = f'{data_path}/chat.json'

# 将数据导出到 JSON 文件，并确保导出后仍包含中文
with open(file_path, 'w', encoding='utf-8') as json_file:
    json.dump(all_chat, json_file, ensure_ascii=False,indent=4)
