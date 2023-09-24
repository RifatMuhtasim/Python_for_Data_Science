import matplotlib.pyplot as plt


minutes = [1, 2, 3, 4, 5, 6, 7, 8, 9]
player1 = [8, 6, 5, 5, 4, 2, 1, 1, 0]
player2 = [0, 1, 2, 2, 2, 4, 4, 4, 4]
player3 = [0, 1, 1, 1, 2, 2, 3, 3, 4]
labels = ["Player 1", "Player 2", "Player 3"]

plt.stackplot(minutes, player1, player2, player3, labels=labels)

plt.title("Stack Plot")
plt.tight_layout()
plt.legend()
plt.savefig("Matplotlib/img/plot_1.04.png")
plt.legend(loc="lower left")
plt.show()