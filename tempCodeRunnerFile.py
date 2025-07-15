import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Create sample data using numpy
x = np.arange(1, 6)  # [1, 2, 3, 4, 5]
y = x ** 2           # Square of x

# Create a DataFrame
data = pd.DataFrame({'X values': x, 'Y = X^2': y})

# Plot the graph
plt.plot(data['X values'], data['Y = X^2'], marker='o', color='blue', label='Y = X^2')
plt.title('Simple Line Graph 📈')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.legend()
plt.grid(True)
plt.show()
