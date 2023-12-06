def valid_parentheses(parens):
    """Are the parentheses validly balanced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> valid_parentheses("(()())")
        True

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False

        >>> valid_parentheses(")()(")
        False
    """

    count = {paren: parens.count(paren) for paren in parens}
    temp = 0
    for val in count.values() :
        if temp == val : 
            return True
        temp = val
    return False

print(valid_parentheses("(()())"))
print(valid_parentheses("((())"))