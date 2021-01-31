import numpy as np
score_type = np.dtype({'names':["name","chinese","english","math"],'formats':['S32','i', 'i', 'i']})
score = np.array([("zhangfei",66,65,30),("guanyu",95,85,98),("zhangyun",93,92,96),("huangzhong",90,88,77),
                  ("dianwei",80,90,90)],dtype = score_type)
chineses = score[:]["chinese"]
englishes = score[:]["english"]
maths = score[:]["math"]
total = score[:]['chinese'] +score[:]['english']+score[:]['math']
print('语文平均成绩：',np.mean(chineses))
print('英语平均成绩：',np.mean(englishes))
print('数学平均成绩：',np.mean(maths))
print('语文最小成绩：',np.amin(chineses))
print('英语最小成绩：',np.amin(englishes))
print('数学最小成绩：',np.amin(maths))
print('语文最大成绩：',np.amax(chineses))
print('英语最大成绩：',np.amax(englishes))
print('数学最大成绩：',np.amax(maths))
print('语文方差：',np.var(chineses))
print('英语方差：',np.var(englishes))
print('数学方差：',np.var(maths))
print('语文标准差：',np.std(chineses))
print('英语标准差：',np.std(englishes))
print('数学标准差：',np.std(maths))
print('按总成绩排序：',np.sort(total))