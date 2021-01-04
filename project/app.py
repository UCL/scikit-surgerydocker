"""This module gives a simple example to demonstrate how to structure
the project to effectively work with any third party data. That includes
reading data from input file and writing results to output file. An input folder with a small
text file and an output folder is included in the repo"""


def read_file(file_path, file_name):
   
   full_path = file_path + file_name
   try:
      with open(full_path, 'r') as input_file:
         return input_file.read()
   except IOError:
      print('An error occurred accessing the input/inputfile.txt')
   



def write_file(file_path, file_name):
   full_path = file_path + file_name
   try:
      with open(full_path, 'w+') as output_file:
         output_file.write(contents)
         for item in range(0,5):
            output_file.write('\nAppended line by write_file function.')

      print('A new file is created successfully in ./output directory')

   except:
      print('Output file cannot be written')


if __name__ == '__main__':
   contents = None
   contents = read_file(file_path='./input/', file_name='input_file.txt')
   write_file(file_path='./output/', file_name='output_file.txt')
