import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

## To make the numpy array values readable
np.set_printoptions(suppress=True)


#y=a+bx+cx^2+dx^3+......
degree=input("what is the degree of polynomial to model data?")


# load the csv into a dataframe using panda and rename the columns
df=pd.read_csv('heat_capaacity_ethane.csv')
df.columns=["y", "x"]

#extract the dataframe series into a numpy array
y=df["y"].values
x=df["x"].values

# make another scale for x inorder to plot our regression model
max_x=np.max(x)
min_x=np.min(x)
X=np.linspace((min_x-0.1*min_x),(max_x+0.01*max_x),1000)

# trying to populate the matrix we would use to solve our regression model(check matrix formula for regression)
B=np.ones(len(y))
for n in range(1,degree+1):
	B=np.c_[B,x**n]

# using linear algebra to find our coefficients for the model
sol=np.linalg.solve(B.T@B, B.T@y)
print(sol)
# populating the values to be plotted in an array

Y=0
for n in range(len(sol)):
	Y+=sol[n]*(X**(n))


#plotting all

plt.plot(x,y,"o",color="Black",label="experimental values")
plt.plot(X,Y,"-",color="Blue",label="polynomial regression")


plt.legend()

plt.show()