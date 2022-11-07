from arithmetic_arranger import arithmetic_arranger

def call_test():
    print("Testing")
    # test_too_many_problems
    print("Test 1 : ")
    print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49", "57 - 9", "421 - 30"]))
    #test_incorrect_operator
    print("Test 2 : ")
    print(arithmetic_arranger(["32 * 8", "1 - 3801", "9999 + 9999", "523 - 49"]))
    #test_too_many_digits
    print("Test 3 : ")
    print(arithmetic_arranger(["312452 + 8", "1 - 3801", "9999 + 9999", "523 - 49"]))
    #test_only_digits
    print("Test 4 : ")
    print(arithmetic_arranger(["3test2 + 8", "1 - 3801", "9999 + 9999", "523 - 49"]))
    #test_solutions
    print("Test 5 : ")
    print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
    #test_solutions
    print("Test 6 : ")
    print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"],True))

