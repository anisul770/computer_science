gradel='ABCDF'
gradeN=4,3,2,1,0
N=input('Enter a letter grade:')
N=N.upper()
h=gradel.find(N)
if h!=-1:
 print('The Numerical Grade is ',float(gradeN[h]))
else:
    print('Invalid Input')

