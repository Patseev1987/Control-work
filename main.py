import json
import os.path
from os import path

main_data = []
id_notes = 1
file_base = "notes.json"

if not path.exists(file_base):
    with open(file_base, "w", encoding="utf-8") as _:
        pass


def read_all_notes_from_file():
    global main_data
    global id_notes
    with open(file_base, "r", encoding="utf-8") as f:
        if os.path.getsize(file_base) != 0:
            main_data = json.load(f)
            if main_data:
                id_notes = len(main_data) + 1
                return main_data
    return []


def show_all():
    if main_data != []:
        for note in main_data:
            print("{}. {}\n{}\n".format(note['id'], note['title'].upper(), note['message'][:20]))
    else:
        print("Notebook is empty!\n")


def save_note():
    with open(file_base, "w", encoding="utf-8") as f:
        json.dump(main_data, f, indent=2)


def save_note_in_file():
    file_name = input("Enter a name for file with out .json\n")
    if check_name(file_name):
        file_name += ".json"
        with open(file_name, "w", encoding="utf-8") as f:
            json.dump(main_data, f, indent=2)
        print("File was successfully saved\n")
    else:
        print("You entered wrong symbol for file name!\n")


def add_note():
    global id_notes
    title = input("Enter a title:\n")
    massage = input("Enter a message:\n")
    temp_note = {"id": id_notes, "title": title, "message": massage}
    main_data.append(temp_note)
    id_notes += 1
    save_note()
    print("Note was added!\n")


def change_note():
    if main_data != []:
        choice = get_choice()
        if choice != -1:
            title = input("Enter a title:\n")
            massage = input("Enter a message:\n")
            temp_note = {"id": choice + 1, "title": title, "message": massage}
            main_data.remove(main_data[choice])
            main_data.insert(choice, temp_note)
            save_note()
            print("Note was successfully changed\n")
        else:
            print("Id was not found!\n")
    else:
        print("Notebook is empty!\n")


def search_note():
    if main_data != []:
        play = True
        while play:
            answer = input("Search menu:\n"
                           "1. Search by id\n"
                           "2. Search by title\n"
                           "3. Search by text\n")
            match answer:
                case "1":
                    search_id()
                    play = False
                case "2":
                    search_title()
                    play = False
                case "3":
                    search_text()
                    play = False
                case _:
                    print("Try again!\n")
    else:
        print("Notebook is empty!\n")


def search_id():
    choice = get_choice()
    if choice != -1:

        if choice < len(main_data):
            print("{}. {}\n{}\n".format(main_data[choice]['id'], main_data[choice]['title'].upper(),
                                        main_data[choice]['message']))
        else:
            print("Id is not found!\n")
    else:
        print("Id was not found!\n")


def search_title():
    choice = input("Enter a title:\n")
    flag = True
    for note in main_data:
        if note["title"].lower().strip() == choice.lower().strip():
            temp_id = note["id"] - 1
            print("{}. {}\n{}\n".format(main_data[temp_id]['id'], main_data[temp_id]['title'].upper(),
                                        main_data[temp_id]['message']))
            flag = False
    if flag:
        print("Title is not found!\n")


def search_text():
    choice = input("Enter a text:\n")
    flag = True
    for note in main_data:
        if choice.lower().strip() in note["message"].lower().strip():
            temp_id = note["id"] - 1
            print("{}. {}\n{}\n".format(main_data[temp_id]['id'], main_data[temp_id]['title'].upper(),
                                        main_data[temp_id]['message']))
            flag = False
    if flag:
        print("Text is not found!\n")


def is_int(str):
    try:
        int(str)
        return True
    except ValueError:
        return False


def delete_note():
    if main_data != []:
        choice = get_choice()
        if choice != -1:
            last = len(main_data) - 1
            main_data.remove(main_data[choice])
            if choice != last:
                for temp_index in range(choice, len(main_data)):
                    temp_note = main_data[temp_index]
                    main_data[temp_index] = {"id": temp_index + 1, "title": temp_note['title'],
                                             "message": temp_note['message']}
                    save_note()
            save_note()
            print("Note was deleted!\n")
        else:
            print("Id was not found!\n")
    else:
        print("Notebook is empty!\n")


def get_choice():
    show_all()
    choice = input("\nEnter id of notes:\n")
    if is_int(choice):
        if ((int(choice) <= len(main_data)) & (int(choice) > 0)):
            x = int(choice)
            x -= 1
            return x
    return -1


def check_name(str):
    list = ["#", "<", "$", "+", "%", "<", ">>", "!", "`", "&", "*", '‘', "|", "{", "?", "“", "=", "}", "/", ":", '\\',
            " ", "@"]
    for latter in str:
        if latter in list:
            return False
    else:
        return True


def main_menu():
    play = True
    while play:
        read_all_notes_from_file()
        answer = input("Notebook:\n"
                       "1. Show all notes\n"
                       "2. Add a note\n"
                       "3. Search a note\n"
                       "4. Change a note\n"
                       "5. Delete a note\n"
                       "6. Save a note\n"
                       "7. Exit\n")
        match answer:
            case "1":
                show_all()
            case "2":
                add_note()
            case "3":
                search_note()
            case "4":
                change_note()
            case "5":
                pass
                delete_note()
            case "6":
                save_note_in_file()
            case "7":
                play = False
            case _:
                print("Try again!\n")


main_menu()
