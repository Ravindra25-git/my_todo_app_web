FILEPATH = "todos.txt"

def get_open_read_file(filepath=FILEPATH):
    """Read a txt file and return the list of todo items"""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def get_open_write_file(todos_local,filepath=FILEPATH):
    """write the todo list in the text file"""
    with open(filepath,'w') as file:
            file.writelines(todos_local)

if __name__ == "__main__":
    print(help(get_open_read_file))
    print(help(get_open_write_file))