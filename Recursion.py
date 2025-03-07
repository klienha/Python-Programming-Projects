#Given two integers num1 and num2, calculate and return how many times you get a fraction when you divide num1 by num2.
def fraction_count(num1, num2):
	
    val = num1 / num2
    int_val = int(val)
    
    if val - int_val == 0:
        return 0 
		
    return 1 + fraction_count(int_val, num2)

#Given two strings str1 and str2, concatenate characters of the two strings in the following order and return the concatenated string:
def concat_order(str1, str2):
    
    if len(str1) == 0:
        return ""
    
    return str1[0] + str2[0] + concat_order(str1[1:], str2[1:])

#Given a list of integers some_list, and two integers i and j, where i is a starting index value and j is an ending index value; calculate and return the sum of product of the elements in some_list between i and j in the following manner:
#(some_list[i] * some_list[j]) + (some_list[i+1] * some_list[j-1]) +
#(some_list[i+2] * some_list[j-2]) +
def sum_product(some_list, i, j):
    
    if i > j or len(some_list) == 0:
        return 0
    if i == j:
        return some_list[i]
    
    return some_list[i] * some_list[j] + sum_product(some_list, i + 1, j - 1)

#Given a list of integers some_list and an integer res, sequentially look at each element of some_list. If the element is an odd number, add that to res; if the element is an even number, multiply that to res; ignore the element if it is 0. Return the final value in res after you looked at every element of some_list.
def calc_res(some_list, res=0):
    
    if len(some_list) == 0:
        return res
    
    if some_list[0] == 0:
        res = calc_res(some_list[1:], res)
    elif some_list[0] % 2 == 0:
        res = calc_res(some_list[1:], res * some_list[0])
    else:
        res = calc_res(some_list[1:], res + some_list[0])
    
    return res
