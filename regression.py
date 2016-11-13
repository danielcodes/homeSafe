
# find the width of the buffer based on the wind parameter
# first gotta create points to plot (wind mph, hurricane category)
# for the input, the user will tell the category of the hurricane and the max wind
# then create a range for the wind, usually max+-(max/2)

import json
from sklearn import datasets, linear_model
from numpy import array

categoryLevels = {'LOW': 0, 'TROPICAL DEPRESSION': 0, 'TROPICAL STORM': 0, 
                  'EXTRATROPICAL STORM': 0, 'EXTRATROPICAL DEPRESSION': 0, 'EXTRATROPICAL STORM-1': 1,
                  'HURRICANE-1': 1, 'HURRICANE-2': 2, 'HURRICANE-3': 3,
                  'HURRICANE-4': 4, 'HURRICANE-5': 5}

# can be adjusted
windToWidth = {0: 0.5, 1: 0.5, 2: 1.0, 3: 1.5, 4: 2.0, 5: 2.5}

# two mappings
# wind -> cat
# wind -> width
with open('katrina.json') as a, open('matthew.json') as b, open('sandy.json') as c:    
    # list of each step of the hurricane
    # interested in wind -> hurricane level
    d1 = json.load(a)
    d2 = json.load(b)
    d3 = json.load(c)

    winds = []
    widths = []
    # every set is diff size
    # first map everything to a list of tuples
    # need to skip col titles
    for i in range(1, len(d1)):
        # print data[i][' WIND'], data[i]['STAT']
        # so first map cat-string->cat and then cat->width, can't modify tuples so.. 
        winds.append(d1[i][' WIND'])
        widths.append(windToWidth[categoryLevels[d1[i]['STAT']]])

    for j in range(1, len(d2)):
        winds.append(d2[j][' WIND']) 
        widths.append(windToWidth[categoryLevels[d2[j]['STAT']]])

    for k in range(1, len(d3)):
        winds.append(d3[k][' WIND']) 
        widths.append(windToWidth[categoryLevels[d3[k]['STAT']]])


# everything is training data
# use regr.predict() to get values
regr = linear_model.LinearRegression()
regr.fit(array(winds).reshape(-1, 1), array(widths).reshape(-1, 1))

# export it as a function
def findWidth(widthSpeed):
    # returns list of lists
    return regr.predict(widthSpeed)



