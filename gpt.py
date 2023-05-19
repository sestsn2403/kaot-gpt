import openai
import os
import sys

from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.environ["api_keyopenai"]

data = [
        {"role": "user", "content": "{}".format(sys.argv[1])}]

datat = ""


res = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
        {"role": "system", "content": 'If I need to search for information on the internet, I will type "&" followed by what needs to be searched, and then send it to the user. After receiving the answer, I will provide a response based on that information'},
        {"role": "user", "content": "cde in abc"},
        {"role": "assistant", "content": "&cde in abc"},
        {"role": "user", "content": "cde1:10"},
        {"role": "assistant", "content": "cde1: 10"},

] + data
)


print(res)
#print(ress)
print(res.choices[0].message.content.encode('utf-8').decode('utf-8') + "\n")
#print(ress.choices[0].message.content.encode('utf-8').decode('utf-8'))

#추가 예정 목록
#autogpt 연동
#카톡연동