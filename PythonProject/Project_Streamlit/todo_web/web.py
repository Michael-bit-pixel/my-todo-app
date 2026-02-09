import streamlit as st
import  functions_web as fd

todos = fd.get_todos()


def add_todo():
    new_todos = st.session_state["new_todo"]
    todos.append(new_todos + "\n")
    fd.write_todos(todos)

st.title("My Todo App")
st.subheader("This is my todo app")
st.write("This app is to increase your productivity.")

for index,todo in enumerate(todos):
    checkbox = st.checkbox(todo,key=todo)
    if checkbox:
        todos.pop(index)
        fd.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input("Enter your productivity here",placeholder="Add a new todo...",
              on_change=add_todo,key="new_todo"
              )

