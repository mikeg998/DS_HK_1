import pandas as pd
import matplotlib.pyplot as plt
from numpy import log
from sklearn import linear_model
from __future__ import division




#Question 1
mammals = pd.read_csv('/Users/TheG/DS_HK_1/data/class/mammals.csv')
mammals['log_body'] = log(mammals['body'])
mammals['log_brain'] = log(mammals['brain'])
body = [[x] for x in mammals['log_body'].values]
brain = mammals['log_brain'].values
regr.fit(body, brain)
plt.scatter(body, brain)
plt.plot(body, regr.predict(body), color='blue', linewidth=1)
plt.show()




#Question2
nytdata = pd.read_csv('./nyagg.csv')

"""Was stuck trying to use the following: Is this doing it the long way or incorrect?
   age = [[x] for x in nytData['Age'].values]
   gender = [[x] for x in nytData['Gender'].values]
I pulled the next line from your example
"""
age_gender = nytdata[['Age','Gender']].values


ctr = nytdata['Ctr'].values
regr = linear_model.LinearRegression()
regr.fit(age_gender,ctr)

#Last 2 lines are from your examples

print "SSE : %0.4f" % (mean((regr.predict(age_gender) - ctr) ** 2))
print "R2 : %0.4f" % (regr.score(age_gender, ctr))

#Getting a "mean is not defined" NameError. Is this because I haven't imported the right library?




"""Question3
Was quite lost on this one. Will need to study your example.

Same with Question4"""
