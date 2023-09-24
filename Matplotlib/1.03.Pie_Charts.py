import matplotlib.pyplot as plt

print("Result: ")

slices = [60,35,30]
labels = ["sixty", "Thirty_five", "Thirty"]


# Language Popularity
slices = [59219, 55466, 47544, 36443, 35917]
labels = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java'] 
explode = [0,0,0,0.1,0]

plt.pie(slices, explode=explode, autopct="%1.1f%%", labels=labels, wedgeprops={'edgecolor': 'black'})
plt.title("Pie Chart")
plt.tight_layout() #Default Padding
plt.savefig("Matplotlib/img/plot_1.03.png")
plt.show()


# autopct="%1.1f%%" # Show the Percentage 
