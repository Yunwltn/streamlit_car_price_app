import streamlit as st

def run_home_app() :
    st.subheader('welcome to car price app! :smile:')
    st.write('이 앱은 고객 데이터와 자동차 구매 데이터에 대한 내용입니다')
    st.write('데이터 분석 및 고객 정보를 넣으면 얼마정도의 차를 구매할지를 예측해줍니다')
    st.info('좌측 사이드바에 정보를 입력해주세요! 인공지능이 자동차 구매 금액을 예측해줍니다 :thumbsup:')

    img_url = 'https://www.bmw.co.kr/content/dam/bmw/common/all-models/x-series/x7/2022/highlights/bmw-x-series-x7-sp-desktop.jpg.asset.1645602668136.jpg'
    st.image(img_url)

