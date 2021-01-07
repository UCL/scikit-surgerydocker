import pytest
from project.app import read_file, write_file

# 1. Test case to check successfully reading the file
def test_read_file():
    data = read_file('./data/', 'test_data.txt')
    assert data == 'Hello World\n'

# 2. Test case to throw general exception
def test_read_except():
    with pytest.raises(Exception):
        data = read_file('./no_path/', 'no_file_exist.txt')

# 3. Test case to successfully writing to a file
def test_write_file():
    write_file('Hello World/n', './data/', 'test_data2.txt')

# 4. Test case to throw general exception
def test_write_except():
    with pytest.raises(Exception):
        write_file('Hello World/n', './no_path/', 'no_file_exist.txt')

