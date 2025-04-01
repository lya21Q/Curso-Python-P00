numbers=[1,2,3]
def find_average(numbers):
    sum=0
    cantidad=0
    if numbers == "":
        return 0
    else:
        for i in numbers:
            sum+=i
            cantidad+=1
        prom=sum/cantidad
        return prom
print(find_average(numbers))