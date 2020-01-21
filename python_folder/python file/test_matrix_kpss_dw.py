#statistic, p-value for adfuller
p_val_adf = []

# statistic and p-value for kpss
p_val_kpss = []

# statistic and p-value for acorr_breusch_godfrey 
p_val_bg = []

# statistic and p-value for durbin_watson
p_val_dw = []

for i in range(len(col_name)):
    temp = adfuller(df[col_name[i]], regression = 'ct')
    p_val_adf.append(temp[1])
    
    temp = kpss(df[col_name[i]], regression = 'ct')
    p_val_kpss.append(temp[1])
    
    temp = durbin_watson(df[col_name[i]])
    p_val_dw.append(temp)

test_matrix = pd.DataFrame(list(zip(col_name, p_val_adf, p_val_kpss, p_val_dw)), 
               columns =['Features','p_adftest', 'p_kpsstest','p_dwtest'])
