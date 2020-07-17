"""
=================================================================================
A script to calculate your income by different intervals. (Days, Weeks, Months.)
=================================================================================

Returns:
    Floating point or integer.

Future plans:
    Gonna try and make the Proxima package
    installable with pip. And make a requirements.txt file.
"""

from Proxima.usr_inputs import UI_Inputs
from rich import print

ui = UI_Inputs()


def main():
    """
    Function responsible for calculating the
    your income in daily, weekly, and monthly
    amounts.

    Returns:
        Float/Int: Based off what you input into the program it returns an integer or a floating point.
    """

    print(
        '\nHow much do you [green]make[/green] in a [bold]year[/bold]? (US Dollars)')
    inc = ui.ask_for(
        ': ', '\nNot an answer, put in a number correlating to the explanation.', float)

    if inc == float or int:
        daily_calc = inc/365
        weekly_calc = inc/52
        monthly_calc = inc/12

        daily_inc = print(f'\nDaily: ${daily_calc:,.2f}')
        weekly_inc = print(f'\nWeekly: ${weekly_calc:,.2f}')
        monthly_inc = print(f'\nMonthly: ${monthly_calc:,.2f}')

        return daily_inc, weekly_inc, monthly_inc


if __name__ == "__main__":
    main()
    repeat = ''
    while True:
        # * Asks to repeat the script.
        print(
            '\nTyping [green]Y[/green] will restart the script, typing [red]N[/red] will terminate it.')

        repeat = input(
            '\nDo you need any more information? (Y/N): ').lower()

        if repeat[0] == 'y':
            main()
            continue

        if repeat[0] == 'n':
            break