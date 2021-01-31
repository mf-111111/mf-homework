import numpy as np
score_title=np.dtype({'names':['name','chinese','math','english'],'formats':['S32','i', 'i', 'i']})

score=np.array([('zhangfei', 68,65,30),('guanyu',95,76,98),('liubei',98,86,88),('dianwei',90,88,77),
                ('xuchu',80,90,90)], dtype=score_title)
chineses=score[:]['chinese']
maths=score[:]['math']
englishes=score[:]['english']
total=score[:]['chinese']+score[:]['math']+score[:]['english']
print('语文平均成绩：', np.mean(chineses))
print('数学平均成绩：', np.mean(maths))
print('英语平均成绩：', np.mean(englishes))
print('语文最小成绩：', np.amin(chineses))
print('数学最小成绩：', np.amin(maths))
print('英语最小成绩：', np.amin(englishes))
print('语文最大成绩：', np.amax(chineses))
print('数学最大成绩：', np.amax(maths))
print('英语最大成绩：', np.amax(englishes))
print('语文方差：', np.var(chineses))
print('数学方差：', np.var(maths))
print('英语方差：', np.var(englishes))
print('语文标准差：', np.std(chineses))
print('数学标准差：', np.std(maths))
print('英语标准差：', np.std(englishes))
print('总成绩排序：', np.sort(total))