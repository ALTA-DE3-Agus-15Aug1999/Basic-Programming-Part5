def join_array_remove_duplicate(arrayA, arrayB):
    setA = set(arrayA)
    setB = set(arrayB)
    result_set = setA.union(setB)
    
    result = sorted(list(result_set), key=lambda x: (arrayA.index(x) if x in arrayA else len(arrayA) + arrayB.index(x)))
    
    # your code here
    return result

if __name__ == '__main__':
    # Test cases
    print(join_array_remove_duplicate(["apel", "anggur"], ["lemon", "leci", "nanas"]))
    # ["apel", "anggur", "lemon", "leci", "nanas"]


    print(join_array_remove_duplicate(["samsung", "apple"], ["apple", "sony", "xiaomi"]))
    # ["samsung", "apple", "sony", "xiaomi"]


    print(join_array_remove_duplicate(["football", "basketball"], ["basketball", "football"]))
    # ["football", "basketball"]
