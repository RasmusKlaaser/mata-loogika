"""File operations."""
import csv
import os.path

def read_file_contents(filename: str) -> str:
    """
    Read file contents into string.

    In this exercise, we can assume the file exists.

    :param filename: File to read.
    :return: File contents as string.
    """
    f = open(filename, "r")
    file_content = f.read()
    f.close()
    return file_content

print(read_file_contents("file.txt"))

def read_file_contents_to_list(filename: str) -> list:
    r"""
    Read file contents into list of lines.

    In this exercise, we can assume the file exists.
    Each line from the file should be a separate element.
    The order of the list should be the same as in the file.

    List elements should not contain new line (\n).

    :param filename: File to read.
    :return: List of lines.
    """

    list_of_lines = []
    with open(f"{filename}", "r") as f:
        for line in f:
            new_line = line.replace("\n", "")
            list_of_lines.append(new_line)
    return list_of_lines

def read_csv_file(filename: str) -> list:
    """
    Read CSV file into list of rows.

    Each row is also a list of "columns" or fields.

    CSV (Comma-separated values) example:
    name,age
    john,12
    mary,14

    Should become:
    [
      ["name", "age"],
      ["john", "12"],
      ["mary", "14"]
    ]

    Use csv module.

    :param filename: File to read.
    :return: List of lists.
    """
    result = []
    with open(f"{filename}") as f:
        for row in csv.reader(f):
            result.append(row)
    return result


def write_contents_to_file(filename: str, contents: str) -> None:
    """
    Write contents to file.

    If the file does not exists, create it.

    :param filename: File to write to.
    :param contents: Content to write to.
    :return: None
    """
    if os.path.exists(filename) != True:
        open(filename, "w")
    f = open(filename, "a")
    f.write(contents)
    f.close()

write_contents_to_file("test1.txt", "some text to file")

def write_lines_to_file(filename: str, lines: list) -> None:
    """
    Write lines to file.

    Lines is a list of strings, each represents a separate line in the file.

    There should be no new line in the end of the file.
    Unless the last element itself ends with the new line.

    :param filename: File to write to.
    :param lines: List of string to write to the file.
    :return: None
    """
    open(filename, "w").write("\n".join(lines))


def write_csv_file(filename: str, data: list) -> None:
    """
    Write data into CSV file.

    Data is a list of lists.
    List represents lines.
    Each element (which is list itself) represents columns in a line.

    [["name", "age"], ["john", "11"], ["mary", "15"]]
    Will result in csv file:

    name,age
    john,11
    mary,15

    Use csv module here.

    :param filename: Name of the file.
    :param data: List of lists to write to the file.
    :return: None
    """
    with open(filename, "w") as file:
        for line in data:
            file.write(",".join(line) + "\n")


def merge_dates_and_towns_into_csv(dates_filename: str, towns_filename: str, csv_output_filename: str) -> None:
    """
    Merge information from two files into one CSV file.

    Dates file contains names and dates. Separated by colon.
    john:01.01.2001
    mary:06.03.2016

    You don't have to validate the date.
    Every line contains name, colon and date.

    Towns file contains names and towns. Separated by colon.
    john:london
    mary:new york

    Every line contains name, colon and town name.
    There are no headers in the input files.

    Those two files should be merged by names.
    The result should be a csv file:

    name,town,date
    john,london,01.01.2001
    mary,new york,06.03.2016

    Applies for the third part:
    If information about a person is missing, it should be "-" in the output file.

    The order of the lines should follow the order in dates input file.
    Names which are missing in dates input file, will follow the order
    in towns input file.
    The order of the fields is: name,town,date

    name,town,date
    john,-,01.01.2001
    mary,new york,-

    Hint: try to reuse csv reading and writing functions.
    When reading csv, delimiter can be specified.

    :param dates_filename: Input file with names and dates.
    :param towns_filename: Input file with names and towns.
    :param csv_output_filename: Output CSV-file with names, towns and dates.
    :return: None
    """
    dates = read_csv_file(dates_filename)
    towns = read_csv_file(towns_filename)
    date_dict = {}
    towns_dict = {}
    names_list = []
    for line in dates:
        line = [0].split(":")
        date_dict[line[0]] = line[1]
        names_list.append(line[0])
#dictionaries are empty and we seperate them with colons
#dates dictionaries file contains dates and is separated by colons

    for line in towns:
        line = [0].split(":")
        towns_dict[line[0]] = line[1]
        names_list.append(line[0])
        if line[0] not in names_list:
            names_list.append(line[0])

#town dictionaries file contains town and is separated by colons

    date = []
    date.append(["name", "date", "town"])

#appending names, dates and towns into a empty list

    for name in name_list:
        row = [name]
    if name in town_dict:
        row.append(date_dict[name])
    else:
        row.append("-")

#checks if the name exists and appends it, if not it adds -

    data.append(row)
    write_csv_file(csv_output_filename, data)

