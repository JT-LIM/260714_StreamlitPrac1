import streamlit as st

st.set_page_config(
    page_title="MBTI 포켓몬 직업 추천",
    page_icon="⚡",
    layout="centered"
)

MBTI_DATA = {
    "INTJ": {
        "job": "전략가, 데이터 분석가, 연구원, 시스템 설계자",
        "pokemon": "뮤츠",
        "reason": "논리적이고 독립적인 INTJ는 높은 지능과 압도적인 집중력을 가진 뮤츠와 잘 어울립니다.",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/150.png"
    },
    "INTP": {
        "job": "개발자, 과학자, 게임 기획자, 발명가",
        "pokemon": "메타그로스",
        "reason": "분석적이고 호기심 많은 INTP는 슈퍼컴퓨터 같은 두뇌를 가진 메타그로스와 잘 맞습니다.",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/376.png"
    },
    "ENTJ": {
        "job": "CEO, 프로젝트 매니저, 변호사, 컨설턴트",
        "pokemon": "리자몽",
        "reason": "강한 추진력과 리더십을 가진 ENTJ는 카리스마 넘치는 리자몽과 어울립니다.",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/6.png"
    },
    "ENTP": {
        "job": "창업가, 마케터, 방송인, 기획자",
        "pokemon": "로토무",
        "reason": "아이디어가 많고 변화에 강한 ENTP는 다양한 형태로 변신하는 로토무와 잘 맞습니다.",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/479.png"
    },
    "INFJ": {
        "job": "상담가, 작가, 심리학자, 사회운동가",
        "pokemon": "가디안",
        "reason": "타인의 감정을 깊이 이해하는 INFJ는 헌신적이고 직관적인 가디안과 어울립니다.",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/282.png"
    },
    "INFP": {
        "job": "작가, 예술가, 디자이너, 동물보호 활동가",
        "pokemon": "이브이",
        "reason": "가능성이 많고 섬세한 INFP는 다양한 방향으로 성장할 수 있는 이브이와 잘 맞습니다.",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/133.png"
    },
    "ENFJ": {
        "job": "교사, 코치, HR 담당자, 사회복지사",
        "pokemon": "피카츄",
        "reason": "사람들에게 긍정적인 에너지를 주는 ENFJ는 밝고 친근한 피카츄와 어울립니다.",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/25.png"
    },
    "ENFP": {
        "job": "크리에이터, 광고기획자, 배우, 여행작가",
        "pokemon": "파이리",
        "reason": "열정적이고 가능성을 즐기는 ENFP는 모험심 가득한 파이리와 잘 맞습니다.",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/4.png"
    },
    "ISTJ": {
        "job": "공무원, 회계사, 품질관리자, 엔지니어",
        "pokemon": "잠만보",
        "reason": "안정적이고 꾸준한 ISTJ는 든든하고 흔들림 없는 잠만보와 어울립니다.",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/143.png"
    },
    "ISFJ": {
        "job": "간호사, 교사, 행정직, 고객지원 전문가",
        "pokemon": "럭키",
        "reason": "다정하고 책임감 있는 ISFJ는 치유와 돌봄의 상징인 럭키와 잘 맞습니다.",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/113.png"
    },
    "ESTJ": {
        "job": "관리자, 경찰, 운영 매니저, 군인",
        "pokemon": "괴력몬",
        "reason": "체계적이고 실행력이 강한 ESTJ는 힘과 책임감을 가진 괴력몬과 어울립니다.",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/68.png"
    },
    "ESFJ": {
        "job": "이벤트 플래너, 상담직, 서비스 매니저, 교사",
        "pokemon": "토게키스",
        "reason": "주변 사람을 챙기고 분위기를 좋게 만드는 ESFJ는 행복을 전하는 토게키스와 잘 맞습니다.",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/468.png"
    },
    "ISTP": {
        "job": "정비사, 파일럿, 개발자, 스포츠 선수",
        "pokemon": "루카리오",
        "reason": "침착하고 실전 감각이 뛰어난 ISTP는 날카로운 판단력을 가진 루카리오와 어울립니다.",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/448.png"
    },
    "ISFP": {
        "job": "음악가, 사진작가, 플로리스트, 패션 디자이너",
        "pokemon": "님피아",
        "reason": "감성적이고 아름다움을 잘 느끼는 ISFP는 우아하고 따뜻한 님피아와 잘 맞습니다.",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/700.png"
    },
    "ESTP": {
        "job": "영업직, 운동선수, 응급구조사, 사업가",
        "pokemon": "번치코",
        "reason": "빠른 판단과 행동력을 가진 ESTP는 역동적인 번치코와 어울립니다.",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/257.png"
    },
    "ESFP": {
        "job": "배우, MC, 인플루언서, 공연기획자",
        "pokemon": "푸린",
        "reason": "사람들 앞에서 매력을 발산하는 ESFP는 무대 체질인 푸린과 잘 맞습니다.",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/39.png"
    },
}

st.title("MBTI별 직업 & 포켓몬 추천")
st.write("MBTI를 선택하면 어울리는 직업과 포켓몬을 추천해드립니다.")

mbti = st.selectbox(
    "당신의 MBTI를 선택하세요",
    list(MBTI_DATA.keys())
)

if st.button("추천 보기"):
    result = MBTI_DATA[mbti]

    st.subheader(f"{mbti}에게 어울리는 직업")
    st.success(result["job"])

    st.subheader("추천 포켓몬")
    st.markdown(f"## {result['pokemon']}")
    st.image(result["image"], width=280)

    st.subheader("추천 이유")
    st.write(result["reason"])

    st.caption(f"이미지 URL: {result['image']}")
