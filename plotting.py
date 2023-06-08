import os 
import matplotlib.pyplot as plt
print("------------_")
print()
print(os.getcwd() + "/src/nodecomh" + "/log_to_plot.txt")

values1 = []
values2 = []
  
f1 = open(os.getcwd() + "/src/nodecomh" + "/log_to_plot.txt","r")

f2 = open(os.getcwd() + "/src/nodecomx" + "/log_to_plot.txt","r")

for row in f1:
        value = row.strip()
        if value:  # Skip empty lines
            values1.append(float(value))

for row in f2:
        value = row.strip()
        if value:  # Skip empty lines
            values2.append(float(value))

plt.plot(values1)
plt.plot(values2)
plt.grid()
plt.show()

print(values1)