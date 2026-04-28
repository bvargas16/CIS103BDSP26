#Brian Vargas
#P12 Chicago Rainfall in 2017

#do not hardcode, get input from a txt file or split

def main():
   filenamein = '/Users/brianvargas/Desktop/temp/rainfall.txt'
   infile =  open(filenamein, 'r')
   numblist = []
   for line in infile:
      line = line.strip()
      numblist.append(float(line))
   print('Data List:', numblist)
   print('-'*30)
   print('Highest: ', max(numblist))
   print('Lowest: ', min(numblist))
   print('Total: ', sum(numblist))
   print('Average: ', sum(numblist)/len(numblist))
   infile.close()
main()
