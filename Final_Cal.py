import matplotlib.pyplot as plt
import numpy as np
np.random.seed(123)
all_walks = []
for i in range(500) :
    random_walk = [0]
    for x in range(100) :
        step = random_walk[-1]
        dice = np.random.randint(1,7)
        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)
        random_walk.append(step)
    all_walks.append(random_walk[-1])

# Convert all_walks to Numpy array: np_aw
np_aw=np.array(all_walks)
#list which shows walks greater then or equal to 60
l = np_aw[np_aw>=60]

#list
print(l)

#length of list
print(len(l))

#chances to get equal to 60 or greater then 60 in 500 chance
print(len(l)/500*100)
