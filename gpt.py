import openai
import os

from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.environ["api_keyopenai"]

res = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
        {"role": "system", "content": '당신은 user가 질문하는 것에 대답하여 줍니다 그리고 인터넷에서 정보를 조사해야할경우 문장앞에 &를 적은후  조사가 필요한 내용을 적은후 user에거 내용을 보냅니다 그후 답이 돌아오면 그 내용을 토대로 질문에 대답을 합니다 예시: "&서울의날씨", "&책의정의"'},
        {"role": "user", "content": "인터넷에서 서울의 날씨를 찾아줘"},
        {"role": "assistant", "content": "&서울의 날씨"},
        {"role": "user", "content": "서울의 날씨는 온도: 10도 맑음"},
        {"role": "assistant", "content": "서울의 날씨는 맑고 기온은 10도 입나다"},
        {"role": "user", "content": "고양이의 정의를 찾아줘"},
        {"role": "assistant", "content": "&고양이의 정의"},
        {"role": "user", "content": "고양이(학명: Felis catus 펠리스 카투스[*])는 식육목 고양이과에 속하는 포유류이다. 집고양이의 기원은 약 1만년 전 중동 지역에서 스스로 숲속을 나와 사람들이 모여사는 마을에 정착하여 길들여진 아프리카들고양이(학명: Felis lybica)로 추측된다."},

    ]
)

print(res)
print(res.choices[0].message.content.encode('utf-8').decode('utf-8'))

#추가 예정 목록
#autogpt 연동
#카톡연동