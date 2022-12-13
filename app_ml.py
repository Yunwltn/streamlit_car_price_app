import streamlit as st
import numpy as np
import joblib

def run_ml_app() :
    st.subheader('자동차 금액 예측')

    # 성별은 여자이고 나이는 50이며, 연봉은 4만달러, 카드빚 5만달러, 자산은 20만달러
    # 이사람은 얼마짜리 차를 살것인가

    # 성별, 나이, 연봉, 카드빚, 자산을 유저한테 모두 입력 받아서 자동차 구매금액 예측하기

    Gender = st.radio('성별을 선택하세요', ['여자', '남자'])
    if Gender == '여자' :
        Gender = 0
    else :
        Gender = 1
    age = st.number_input('나이를 입력하세요',18, 100)
    Annual_Salary = st.number_input('연봉을 입력하세요', 10000, 1000000)
    Credit_Card_Debt = st.number_input('카드빚을 입력하세요', 0, 1000000)
    Net_Worth = st.number_input('자산을 입력하세요',1000, 10000000)

    new_data = np.array([Gender, age, Annual_Salary, Credit_Card_Debt, Net_Worth])
    new_data = new_data.reshape(1, 5)
    
    regressor = joblib.load('regressor.pkl')
    y_pred = regressor.predict(new_data)

    y_pred = round(y_pred[0], 1)

    if y_pred < 0 :
        st.info('입력한 데이터로는 금액을 예측하기 어렵습니다')
    else :
        st.info('예측한 자동차 금액은 {} 달러 입니다.'.format(y_pred))