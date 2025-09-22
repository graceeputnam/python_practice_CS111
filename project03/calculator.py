from pair import *
from pair import Pair, nil
from operator import add, sub, mul, truediv


def tokenize(expression):
    """ Takes a string and returns a list where each item
    in the list is a parenthesis, one of the four operators (/, *, -, +),
    or a number literal.
    >>> tokenize("(+ 3 2)")
    ['(', '+', '3', '2', ')']
    >>> tokenize("(- 9 3 3)")
    ['(', '-', '9', '3', '3', ')']
    >>> tokenize("(+ 10 100)")
    ['(', '+', '10', '100', ')']
    >>> tokenize("(+ 5.5 10.5)")
    ['(', '+', '5.5', '10.5', ')']
    >>> expr = "(* (- 8 4) 4)"
    >>> tokenize(expr)
    ['(', '*', '(', '-', '8', '4', ')', '4', ')']
    >>> expr = "(* (- 6 8) (/ 18 3) (+ 10 1 2))"
    >>> tokenize(expr)
    ['(', '*', '(', '-', '6', '8', ')', '(', '/', '18', '3', ')', '(', '+', '10', '1', '2', ')', ')']
    """
    """*** YOUR CODE HERE ***"""
    tokens = []
    current_num = ""

    for char in expression:
        if char in "()+-*/":
            if current_num:
                tokens.append(current_num)
                current_num = ""
            tokens.append(char)
        elif char.isdigit() or char == ".":
            current_num += char
        elif char.isspace():
            if current_num:
                tokens.append(current_num)
                current_num = ""
    if current_num:
        tokens.append(current_num)
    return tokens


def parse_tokens(tokens, index):
    """ Takes a list of tokens and an index and converts the tokens to a Pair list

    >>> parse_tokens(['(', '+', '1', '1', ')'], 0)
    (Pair('+', Pair(1, Pair(1, nil))), 5)
    >>> parse_tokens(['(', '*', '(', '-', '8', '4', ')', '4', ')'], 0)
    (Pair('*', Pair(Pair('-', Pair(8, Pair(4, nil))), Pair(4, nil))), 9)
    """
    """*** YOUR CODE HERE ***"""
    if tokens[index] == "(":
        operator = tokens[index + 1]
        if index != 0:
            pair_list, index = parse_tokens(tokens, index + 2)
            operator = Pair(operator, pair_list)
        if index == 0:
            index += 2
        pair_list_2, index = parse_tokens(tokens, index)
        return Pair(operator, pair_list_2), index
    elif tokens[index] == ")":
        return nil, index + 1
    else:
        try:
            if "." in tokens[index]:
                number = float(tokens[index])
            else:
                number = int(tokens[index])
            new_pair, index_3 = parse_tokens(tokens, index + 1)
            index = index_3
            return Pair(number, new_pair), index
        except Exception as e:
            raise TypeError(e)


def parse(tokens):
    def parse_tokens(tokens, index):
        """ Takes a list of tokens and an index and converts the tokens to a Pair list

        >>> parse_tokens(['(', '+', '1', '1', ')'], 0)
        (Pair('+', Pair(1, Pair(1, nil))), 5)
        >>> parse_tokens(['(', '*', '(', '-', '8', '4', ')', '4', ')'], 0)
        (Pair('*', Pair(Pair('-', Pair(8, Pair(4, nil))), Pair(4, nil))), 9)
        """
        """*** YOUR CODE HERE ***"""
        if tokens[index] == "(":
            operator = tokens[index + 1]
            if index != 0:
                pair_list, index = parse_tokens(tokens, index + 2)
                operator = Pair(operator, pair_list)
            if index == 0:
                index += 2
            pair_list_2, index = parse_tokens(tokens, index)
            return Pair(operator, pair_list_2), index
        elif tokens[index] == ")":
            return nil, index + 1
        else:
            try:
                if "." in tokens[index]:
                    number = float(tokens[index])
                else:
                    number = int(tokens[index])
                new_pair, index_3 = parse_tokens(tokens, index + 1)
                index = index_3
                return Pair(number, new_pair), index
            except Exception as e:
                raise TypeError(e)

    pairs, index = (parse_tokens(tokens, 0))
    return pairs


def reduce(func, operands, initial):
    total = initial
    while operands != nil:
        total = func(total, operands.first)
        operands = operands.rest
    return total


def apply(operator, operands):
    if operator == "+":
        return reduce(add, operands, 0)
    if operator == "-":
        return reduce(sub, operands.rest, operands.first)
    if operator == "*":
        return reduce(mul, operands, 1)
    if operator == "/":
        return reduce(truediv, operands.rest, operands.first)
    else:
        raise TypeError


def eval(syntax_tree):
    if isinstance(syntax_tree, int) or isinstance(syntax_tree, float):
        return syntax_tree
    elif isinstance(syntax_tree, Pair):
        operator = syntax_tree.first
        operands = syntax_tree.rest
        while operands != nil:
            operands.first = eval(operands.first)
            operands = operands.rest
        return apply(operator, syntax_tree.rest)
    else:
        raise TypeError


def main():
    print("Welcome to the CS 111 Calculator Interpreter.")
    while True:
        user_input = input('calc >> ')
        if user_input == "exit":
            break
        try:
            pairs = parse(tokenize(user_input))
            results = eval(pairs)
            print(results)
        except Exception as e:
            print("Error" + e)
    print("Goodbye!")


if __name__ == "__main__":
    main()
