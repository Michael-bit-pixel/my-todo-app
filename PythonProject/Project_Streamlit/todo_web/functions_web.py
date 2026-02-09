def get_todos(filepath="/workspaces/my-todo-app/PythonProject/Project_Streamlit/todo_web/todos_web.txt"):
    """ Read a text file and return the list of
    to-do items.
    """
    with open(filepath, "r") as file:
        todos_local = file.readlines()
    return todos_local


def write_todos(todos_arg,filepath="/workspaces/my-todo-app/PythonProject/Project_Streamlit/todo_web/todos_web.txt"):
    """ Write a list of to-do items to a text file."""
    with open(filepath, "w") as file:
        file.writelines(todos_arg)

if __name__ == "__main__":
    print(get_todos())
