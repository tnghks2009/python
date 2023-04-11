# streamlit, pandas 라이브러리 불러오기 
import streamlit as st
import pandas as pd


st.title('Unit 3. Data display elements')
st.caption('참조사이트: https://docs.streamlit.io/library/api-reference/data')

st.header(' 1. Metric')
st.metric(label='Temperature', value='30.5 ℃', delta='2.5 ℃')
st.metric(label='Temperature', value='28.0 ℃', delta='-2.5 ℃')


st.header('2. columns')
col1, col2, col3 = st.columns(3)
col1.metric('기온', '30.5 ℃', '2.5 ℃')
col2.metric('풍속', '9 mph', '-8 %')
col3.metric('습도', '86 %', '4 %')

st.header('3. Dataframe 조회하기')

# 파일 위치- https://raw.githubusercontent.com/huhshin/streamlit/master/data_titanic.csv
titanic = pd.read_csv('https://raw.githubusercontent.com/huhshin/streamlit/master/data_titanic.csv')

st.markdown('- st.dataframe(상위 15행)')
st.caption('dataframe, write- 10개 행  기준 스크롤, 열 크기조정, 열 정렬, 테이블  확대')
st.dataframe(titanic.head(15))

st.markdown('- st.write(상위 15행)')
st.write(titanic.head(15))

st.markdown('- st.table(상위 15행)')
st.caption('table- 형태 고정')
st.table(titanic.head(15))

st.header('4. Dataframe 수정하기')
st.markdown('- st.experimental_data_editor(df)')
edited_titanic = st.experimental_data_editor(titanic)

if st.button('Press button to Save titanic_실습.csv'):   # ***를 원하는 파일명으로 바꾸세요.
    edited_titanic.to_csv('titanic_실습.csv')
    st.write('💾 Saved')

# 파일실행: File > New > Terminal(anaconda prompt) - streamlit run 3.data.py