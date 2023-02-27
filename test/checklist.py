import os, time, ast
from datetime import datetime
clear = lambda: os.system('cls')
clear()

class checklist:
    id = 0
    description = ''
    status = False
    completed_date = 0
    created_date = 0

    def __init__(this, id, description, status, completed_date, created_date):
        this.id = id
        this.description = description
        this.status = status
        this.completed_date = completed_date
        this.created_date = created_date

    def read_list_function(filename, listform = bool):
        #reads the CSV file and returns a list with all the lines
        if listform == False:
            f = open(filename, 'r')
            dirty_list = f.readlines()
            clean_list = []
            for x in dirty_list:
                clean_list.append(x.replace("\n", ""))
            clear()
            return clean_list
        elif listform == True:
            #reads the given file and turns every line into a list that ast.literal_eval() can understand
            f = open(filename, 'r')
            whole_file = []
            for line in f:
                line_list = []
                pieces = line.split(',')
                for p in pieces:
                    line_list.append(p.strip())
                whole_file.append(line_list)

                '''
                start_quotes = "'" + str(line) + "'"
                quotes_line = str(start_quotes).replace('_', "'")
                bracketed_line = '[' + quotes_line + ']'
                finished_line = bracketed_line.replace('\n', '')
                
                clean_list.append(finished_line)
                '''
            return whole_file
    def remove_list_elements(listed_line):
        #reverses checklist.read_list_function('x', True)
        remove_quotes = str(listed_line).replace("'", ' ')
        remove_bracket_1 = str(remove_quotes).replace('[', '')
        remove_bracket_2 = str(remove_bracket_1).replace(']', '')
        finished_line = str(remove_bracket_2) + '\n'
        return finished_line

#start program
current_time = datetime.now()
unix_time = (time.mktime(current_time.timetuple()))
try:
    #checks if file exists and removes old completed items
    old_list = checklist.read_list_function('checklist_save_data.csv', True)
    for line in old_list:
        line = ast.literal_eval(line)
        if line[2] == 'incomplete':
            pass
        elif int(float(line[2])) < (unix_time - 604800):
            old_list.remove(line)
    f = open('checklist_save_data.csv', 'w')
    for line in old_list:
        fixed_line = checklist.remove_list_elements(line)
        f.write(fixed_line)
    f.close()
except:
    f = open('checklist_save_data.csv', 'a')
    f.close()

while True:
    #main loop
    clear()
    main_menu = input('[1] - read checklist\n[2] - read only incomplete items\n[3] - read only complete items\n[4] - mark an item as complete\n[5] - delete an item\n[6] - add an item\n[7] - exit the program\n--> ')
    if main_menu == '1':
        for line in checklist.read_list_function('checklist_save_data.csv', False):
            print(line)
        input('press enter when done: ')

    if main_menu == '2':
        clear()
        for line in checklist.read_list_function('checklist_save_data.csv', False):
            if 'complete = False' in line:
                print(line)

    if main_menu == '3':
        clear()
        for line in checklist.read_list_function('checklist_save_data.csv', False):
            if 'complete = True' in line:
                print(line)


    if main_menu == '4':
        clear()

        while True:
            delete_list = checklist.read_list_function('checklist_save_data.csv', False)
            completed = []
            clear()
            x = 0
            for line in delete_list:
                x += 1
                print(x, '-', line)
            user_delete_choice = input('Enter the line number of the item you would like to complete, or press enter to stop completing items: ')
            delete_list_lines = len(delete_list)
            
            if user_delete_choice == '':
                break
            elif user_delete_choice.isdigit() == False:
                print('Not a valid input!')
                time.sleep(0.75)
            elif int(user_delete_choice) <= delete_list_lines and int(user_delete_choice) > 0:
                whole_file = checklist.read_list_function('checklist_save_data.csv', True)
                #completed_item = ast.literal_eval(whole_file[int(user_delete_choice) - 1])
                items = whole_file[int(user_delete_choice) - 1]
                #print(items)
                #print(type(completed_item))
                
                if items[1] == 'complete=False':
                    items[1] = 'complete=True'
                    items[2] = str(unix_time)
                    whole_file.remove(whole_file[int(user_delete_choice) - 1])
                    whole_file.append(items)
                    f = open('checklist_save_data.csv', 'w')
                    for line in whole_file:
                        line_data = ",".join(line)
                        #cleaned_line = checklist.remove_list_elements(line)
                        print(line_data)
                        input('press enter to continue')
                        f.write(line_data + "\n")
                    f.close()
                
            else:
                print('Not a valid input!')
                time.sleep(0.75)


    if main_menu == '5':
        clear()

        delete_list = checklist.read_list_function('checklist_save_data.csv', False)
        while True:
            clear()
            x = 0
            for line in delete_list:
                x += 1
                print(x, '-', line)
            user_delete_choice = input('Enter the line number of the item you would like to delete, or press enter to stop deleting items: ')
            delete_list_lines = len(delete_list)
            
            if user_delete_choice == '':
                break
            elif int(user_delete_choice) <= delete_list_lines and int(user_delete_choice) > 0:
                delete_list.remove(delete_list[int(user_delete_choice) - 1])
                f = open('checklist_save_data.csv', 'w')
                for line in delete_list:
                    f.write(str(line) + '\n')
                f.close()
            else:
                print('Not a valid input!')
                time.sleep(1)

    if main_menu == '6':
        clear()
        while True:
            clear()
            taskname = input('Label your task or press enter to return to main menu: ')
            if taskname == '':
                break
            else:
                clear()
                f = open('checklist_save_data.csv', 'a')
                print(str(taskname) + ' , complete=False , ' + 'incomplete')
                user_confirm = input('Is this correct?: ')
                if user_confirm == 'y':
                    clear()
                    f.write(str(taskname) + ' , complete=False , ' + 'incomplete' + '\n')
                    print('Added task!')
                    time.sleep(0.75)
                else:
                    clear()
                    print('Task not added')
                    time.sleep(0.75)
                f.close()


    if main_menu == '7':
        print(checklist.read_list_function('checklist_save_data.csv', True))
        #clear()
        quit()