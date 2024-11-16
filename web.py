import streamlit as st
import custom_func_todo


todos = custom_func_todo.get_open_read_file()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    custom_func_todo.get_open_write_file(todos)

st.title("My Todo App")
st.subheader("This is my Todo App.")
st.write("This app is to increase your productivity")


for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        custom_func_todo.get_open_write_file(todos)
        del st.session_state[todo]
        st.rerun()


st.text_input(label='', placeholder="Enter new todo...",
              on_change=add_todo, key='new_todo')

print("Hello")
st.session_state