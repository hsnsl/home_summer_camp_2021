vowels=['a','i','e','o','u']
va=0
vi=0
ve=0
vo=0
vu=0
v=0
a=input('write:')
for vv in a:
    if(vv.lower()  in vowels):
        v=v+1
        if(vv.lower() == 'a'):
            va=va+1
        if(vv.lower() == 'i'):
            vi=vi+1
        if(vv.lower() == 'e'):
            ve=ve+1
        if(vv.lower() == 'o'):
            vo=vo+1
        if(vv.lower() == 'u'):
            vu=vu+1
print('Number of Vowels is :'+str(v))
print('Number of repeats vowel a :'+str(va))
print('Number of repeats vowel i :'+str(vi))
print('Number of repeats vowel e :'+str(ve))
print('Number of repeats vowel o :'+str(vo))
print('Number of repeats vowel u :'+str(vu))
