import sys
import controler
from copy import deepcopy


def read_command():
    """This function splits up the command"""

    cmd = input("Command: ")
    if cmd.find(" ") == -1:
        command = cmd
        params=""
    else:
        command = cmd[0:cmd.find(" ")]
        params = cmd[cmd.find(" "):]
        params = params.split(" ")
        for i in range(0, len(params)):
            params[i] = params[i].strip()
    return command,params


def add_command(List, par):
    """This function checks the introduced parameter.
        If it is not a complex number, the function will show an alert message."""
    if controler.check_val(par[1], complex):
        controler.add_number(List, complex(par[1]))
    else:
        print("The number is invalid")


def add_more_numbers(List, par):
    for i in range(len(par)):
        add_insert.add_number(List, complex(par[i]))
    else:
        print("Not a valid command!")


def insert_number_at_position(List, par):
    """This function validates the number and the position
        and inserts the number in the list"""

    if par[2] == 'at':
        if controler.check_val(par[1], complex) and controler.check_val(par[3], int):
            controler.insert_number(List, complex(par[1]), int(par[3]))
        else:
            print("Invalid number or position!")
    else:
        print("Invalid command!")


def remove_item_at_poz(List, par):
    """The function calls the remove function and removes an element."""

    if controler.check_val(par[1], int):
        controler.remove_position(List, int(par[1]))
    else:
        print("Invalid position or command!")


def remove_more_numbers(List, par):
    """The function calls the remove function and removes an element."""
    for i in range(len(par)):
        if controler.check_val(par[i], int):
            controler.remove_position(List, int(par[i]))


def remove_items_range(List, par):
    """This function removes items in a given range"""

    if controler.check_val(par[1], int) and controler.check_val(par[3], int) and par[2] == 'to':
        controler.remove_items(List, int(par[1]), int(par[3]))


def replace_item(List, par):
    """This function replaces an item by ots given position."""
    if par[2] == 'with':
        if controler.check_val(par[1], complex) and controler.check_val(par[3], complex):
            controler.replace_item_range(List, complex(par[1]), complex(par[3]))
        else:
            print("Invalid numbers!")
    else:
        print("Invalid command!")


def return_sume(List, par):
    if controler.check_val(par[1], int) and controler.check_val(par[3], int) and par[2] == 'to':
        controler.sum_nbs(List, int(par[1]), int(par[3]))
    else:
        print("Invalid numbers!")


def return_prod(List, par):
    if controler.check_val(par[1], int) and controler.check_val(par[3], int) and par[2] == 'to':
        controler.prod_nbs(List, int(par[1]), int(par[3]))
    else:
        print("Invalid numbers!")


def print_entire_list(List, par):
    controler.print_list(List)


def print_real_numbers(List, par):
    if Params[3] == 'to':
        if controler.check_val(par[2], int) and controler.check_val(par[4], int):
            controler.print_real_nbs(List, int(par[2]), int(par[4]))
        else:
            print("Invalid numbers")
    else:
        print("Invalid command enter help for information!")


def print_modulo_numbers(List, par):
    if controler.check_val(par[3], int) or controler.check_val(par[3], float):
        controler.print_numbers_modulo(List, par[2], float(par[3]))
    else:
        print("That is not a number")


def filter_real_numbers(List, par):
    controler.filter_real(List)

def filter_modulo_numbers(List, par):
    if controler.check_val(par[3], int) or controler.check_val(par[3], float):
        if par[2] != 0 and par[3] != 0:
            controler.filter_modulo(List, par[2], float(par[3]))
    else:
        print("That is not a number")


def exit_function(my_list, params):
    sys.exit()


