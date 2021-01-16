import pandas as pd
import numpy as np


def dot():
    print("**********************************************************")

x_list = []
y_list = []

total_entries = int(input("enter the number of entries: "))

for i in range(total_entries):
    xin = float(input(" enter the value for x: "))
    x_list.append(xin)
dot()
for i in range(total_entries):
    yin = float(input(" enter the value for y: "))
    y_list.append(yin)

my_dict = {"x": x_list, "y": y_list}
file = pd.DataFrame(my_dict)

# for adding serial numbers to the dataset
def setIndex(df):
    df['sr_no'] = np.arange(1, df.shape[0] + 1)
    df.set_index('sr_no', inplace=True)
setIndex(file)

def filemodifier(file):
    file["xy"] = file.x * file.y
    file['x2'] = file.x ** 2
    file['y2'] = file.y ** 2
    return file
filemodifier(file)

def total(file):
    l = list(file.x)
    return len(l)
N = total(file)

def meanx(file):
    return file.x.sum() / N

def meany(file):
    return file.y.sum() / N

x_bar = meanx(file)
y_bar = meany(file)

sigmax = ((file.x2.sum() / N) - x_bar ** 2) ** 0.5
sigmay = ((file.y2.sum() / N) - y_bar ** 2) ** 0.5

cov = (file.xy.sum() / N) - (x_bar * y_bar)

coeff_of_correlation = cov / (sigmax * sigmay)

byx = coeff_of_correlation * (sigmay / sigmax)
bxy = coeff_of_correlation * (sigmax / sigmay)

dot()
print(file)
dot()

print('sum of x: '+str(file.x.sum()))
print('sum of y: '+str(file.y.sum()))
print('sum of x2: '+str(file.x2.sum()))
print('sum of y2: '+str(file.y2.sum()))
print('sum of xy: '+str(file.xy.sum()))
dot()

print("mean of x: " + str(x_bar) + '\n' +
      "mean of y: " + str(y_bar) + '\n' +
      "standard deviation of x: " + str(sigmax) + '\n' +
      "standard deviation of y: " + str(sigmay) + '\n' +
      "covariance(x,y): " + str(cov) + '\n' +
      "byx: " + str(byx) + '\n' +
      "bxy: " + str(bxy) + '\n' +
      "the Coefficien of correlation: " + str(coeff_of_correlation))
dot()
print("the lines of regression are: ")
print('y = ' + str(byx) + 'x +' + str(y_bar - (byx * x_bar)))
print('x = ' + str(bxy) + 'y +' + str(x_bar - (bxy * y_bar)))