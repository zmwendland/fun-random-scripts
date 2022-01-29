import pandas as pd
import matplotlib.pyplot as plt

F = pd.read_csv('Ford Stock.csv')

F.set_index('Date', inplace=True, drop=True)

#Price Action
F['Close/Last'].plot(label='Ford Close',figsize=(16,6))
plt.legend()
plt.title('Ford Stock Price YTD')
plt.ylabel('Stock Price')
plt.show()

#Moving Average
F['Close/Last'].plot(figsize=(16,8))
F['MA30'] = F['Close/Last'].rolling(30).mean()
plt.title('Ford Stock Price 30D Moving Average YTD'()
plt.ylabel('Stock Price')
F['MA30'].plot()

#Returns
F['Returns'] = (F['Close/Last']/F['Close/Last'].shift(1))-1
F['Returns'].hist(bins=50)
plt.title('Ford Daily Returns YTD')
plt.show()



