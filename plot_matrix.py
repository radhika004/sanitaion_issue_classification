import pandas as pd
import matplotlib.pyplot as plt

results_path = 'runs/classify/train5/results.csv'



results = pd.read_csv(results_path)



plt.figure()
k=plt.plot(results['                  epoch'], results['             train/loss'],label='train loss')
p=plt.plot(results['                  epoch'], results['               val/loss'],label='val loss',c = 'red')

plt.grid()
plt.title('loss vs epochs')
plt.ylabel('loss')
plt.xlabel('epochs')
plt.legend()

plt.figure()
plt.show() 
