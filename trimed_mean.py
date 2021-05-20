from statistics import mean
from scipy import stats
Estimates = [100,1010,1786,2000,1500,100,120,150,150,150,175,200,200,250,300,600,500,500,350,375,400,120,800,1000,450,320,800]
Estimates.sort()

m = stats.trim_mean(Estimates,0.1)
print(m)

# tv = int(0.1*len(Estimates))
# Estimates = Estimates[tv:]
# Estimates = Estimates[:len(Estimates)-tv]
# print(mean(Estimates))