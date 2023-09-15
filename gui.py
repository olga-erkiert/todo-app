import functions
import PySimpleGUI as gui
import time


gui.theme('DarkTeal6')

clock = gui.Text("", key='clock')
label = gui.Text("Type in a to do:")
input_box = gui.InputText(tooltip="Enter to do", key='todo')
add_button = gui.Button("Add")
list_box = gui.Listbox(values=functions.get_todos(), key='todo_items',
                       enable_events=True, size=(45, 10))
edit_button = gui.Button("Edit")
complete_button = gui.Button("Complete")
exit_button = gui.Button("Exit")

window = gui.Window('To Do List App',
                    layout=[[clock],
                            [label],
                            [input_box, add_button],
                            [list_box, edit_button, complete_button],
                            [exit_button]],
                    font=('Verdana', 13))

while True:
    action, values = window.read(timeout=200)
    window['clock'].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    match action:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + '\n'
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todo_items'].update(values=todos)
        case "Edit":
            try:
                todo_to_edit = values['todo_items'][0]
                new_todo = values['todo']

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todo_items'].update(values=todos)
            except IndexError:
                gui.popup("Please select an item to edit first.", font=('Verdana', 13))
        case "Complete":
            try:
                todo_to_complete = values['todo_items'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todo_items'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                gui.popup("Please select an item to complete first.", font=('Verdana', 13))
        case "Exit":
            break
        case 'todo_items':
            window['todo'].update(value=values['todo_items'][0])
        case gui.WIN_CLOSED:
            break

window.close()
