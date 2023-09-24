import matplotlib.pyplot as plt 
import pandas as pd 


data = pd.read_csv("Matplotlib/img/data.csv")
ages = data['Age']
dev_salaries = data['All_Devs']
py_salaries = data['Python']
js_salaries = data['JavaScript']
overall_median = 57231

plt.plot(ages, dev_salaries, label="All Devs")
plt.plot(ages, py_salaries, label="Python Devs")

# plt.fill_between(ages, py_salaries, overall_median, alpha=0.20)

plt.fill_between(ages, py_salaries, dev_salaries, where=(py_salaries > dev_salaries), interpolate=True, alpha=0.25, label="About Avg")
plt.fill_between(ages, py_salaries, dev_salaries, where=(py_salaries <= dev_salaries), interpolate=True, alpha=0.25, label="Below Avg")


plt.title("Median Salary (USD) by Age")
plt.xlabel("Age")
plt.ylabel("Median Salary")

plt.legend()
plt.tight_layout()
plt.savefig("Matplotlib/img/plot_1.05.png")
plt.show()