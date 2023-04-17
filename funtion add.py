def my_add (input):
    sum=1
    for x in input:
        sum *=int(x)
    return sum

#Input
input=[10,20,30]

#process
answer=my_add(input)

#output
print(f'anwser:{answer}')

input=[874,345,623,6345,13423,6434]

#process
answer=my_add(input)

#output
print(f'anwser:{answer}')


