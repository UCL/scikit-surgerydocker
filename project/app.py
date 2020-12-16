"""This module gives a simple example to demonstrate how to structure
the project to effectively work with any third party data. That includes
reading the data and writing the results.  An input folder with a small
text file and an output folder is included in the repo"""


def main():
   """The main function that reads the data from input file in the
   input folder, process it and store the results in the output file
   in the output folder. The input folder, inputfile.txt and output
   folder already exist.
   
   Args:
    None
   Returns:
    None
   Raises:
    IOError: An error occurred accessing the input/inputfile.txt.
    
   
   """


   
   contents = ''

   try:
      with open('./input/inputfile.txt', 'r') as inputfile:
         contents = inputfile.read()
   except IOError:
      print('An error occurred accessing the input/inputfile.txt')

   try:
      with open('./output/outputfile.txt', 'w+') as outputfile:
         outputfile.write(contents)
         for item in range(0,5):
            outputfile.write('\nText is copied from input/file.txt and \
               pasted to a new file output/file.txt along with these 5 new lines.')
      print('A new file is created successfully in ./output directory')

   except:
      print('Output file cannot be written')


if __name__ == '__main__':
   main()
