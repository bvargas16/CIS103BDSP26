# Brian Vargas P11
from datetime import datetime

def main(): # read line first
    starttime = datetime.now()
    print('Program started at:', starttime)

    pointsin = '/Users/brianvargas/Desktop/temp/points.txt'
    infile = open(pointsin, 'r')

    gradesout = '/Users/brianvargas/Desktop/temp/grades.txt'
    gradefile = open(gradesout, 'w')

    errorout = '/Users/brianvargas/Desktop/temp/errors.txt'
    errorfile = open(errorout, 'w')

    reccnt = 0
    acnt = 0
    bcnt = 0
    ccnt = 0
    dcnt = 0
    fcnt = 0
    goodcnt = 0
    errorcnt = 0
   
    line = infile.readline()
   
    while line != '':
        reccnt += 1

        var1 = line.strip().split(',')

        idnum = var1[0]
        name = var1[1]
        points = var1[2]

        try:
            points = int(points)
            
            if points < 0:
                rcd = idnum + ',' + name + ',' + str(points) + ',' + 'Points cannot be negative\n'
                errorfile.write(rcd)
                errorcnt += 1

            elif points > 1000:
                rcd = idnum + ',' + name + ',' + str(points) + ',' + 'Points cannot be greater than 1000\n'
                errorfile.write(rcd)
                errorcnt += 1    
            
            else: #use the grade logic table to determine the grade
                if points >= 900:
                    grade = 'A'
                    acnt += 1
                elif points >= 800:
                    grade = 'B'
                    bcnt += 1
                elif points >= 700:
                    grade = 'C'
                    ccnt += 1
                elif points >= 600:
                    grade = 'D'
                    dcnt += 1
                else:
                    grade = 'F'
                    fcnt += 1

                rcd = idnum + ',' + name + ',' + str(points) + ',' + grade + '\n'
                gradefile.write(rcd)
                goodcnt += 1

        except ValueError:
            rcd = idnum + ',' + name + ',' + points + ',' + 'INVALID POINTS\n'
            errorfile.write(rcd)
            errorcnt += 1

        line = infile.readline()
        
    infile.close()
    gradefile.close()
    errorfile.close()

    endtime = datetime.now()

    print('\nNumber of records read:', reccnt)
    print('Number of good records:', goodcnt)
    print('Number of error records:', errorcnt)
    print('\nGrade distribution:')
    print('A:', acnt)
    print('B:', bcnt)
    print('C:', ccnt)
    print('D:', dcnt)
    print('F:', fcnt)
    print('\nProgram ended at:', endtime)
main()
