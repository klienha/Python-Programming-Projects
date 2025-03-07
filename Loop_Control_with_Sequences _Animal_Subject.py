#helper function
def is_vertebrate(name, vertebrates):
    for vert in vertebrates:
        if name==vert:
            return True
    return False

def biggest_vertebrate(animals, weights, vertebrates):
    biggest = None
    biggest_i = None
    for i in range(len(animals)):
        if is_vertebrate(animals[i],vertebrates):
            if biggest_i==None or weights[i]>weights[biggest_i]:
                biggest_i = i
                biggest = animals[i]
    if biggest_i != None:
        return animals[biggest_i]
    return None


 
def within_weight(animals, weights, weightLimit):
    meets = []
    for i in range(len(animals)):
        if weights[i]<=weightLimit:
            meets.append(animals[i])
    return meets
    

def any_adjacent_vertebrates(animals, vertebrates):
    for i in range(len(animals)-1):
        if is_vertebrate(animals[i],vertebrates) and is_vertebrate(animals[i+1],vertebrates):
            return True
    return False
    


def count_weights(weight_list):
    counter = 0
    for i in range(0, len(weight_list)):
        for j in range(i+1, len(weight_list)):
            for s in weight_list:
                if weight_list[i]+weight_list[j] == s:
					#print(num_list[i], num_list[j])
                    counter += 1
                    break
    return counter