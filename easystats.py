import pandas as pd
import numpy as np
def line():
    print("-----------------------------------------------------------------------")

def filemaker():
    total_entries = int(input("enter the total number of entries: "))
    class_width = int(input("enter the class width: "))
    l1 = int(input("enter the first lower limit: "))
    lower_limit = [l1]
    upper_limit = []

    for i in range(total_entries - 1):
        l1 += class_width
        lower_limit.append(l1)
    for i in lower_limit:
        i += class_width
        upper_limit.append(i)

    my_dict = {"LowLimit": lower_limit, "UpLimit": upper_limit}
    file = pd.DataFrame(my_dict)

    # for adding serial numbers to the dataset
    def setIndex(df):
        df['sr_no'] = np.arange(1, df.shape[0] + 1)
        df.set_index('sr_no', inplace=True)

    setIndex(file)
    frequency = []
    for i in range(total_entries):
        freq = int(input("enter the frequency: "))
        frequency.append(freq)
    file["freq"] = frequency
    return file
file = filemaker()

def fileModifier(file):
    file['x'] = (file.LowLimit + file.UpLimit) / 2
    file['x2'] = (file.x) ** 2
    file['fx'] = file.freq * file.x
    file['cf'] = file.freq.cumsum()
    file['fx2'] = file.freq * file.x2
fileModifier(file)

# mean
def mean(file):
    return file.fx.sum() / file.freq.sum()

# for median
def class_width(file):
    class_width = file.UpLimit - file.LowLimit
    w = list(set(class_width))
    return w[0]
class_width(file)

def LowerLimitOfMedianclass(file):
    n = file.freq.sum() / 2
    small_list = []
    for i in file.cf:
        if i > n:
            small_list.append(i)
    small_list.sort()
    c = small_list[0]
    list1 = list(file.cf)
    for i in list1:
        if i == c:
            index = list1.index(c)
    list2 = list(file.LowLimit)
    return list2[index]
LowerLimitOfMedianclass(file)

def cfofclasspreceedingmedianclass(file):
    n = file.freq.sum() / 2
    small_list = []
    for i in file.cf:
        if i > n:
            small_list.append(i)
    small_list.sort()
    c = small_list[0]
    list1 = list(file.cf)
    for i in list1:
        if i == c:
            index = list1.index(c)
    list2 = list(file.cf)
    return list2[index - 1]
cfofclasspreceedingmedianclass(file)

def frequencyOfMedianClass(file):
    n = file.freq.sum() / 2
    small_list = []
    for i in file.cf:
        if i > n:
            small_list.append(i)
    small_list.sort()
    c = small_list[0]
    list1 = list(file.cf)
    for i in list1:
        if i == c:
            index = list1.index(c)
    list2 = list(file.freq)
    return list2[index]
frequencyOfMedianClass(file)

def median(file):
    l = LowerLimitOfMedianclass(file)
    h = class_width(file)
    N = file.freq.sum() / 2
    c = cfofclasspreceedingmedianclass(file)
    f = frequencyOfMedianClass(file)
    m = l + (h / f) * (N - c)
    return m

# mode
def mode(file):
    l1 = list(file.freq)
    index = 0
    for i in l1:
        if i == file.freq.max():
            index = l1.index(i)
    l2 = list(file.LowLimit)
    l = l2[index]
    f1 = file.freq.max()
    f0 = l1[index - 1]
    f2 = l1[index + 1]
    h = class_width(file)
    mode = l + ((h * (f1 - f0)) / (2 * f1 - f0 - f2))
    return mode

# standard deviation
def standardDeviation(file):
    return (file.fx2.sum() / file.freq.sum() - mean(file) ** 2) ** (1 / 2)

# coefficients of variation
def CV(file):
    return standardDeviation(file) / mean(file) * 100

am = mean(file)
m = median(file)
M = mode(file)
sigma = standardDeviation(file)
cv = CV(file)
line()

print("mean: \t" + str(am) + "\n" + "median: \t" + str(m) +
      "\n" + "Mode: \t" + str(M) + "\n" + "Standard deviation: \t" + str(sigma) + "\n" + "Coefficient of Variation: \t" + str(
    cv) + "\n")
