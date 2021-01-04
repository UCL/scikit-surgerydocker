"""This module gives a simple example to demonstrate how to structure
the project to effectively work with any third party data. That includes
reading data from input file and writing results to output file. An input folder with a small
text file and an output folder is included in the repo"""


def read_file(file_path, file_name):
   """Read data from a text file stored in the input directory

   Args:
      file_path (str, optional): The path containing the file to read.
      file_name (str, optional): The name of the file to be read.

   Returns:
      data (str) data read from the file.
   
   Raises:
      IOError: An exception thrown if ./input/inputfile.txt not found.
   """
   
   full_path = file_path + file_name
   try:
      with open(full_path, 'r') as input_file:
         data = input_file.read()
         return data
   except IOError:
      print('An error occurred accessing the input/input_file.txt')
   except Exception as e:
      print('An exception is thrown when reading the input file.', e)
   



def write_file(contents, file_path, file_name):
   """Write data to a text file stored in the output directory.

   Args:
      contents (str): The text to write to output file.
      file_path (str, optional): The path containing the file to read.
      file_name (str, optional): The name of the file to be read.

   Returns:
      None
   
   Raises:
      When the program fail to create and write to text file.
   """
   full_path = file_path + file_name
   try:
      with open(full_path, 'w+') as output_file:
         output_file.write(contents)
         for item in range(0,5):
            output_file.write('\nAppended line {} by write_file function.'.format(item))

      print('A new file is created successfully in ./output directory')

   except:
      print('Output file cannot be written')


if __name__ == '__main__':
   contents = read_file(file_path='./input/', file_name='input_file.txt')
   write_file(contents, file_path='./output/', file_name='output_file.txt')
