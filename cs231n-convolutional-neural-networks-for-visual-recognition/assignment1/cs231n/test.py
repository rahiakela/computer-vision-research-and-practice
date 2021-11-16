import numpy as np

data = np.array([
    [1.00,	1.04],
    [2.00,	2.04],
	[2.64,	2.70],
	[3.16,	3.22],
	[3.60,	3.67],
	[4.00,	4.07],
	[4.35,	4.44],
	[4.69,	4.77],
	[5.00,	4.88]
])

all_errors = 0
for i in range(len(data)):
  error = (data[i][0] - data[i][1]) ** 2
  all_errors += + error
print(all_errors)
