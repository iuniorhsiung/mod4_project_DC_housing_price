def first_diff(data = res.predict(train_X), ini_value = df['Median Sale Price'][0]):
    pred_y = []
    pred_y.append(ini_value)
    for i in range(len(data)):
        temp = pred_y[i] + data[i+1]
        pred_y.append(temp)
    return pred_y 
