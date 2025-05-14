import statistics
import matplotlib.pyplot as plt
Estimates=[100,120,320,40,400,50,150]

y=[]
Estimates.sort()
tv=int(0.1*(len(Estimates)))

Estimates=Estimates[tv:]
Estimates=Estimates[:len(Estimates)-tv]
for i in range(len(Estimates)):
  y.append(5)
  plt.plot(Estimates,y,'r--')
  plt.plot([statistics.mean(Estimates)],[5],'ro')
  plt.plot([statistics.median(Estimates)],[5],'bs')
  plt.plot([375],[5],'g^')
  plt.ylabel()
  plt.xlabel()
  plt.show()
           
  
