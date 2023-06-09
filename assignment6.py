#
# Covariance for Python program
#
import statistics, math


def my_covariance(input_x, input_y):
    print(f'Input x :{input_x},Input y :{input_y}')
    length=len(input_x)
    cov = 0
    sum = 0
    
    meanx = statistics.mean(input_x)
    meany = statistics.mean(input_y)
    print(f'Mean x :{meanx},Mean y :{meany}')
    for index in range (len(input_x)):
       sum += (input_x[index]-meanx)*(input_y[index]-meany)
    cov = sum / length
    return cov



# 1. Input
input_x = [10,20,30]
input_y = [12,21,33]

# 2. Process
answer = my_covariance(input_x, input_y)
answer = round(answer, 2)

# 3. Output
print(f'Covariance: {answer}')
