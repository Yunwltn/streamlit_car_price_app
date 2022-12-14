import streamlit as st

def run_home_app() :
    st.text('환영합니다')
    st.text('이 앱은 고객 데이터와 자동차 구매 데이터에 대한 내용입니다')
    st.text('데이터 분석 및 고객 정보를 넣으면 얼마정도의 차를 구매할지를 예측해줍니다')

    img_url = 'https://file.newswire.co.kr/data/datafile2/thumb_480/2021/07/3554238800_20210709103022_2517669736.jpg'
    st.image(img_url)
