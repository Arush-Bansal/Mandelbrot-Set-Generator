import matplotlib.pyplot as plt
data = [
    [False, False, False, False, False, False, False], 
    [False, False, False, True, False, False, False], 
    [False, False, False, True, False, False, False], 
    [False, False, True, True, True, False, False], 
    [False, False, False, False, False, False, False], 
    [False, False, False, False, False, False, False], 
    [False, False, False, False, False, False, False]
]


plt.imshow(data, cmap='hot')
plt.show()