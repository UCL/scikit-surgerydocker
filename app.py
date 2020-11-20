def main():

   with open('input/file.txt', 'r') as inputfile:
      contents = inputfile.read()

   with open('output/file.txt', 'w+') as outputfile:
      outputfile.write(contents)
      for item in range(0,5):
         outputfile.write('\nText is copied from input/file.txt and \
         pasted to a new file output/file.txt along with these 5 new lines.')

if __name__ == '__main__':
   main()