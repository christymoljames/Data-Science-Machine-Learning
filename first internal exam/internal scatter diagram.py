import matplotlib.pyplot as plt
import pandas as pd
math_marks = [38, 62, 18, 75, 38, 59, 66, 92, 52, 75]
english_marks = [74, 44, 85, 19, 88, 69, 50, 33, 29, 32]
marks_range = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
plt.scatter(marks_range, math_marks, label='Math marks', color='r')
plt.scatter(marks_range, english_marks, label='Science marks', color='g')
plt.title('Scatter Plot')
plt.xlabel('english')
plt.ylabel('Maths')
plt.legend()
plt.show()