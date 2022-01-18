import numpy as np
import matplotlib.pyplot as plt
from sklearn import preprocessing
import scipy.optimize

NDVI = [0.11297952701146294, 0.10463243479952597, 0.10271533158016358, 0.11610425681015422, 0.1139359907584328, 0.0985856971250338, 0.10441799906012686, 0.10099830027367467, 0.09261755659354609, 0.09408055616942715, 0.0989224794119312, 0.0934717545232658, 0.08919097151876965, 0.08589310194156752, 0.08452600505932445, 0.08370755329742853, 0.08572898762682432, 0.0789714429285833, 0.08973785278932943, 0.0844367045036737] # len 20

def sigmoid(p,x):
  # logistic curve equation
    x0,y0,c,k=p
    y = c / (1 + np.exp(-k*(x-x0))) + y0
    return y

def residuals(p,x,y):
  # difference between observed value of the response variable and the value of the response variable predicted from the regression line
    return y - sigmoid(p,x)

# define variables
NDVI = preprocessing.normalize([NDVI])[0]
y = NDVI
x = preprocessing.normalize([np.arange(20)])[0]
print(x)
print(y)

p_guess=(np.median(x),np.median(y),1.0,1.0) # initial guess
# least squares to look for best parameters to fit curve
p, cov, infodict, mesg, ier = scipy.optimize.leastsq(
    residuals,p_guess,args=(x,y),full_output=1) 

# print parameters
x0,y0,c,k=p
print('''\
x0 = {x0}
y0 = {y0}
c = {c}
k = {k}
'''.format(x0=x0,y0=y0,c=c,k=k))

xp=np.linspace(0,max(x),2000)
pxp=sigmoid(p, xp)

# Plot results
plt.title("NDVI vs Time")
plt.plot(x, y, '.', xp, pxp, '-')
plt.xlabel('Time')
plt.ylabel('NDVI')
plt.grid(True)
plt.show()
