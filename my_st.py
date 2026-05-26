import streamlit as st #streamlit 라이브러리 임포트

'''
# 비즈니스 모델 분석 ㅎ

[네이버](https://www.naver.com/)\n
[홍익대학교](https://www.hongik.ac.kr)

이것이 일반 본문 **이것이 굵은 글씨** *이것이 기울임 글씨* ~~이것이 취소선~~

:red[팔랑귀팔랑귀] :green[뭘넘어가기 그린그린] :blue[파란글씨]

```python
import streamlit as st

print('코드 블록')
```

'''

st.caption('캡션(작고 흐린 글씨로 표현됨): st.caption()')

with st.echo():
    # 이 블록의 코드와 결과를 출력
    name = '윤토'
    st.write('Hello, Streamlit!', name)

st.latex('\int_a^b f(x)dx')
'$$\int_a^b f(x)dx$$'

'#### :orange[이미지: st.image()]'
st.image('./data/파이썬설명.jpeg', caption='파이썬 로고', width=500)

'#### :orange[오디오: st.audio()]'
st.audio('./data/사운드.mp3', format='audio/mpeg', loop=True)

'#### :orange[비디오: st.video()]'
# 'rb': 바이너리 모드로 파일 열기
video_file = open('./data/바다영상.mp4', 'rb')
video_bytes = video_file.read()

st.video(video_bytes)

st.divider()
