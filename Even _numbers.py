def even_of_number():
    for x in range(1,21) :
        if x%2==0:
            print(x)
even_of_number()
even_of_number_comprehension=[ x for x in range(1,21) if x % 2 == 0 ]
print(even_of_number_comprehension)
