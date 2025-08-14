import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_excel(r'f:\Student_Performance_Dataset.xlsx')
print(df.head()) # اطمینان برای صحت وارد شدن دیتا 
df['MeanScore'] = df[['Math', 'Science', 'Literature']].mean(axis=1)# محاسبه میانگین نمره دروس برای هر دانش‌آموز

class Student: # بحث شی گرایی 
       def __init__(self, name, gender, math, science, literature):
        self.name = name
        self.gender = gender
        self.math = math
        self.science = science
        self.literature = literature
        self.mean_score = self.calculate_mean() 

 def calculate_mean(self):
     return (self.math + self.science + self.literature) / 3
    
for index, row in df.iterrows():# بررسی جنسیت و طبقه‌بندی میانگین نمره با if / elif / else
    gender = row['Gender']
    mean_score = row['MeanScore']
    
    if mean_score >= 17:
        level = 'عالی'

    elif mean_score >= 12:
        level = 'متوسط'

    else:
        level = 'ضعیف'

    print(f"{row['Student']} ({gender}) - میانگین: {mean_score:.1f} → عملکرد: {level}")

plt.figure(figsize=(6, 5)) # رسم نمودار ستونی میانگین نمرات بر اساس جنسیت 
sns.barplot(data=df, x='Gender', y='MeanScore', ci=None, palette='pastel')
plt.title('میانگین نمرات بر اساس جنسیت')
plt.xlabel('جنسیت')
plt.ylabel('میانگین نمره')
plt.show()

plt.figure(figsize=(6, 5)) #رسم نمودار هیستوگرام برای نمرات افسردگی 
sns.histplot(data=df, x='DepressionScore', bins=10, kde=True, color='skyblue')
plt.title('توزیع نمره افسردگی')
plt.xlabel('نمره افسردگی')
plt.ylabel('تعداد')
plt.show()

plt.figure(figsize=(6, 5)) #رسم نمودار scatter plot برای مصرف اینترنت و افسردگی 
sns.scatterplot(data=df, x='InternetUsage', y='DepressionScore', hue='Gender', palette='Set2')
plt.title('رابطه مصرف اینترنت و افسردگی')
plt.xlabel('میزان مصرف اینترنت')
plt.ylabel('نمره افسردگی')
plt.legend(title='جنسیت')
plt.show()
