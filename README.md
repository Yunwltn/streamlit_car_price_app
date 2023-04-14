<div align=center>
	<img src="https://capsule-render.vercel.app/api?type=waving&color=0:FF0000,100:a82da&height=200&fontColor=FFFFFF&section=header&text=streamlit%20car%20price%20app&fontSize=60&animation=twinkling" />
</div>	
<div align=center>
	<a href="mailto:yunwltn98@gmail.com"><img src="https://img.shields.io/badge/Gmail-EA4335?style=flat&logo=Gmail&logoColor=white&link="mailto:yunwltn98@gmail.com" />
	<a href="https://coding-jisu.tistory.com/"><img src="https://img.shields.io/badge/Tistory-000000?style=flat&logo=Tistory&logoColor=white&link="https://coding-jisu.tistory.com" />
	<br>
	<br>
</div>	
<div align=center> 
	<h3> 📌프로젝트 명📌 <h3>
	<h4> Car Price App <h4>
	<h6> 고객 데이터와 자동차 구매 데이터에 대한 내용입니다 <h6>
	<h6> 데이터 분석 및 고객 정보를 입력하면 얼마정도의 차를 구매할지 가격을 예측해줍니다 <h6>
	<br>
	<h4>
		
👉웹대시보드 주소 <http://ec2-3-38-117-95.ap-northeast-2.compute.amazonaws.com:8504/>

</div>	
<div align=center> 
	<br>
	<br>
	<h3> 프로젝트 구성📋 <h3>
	<h4> 자동차 구매 가격 예측에 사용된 데이터를 표시
  <h4> 좌측 사이드바에 자동차 구매 가격을 예측할 수 있는 인공지능 설정
	<br>
	<br>
	<br>
	<br>
	<h3> 사용한 데이터📂 <h3>
	<h4> Car Purchasing Model <h4>

<https://www.kaggle.com/datasets/dev0914sharma/car-purchasing-model>
</div>	
<div align=center>
	<br>
	<br>
	<h3> 사용한 컬럼📑 <h3>
	<h4> Car Purchasing Model의 성별, 나이, 연봉, 카드빚, 자산, 자동차 구매 금액 컬럼 <h4>
	<br>
	<br>
	<h3> 사용한 라이브러리✏️ <h3>	
	<img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=Streamlit&logoColor=white" />
	<img src="https://img.shields.io/badge/NumPy-013243?style=flat&logo=NumPy&logoColor=white" />
	<img src="https://img.shields.io/badge/pandas-150458?style=flat&logo=pandas&logoColor=white" />
	<img src="https://img.shields.io/badge/matplotlib-000000?style=flat&logo=&logoColor=white" />
	<img src="https://img.shields.io/badge/seaborn-000000?style=flat&logo=&logoColor=white" />
	<br>
	<img src="https://img.shields.io/badge/joblib-000000?style=flat&logo=&logoColor=white" />
	<img src="https://img.shields.io/badge/LinearRegression-000000?style=flat&logo=&logoColor=white" />
	<img src="https://img.shields.io/badge/train_test_split-000000?style=flat&logo=&logoColor=white" />
	<h3> 사용한 Tools🔨 <h3>
	<img src="https://img.shields.io/badge/Jupyter-F37626?style=flat&logo=Jupyter&logoColor=white" />
	<img src="https://img.shields.io/badge/Visual Studio Code-007ACC?style=flat&logo=Visual Studio Code&logoColor=white" />
	<img src="https://img.shields.io/badge/GitHub-181717?style=flat&logo=GitHub&logoColor=white" />
	<br>
	<br>
</div>	

		
---


<h3>진행과정💬<h3>

<h4>Jupyter Notebook에서 데이터 분석<h4>
	
<h5> <h5>
	
- 데이터 파일 불러와서 연봉이 가장 많은 사람과 적은 사람의 데이터를 확인
- 남자가 몇명이고 여자가 몇명인지 각 성별 갯수 확인
- 성별, 나이, 연봉, 카드빚을 히스토그램으로 확인
- 데이터프레임과 히트맵으로 각 컬럼간의 상관 관계 확인
- 인공지능에게 예측할 값을 X와 y로 분리
- 빈 인공지능을 만들어 X와 y데이터를 학습용, 테스트용으로 분리해 학습용으로 학습
- 테스트용을 예측하게 실행한 값의 오차값을 구해 성능 측정
- 새로운 예제를 만들어 테스트해서 결과가 잘 나오는지 확인
- 만든 인공지능과 사용한 변수를 pkl파일로 만들어 저장

<h4>Visual Studio Code에서 Streamlit 라이브러리로 작업<h4>

<h5> 메인 앱 화면 생성<h5>

- 앱을 대표하는 이미지와 무슨 앱인지 소개하는 글 작성
- 사용한 데이터프레임의 기본 정보를 볼 수 있게 데이터프레임 입력
- 기본 통계, 컬럼별 최대/최소값, 컬럼별 히스토그램, 컬럼별 상관관계 히트맵 입력
- 사이드바 메뉴에 데이터분석할때 만든 인공지능 설정
- 인공지능에 값을 입력할시 예측한 금액이 얼마인지 나올 수 있게 설정

	
---
	
	

![1](https://user-images.githubusercontent.com/120348555/209048487-e960db2e-001a-495b-b819-34f0e59fa5b0.PNG)
![2](https://user-images.githubusercontent.com/120348555/209048523-9aba3c5c-6a21-45b8-9635-092c163829f2.PNG)
![3](https://user-images.githubusercontent.com/120348555/209048547-0290c0b6-f1ad-4cdb-9dbf-956dbbf8b2d5.PNG)

<div align=center>
	<img src="https://capsule-render.vercel.app/api?type=waving&color=0:FF0000,100:a82da&height=100&section=footer&text=Thank%20you&fontSize=50&animation=twinkling" />
</div>	
