import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import platform

# CSV 파일 로드 (파일 경로를 적절히 수정하세요)
file_path = r'C:\C\goyang.csv'
data = pd.read_csv(file_path, encoding='cp949')  # 또는 'euc-kr'

# 한글 폰트 설정
if platform.system() == 'Windows':
    plt.rc('font', family='Malgun Gothic')

plt.rc('axes', unicode_minus=False)

# 필요한 열만 추출
data = data[['연번', '노선명', '차로수', '관측지점', '2021년 교통량', '2022년 교통량']]

# 연도별 총 교통량 계산
total_traffic = data[['2021년 교통량', '2022년 교통량']].sum()

# 총 교통량 시각화
plt.figure(figsize=(10, 6))
sns.barplot(x=total_traffic.index, y=total_traffic.values)
plt.title('2021년과 2022년의 총 교통량 비교')
plt.xlabel('연도')
plt.ylabel('총 교통량')
plt.show()

# 각 연번별로 2021년과 2022년의 교통량 비교
fig, axes = plt.subplots(nrows=5, ncols=5, figsize=(20, 20))
axes = axes.flatten()

for i, row in data.iterrows():
    sns.barplot(ax=axes[i], x=['2021년 교통량', '2022년 교통량'], y=[row['2021년 교통량'], row['2022년 교통량']])
    axes[i].set_title(f'연번 {row["연번"]}', fontsize=10)
    axes[i].set_xlabel('')
    axes[i].set_ylabel('')

plt.tight_layout(pad=3.0)
plt.show()
