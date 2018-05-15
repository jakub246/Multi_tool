import calc.primaryCalc
import consolemenu


def calc_main():
    try:
        calc.primaryCalc.get_expression()
    except:
        consolemenu.Screen().input('\tJebło\nPress [Enter] to continue')

