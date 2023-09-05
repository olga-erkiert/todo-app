import functions
import PySimpleGUI as gui


label = gui.Text("Type in a to do:")
input_box = gui.InputText(tooltip="Enter to do", key='todo')
add_button = gui.Button("Add")
list_box = gui.Listbox(values=functions.get_todos(), key='todo_items',
                       enable_events=True, size=[45, 10])
edit_button = gui.Button("Edit")

window = gui.Window('To Do List App',
                    layout=[[label], [input_box, add_button], [list_box,edit_button]],
                    font=('Verdana', 14))

while True:
    action, values = window.read()
    print(action)
    print(values)
    match action:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + '\n'
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todo_items'].update(values=todos)
        case "Edit":
            todo_to_edit = values['todo_items'][0]
            new_todo = values['todo']

            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.write_todos(todos)
            window['todo_items'].update(values=todos)
        case 'todo_items':
            window['todo'].update(value=values['todo_items'][0])
        case gui.WIN_CLOSED:
            break

window.close()
