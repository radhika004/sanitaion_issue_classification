plt.figure()
plt.plot(results['                  epoch'], results['             train/loss'],label='train loss')
plt.plot(results['                  epoch'], results['               val/loss'],label='val loss',c = 'red')

plt.grid()
plt.title('loss vs epochs')
plt.ylabel('loss')
plt.xlabel('epochs')
plt.legend()

plt.figure()
plt.show() 