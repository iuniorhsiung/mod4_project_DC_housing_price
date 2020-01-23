def hypo_test(col_name = col_name, data = df):
    # p-value for adfuller
    p_val_adf = []
    
    # p-value for kpss
    p_val_kpss = []

    # p-value for acorr_breusch_godfrey 
    p_val_bg = []

    # p-value for Ljung–Box Q test
    p_val_lj = []

    # statistic for durbin_watson
    stat_dw = []
    for i in range(len(col_name)):
        temp = adfuller(data[col_name[i]], regression = 'ct')
        p_val_adf.append(temp[1])
    
        temp = kpss(data[col_name[i]], regression = 'ct')
        p_val_kpss.append(temp[1])
    
        temp = acorr_ljungbox(data[col_name[i]], lags = 10)
        p_val_lj.append(temp[1][0])
    
        temp = durbin_watson(data[col_name[i]])
        stat_dw.append(temp)
        
    test_matrix = pd.DataFrame(list(zip(col_name, p_val_adf, p_val_kpss, p_val_lj, stat_dw)), 
               columns =['Features','p_adftest', 'p_kpsstest','p_ljtest', 'stat_dw'])
    return test_matrix