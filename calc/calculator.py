from calc.primaryCalc import get_expression


def calc_main():
    try:
     get_expression()
    except:
        Screen().input('\tJebło\nPress [Enter] to continue')

