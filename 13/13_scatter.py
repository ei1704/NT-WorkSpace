import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

stu_score = pd.read_csv('test_score.csv')

#subs = ["国語","数学","英語","理科","社会"]
subs = list(pd.DataFrame(stu_score))[3:]

fig, ax = plt.subplots(5,5,tight_layout=True)

for i in range(5):
  for j in range(5):
    ax[i,j].tick_params(labelsize=5)
    ax[i,j].set_xlabel(subs[i], fontname="MS Gothic",fontsize="5")
    ax[i,j].set_ylabel(subs[j], fontname="MS Gothic",fontsize="5")
    ax[i,j].grid(True)
    ax[i,j].scatter(stu_score[subs[j]],stu_score[subs[i]])

#イメージの保存
plt.savefig('13_Fig.png') 
plt.show()
