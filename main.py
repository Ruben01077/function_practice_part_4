print("========================================")
def max_num(*a):

    maxNum=0
    for i in a:
      if i > maxNum:
        maxNum = i
    print(f"The max number from three number is {maxNum}")

max_num(22,43,67)

print("========================================")

def mult_list(*a):

    result = 1

    for i in a:
        if result > 0:
         result = result * i 
    print(f"The result is {result}")

mult_list(2,5,2,5,10)

print("========================================")

def rev_string(*args):
  
  for i in args:
   str_rev =i[::-1]
   
   print(str_rev.capitalize())
         
rev_string("Ruben")

print("========================================")

def num_within(a,c,b):
  print(a in range(c,b+1))
     
num_within(3,2,40)    

print("========================================")

triangle = [[1],[1,1]]
def pascal(n):

  if n < 1:
    print("invalid number of rows")
  elif n == 1:
    print(triangle[0])
  else:
    row_number = 2 
    
    while len(triangle) < n:
      row = []
      row_prev = triangle[row_number - 1]
    
      length = len(row_prev)+1
      for i in range(length):
       
        if i == 0:
          row.append(1)
      
        elif i > 0 and i < length-1:
          row.append(triangle[row_number-1][i-1]+triangle[row_number-1][i])
    
        else:
          row.append(1)
      triangle.append(row)
      row_number += 1

  
    for row in triangle:
      print(row)


pascal(11)


print("========================================")