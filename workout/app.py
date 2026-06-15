import streamlit as st
import matplotlib.pyplot as plt

# Page Config
st.set_page_config(
    page_title="학점 계산기 (Grade Calculator)",
    page_icon="🎓",
    layout="centered"
)

# Custom CSS for premium styling
st.markdown("""
<style>
    .main-title {
        font-size: 2.2rem;
        font-weight: 800;
        color: #1E293B;
        text-align: center;
        margin-bottom: 0.5rem;
    }
    .sub-title {
        font-size: 1.1rem;
        color: #64748B;
        text-align: center;
        margin-bottom: 2rem;
    }
    .metric-card {
        background-color: #F8FAFC;
        border: 1px solid #E2E8F0;
        border-radius: 12px;
        padding: 1.5rem;
        margin-bottom: 1.5rem;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">🎓 스마트 학점 계산기</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">중간고사와 기말고사 점수를 입력하여 성적을 계산하고 점수 추이를 확인하세요.</div>', unsafe_allow_html=True)

# 1. 입력 위젯 구성 (Streamlit 사이드바)
st.sidebar.header("📝 점수 입력")
midterm = st.sidebar.number_input(
    "중간고사 점수",
    min_value=0,
    max_value=100,
    value=80,
    step=1,
    help="0점에서 100점 사이의 중간고사 점수를 입력하세요."
)

final = st.sidebar.number_input(
    "기말고사 점수",
    min_value=0,
    max_value=100,
    value=85,
    step=1,
    help="0점에서 100점 사이의 기말고사 점수를 입력하세요."
)

# 2. 성적 처리 로직 (파이썬 함수 및 제어문)
def calculate_average(midterm_score, final_score):
    return (midterm_score + final_score) / 2

avg_score = calculate_average(midterm, final)

st.markdown(f"""
<div class="metric-card">
    <h4 style="margin: 0; color: #475569;">📊 성적 요약</h4>
    <div style="display: flex; justify-content: space-around; margin-top: 1rem;">
        <div style="text-align: center;">
            <div style="font-size: 0.85rem; color: #64748B;">중간고사</div>
            <div style="font-size: 1.5rem; font-weight: 700; color: #0F172A;">{midterm}점</div>
        </div>
        <div style="text-align: center; border-left: 1px solid #E2E8F0; padding-left: 2rem; padding-right: 2rem;">
            <div style="font-size: 0.85rem; color: #64748B;">기말고사</div>
            <div style="font-size: 1.5rem; font-weight: 700; color: #0F172A;">{final}점</div>
        </div>
        <div style="text-align: center; border-left: 1px solid #E2E8F0; padding-left: 2rem;">
            <div style="font-size: 0.85rem; color: #64748B;">평균 점수</div>
            <div style="font-size: 1.5rem; font-weight: 700; color: #3B82F6;">{avg_score:.1f}점</div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# 학점 판단 및 메시지 출력
if avg_score >= 90:
    st.success("A등급 🎉")
elif avg_score >= 80:
    st.info("B등급 👍")
else:
    st.error("재수강 권장 😢")

# 3. 데이터 시각화 (Matplotlib 필수 활용)
st.markdown("### 📈 Test Score Trend")

fig, ax = plt.subplots(figsize=(8, 4.5))

# x축 항목 및 y축 점수 리스트 정의
exams = ['Midterm', 'Final']
scores = [midterm, final]

# [중요 - 14장 반영] 그래프 스타일 적용
# 사용자의 요구사항 'kb:' (검은색 k, 플러스 마커 +, 점선 :) 조합 사용
# Note: matplotlib 포맷 문자열로 'kb:'를 직접 주면 두 개의 색상 코드(k=black, b=blue)로 인식되어 ValueError가 발생하므로,
# 'k+:' 형식을 적용하여 검은색(k), 플러스 마커(+), 점선(:)을 온전하게 시각화합니다.
ax.plot(exams, scores, 'k+:', linewidth=2, markersize=12, markeredgewidth=2, label='Score')

# 제목, 축 라벨, 그리드 설정
ax.set_title("Test Score Trend", fontsize=14, fontweight='bold', pad=15)
ax.set_xlabel("Exam", fontsize=11, labelpad=10)
ax.set_ylabel("Score", fontsize=11, labelpad=10)
ax.set_ylim(0, 105) # 0~100점 범위가 잘 보이도록 설정
ax.grid(True, linestyle='--', alpha=0.5)

# 축 스타일 개선
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_color('#cccccc')
ax.spines['bottom'].set_color('#cccccc')

# 틱 레이블 크기 조절
ax.tick_params(axis='both', which='major', labelsize=10)

# 각 점에 값 표시 데코레이션
for i, score in enumerate(scores):
    ax.annotate(f"{score}pts", (exams[i], score), textcoords="offset points", xytext=(0,10), ha='center', fontweight='bold', color='#1E293B')

st.pyplot(fig)
