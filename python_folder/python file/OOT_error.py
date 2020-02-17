temp = res.predict(test_X).reset_index()[0]
temp.index += 1
pred_y_oot = first_diff(data = temp, ini_value = df['Median Sale Price'][100])
error_oot = df["Median Sale Price"][100:117] - pred_y_oot[1:18]
