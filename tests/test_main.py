import pytest
from project.app import read_file, write_file

def test_read_file():
    data = read_file('./data/', 'test_data.txt')
    assert data == 'Hello World\n'

def test_read_except():
    with pytest.raises(IOError):
        data = read_file('./data/', 'no_file_exist.txt')

def test_write_file():
    write_file('Hello World/n', './data/', 'test_data2.txt')

def test_write_except():
    with pytest.raises(FileNotFoundError):
        write_file('Hello World/n', './no_path/', 'test_data2.txt')

