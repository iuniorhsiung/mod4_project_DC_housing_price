# Feature selection using KBest
# https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectKBest.html?highlight=selectkbest#sklearn.feature_selection.SelectKBest

from sklearn.feature_selection import SelectKBest, f_classif, f_regression, chi2, mutual_info_regression
bestfeatures = SelectKBest(score_func = f_regression , k = 10)  # change score_func to chi2, mutual_info_regression
fit = bestfeatures.fit(train_x,train_y)
dfscores = pd.DataFrame(fit.scores_)
dfcolumns = pd.DataFrame(train_x.columns)
#concat two dataframes for better visualization 
featureScores = pd.concat([dfcolumns,dfscores],axis=1)
featureScores.columns = ['Specs','Score']  #naming the dataframe columns
print(featureScores.nlargest(10,'Score'))  #print 10 best features
