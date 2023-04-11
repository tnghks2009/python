import streamlit as st

st.title('Unit 5. Layouts & Containers')
st.caption('참조사이트: https://docs.streamlit.io/library/api-reference/layout')

# sidebar- with 사용하기 📧  📱  ☎︎
with st.sidebar :
    st.header('1.Sidebar')

add_selectbox = st.sidebar.selectbox('어디로 연락 드릴까요?', ('E-mail', 'Mobile', 'Office'))

if add_selectbox == 'E-mail':
    st.sidebar.title('📧')
elif add_selectbox == 'Mobile':
    st.sidebar.title('📱')
else:
    st.sidebar.title('☎︎')



# columns  
# 고양이 https://images.pexels.com/photos/2071873/pexels-photo-2071873.jpeg?auto=compress&cs=tinysrgb
# 개     https://images.pexels.com/photos/3361739/pexels-photo-3361739.jpeg?auto=compress&cs=tinysrgb
# 부엉이 https://images.pexels.com/photos/3737300/pexels-photo-3737300.jpeg?auto=compress&cs=tinysrgb

st.header('2. Columns')

col1, col2, col3 = st.columns(3)

with col1:
    st.text('kitty')
    st.image('https://images.pexels.com/photos/2071873/pexels-photo-2071873.jpeg?auto=compress&cs=tinysrgb')
    
with col2:
    st.text('puppy')
    st.image('https://images.pexels.com/photos/3361739/pexels-photo-3361739.jpeg?auto=compress&cs=tinysrgb')
    
with col3:
    st.text('owl')
    st.image('https://images.pexels.com/photos/3737300/pexels-photo-3737300.jpeg?auto=compress&cs=tinysrgb')


    
# tabs - width=200

st.header('3. Tabs')

tab1, tab2, tab3 = st.tabs(['고양이', '개', '부엉이'])

with tab1:
    st.caption('Kitty')
    st.image('https://images.pexels.com/photos/2071873/pexels-photo-2071873.jpeg?auto=compress&cs=tinysrgb', width=500)
    
with tab2:
    st.caption('Puppy')
    st.image('https://images.pexels.com/photos/3361739/pexels-photo-3361739.jpeg?auto=compress&cs=tinysrgb', width=500)
    
with tab3:
    st.caption('Owl')
    st.image('https://images.pexels.com/photos/3737300/pexels-photo-3737300.jpeg?auto=compress&cs=tinysrgb', width=500)


    
# 파일실행: File > New > Terminal(anaconda prompt) - streamlit run 5-1.layouts.py