from consolemenu import *
from calc.calcFunction import *


def show_expression(expression):
    print("expression: " + expression)
    Screen().input('Press [Enter] to continue')


def get_expression():
    print("Brakuje systemu sprawdzania i poprawy składni, wiec jak użyjesz samo e a nie e() to jebnie, tak samo jebnie jak wstawisz inne znaki, no i czasem minus traktuje źle, np (12+12)-12 jebnie, można naprawic (12+12)-(12) \npozdrawiam\n")
    expr = Screen().input('Enter an expression (using +,-,*,/,^, sin(), cos(), e(), pi()): \n')
    print(solve_expression(expr))
    Screen().input('Press [Enter] to continue')


def is_bracket(char):
    if char == '(' or char == '[' or char == '{' or char == ')' or char == ']' or char == '}':
        return True
    else:
        return False


def reverse_bracket(bracket):
    if bracket == '(':
        return ')'
    if bracket == ')':
        return '('
    if bracket == '[':
        return ']'
    if bracket == ']':
        return '['
    if bracket == '{':
        return '}'
    if bracket == '}':
        return '{'
    return ''


def is_open_bracket(bracket):
    if bracket == '(':
        return True
    if bracket == '[':
        return True
    if bracket == '{':
        return True
    return False


def check_bracket(list_expr):
    stack = []
    if not list_expr:
        return False

    for elem in list_expr:
        if 'bracket' in elem:
            br = elem['bracket']
            if is_open_bracket(br):
                stack.append(br)
            else:
                if not stack:
                    return False
                rbr = stack.pop()
                if not br == reverse_bracket(rbr):
                    return False
    if stack:
        #         stack is not empty
        return False
    else:
        return True


# this function convert str to list dictionary with keys: value, expr, bracket
def str_to_list_expr(string):
    string.replace(" ", "")
    string = "0+" + string + "()END0"
    last_char = 0
    result = []

    if string[0].isdigit():
        expr = False
    else:
        expr = True
    expression = ''
    try:
        while expression != 'END' and last_char < len(string):
            if not expr:
                if string[last_char] == "-":
                    i = last_char + 1
                else:
                    i = last_char

                while i < len(string) and string[i].isdigit():
                    i = i + 1
                if i < len(string) and string[i] == '.':
                    i += 1
                    while i < len(string) and string[i].isdigit():
                        i = i + 1

                if string[last_char:i] == '-':
                    #     only - in string
                    result.append({'expr': '-'})
                else:
                    value = float(string[last_char:i])
                    result.append({'value': value})
                last_char = i
                expr = True
            # else if expr == False
            else:
                if string[last_char] == "-":
                    i = last_char + 1
                else:
                    i = last_char

                while i < len(string) and not string[i].isdigit() and string[i] != '-':
                    i = i + 1
                expression = string[last_char:i]
                # find bracket and add to list all
                j = 0
                r = 0
                tym = ''
                while j < len(expression):
                    if is_bracket(expression[j]):
                        if r > 0:
                            result.append({'expr': expression[j - r: j]})
                            tym = expression[j - r: j]
                            r = 0
                        result.append({'bracket': expression[j]})
                    else:
                        r += 1
                    j += 1
                if r > 0:
                    result.append({'expr': expression[j - r: j]})
                    tym = expression[j - r: j]
                expression = tym

                last_char = i
                expr = False

    except IndexError:
        return None
    except ValueError:
        return None

    return result


# function below add to operation param:
#   name function to execute
#   type operation(one or two arguments operation)
#   operator precedence
def add_to_expr_param(list_expr):
    new_list = []
    for elem in list_expr:
        if 'expr' in elem:
            symbol = elem['expr']
            expr = get_expr(symbol)
            if expr:
                new_list.append(expr)
            else:
                expr = get_expr(symbol[0])
                expr2 = get_expr(symbol[1:])
                if expr and expr2:
                    new_list.append(expr)
                    new_list.append(expr2)

        else:
            new_list.append(elem)

    return new_list


def convert_to_rnp(list_expr):
    list_expr = add_to_expr_param(list_expr)

    converted = []
    oper_stack = []

    for elem in list_expr:
        if 'value' in elem:
            converted.append(elem)

        if 'expr' in elem:
            e_prec = elem['prec']
            if not oper_stack:
                oper_stack.append(elem)
            else:
                if 'prec' in oper_stack[-1]:
                    s_prec = oper_stack[-1]['prec']
                    if s_prec < e_prec:
                        oper_stack.append(elem)
                    else:
                        #             else gdy s_prec >= e_prec
                        while oper_stack and 'expr' in oper_stack[-1] and oper_stack[-1]['prec'] >= elem['prec']:
                            converted.append(oper_stack.pop())
                        #         nie jestem pewny co to tego
                        oper_stack.append(elem)
                else:
                    #             there on stack is bracket
                    oper_stack.append(elem)

        if 'bracket' in elem:
            if is_open_bracket(elem['bracket']):
                oper_stack.append(elem)
            else:
                while oper_stack:
                    if 'bracket' in oper_stack[-1]:
                        if is_open_bracket(oper_stack[-1]['bracket']):
                            oper_stack.pop()
                            break
                    else:
                        converted.append(oper_stack.pop())
    while oper_stack:
        converted.append(oper_stack.pop())

    return converted


def solve_expression(expression):
    list_expr = str_to_list_expr(expression)

    if not list_expr:
        return "Expression structure error"
    if not check_bracket(list_expr):
        return "Bracket error"

    rnp = convert_to_rnp(list_expr)

    try:
        while len(rnp) > 1:
            i = 0
            while i < len(rnp) and 'expr' not in rnp[i]:
                i += 1
            if i < len(rnp):
                oper = rnp[i]
                if oper['type'] == 2:
                    value = oper['func'](rnp[i - 2]['value'], rnp[i - 1]['value'])
                    del rnp[i - 2:i + 1]
                    rnp.insert(i - 2, {'value': value})
                if oper['type'] == 1:
                    value = oper['func'](rnp[i - 1]['value'])
                    del rnp[i - 1:i + 1]
                    rnp.insert(i - 1, {'value': value})
                if oper['type'] == 0:
                    value = oper['func']()
                    del rnp[i:i + 1]
                    rnp.insert(i, {'value': value})
            else:
                return "Something wrong with expression"

    except IndexError:
        return "Something wrong with expression"
    except ArithmeticError:
        return "Calculation error"

    return 'Result: ' + str(rnp[0]['value'])
