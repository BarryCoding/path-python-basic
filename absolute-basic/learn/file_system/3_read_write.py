# Open and Close a File
import csv
from pathlib import Path
from typing import Literal

# Explain each mode for opening files in Python:

"""
"r"   : Open for reading (default). File must exist.
"r+"  : Open for reading and writing. File must exist. Does not truncate.
"w"   : Open for writing, truncating the file first. Creates file if it does not exist.
"w+"  : Open for reading and writing. Truncates file to zero length or creates new file.
"a"   : Open for writing, appending to the end of the file if it exists.
"a+"  : Open for reading and appending (writing at end of file). Creates file if it does not exist.
"x"   : Open for exclusive creation, failing if the file already exists.
"x+"  : Open for reading and writing. Exclusive creation, fails if file exists.
"b"   : Binary mode (e.g. "rb" or "wb"). Read/write bytes, not text.
"t"   : Text mode (default; e.g. "rt" or "wt"). Read/write text (strings).
"""
OpenTextMode = Literal["r", "w", "a", "x", "b", "t", "r+", "w+", "a+", "x+"]

DEFAULT_ENCODING = "utf-8"

RANDOM_TEXT = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit.
Vivamus lacinia odio vitae vestibulum vestibulum.
Cras venenatis euismod malesuada.
Curabitur sit amet facilisis urna.
Praesent sed sem nec velit cursus malesuada a nec dui.
"""


def get_csv_file_path():
    cwd = Path.cwd()
    return cwd / "learn" / "file_system" / "December_Expenses.csv"


def read_and_close_a_file():
    csv_file_path = get_csv_file_path()

    with csv_file_path.open() as csv_file:
        print(f"csv_file: {csv_file}")

    print(f"csv_file closed: {csv_file.closed}")


def understand_text_and_binary_files(mode: str = "r"):
    csv_file_path = get_csv_file_path()

    with csv_file_path.open(mode) as csv_file:
        print(f"csv_file mode: {csv_file.mode}")
        print(f"csv_file readable: {csv_file.readable()}")
        print(f"csv_file writable: {csv_file.writable()}")


def specify_character_encoding(encoding: str = DEFAULT_ENCODING):
    text_bytes = "cash".encode(encoding)
    print(text_bytes)
    text_bytes_list = list(text_bytes)
    print(text_bytes_list)
    text_string = bytes(text_bytes_list).decode(encoding)
    print(text_string)


def choose_line_ending(newline: str = "\n"):
    csv_file_path = get_csv_file_path()

    with csv_file_path.open(
        encoding=DEFAULT_ENCODING,
        newline=newline,
    ) as csv_file:
        for line in csv_file:
            print(line)


def explore_different_file_modes(mode: OpenTextMode = "r+"):
    csv_file_path = get_csv_file_path()
    with csv_file_path.open(mode, encoding=DEFAULT_ENCODING) as csv_file:
        print(f"csv_file mode: {csv_file.mode}")
        print(f"csv_file readable: {csv_file.readable()}")
        print(f"csv_file writable: {csv_file.writable()}")


def read_and_write_text_files():
    test_file_path = Path.cwd() / "learn" / "file_system" / "test.txt"
    with test_file_path.open(mode="w+", encoding=DEFAULT_ENCODING) as test_file:
        num_of_characters_written = test_file.write(RANDOM_TEXT)
        print(f"num_of_characters_written: {num_of_characters_written}")
        test_file.seek(0)  # Reset the file pointer to the beginning of the file
        print(f"text_read: {test_file.read()}")
        print("new line written by print", file=test_file)
        test_file.seek(0)
        print(f"text_read: {test_file.read()}")

    print("--------------------------------")
    csv_file_path = get_csv_file_path()
    with csv_file_path.open(mode="r", encoding=DEFAULT_ENCODING) as csv_file:
        csv_file_lines = csv_file.readlines()
        for line in csv_file_lines:
            print(line)
        csv_file.seek(0)
        for line in csv_file:
            print(line.strip())


def read_csv_data_with_reader():
    csv_file_path = get_csv_file_path()
    with csv_file_path.open(
        mode="r", encoding=DEFAULT_ENCODING, newline=""
    ) as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            print(row)


def read_csv_data_with_dict_reader():
    csv_file_path = get_csv_file_path()
    with csv_file_path.open(
        mode="r", encoding=DEFAULT_ENCODING, newline=""
    ) as csv_file:
        dict_reader = csv.DictReader(csv_file)
        print(f"fieldnames: {dict_reader.fieldnames}")
        for row in dict_reader:
            print(row)


def write_csv_data_with_writer():
    test_file_path = Path.cwd() / "learn" / "file_system" / "test_write.csv"
    with test_file_path.open(
        mode="w", encoding=DEFAULT_ENCODING, newline=""
    ) as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(["Date", "Amount", "Category"])
        csv_writer.writerow(["2025-01-01", "100", "Food"])
        csv_writer.writerow(["2025-01-02", "200", "Transport"])


def write_csv_data_with_dict_writer():
    test_file_path = Path.cwd() / "learn" / "file_system" / "test_write_dict.csv"
    with test_file_path.open(
        mode="w", encoding=DEFAULT_ENCODING, newline=""
    ) as csv_file:
        dict_writer = csv.DictWriter(
            csv_file, fieldnames=["Date", "Amount", "Category"]
        )
        dict_writer.writeheader()
        dict_writer.writerow(
            {"Date": "2025-01-01", "Amount": "100", "Category": "Food"}
        )
        dict_writer.writerow(
            {"Date": "2025-01-02", "Amount": "200", "Category": "Transport"}
        )


def main():
    # read_and_close_a_file()
    # understand_text_and_binary_files(mode="rb")
    # specify_character_encoding()
    # choose_line_ending()
    # explore_different_file_modes()
    # read_and_write_text_files()

    # read_csv_data_with_reader()
    # read_csv_data_with_dict_reader()

    # write_csv_data_with_writer()
    write_csv_data_with_dict_writer()


if __name__ == "__main__":
    main()
