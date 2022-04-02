#repeating substring
#For a given nonempty string s,f(s) finds a minimum substring t and the maximum number k,
# such that the entire string s is equal to t repeated k times.

def f(s):
    x=2
    t=s[:2]
    k=s.count(t)
    while len(t)*k != len(s):
        x=x+1
        t=s[:x]
        k=s.count(t)
    return (t,k)
#function that will be given two strings a and b consisting of lower case letters,
# but a will have at most one asterix character.
# The asterix (if any) can be replaced with an arbitrary sequence (possibly empty) of lowercase letters.
# No other character of string a can be replaced.
# If it is possible to replace the asterix in a to obtain string b, then string b matches the pattern.
def solve(a,b):
    if '*' not in a and a==b:
        return True
    elif '*' not in a and a!=b:
        return False
    elif '*' == a:
        return True
    elif a.startswith('*') and b.endswith(a[1:]):
        return True
    elif a.endswith('*') and b.startswith(a[:-1]):
        return True
    else:
        x=a.find('*')
        if b.startswith(a[:x]) and b.endswith(a[x+1:]):
            return True
        else:
            return False
#Write a function that checks if a given string (case insensitive) is a palindrome.
def is_palindrome(s):
    x=s[::-1]
    if x.lower()==s.lower() :
        return True
    else:
        return False
        