#Link: https://www.hackerrank.com/challenges/capitalize/problem?isFullScreen=true

#My solution to the problem is as follows:
def solve(s):
    list_string = s.split(" ")
    
    for i in range(len(list_string)):
        list_string[i] = list_string[i].capitalize()
    
    return " ".join(list_string)

#Better way: Using List Comprehension
def better_solve(s):
    return " ".join(word.capitalize() for word in s.split(" "))