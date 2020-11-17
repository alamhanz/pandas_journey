data = pd.read_csv(PATH_DATA+'votes.csv')
data['voteDate'] = pd.to_datetime(data.voteDate)
data['date_day'] = data['voteDate'].dt.strftime('%Y-%m-%d')
data2 = data.groupby(['employee','date_day']).vote.mean().reset_index()
data2['employee'] = data2['employee'].astype(int)

for i in range(9000):
    x = random.randint(10,120000)
    data2['vote'].loc[x] = np.NaN
    
for i in range(300):
    x = random.randint(10,120000)
    data2['employee'].loc[x] = np.NaN
    
for i in range(100):
    x = random.randint(10,120000)
    data2['date_day'].loc[x] = np.NaN
    
for i in range(200):
    x = random.randint(10,120000)
    data2['vote'].loc[x] = np.random.normal(loc = 0.5, scale = 0.8)
    
for i in range(200):
    x = random.randint(10,120000)
    data2['vote'].loc[x] = np.random.normal(loc = 5, scale = 2)
    
d1 = data2.sample(80000)
d2 = data2.sample(60000)
data3 = pd.concat([d1,d2])
data3 = data3.reset_index()
del data3['index']

data3.columns = ['x_id','date_day','x_value']
data3.to_csv(PATH_DATA+'unclean_data.csv',index = False)