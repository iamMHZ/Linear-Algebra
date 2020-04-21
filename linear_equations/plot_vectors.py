from matplotlib import pyplot as plt

from_ = [0, 0]
to = [10, 10]

# plt.quiver(origin, end)
# # plt.show()

ax = plt.axes()
ax.arrow(from_[0], from_[1], to[0], to[1], head_width=0.5, head_length=0.5)

plt.xlim(0, 20)
plt.ylim(0, 20)
plt.show()
