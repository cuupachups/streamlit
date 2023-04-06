import streamlit as st

st.set_page_config(
    page_title="선택과목 수요조사",
    page_icon='✔'
)

st.header("선택과목 수요조사 (현 1학년)")
st.sidebar.subheader('과목 선택 현황')

반 = st.selectbox('본인의 반을 선택하세요',('1','2','3','4','5','6','7','8','9'))

number = st.text_input('번호')
name = st.text_input('이름')

list = ['언어와 매체', '실용영어','수학 2']
과목1 = st.radio('선택군 1 : 공통 과목 (1학기)', list)

list2=['언어와 매체','실용영어','수학 2']
list2.remove(과목1)
if 과목1 == '수학 2':
    list2.append('미적분')
과목2 = st.radio('선택군 1 : 공통 과목 (2학기)', list2)
st.sidebar.write('공통:' + 과목1 + ',' +과목2 + '을 선택하셨습니다.')

options = st.multiselect("선택군 2: 탐구 과목", ('윤리와 사상','세계사','한국 지리','정치와 법','사회 문제 탐구','물리학1','화학1',
                                          '생명과학1','지구과학1','과학 과제 연구'))
st.sidebar.write('탐구:' , options , '을 선택하셨습니다.')

외국 = st.radio('선택군 3: 제 2 외국어', ('일본어','중국어'))
st.sidebar.write('제2외국어:' + 외국 + '을 선택하셨습니다.')

btn = st.button('제출')
if btn:
    if number == '':
        st.write('번호를 입력하세요.')
        if name == '':
            st.write('이름을 입력하세요.')
    elif name == '':
        st.write('이름을 입력하세요.')
    elif options == '':
        st.write('탐구 과목을 선택하세요.')
    else:
        st.subheader('응답 결과가 정상적으로 제출되었습니다. 수고하셨습니다.')

