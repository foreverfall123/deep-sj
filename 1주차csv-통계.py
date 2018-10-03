import pandas
import matplotlib
import matplotlib.pyplot as plt

#CSV파일 읽어서 저장(pandas사용)
data = pandas.read_csv('1주차csv-통계.csv')
#CSV파일의 칼럼 출력
print(data.columns)
#추출할 칼럼들만 이용해서 데이터프레임 다시 만듬(숫자가 아닌 항목은 차트로 만들수 없는듯)
dataset = data[['SepalLength','SepalWidth']]
#정상적으로 추출이 되었는지 확인
print(dataset)
#데이터를 이용하여 차트 만듬
dataset.plot(kind='bar')
#만든 차트를 matplotlib를 이용하여 윈도우에 띄움
plt.show()
