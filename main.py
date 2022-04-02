from string_ops import f, solve, is_palindrome

if __name__ == '__main__':
    print('repeating substring')
    print(f('ababab'))
    print(f('abcde'))
    print('------------------------------')
    print('Simple string matching')
    print(solve("code*s","codewars") ,'\n',
    solve("codewar*s","codewars"),'\n',
    solve("codewars","codewars"),'\n',
    solve("a","b"),'\n',
    solve("*s", "sssss"))
    print('------------------------------')
    print('is_palindrome')
    print(is_palindrome('AbBa'))
    print(is_palindrome('Abca'))
    print('------------------------------')
    