import os


def move_file(command: str) -> None:
    parts = command.split(" ")

    if not len(parts) == 3:
        return

    if not parts[0] == "mv":
        return

    test = parts[2].split("/")
    path = "/".join(test[0:-1])
    if path:
        os.makedirs(path, exist_ok=True)

    with open(parts[2], "w") as file1, open(parts[1], "r") as file2:
        file1.write(file2.read())

    os.remove(parts[1])
