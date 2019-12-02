import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

#Graph #1
objects = ('Solar Eclipse', 'Black Holes', 'Aliens', 'Constellations')
y_pos = np.arange(len(objects))
performance = [7,35,21,101]
plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('Number of Tweets')
plt.xlabel('Topic')
plt.title('Total Tweets for Astronomy Topics by NASA')
plt.show()

#Graph #2
objects = ('Solar Eclipse', 'Black Holes', 'Aliens', 'Constellations')
y_pos = np.arange(len(objects))
performance = [34077,354311,99151,655642]
plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('Engagement')
plt.xlabel('Topic')
plt.title('Engagement for Astronomy Topics by NASA')
plt.show()

#Graph 3
# data to plot
n_groups = 4
means_frank = (34077, 55, 40, 65)
means_guido = (34077, 62, 54, 20)

# create plot
fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.35
opacity = 0.8

rects1 = plt.bar(index, means_frank, bar_width,
alpha=opacity,
color='b',
label='Frank')

rects2 = plt.bar(index + bar_width, means_guido, bar_width,
alpha=opacity,
color='g',
label='Guido')

plt.xlabel('Topics')
plt.ylabel('Likes and Retweets vs. Engagement')
plt.title('Likes and Retweets of NASA Tweets vs. Engagement')
plt.xticks(index + bar_width, ('Solar Eclipse', 'Black Holes', 'Aliens', 'Constellations'))
plt.legend()

plt.tight_layout()
plt.show()