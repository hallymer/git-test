# add program
def sum_function( n1 , n2): # 두 정수의 합을 구하는 함수
    return n1 + n2

num1 = int ( input("input number 1") )
num2 = int ( input("input number 2") )

sum = sum_function( num1 , num2)

print(num1 , "+" , num2 , "=" , sum )
