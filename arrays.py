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

#1.5 One Away
#replace, insert, remove
def check_one_away(str1, str2):
    #make str1 the bigger one
    if len(str2) > len(str1):
        temp = str2
        str2 = str1
        str1 = temp
    
    if len(str1) == len(str2):
        for i in range(len(str2)):
            if str2[i] in str1:
                str1 = str1.replace(str2[i], "", 1)
        return len(str1) == 1 or len(str1) == 0
    elif len(str1) == (len(str2)+1):
        return check_length(str1, str2) 
    elif (len(str1)-1) == (len(str2)):
        return check_length(str1, str2)
    return False
        

def check_length(str1, str2):
    for i in range(len(str2)):
        if str2[i] in str1:
            str1 = str1.replace(str2[i], "", 1)
    return len(str1) == 1

assert (check_one_away('pale', 'pale')) == True
assert(check_one_away('kale', 'pale')) == True

assert(check_one_away('pale', 'ple')) == True
assert(check_one_away('pales', 'pale')) == True
assert(check_one_away('pale', 'pales')) == True

assert(check_one_away('ple', 'pale')) == True
assert(check_one_away('pale', 'bake')) == False
assert(check_one_away('pale', 'bakessss')) == False
        
#1.6 String Compression
def compress_str(string):
    lst = []
    count = 1 
    for i in range(1, len(string)):
        if string[i] != string[i-1]:
            add_to_list(lst, string[i-1], count)
            count = 1
        else:
            count += 1
    add_to_list(lst, string[-1], count)
    return ''.join(lst)

def add_to_list(lst, string, count):
    lst.append(string)
    lst.append(str(count))
        
print(compress_str('aabcccccaaa'))
assert compress_str('aabcccccaaa') == 'a2b1c5a3'

#1.7 Rotate matrix by 90
def rotate_matr_90(matr):
    n = len(matr[0])
    for i in range(n):
        for j in range(i+1, n):
            matr[i][j], matr[j][i] = matr[j][i], matr[i][j]
        matr[i].reverse()
    return matr

print(rotate_matr_90([  [1, 2, 3],
                        [4, 5, 6],
                        [7, 8, 9]
                        ]))

#1.8 Zero column and row matrix
def zero_matrix(matr):
    
    matr_copy = []

    for row in matr:
        matr_copy.append(row[:])
    print(matr_copy)

    for i in range(len(matr)):
        for j in range(len(matr[i])):
            if matr[i][j] == 0:
                # print(matr[i][j])
                # print(i,j)
                matr_copy[i] = [0] * len(matr[i])
                # print(matr)
                for k in range(len(matr)):
                    matr_copy[k][j] = 0
                    print(k, j, 'k & j')
                    
    return matr_copy
                

    
print(zero_matrix([ [0, 2, 3],
                    [4, 5, 6]]))

assert zero_matrix([ [1, 2, 3],
[4, 5, 0] ]) == [[1, 2, 0], [0, 0, 0]]

assert zero_matrix([ [0, 2, 3],
                     [4, 5, 0]]) == [[0, 0, 0], [0, 0, 0]]

assert zero_matrix([ [0, 2, 3],
                     [4, 5, 6]]) == [[0, 0, 0], [0, 5, 6]]

assert zero_matrix([ [0, 2, 3],
                     [4, 5, 0], 
                     [7, 8, 9]]) == [[0, 0, 0], [0, 0, 0], [0, 8, 0]]
                   

# HACKERRANK
def hourglassSum(arr):
    hourglass_sum = []
    for i in range(len(arr)-2):
        for j in range(len(arr)-2):
            summ = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
            # print(summ)
            hourglass_sum.append(summ)
    return max(hourglass_sum)
 


#leetcode
def reverseVowels(strr):
    vowels= list('AEIOUaeiou')
    strr = list(strr)
    start = 0
    end = len(strr)-1
    while start < end:
        if strr[start] in vowels and strr[end] in vowels:
            strr[start], strr[end] = strr[end], strr[start]
            start += 1
            end -= 1
        if strr[start] not in vowels:
            start += 1
        if strr[end] not in vowels:
            end -=1
    return ''.join(strr)
    
print(reverseVowels('leetcodeeeeee'))

# Input: command = "G()(al)"
# Output: "Goal"
# Explanation: The Goal Parser interprets the command as follows:
# G -> G
# () -> o
# (al) -> al
# The final concatenated result is "Goal".

def interpret(command):
    cmd = []
    i = 0
    while i < len(command):
        print(i)
        if command[i] == "G":
            cmd.append("G")
            i+= 1
        if command[i:i+2] == '()':
            cmd.append('o')
            i+=2
        if command[i:i+4] == '(al)':
            cmd.append('al')
            i+= 4
    return ''.join(cmd)

