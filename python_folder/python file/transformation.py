## 

# create a log transformed variable in df
for i in range(len(col_name)):
    df[col_name[i] + '_log'] =  np.log(df[col_name[i]])
    

df_test = df.drop(columns=['Time', 'DATE'])
col_name = df_test.columns
#col_name

# create a 1st diff transformed variable
def difference(dataset, interval = 1):
	diff = list()
	for i in range(interval, len(dataset)):
		value = dataset[i] - dataset[i - interval]
		diff.append(value)
	return diff

df1 = pd.DataFrame(df['Time'][1:117])
# create a log transformed variable in df1
for i in range(len(col_name)):
    df1[col_name[i] + '_1diff'] = difference(df[col_name[i]])
    

col_name1 = df1.drop(columns=['Time']).columns