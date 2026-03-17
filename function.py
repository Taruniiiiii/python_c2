# Function to find the second largest number in a list
def s_lar_num(nums):
    nums.sort()
    return nums[-2]
nums=[1,3,2,4,6,91,8]
print(s_lar_num(nums))

#longest word in a sequence
def longest_word(words):
    longest=""
    for word in words:
        if len(word)>len(longest):
            longest=word
    return longest
words="hello im taruni medishetty".split()
print(longest_word(words))

#missing number

def find_missing(nums):
    n=len(nums)+1
    s=set(nums)
    for i in range(1,n+1):
        if i not in s:
            return i
nums=[1,2,3,5]
print(find_missing(nums))