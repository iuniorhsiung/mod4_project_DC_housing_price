df_temp = pd.read_csv("../data/full_data.csv")
temp = pred_y + pred_y_oot[1:18]
temp = pd.Series(temp)
df_predict = pd.DataFrame(df_temp['Time'])
df_predict["Median Sale Price"] = df["Median Sale Price"]
df_predict['In Time'] = pd.Series(temp, index=df1.index)
df_predict['OOT Time'] = df_predict['In Time']
index = pd.date_range("2 1 2010", periods=117,
                      freq="m", name="date")
data_temp = df_predict[["Median Sale Price", "In Time", "OOT Time"]]
predict_m = pd.DataFrame(data_temp, index)
predict_m["Median Sale Price"] = np.array(df["Median Sale Price"])
predict_m["In Time"] = np.array(temp)
predict_m["OOT Time"] = np.array(temp)
predict_m['In Time'][100:117] = np.NaN
predict_m['OOT Time'][0:100] = np.NaN
predict_m.to_csv('../data/predict_m.csv')