import matplotlib.pyplot as plt 
import pandas as pd 

plt.style.use('fivethirtyeight')

def histogram1():
   ages = [18, 19, 21, 25, 26, 26, 30, 32, 38, 45, 55]
   bins = [10 , 20, 30, 40, 50, 60]

   plt.hist(ages, bins=bins, edgecolor="black")

   plt.title("Histogram")
   plt.savefig("Matplotlib/img/plot_1.06.png")
   plt.show()

#histogram1()


def histogram2():
   data = pd.read_csv("https://raw.githubusercontent.com/CoreyMSchafer/code_snippets/master/Python/Matplotlib/06-Histograms/data.csv")
   print(data.head(5))

   ids = data['Responder_id']
   ages = data['Age']
   bins = [10,20,30,40,50,60,70,80,90,100]
   median_age = 29

   plt.hist(ages, bins=bins, edgecolor="black")
   plt.axvline(median_age, color="red", label="Median Age", linewidth=2)

   plt.title("Age of Respondents (Histogram)")
   plt.xlabel("Ages")
   plt.ylabel("Total Respondents")

   plt.savefig("Matplotlib/img/plot_1.06.png")
   plt.tight_layout()
   plt.legend()
   plt.show()

histogram2()