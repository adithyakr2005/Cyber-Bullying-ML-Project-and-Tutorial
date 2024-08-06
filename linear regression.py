import matplotlib.pyplot as plt
from scipy import stats

x = [5,6,7,8,9,11,12,15,17,18,19,20]
y = [10,12,14,16,18,22,24,30,34,36,38,40]
slope, intercept, r, p, std_err = stats.linregress(x, y)

def myfunc(x):
  return slope * x + intercept

mymodel = list(map(myfunc, x))

plt.scatter(x, y)
plt.plot(x, mymodel)
plt.show()
