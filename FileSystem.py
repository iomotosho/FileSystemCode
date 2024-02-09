def main():
    fs = FileSystem()

    while True:
        command = input("$ ").split()

        if not command:
            continue

        if command[0] == "ls":
            fs.ls()
        elif command[0] == "mkdir":
            if len(command) < 2:
                print("Usage: mkdir <directory_name>")
            else:
                fs.mkdir(command[1])
        elif command[0] == "touch":
            if len(command) < 2:
                print("Usage: touch <file_name>")
            else:
                fs.touch(command[1])
        elif command[0] == "cd":
            if len(command) < 2:
                print("Usage: cd <directory_name>")
            else:
                fs.cd(command[1])
        elif command[0] == "exit":
            break
        else:
            print("Command not recognized")

class Directory:
    def __init__(directory, name):
        directory.name = name
        directory.children = []

    def add_child(directory, child):
        directory.children.append(child)

    def __repr__(directory):
        return f"<Directory {directory.name}>"


class File:
    def __init__(directory, name):
        directory.name = name

    def __repr__(directory):
        return "<File {directory.name}>"


class FileSystem:
    def __init__(directory):
        directory.root = Directory('/')
        directory.current_directory = directory.root

    def mkdir(directory, directory_name):
        new_dir = Directory(directory_name)
        directory.current_directory.add_child(new_dir)

    def touch(directory, file_name):
        new_file = File(file_name)
        directory.current_directory.add_child(new_file)

    def ls(directory):
        for item in directory.current_directory.children:
            print(item.name)

    def cd(directory, directory_name):
        if directory_name == "..":
            if directory.current_directory != directory.root:
                directory.current_directory = directory._find_parent(directory.root, directory.current_directory)
        else:
            found = False
            for item in directory.current_directory.children:
                if isinstance(item, Directory) and item.name == directory_name:
                    directory.current_directory = item
                    found = True
                    break
            if not found:
                print("Directory not found")

    def _find_parent(directory, root, target):
        if target in root.children:
            return root
        for item in root.children:
            if isinstance(item, Directory):
                parent = directory._find_parent(item, target)
                if parent:
                    return parent
        return None


if __name__ == "__main__":
    main()
