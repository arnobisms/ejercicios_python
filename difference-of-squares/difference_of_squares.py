def square_of_sum(numero):
    sum = 0
    for i in range(numero+1):
        sum += i
    return (sum * sum)



def sum_of_squares(numero):
    sum = 0
    for i in range(numero+1):
        sum += (i * i)
    return sum



def difference_of_squares(numero):
    return ((square_of_sum(numero)) - (sum_of_squares(numero)))