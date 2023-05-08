import streamlit as st
from utils import FINALPROJECT_CHATBOT_desc as p2c
from PIL import Image
def app():

    st.write('''
                ###동의보감 AI 서비스 챗봇 테스트 페이지
                ''')
    p2c.desc()

app()
image = Image.open('C:/Users/dign1/OneDrive/Documents/project_seven/data/list50.png')

st.image(image,width=800)
