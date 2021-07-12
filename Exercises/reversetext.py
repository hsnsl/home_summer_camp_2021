a=input('Enter The Word: ')
new=''
for i in range(0,len(a)):
    new=new+a[len(a)-1-i]
print(new.capitalize())
