
import statistics
import matplotlib.pyplot as plt
#red dots: ro, red dashes: r--, blue_squares: bs, green_triangles: g^

Estimates = [1000,1010,1786,2000,1500,100,120,150,150,150,175,200,200,250,300,600,500,500,350,375,400,120,800,1000,450,320,800]
y = []

Estimates.sort()
tv = int(0.1*len(Estimates))
Estimates = Estimates[tv:]
Estimates = Estimates[:len(Estimates)-tv]

for i in range(len(Estimates)):
    y.append(5)
plt.plot(Estimates,y,'r--')
plt.plot([statistics.mean(Estimates)],[5],'ro')
plt.plot([statistics.median(Estimates)],[5],'bs')
plt.plot([450],[5],'g^')