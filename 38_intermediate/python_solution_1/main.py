"""
ALGORITHM (created and implemented by ME)

In this algorithm I will assume that the input is fully parenthesized, 
i.e. there is one pair of parentheses for each operator.

The input can contain spaces. But the output will not contain spaces.
Also in input every operand can be a single alphanumeric character.
"""

def transform_into_rpn(exp):
    """
    >>> transform_into_rpn("(a+(b*c))")
    'abc*+'
    >>> transform_into_rpn("((a+b)*(z+x))")
    'ab+zx+*'
    >>> transform_into_rpn("((a+t)*((b+(a+c)) ^ (c+d)))")
    'at+bac++cd+^*'
    """

    operators = ['+', '-', '*', '/', '^']
    operator_stack = []
    operand_stack = []
    for x in exp:
        if x.isalnum():
            operand_stack.append(x)
        elif x in operators:
            operator_stack.append(x)
        elif x == ')':
            operator = operator_stack.pop()
            operand2 = operand_stack.pop()
            operand1 = operand_stack.pop()

            operand_stack.append("".join([operand1, operand2, operator]))

    return operand_stack.pop()


if __name__ == '__main__':
    import doctest
    doctest.testmod()