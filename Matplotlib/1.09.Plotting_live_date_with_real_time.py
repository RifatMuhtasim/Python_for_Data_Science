import matplotlib.pyplot as plt 
import random
import pandas as pd 
from matplotlib.animation import FuncAnimation 
from itertools import count 
import csv 
import time 


def Snippets():
   x_values = []
   y_values = []

   index = count()

   def animate(i):
      x_values.append(next(index))
      y_values.append(random.randint(0, 5))

      plt.cla()
      plt.plot(x_values, y_values)

   ani = FuncAnimation(plt.gcf(), animate, interval=100)

   plt.tight_layout()
   plt.show()


# Snippets()


def Function_generation():
   x_value = 0
   total_1 = 1000
   total_2 = 1000

   fieldnames = ["x_value", "total_1", "total_2"]

   with open("Matplotlib/img/data_gen.csv", "w") as csv_file:
      csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
      csv_writer.writeheader()
   
   while True:
      with open('Matplotlib/img/data_gen.csv', 'a') as csv_file:
         csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

         info = {
            "x_value": x_value,
            "total_1": total_1,
            "total_2": total_2
         }

         csv_writer.writerow(info)
         print(x_value, total_1, total_2)

         x_value += 1
         total_1 = total_1 + random.randint(-6, 8)
         total_2 = total_2 + random.randint(-5, 6)
         time.sleep(1)

# Function_generation()


def Function1():
   def animate(i):
      data = pd.read_csv("Matplotlib/img/data_gen.csv")
      x = data['x_value']
      y1 = data['total_1']
      y2 = data['total_2']

      plt.cla()
      plt.plot(x, y1, label="Channel 1")
      plt.plot(x, y2, label="Channel 2")
      plt.legend()
   
   ani = FuncAnimation(plt.gcf(), animate, interval=1000)
   plt.tight_layout()
   plt.show()

Function1()


