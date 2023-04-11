import streamlit as st
import pandas as pd

# 메인페이지 
# Iris 사진 나타하기 - https://images.pexels.com/photos/5677011/pexels-photo-5677011.jpeg?auto=compress&cs=tinysrgb&w=200
# https://raw.githubusercontent.com/huhshin/streamlit/master/data_iris.csv 읽고 나타내기 
df = pd.read_csv('https://raw.githubusercontent.com/huhshin/streamlit/master/data_iris.csv')

def main_page():
    st.header('Main Page')
    st.image('https://images.pexels.com/photos/5677011/pexels-photo-5677011.jpeg?auto=compress&cs=tinysrgb&w=200')
    st.write(df.head(1))

    
# 2페이지: 세 개의 columns으로 나누어 꽃 이름과 사진 나타내기
def page2():
    st.header('Page 2')
    col1, col2, col3 = st.columns(3)          # column 별 사진 size 비율
    
    with col1:
        st.text('Setosa')
        st.image('https://m.media-amazon.com/images/I/61pLvdbjC7L._AC_.jpg')
    with col2:
        st.text('Versicolor')
        st.image('https://upload.wikimedia.org/wikipedia/commons/2/27/Blue_Flag%2C_Ottawa.jpg')
    with col3:
        st.text('Virginica')
        st.image('https://upload.wikimedia.org/wikipedia/commons/thumb/f/f8/Iris_virginica_2.jpg/1920px-Iris_virginica_2.jpg')


# 3페이지: 세 개의 tab을 사용하여 iris 3가지 꽃 나타내기
def page3():
    st.header('Page 3')
    tab1, tab2, tab3 = st.tabs(['Setosa', 'Versicolor', 'Virginica'])
    
    with tab1:
        st.header('Setosa')
        st.image('https://m.media-amazon.com/images/I/61pLvdbjC7L._AC_.jpg')
    with tab2:
        st.header('Versicolor')
        st.image('https://upload.wikimedia.org/wikipedia/commons/2/27/Blue_Flag%2C_Ottawa.jpg')
    with tab3:
        st.header('Virginica')
        st.image('https://upload.wikimedia.org/wikipedia/commons/thumb/f/f8/Iris_virginica_2.jpg/1920px-Iris_virginica_2.jpg')

        
# 딕셔너리 선언 {  ‘selectbox항목’ : 페이지명 …  }
page_names_to_funcs = {'Main Page': main_page, 'Page 2': page2, 'Page 3': page3}

# 사이드 바에서 selectbox 선언 & 선택 결과 저장
selected_page = st.sidebar.selectbox('Select a page', page_names_to_funcs.keys())

# 해당 페이지 부르기
page_names_to_funcs[selected_page]()

# 파일실행: File > New > Terminal(anaconda prompt) - streamlit run 5-3.layouts.py