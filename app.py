import joblib
import numpy as np
import streamlit as st
from app_home import run_home_app
from app_eda import run_eda_app

def main() :
    st.title('자동차 구매 가격 예측 앱')
    st.sidebar.image('https://www.genesis.com/content/dam/genesis-p2/kr/bto/jj/d/jj_uyh_d.png.thumb.1280.720.png')
    st.sidebar.title(':car: car price app :car:')

    st.sidebar.subheader('구매금액 예측 :memo:')
    Gender = st.sidebar.radio('성별을 선택하세요', ['여자', '남자'])
    if Gender == '여자' :
        Gender = 0
    else :
        Gender = 1
    age = st.sidebar.number_input('나이를 입력하세요',18, 100)
    Annual_Salary = st.sidebar.number_input('연봉을 입력하세요 ($)', 10000, 1000000)
    Credit_Card_Debt = st.sidebar.number_input('카드빚을 입력하세요 ($)', 0, 1000000)
    Net_Worth = st.sidebar.number_input('자산을 입력하세요 ($)',1000, 10000000)

    new_data = np.array([Gender, age, Annual_Salary, Credit_Card_Debt, Net_Worth])
    new_data = new_data.reshape(1, 5)
    regressor = joblib.load('regressor.pkl')
    y_pred = regressor.predict(new_data)

    y_pred = round(y_pred[0], 1)
    if y_pred < 0 :
        st.sidebar.error('입력한 데이터로는 금액을 예측하기 어렵습니다')
    else :
        st.sidebar.info('예측한 자동차 금액은 {} 달러 입니다.'.format(y_pred))
    
    run_home_app()

    st.write('')
    run_eda_app()


if __name__ == '__main__' :
    main()