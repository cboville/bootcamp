import numpy as np
import matplotlib.pyplot as plt

#import seaborn and set default
import seaborn as sns
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728',
          '#9467bd', '#8c564b', '#e377c2', '#7f7f7f',
          '#bcbd22', '#17becf']
sns.set(style='whitegrid', palette=colors, rc={'axes.labelsize': 16})

def ecdf(data):
    x=np.sort(data)
    y=np.arange(1,len(data)+1)/len(data)
    return x,y

data=np.loadtxt('data/xa_high_food.csv', comments='#')
ldata=np.loadtxt('data/xa_low_food.csv', comments='#')

x_data, y_data=ecdf(data)
x_ldata, y_ldata=ecdf(ldata)

fig, ax=plt.subplots(1,1)
_=ax.set_xlabel('eggs')
_=ax.set_ylabel('probability')

_=ax.plot(x_data, y_data, marker='.', linestyle='none')
_=ax.plot(x_ldata, y_ldata, marker='.', linestyle='none')

plt.show()
