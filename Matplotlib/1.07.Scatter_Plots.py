import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd

plt.style.use('seaborn')


def Scatter_Plot1():
   x = [5, 7, 8, 5, 6, 7, 9, 2, 3, 4, 4, 4, 2, 6, 3, 6, 8, 6, 4, 1]
   y = [7, 4, 3, 9, 1, 3, 2, 5, 2, 4, 8, 7, 1, 6, 4, 9, 7, 7, 5, 1]

   colors = [7, 5, 9, 7, 5, 7, 2, 5, 3, 7, 1, 2, 8, 1, 9, 2, 5, 6, 7, 5]
   sizes = [209, 486, 381, 255, 191, 315, 185, 228, 174, 538, 239, 394, 399, 153, 273, 293, 436, 501, 397, 539]


   plt.scatter(x, y, c=colors, s=sizes, edgecolors="black", alpha=0.80, linewidths=1)

   cbar = plt.colorbar()
   cbar.set_label("Satisfaction")

   plt.tight_layout()
   plt.savefig("Matplotlib/img/plot_1.07.png")
   plt.show()

# Scatter_Plot1()


def Scatter_Plot2():
   
   df= pd.read_csv("https://raw.githubusercontent.com/CoreyMSchafer/code_snippets/master/Python/Matplotlib/07-ScatterPlots/2019-05-31-data.csv")
   print(df.head())
   
   view_count = df['view_count']
   likes = df['likes']
   ratio = df['ratio']

   plt.scatter(view_count, likes, c=ratio, edgecolors="black", alpha=0.75, linewidths=1, cmap="summer")
   
   cbar = plt.colorbar()
   cbar.set_label("Like/Dislike Ratio")

   plt.xscale('log')
   plt.yscale('log')
   plt.xlabel("View Counts")
   plt.ylabel("Total Likes")
   plt.tight_layout()
   plt.savefig("Matplotlib/img/plot_1.07.png")
   plt.show()

Scatter_Plot2()