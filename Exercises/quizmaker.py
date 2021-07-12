#Quiz Maker By: Hasan Saleh
from tkinter import *
from tkinter import filedialog
import os,random,webbrowser,time
global exportfile
folder=""
ansar=[]
s=0
num=0
root=Tk()
def __remove__(str):
    return str.replace('_',' ')
def __read__():
    #TO HTML
    global folder
    root.withdraw()
    root.filename=filedialog.askopenfilename(initialdir="C:/",title="Select A File")
    folderf=""
    for h in range(len(root.filename.split('/'))-1):
        folderf=folderf+root.filename.split('/')[h]+"/"
    folder=folderf
    f2=folder
    exportfile=open(folder+'exam.html','w')
    exportfile.write('''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Exam</title>
    </head>
    <body>
        <style>
        body{
            background-color:#ccc;
        }
        pre{
            background-color:gainsboro;
        }
    </style>
    ''')
    s=0
    filer=open(root.filename,'r')
    num=11
    for x in filer:
        ans=1
        s=s+1
        t=random.randint(0,3)
        if(t==0):
            q=(str(s)+'. '+__remove__(x.split()[0])+'\nA.'+__remove__(x.split()[3])+'\nB.'+__remove__(x.split()[2])+'\nC.'+__remove__(x.split()[1])+'\nD.'+__remove__(x.split()[4]))
            ansar.append('C')
            exportfile.write('''
                <strong>
                    <pre>
                        '''+q+'''<br><input type="text" id="q'''+str(s)+'''"/></pre></strong>
        ''')
        if(t==1):
            q=(str(s)+'. '+__remove__(x.split()[0])+'\nA.'+__remove__(x.split()[2])+'\nB.'+__remove__(x.split()[1])+'\nC.'+__remove__(x.split()[3])+'\nD.'+__remove__(x.split()[4]))
            ansar.append('B')
            exportfile.write('''
                <strong>
                    <pre>
                        '''+q+'''<br><input type="text" id="q'''+str(s)+'''"/></pre></strong>
        ''')
        if(t==2):
            q=(str(s)+'. '+__remove__(x.split()[0])+'\nA.'+__remove__(x.split()[4])+'\nB.'+__remove__(x.split()[2])+'\nC.'+__remove__(x.split()[3])+'\nD.'+__remove__(x.split()[1]))
            ansar.append('D')
            exportfile.write('''
                <strong>
                    <pre>
                        '''+q+'''<br><input type="text" id="q'''+str(s)+'''"/></pre></strong>
        ''')
        if(t==3):
            q=(str(s)+'. '+__remove__(x.split()[0])+'\nA.'+__remove__(x.split()[1])+'\nB.'+__remove__(x.split()[3])+'\nC.'+__remove__(x.split()[2])+'\nD.'+__remove__(x.split()[4]))
            ansar.append('A')
            exportfile.write('''
                <strong>
                    <pre>
                        '''+q+'''<br><input type="text" id="q'''+str(s)+'''"/></pre></strong>
        ''')
    exportfile.close()
    print('The Exam have '+str(s)+' Questions')
    num=s
__read__()
os.system('pause')
webbrowser.open_new(folder+'exam.html')
stransar='['
for i in range(len(ansar)):
    stransar+='"'+ansar[i]+'"'
    if(i != len(ansar)-1):
        stransar+=','
    else:
        stransar+=']'
filev=open(root.filename,'r')
for x in filev:
    num=num+1
file=open(folder+'exam.html','a')
file.write('''<button onclick="check()"> Submit </button>
<script>const ansar='''+stransar+''';
function check(){
    score=0;
    for(var i=1;i<='''+str(num)+''';i++){
        if(document.getElementById('q'+i.toString()).value == ansar[i-1]){
            score++;
        }else{
            //Nothing....
        }
    }
    score=(Math.ceil(score/'''+str(num)+'''*100))
    document.write()

    document.write("<!DOCTYPE HTML><HTML><head><title>Result</title><body><center><h1>The Result is:"+score.toString()+'%</h1></center></body></html>')
}
</script>
''')
file.close()
time.sleep(2)
Tk.destroy()
exit()
