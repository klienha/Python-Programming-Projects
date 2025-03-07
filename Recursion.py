def fraction_count(num1, num2):
	
    val = num1 / num2
    int_val = int(val)
    
    if val - int_val == 0:
        return 0 
		
    return 1 + fraction_count(int_val, num2)


def concat_order(str1, str2):
    
    if len(str1) == 0:
        return ""
    
    return str1[0] + str2[0] + concat_order(str1[1:], str2[1:])


def sum_product(some_list, i, j):
    
    if i > j or len(some_list) == 0:
        return 0
    if i == j:
        return some_list[i]
    
    return some_list[i] * some_list[j] + sum_product(some_list, i + 1, j - 1)


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