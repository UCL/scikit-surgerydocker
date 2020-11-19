def main():

   with open('input/file.txt', 'r') as inputfile:
      contents = inputfile.read()

   with open('output/file.txt', 'w+') as outputfile:
      outputfile.write(contents)
      for item in range(0,5):
         outputfile.write('\nThis line is appended by the program')

if __name__ == '__main__':
   main()