def print_help(params):
    print("\nHelp:")
    print("\tadd <number>")
    print("\tinsert <number> at <position>")
    print("\tadd <numbers>")
    print("\tremove <position>")
    print("\tremove_more <positions>")
    print("\tremove <start position> to <end position>")
    print("\treplace <old number> with <new number>")
    print("\tlist")
    print("\tlist real <start position> to <end position>")
    print("\tlist modulo [<|=|>] <number>")
    print("\tsum <start position> to <end position>")
    print("\tproduct <start position> to <end position>")
    print("\tfilter real")
    print("\tfilter modulo [<|=|>] <number>")
    print("\tundo")
    print("\tExit!")
    print("\tHelp!")


def undo_list(List, backup_list):

    if backup_list[len(backup_list)-1] != List:
        backup_list.append(deepcopy(List))



def undo_function(List, backups):
    #This frunction replaces the list with the last list before the previous opperation.

    if len(backups) > 1:
        del backups[len(backups)-1]
        del List[:]
        for i in range(0,len(backups[len(backups)-1])):
            List.append(backups[len(backups)-1][i])
        print("Success!")
    else:
        print("Something went wrong!")

def mainMenu():
    #tests.run_tests()
    print("\n\tWelcome to the complex number application!")
    print("\n\tFor further information, please type Help!\n")

    my_list = [[1, 5], [3, 6], [6, 4], [11, 0], [4, 5], [-23, 7], [2, 10], [0, 0], [0, -3], [-8, 0]]
    backup_list = []
    backup_list.append(deepcopy(my_list))

    Commands = {'add': [add_command, 2, "add <number>"],
                'insert': [insert_number_at_position, 4, "insert <number> at <position>"],
                'add_more': [add_more_numbers, 2, "add_more <numbers>"],
                'remove': [remove_item_at_poz, 2, "remove <position>"],
                'remove_more': [remove_more_numbers, 2, "remove_more <positions>"],
                'remove_in_range': [remove_items_range, 4, "remove <start position> to <end position>"],
                'replace': [replace_item, 4, "replace <old number> with <new number>"],
                'list': [print_entire_list, 0, "list"],
                'list real': [print_real_numbers, 5, "list real <start position> to <end position>"],
                'list modulo': [print_modulo_numbers, 4, "list modulo [<|=|>] <number>"],
                'sum': [return_sume, 4, "sum <start position> to <end position>"],
                'product': [return_prod, 4, "product <start position> to <end position>"],
                'filter real': [filter_real_numbers, 2, "filter real"],
                'filter modulo': [filter_modulo_numbers, 4, "filter modulo [<|=|>] <number>"],
                'undo': ['', '', "undo"],
                'Exit!': [exit_function, 0, "Exit!"],
                'Help!': [print_help, 0, "Help!"]}


    while True:
        all_commands = read_command()
        Command = all_commands[0]
        Params = all_commands[1]
        if Command == 'add_more':
            for i in range(1, len(Params)):
                if controler.check_val(Params[i], complex):
                    controler.add_number(my_list, complex(Params[i]))
                else:
                    print("Not a valid command!")

        if Command == 'remove_more':
            i = len(Params) - 1
            while i >= 0:
                if controler.check_val(Params[i], int):
                    controler.remove_position(my_list, int(Params[i]))
                i -= 1
        if Command == 'filter' and len(Params) == 2:
            filter_real_numbers(my_list, Params)
        if Command == 'filter' and len(Params) == 4:
            filter_modulo_numbers(my_list, Params)
        if Command in Commands:
            if len(Params) > 1:
                if Command == 'remove' and len(Params) == 4:
                    Command = "remove_in_range" 
                if Command == 'list' and Params[1] == 'real':
                    Command = 'list real'
                if Command == 'list' and Params[1] == 'modulo':
                    Command='list modulo'
                if Command=='filter' and Params[1] == 'modulo':
                    Command = 'filter modulo'
                    filter_modulo_numbers(my_list, Params)
            if Command == 'Help!':
                print_help(Commands)
            elif Command == 'undo':
                undo_function(my_list,backup_list)
            else:
                if Commands[Command][1] == len(Params):
                    Commands[Command][0](my_list, Params)
                    undo_list(my_list, backup_list)


mainMenu()
