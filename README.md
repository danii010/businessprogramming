# 지점 매출 분석 대시보드 📊

지점별 분기 매출 데이터를 입력·저장하고, 등급·순위·통계를 한눈에 확인하는 Streamlit 대시보드입니다.

## 주요 기능

| 탭 | 설명 |
|---|---|
| 지점 입력 | 지점명과 1·2·3분기 매출을 입력해 목록에 추가 (세션 유지) |
| 지점별 실적 | 총매출, 평균, 등급, 성과급률 표 |
| 분기별 통계 | 분기별 평균·최고 매출 및 막대그래프 |
| 순위 & 등급 분포 | 총매출 기준 순위표, 등급 분포 막대그래프 |

## 계산 규칙

- **총매출** = 1분기 + 2분기 + 3분기  
- **평균** = 총매출 ÷ 3  
- **등급** (평균 기준): A(120↑) / B(100↑) / C(80↑) / D(60↑) / F(그 외)  
- **성과급률**: A=5% / B=4% / C=3% / D=2% / F=0%  
- **목표 달성**: 평균 90 이상인 지점 비율

## 로컬 실행 방법

```bash
pip install -r requirements.txt
streamlit run app.py
```

## 파일 구조

```
bizpro_final/
├── app.py            # Streamlit 화면 (UI)
├── utils.py          # 계산 함수 모음
├── banner.png        # 상단 배너 이미지
├── requirements.txt  # 패키지 의존성
└── .gitignore
```

## Streamlit Cloud 배포

1. 이 리포지토리를 GitHub에 push
2. [share.streamlit.io](https://share.streamlit.io) 접속 → **New app**
3. 리포지토리·브랜치 선택, Main file path: `app.py` 입력 → **Deploy**
