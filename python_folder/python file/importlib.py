#Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import linear_model
import statsmodels.api as sm
from statsmodels.compat import lzip

%matplotlib inline

# feature selection: KBest using f_regression, chi2, mutual_info_regression
from sklearn.feature_selection import SelectKBest, f_classif, f_regression, chi2, mutual_info_regression

# tests for stationary 
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.stattools import kpss

import statsmodels.api as sm

#tests for autocorrelation
from statsmodels.stats.diagnostic import acorr_breusch_godfrey
from statsmodels.stats.stattools import durbin_watson
from statsmodels.stats.diagnostic import acorr_ljungbox

#test of Heteroscedasticity
from statsmodels.stats.diagnostic import het_breuschpagan
from statsmodels.stats.diagnostic import het_goldfeldquandt

#test for cointegration
from statsmodels.tsa.vector_ar.vecm import coint_johansen 

df = pd.read_csv("../data/full_data.csv")

df_test = df.drop(columns=['Time', 'DATE', 'Median Sale Price MoM', 'New Listings MoM', 'Homes Sold MoM', 'Inventory MoM', 'Days on Market MoM', 'Average Sale To List MoM', 'DC_PER'])
col_name = df_test.columns

# create a log transformed variable
for i in range(len(col_name)):
    df[col_name[i] + '_log'] =  np.log(df[col_name[i]])
    
# Create a col list for hypothesis testing
df_test = df.drop(columns=['Time', 'DATE'])
col_name = df_test.columns
col_name
