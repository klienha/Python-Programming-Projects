def break_time(hours_worn, last_break):
    
    result = 0
    while hours_worn > 0:
        val = hours_worn / last_break
        int_val = int(val)
        if val - int_val == 0:
            break
        else:
            hours_worn = int_val
            result += 1
    
    return result


def how_many_uruks(strength_values, init_fund_needed):
    budget = 0
    
    for val in strength_values:
        if val == 0:
            continue
        elif val % 2 == 0:
            budget *= val
        else:
            budget += val
    
    num_uruk = 0
    while True:
        if (budget - init_fund_needed) < 0:
            break
        
        budget = budget - init_fund_needed
        init_fund_needed += 1
        num_uruk += 1
    
    return num_uruk


def years_to_rule(n1, n2, n3):
    num_years = 0
    i = 1
    while i <= n1:
        j = 1
        while j <= n2:
            temp = i * j
            temp //= n3
            num_years += temp
            j += 1
        i += 1
    
    return num_years


def lotr_popularity(char_list):
    
    num_gandalf = 0
    num_aragorn = 0
    num_legolas = 0
    
    for char in char_list:
        if char == "Gandalf":
            num_gandalf += 1
        elif char == "Aragorn":
            num_aragorn += 1
        elif char == "Legolas":
            num_legolas += 1
        else:
            continue
    
    winner = ""
    if num_gandalf > num_aragorn and num_gandalf > num_legolas:
        winner = "Gandalf"
    elif num_aragorn > num_legolas and num_aragorn > num_gandalf:
        winner = "Aragorn"
    else:
        winner = "Legolas"
    
    popularity = (num_gandalf * 10) + (num_aragorn * 20) + (num_legolas * 5)
    
    return "Most Appeared: " + winner + ", Popularity: " + str(popularity)