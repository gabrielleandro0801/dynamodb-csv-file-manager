from csv_manager.manager import read, write
from csv_manager.translator import get_headers, transform_json


def main():
    OLD_FILE = "./old_file.csv"
    old_content = read(OLD_FILE)
    print("Old Content")
    print(old_content)

    headers, content = get_headers(old_content)
    new_content = transform_json(content)

    NEW_FILE = "./new_file.csv"
    write(NEW_FILE, headers, new_content)
    new_open = read(NEW_FILE)
    print("\nNew Content")
    print(new_open)


if __name__ == '__main__':
    main()
