import os,time,datetime,webbrowser
def run(file):
    os.system('mkdir final')
    f2=open('final/index.html','a')
    ff=open('final/index.html','w')
    ff.write('')
    f2.write('''<!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
        ''')
    f=open(file,'r')
    for x in f:
        if(x.lower().split()[0]=='title'):
            f2.write('<title>')
            n=0
            try:
                while(x.lower().split()[n] != "" or x.lower().split()[n] != " "):
                    n=n+1
                    f2.write(" ")
                    f2.write(x.lower().split()[n])
            except:
                f2.write('</title>')
                print('Errors Igroned')
        if(x.lower().split()[0] == 'import'):
                f2.write('''
                <link rel="stylesheet" href="'''+x.lower().split()[1]+'''">''')
        if(x.lower().split()[0] == 'img'):
            f2.write('''
            <img src="'''+x.split()[1]+'''" id="'''+x.split()[2])
        
        if(x.lower().split()[0]=='head_end'):
            f2.write('''
            </head><body>''')
        if(x.lower().split()[0]=="h1"):
            x=x.replace('_','&#32;')
            f2.write('<h1 id="'+x.split()[2]+'" class="'+x.split()[3]+'">'+x.split()[1]+'</h1>')

        if(x.lower().split()[0]=="h2"):
            x=x.replace('_','&#32;')
            f2.write('<h2 id="'+x.split()[2]+'" class="'+x.split()[3]+'">'+x.split()[1]+'</h21>')
        
        if(x.lower().split()[0]=="h3"):
            x=x.replace('_','&#32;')
            f2.write('<h3 id="'+x.split()[2]+'" class="'+x.split()[3]+'">'+x.split()[1]+'</h3>')

        if(x.lower().split()[0]=="h4"):
            x=x.replace('_','&#32;')
            f2.write('<h4 id="'+x.split()[2]+'" class="'+x.split()[3]+'">'+x.split()[1]+'</h4>')

        if(x.lower().split()[0]=="h5"):
            x=x.replace('_','&#32;')
            f2.write('<h5 id="'+x.split()[2]+'" class="'+x.split()[3]+'">'+x.split()[1]+'</h5>')

        if(x.lower().split()[0]=="h6"):
            x=x.replace('_','&#32;')
            f2.write('<h6 id="'+x.split()[2]+'" class="'+x.split()[3]+'">'+x.split()[1]+'</h6>')

        if(x.lower().split()[0]=="p"):
            x=x.replace('_','&#32;')
            f2.write('<p id="'+x.split()[2]+'" class="'+x.split()[3]+'">'+x.split()[1]+'</p>')

        if(x.lower().split()[0]=="label"):
            x=x.replace('_','&#32;')
            f2.write('<label id="'+x.split()[2]+'" class="'+x.split()[3]+'">'+x.split()[1]+'</label>')
        if(x.lower().split()[0] == "line"):
            f2.write('<br>')
        
        if(x.lower().split()[0]=="link"):
            x=x.replace('_','&#32;')
            f2.write('<a href='+x.split()[2]+' " id="'+x.split()[3]+'" class="'+x.split()[4]+'">'+x.split()[1]+'</a>')
        if(x.lower().split()[0]=="video"):
            f2.write('''
                <video width="320" height="240" controls autoplay>
                <source src="'''+x.split()[1]+'''" type="video/mp4">
                <source src="'''+x.split()[1]+'''" type="video/ogg">
                Your browser does not support the video tag.
                </video>)''')
        if(x.lower().split()[0]=="youtube"):
            f2.write('''
            <iframe width="853" height="480" src="https://www.youtube.com/embed/'''+x.split()[1]+'''" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>''')
        if(x.lower().split()[0]=="facebook"):
            f2.write('''
            <iframe src="https://www.facebook.com/plugins/video.php?height=314&href='''+x.split()[1]+'''&show_text=true&width=560&t=0" width="560" height="429" style="border:none;overflow:hidden" scrolling="no" frameborder="0" allowfullscreen="true" allow="autoplay; clipboard-write; encrypted-media; picture-in-picture; web-share" allowFullScreen="true"></iframe>
            ''')
        if(x.lower().split()[0]=="img"):
            f2.write('''
            <img src="'''+x.split()[1]+'''" id="'''+x.split()[2]+'''" class="'''+x.split()[3]+'''">''')
        if(x.lower().split()[0]=="favicon"):
            f2.write('''
            <link rel="icon" type="image/x-icon" href="'''+x.split()[1]+'''">''')
        if(x.lower().split()[0]=="ul"):
            f2.write('<ul>')
        if(x.lower().split()[0]=="li"):
            f2.write("<li>"+x.split()[1]+"</li>")
        if(x.lower().split()[0]=="ul_end"):
            f2.write("</ul>")
        if(x.lower().split()[0]=="hr"):
            f2.write("<hr>")
        if(x.lower().split()[0]=="strong"):
            f2.write("<strong>"+x.split()[1]+"</strong>")
        if(x.lower().split()[0]=="del"):
            f2.write("<del>"+x.split()[1]+"</del>")
        if(x.lower().split()[0]=="u"):
            f2.write("<u>"+x.split()[1]+"</u>")
        if(x.lower().split()[0]=="mark"):
            f2.write("<mark>"+x.split()[1]+"</mark>")
        if(x.lower().split()[0]=="samp"):
            f2.write("<samp>"+x.split()[1]+"</samp>")
        if(x.lower().split()[0]=="code"):
            f2.write("<code>"+x.split()[1]+"</code>")
        if(x.lower().split()[0]=="var"):
            f2.write("<var>"+x.split()[1]+"</var>")
        if(x.lower().split()[0]=="mail"):
            f2.write('''<a href="mailto:'''+x.split()[1]+'''">'''+x.split()[1]+"</a>")
        if(x.lower().split()[0]=="jump"):
            f2.write('''<a href="#'''+x.split()[1]+'''>"+x.split()[1]+"</a>''')
        if(x.lower().split()[0]=="button"):
            f2.write('''<button id="'''+x.split()[1]+'''" class="'''+x.split()[2]+'''">'''+x.split()[1]+'''</button>''')
        if(x.lower().split()[0]=="script"):
            f2.write('''<script src="'''+x.split()[1]+'"></script>')
        if(x.lower().split()[0]=="body_end"):
            f2.write("</body>")
print("BWeb Descriptor Language All Rights Reserved to Hasan Saleh ©")
print("Special Thanks to Harmash.com for The Resources 	♥ ")
print("The Source file is a.cwc")
run('a.cwc')
print("\033[1m\033[92m ✓ Test Passed [VER:"+str(datetime.datetime.now())+"  ] ")
time.sleep(2)
path=os.getcwd()
path=path+'/'
path=path+'final\index.html'
webbrowser.open_new(path)
os.system("pause")