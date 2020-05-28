import requests
import pyperclip


#spec = '{"type":"page", "canvas":"https://uah.instructure.com/courses/45964/pages/11-oo-basics", "github":"https://github.com/topherCantrell/class-IntroPython/blob/master/Topics/11_OO_Basics/README.md"},'
spec = '{"type":"page", "canvas":"https://uah.instructure.com/courses/45964/pages/01-environment", "github":"https://github.com/topherCantrell/class-IntroPython/blob/master/Topics/01_Environment/README.md"},'

i = spec.find('"canvas":')+9
i = spec.find('"',i)+1
j = spec.find('"',i)
canvas = spec[i:j]

i = spec.find('"github":')+9
i = spec.find('"',i)+1
j = spec.find('"',i)
github = spec[i:j]

def replace_images_with_ref(text):
    
    pos = 0
    while True:
        i = text.find('<img',pos)
        if i<0:
            return text
        j = text.find('>',i)
        pos = j
        
        i = text.rfind('<a ',0,i)
        j=j+4
        print(text[i:j+1])
        
        rep = text[i+1:j]
        rep = rep.replace('<','')
        rep = rep.replace('>','')
        
        text = text[0:i]+'\n\n<p>IMGREP '+rep+'</p>\n\n'+text[j+1:]        

def replace_class_with_style(text):
    
    # Find all the classes we are using
    
    classes = set()
    pos = 0
    
    while True:
        i = text.find('class=',pos)
        if i<0:
            break
        i = text.find('"',i)+1
        j = text.find('"',i)
        c = text[i:j]
        pos = j
        classes.add(c)
        
    styles = {}
    with open('frameworks.css') as f:
        style = f.read()
        
    for c in classes:
        i = style.find('.'+c)
        if i<0:
            continue
        i = style.find('{',i)
        j = style.find('}',i)
        styles[c] = style[i+1:j]
        
    for c in styles:
        cs = 'class="'+c+'"'
        rep = 'style="'+styles[c]+'"'
        text = text.replace(cs,rep)
        
    return text
            
r = requests.get(github)
t = r.text

i = t.find('<article')
i = t.find('>',i)+1
j = t.find('</article>',i)
t = t[i:j]

rep = replace_class_with_style(t)

rep = replace_images_with_ref(rep)

rep.find('topherCantrell')
pyperclip.copy(rep)           


    
            