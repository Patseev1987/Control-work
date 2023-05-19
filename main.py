import json
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
    with open(file_base, encoding="utf-8") as f:
        main_data = json.load(f)
        if main_data:
            id_notes = len(main_data) + 1
            return main_data
    return []


def show_all():
    for note in main_data:
        print("{}. {}\n{}".format(note['id'], note['title'].upper(), note['message'][:20]))



def save_note_in_file():
    with open(file_base, "w", encoding="utf-8") as f:
        json.dump(main_data, f, indent=2)
    print("File was successfully saved")


def add_note():
    global id_notes
    title = input("Enter a title:\n")
    massage = input("Enter a message:\n")
    temp_note = {"id": id_notes, "title": title, "message": massage}
    main_data.append(temp_note)
    print("Note was added!\n")
    id_notes += 1
    save_note_in_file()

def change_note():
    show_all()
    choice=int(input("\nEnter id of notes:\n"))
    choice-=1
    print("{}. {}\n{}".format(main_data[choice]['id'], main_data[choice]['title'].upper(), main_data[choice]['message']))

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
                # search_note()
                pass
            case "4":
                change_note()
            case "5":
                pass
                # delete_note()
            case "6":
                save_note_in_file()
            case "7":
                play = False
            case _:
                print("Try again!\n")


main_menu()
