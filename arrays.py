#CTCI #1 Implement an algorithm to determine if a string has all unique characters. 
#What if you cannot use additional data structures
def check_string_uniqueness(string):
    #METHOD 1 - using a dictionary

    # dct = {}
    # for char in string:
    #     if char in dct:
    #         return False
    #     else:
    #         dct[char] = char
    # return True

    #METHOD 2 - using a set

    # new_set = set()
    # for char in string:
    #     if char in new_set:
    #         return False
    #     else:
    #         new_set.add(char)
    # return True

    #METHOD 3 - using no additional data structures
    for i in range(len(string)):
        for j in range(i+1, len(string)):
            if string[i] == string[j]:
                return False
    return True

    #Time complexity is O(n) 
                
    
print(check_string_uniqueness('string'))
print(check_string_uniqueness('aba'))

assert check_string_uniqueness('string') == True
assert check_string_uniqueness('bb') == False

#1.2 Given two strings, write a method to decide if one is a permutation of the other. (have the same characters)

#Question to ask:
    #does white space make a difference?
    #does capitalization make a difference?

def check_str_permutation(str1, str2): 


    #Method 1: (without sorting)
        
    # str1 = str1.replace(" ", "")
    # str2 = str2.replace(" ", "")

    # for char in str1:
    #     if char in str2:
    #         str2 = str2.replace(char, "", 1)
    # return len(str2) == 0
    

    #Method 2: (without sorting)
    # NO_OF_CHARS = 256

    # count1 = [0] * NO_OF_CHARS 
    # count2 = [0] * NO_OF_CHARS 
    
  
    # # For each character in input strings, 
    # # increment count in the corresponding 
    # # count array 
    # str1 = str1.replace(" ", "")
    # str2 = str2.replace(" ", "")
    # for i in str1: 
    #     count1[ord(i)]+=1
  
    # for i in str2: 
    #     count2[ord(i)]+=1
  
    # # If both strings are of different length. 
    # # Removing this condition will make the  
    # # program fail for strings like 
    # # "aaca" and "aca" 
    # if len(str1) != len(str2): 
    #     return False
  
    # # Compare count arrays 
    # for i in range(len(count1)): 
    #     if count1[i] != count2[i]: 
    #         return False
    # return True
    
    #Method 3 (with sort)
    # return sorted(str1.replace(" ", "").lower()) == sorted(str2.replace(" ", "").lower())

    #Method 4 (O(n))
    NO_OF_CHARS = 256

    count = [0] * NO_OF_CHARS 

    str1 = str1.replace(" ", "").lower() #This accounts for spaces and uppercase
    str2 = str2.replace(" ", "").lower()
    for i in str1: 
        count[ord(i)]+=1
 
    for i in str2: 
        count[ord(i)]-=1
  
    if len(str1) != len(str2): 
        return False
  
    for i in range(len(count)): 
        if count[i] != 0:
            return False
    return True
    #"Time complexity of this method depends upon the sorting technique used. In the above implementation, quickSort is used which may be O(n^2) in worst case. If we use a O(nLogn) sorting algorithm like merge sort, then the complexity becomes O(nLogn)"

# print(check_str_permutation('1a@!34Bc hello', 'bc134a@! elloh'))
# print(check_str_permutation('cat', 'taco'))

assert check_str_permutation('1a@!34Bc hello', 'bc134a@! elloh') == True
assert check_str_permutation('abc', 'bca') == True
assert check_str_permutation('cat', 'taco') == False


#1.3 URLify Replace all spaces in a string with '%20'


#1.4 Palindrome Permutation

#racecar #if the length is odd, one is odd the rest have a pair
#caac #if the length is even, same letter of chars
def is_palindrome_perm(string):
    string = string.replace(" ", "").lower()
    print(string)
    
    d = {}
    for char in string:
        if char not in d:
            d[char] = 1
        else:
            d[char] += 1
    
    if len(string) % 2 != 0: #odd
        for char in string:
            if d[char] % 2 == 0:
                string = string.replace(char, "")
        return len(string) == 1
    else: #even
        for char in string:
            if d[char] % 2 != 0:
                return False
        return True
        
        
print(is_palindrome_perm('Tact Coa'))
print(is_palindrome_perm('moom'))

assert is_palindrome_perm('racecar') == True
assert is_palindrome_perm('race car') == True
assert is_palindrome_perm('tactcoapapa') == True


