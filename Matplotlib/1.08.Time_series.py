import matplotlib.pyplot as plt 
import pandas as pd 
from datetime import timedelta, datetime 
from matplotlib import dates as mpl_dates

plt.style.use("seaborn")

def Time_series1():

   dates = [
      datetime(2019, 5, 24),
      datetime(2019, 5, 25),
      datetime(2019, 5, 26),
      datetime(2019, 5, 27),
      datetime(2019, 5, 28),
      datetime(2019, 5, 29),
      datetime(2019, 5, 30)
   ]
   y = [0, 1, 3, 4, 6, 5, 7]

   plt.plot_date(dates, y, linestyle="solid")

   plt.tight_layout()
   plt.savefig("Matplotlib/img/plot_1.08.png")
   plt.show()


# Time_series1()


def Time_series2():
   data = pd.read_csv("https://raw.githubusercontent.com/CoreyMSchafer/code_snippets/master/Python/Matplotlib/08-TimeSeries/data.csv")
   print(data.head())
   price_date = data['Date']
   price_close = data['Close']

   plt.plot_date(price_date, price_close, linestyle="solid")

   plt.title("Bitcoin Price")
   plt.xlabel("Date")
   plt.ylabel("Closing Price")
   plt.tight_layout()
   plt.show()


Time_series2()