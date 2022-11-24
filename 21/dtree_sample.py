from sklearn.datasets import *
from sklearn import tree
from dtreeviz.trees import *

regr = tree.DecisionTreeRegressor(max_depth=2)
boston = load_boston()
regr.fit(boston.data, boston.target)

viz = dtreeviz(regr,
               boston.data,
               boston.target,
               target_name='price',
               feature_names=boston.feature_names)
              
#viz.view()
viz.save('dtree_sample.svg')