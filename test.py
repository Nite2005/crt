import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 

df = pd.read_csv('Book1.csv')
df.head()

#17. Calculate the average salary using NumPy.

avg_salary= df['Salary'].mean()


#18 18. Using the above Dataset , Filter out employees with salary greater than 60000 using Pandas.
print(df[df['Salary']>60000])




#19.  Using the above Dataset , Plot a bar chart representing the department-wise average salary using Matplotlib.

plt.bar('Department','Salary',data=df)