print(interpret("G()(al)"))
print(interpret("G()()()()(al)"))
print(interpret("(al)G(al)()()G"))
        
#this is not exactly optimal..use pointers instead
def is_long_name(name, typed):
    name_lst = []
    count = 1
    for i in range(1, len(name)):
        if name[i] != name[i-1]:
            name_lst.append(count)
            name_lst.append(name[i-1])
            count = 1
            
        else:
            count += 1
    name_lst.append(count)
    name_lst.append(name[-1])

    typed_lst = []
    count2 = 1
    for j in range(1, len(typed)):
        if typed[j] != typed[j-1]:
            typed_lst.append(count2)
            typed_lst.append(typed[j-1])
            count2 = 1
        else:
            count2 += 1
    typed_lst.append(count2)
    typed_lst.append(typed[-1])

    if len(name_lst) != len(typed_lst):
        return False
    
    for k in range(1, len(name_lst), 2):
        if name_lst[k] != typed_lst[k]:
            return False
            
    print(name_lst, typed_lst)
    
    for l in range(0, len(name_lst), 2):
        if int(name_lst[l]) > int(typed_lst[l]):
            return False
        
    
    return True
    
    
print(is_long_name('alex', 'aaleex'))
print(is_long_name('saeed', 'ssaaedd')) #False


# Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements.

# Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.

 

# Example 1:

# Input: nums = [1,2,2,3,1]
# Output: 2
# Explanation: 
# The input array has a degree of 2 because both elements 1 and 2 appear twice.
# Of the subarrays that have the same degree:
# [1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
# The shortest length is 2. So return 2.

def test(nums):
    left, right, count = {}, {}, {}
    for i, num in enumerate(nums):
        if num not in left:
            left[num] = i
        right[num] = i
        count[num] = count.get(num, 0) + 1
    print(left, right, count)
    max_count = max(count.values())
    # print(max_count) #2
    ans = len(nums)
    for num in count:
        if count[num] == max_count:
            ans = min(ans, right[num] - left[num] + 1)
    return ans
            
print(test([1,2,2,3,1]))

def maxSubArray(nums):
#         if len(nums) == 1:
#             return nums[0]
    
#         maxx = nums[0]
    
#         for i in range(len(nums)):
#             for j in range(i, len(nums)):
#                 if sum(nums[i:j+1]) > maxx:
#                     maxx = sum(nums[i:j+1])
#         return maxx
    sum_ = 0
    max_ = nums[0]
    for num in nums:
        if sum_ < 0:
            sum_ = 0
        sum_ += num
        max_ = max(max_, sum_)
    return max_

#Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        lst = []
        for i in range(numRows):
            lst.append([1] * (i+1))
            for j in range(1, len(lst[i])-1):
                lst[i][j] = lst[i-1][j-1] + lst[i-1][j] 
        return lst
        
# Example

#     For operations = ["INSERT Code", "INSERT Signal", "DELETE", "UNDO"], the output should be newTextEditor(operations) = "CodeSignal".
	
#         Initially the text is empty,
		
#         After the "INSERT Code" operation, the text is "Code",
		
#         After the "INSERT Signal" operation, the text is "CodeSignal",
		
#         After the "DELETE" operation, the last character is removed, so the text is "CodeSigna",
		
#         After the "UNDO" operation, the DELETE operation is undone, so the text is "CodeSignal",
#         So the final string is "CodeSignal".
#   INSERT <text> - add <text> to the end of the current text, where <text> consists of at most 20 English letters,
	
#     DELETE - erase the last character of the current text (if the current text is empty, does nothing),
	
#     COPY <index> - copy the substring of the current text starting from <index> and spanning until the end (if <index> is out of bounds copies an empty string), i.e. sets the clipboard value equal to the given substring,
	
#     PASTE - add the last copied text to the end of the current text (if the last copied text is empty, does nothing),
	
#     UNDO - undo the last successful INSERT, DELETE or PASTE operation (if there is nothing to undo, does nothing).
def texteditors(arr):
    res = []
    last = None
    last_char = None
    clipboard = None
    for i in range(len(arr)):
        x = arr[i].split()
        
        if x[0] == 'INSERT':
            res.append(x[1])
            last = x
        elif x[0] == 'DELETE':
            if len(res) != 0:
                last_char = res[-1][-1]
                res[-1] = res[-1][:-1]
                last = x
        elif x[0] == 'UNDO':
            if last[0] == 'DELETE':
                res[-1] = res[-1] + last_char 
                print('lastchar', res[-1])
            if last[0] == 'INSERT' or last[0] == 'PASTE':
                res.pop()
        elif x[0] == 'COPY':
            res_str = ''.join(res)
            start = int(x[1])
            clipboard = res_str[start:]
        elif x[0] == 'PASTE':
            last = x
            res.append(clipboard)
    return ''.join(res)
