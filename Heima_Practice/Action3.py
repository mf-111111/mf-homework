
import numpy as np
import pandas as pd

#数据加载
result = pd.read_csv("car_complain.csv")
#print(result)

#数据预处理
result = result.drop("problem", axis = 1).join(result.problem.str.get_dummies(','))
#print(result)

# 数据清洗
def f(x):
    x = x.replace("一汽-大众","一汽大众")
    return x
result['brand'] = result['brand'].apply(f)
#print(result)

# 数据统计
result1 = result.groupby(['brand'])['id'].agg(['count']).sort_values('count',ascending=False)
result1.reset_index(inplace=True)
print('品牌投诉总数按大小顺序分别为：')
print(result1)

result2 = result.groupby(['car_model'])['id'].agg(['count']).sort_values('count', ascending = False)
result2.reset_index(inplace=True)
print('车型投诉总数按大小顺序分别为：')
print(result2)

result3 = result.groupby(['brand','car_model'])['id'].agg(['count'])
result3 = result3.groupby(['brand']).mean().sort_values('count', ascending = False)
result3.reset_index(inplace=True)
print('品牌的平均车型投诉总数按大小顺序分别为：')
print(result3)







