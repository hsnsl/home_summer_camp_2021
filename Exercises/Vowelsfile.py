import os
vowels=['a','i','e','o','u']
va=0
vi=0
ve=0
vo=0
vu=0
v=0
words=0
file=open('file_here!','r')
for vv in file:
        s=len(vv.split())
        for ss in vv:
            if(ss.lower() == 'a'):
                va=va+1
            if(ss.lower() == 'i'):
                vi=vi+1
            if(ss.lower() == 'e'):
                ve=ve+1
            if(ss.lower() == 'o'):
                vo=vo+1
            if(ss.lower() == 'u'):
                vu=vu+1
        words=words+s
print('Number of Words:'+str(words))
print('Number of Vowels is :'+str(v))
print('Number of repeats vowel a :'+str(va))
print('Number of repeats vowel i :'+str(vi))
print('Number of repeats vowel e :'+str(ve))
print('Number of repeats vowel o :'+str(vo))
print('Number of repeats vowel u :'+str(vu))
