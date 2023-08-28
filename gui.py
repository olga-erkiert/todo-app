import functions
import PySimpleGUI as gui


label = gui.Text("Type in a to do:")
input_box = gui.InputText(tooltip="Enter to do", key="todo")
add_button = gui.Button("Add")

window = gui.Window('To Do List App',
                    layout=[[label], [input_box, add_button]],
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
        case gui.WIN_CLOSED:
            break

window.close()
