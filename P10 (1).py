def main():
    thetext = '''
       Python was conceived in the late 1980’s by Netherlands programmer
Guido Van Rossum and rolled out in 1991. Developing the language
was a hobby project for Van Rossum to keep him occupied over
Christmas, though he soon began implementing the language at
his employer Centrum Wiskunde & Informatica (CWI). The name of
the language was inspired by Monty Python’s Flying Circus, and
today users of this code often work in references to Monty Python.
Python is one of the most popular programming languages in the
world. As a scripting language that can automate a complex series
of tasks, Python is used on the back end of many web applications,
games, and digital and animated special effects. Sites like YouTube
and Instagram are among some of the titans that rely on this
language to support both front-end and back-end functionality.    
        '''
    print(thetext)


# ---------------------------------
#  put assignment statements here
    var1 = len(thetext)
    print('the length is:', var1, 'characters')
    stripped_text = thetext.strip()
    print('the new length is:', len(stripped_text), 'characters')

    nb1 = thetext.count('the')
    print('the word the is found', nb1, 'times')

    if 'little' in thetext:
        print('little is in the text')
    else:
        print('little IS NOT in the text')

    if 'titan' not in thetext:
        print('titan is not in the text')
    else:
        print('titan IS IN the text')

    nb2 = thetext.find('appl')
    print('position number for appl is:', nb2)

    thetext2 = '''
        Python was conceived in the late 1980’s by Netherlands programmer
Guido Van Rossum and rolled out in 1991. Developing the language
was a hobby project for Van Rossum to keep him occupied over
Christmas, though he soon began implementing the language at
his employer Centrum Wiskunde & Informatica (CWI). The name of
the language was inspired by Monty Python’s Flying Circus, and
today users of this code often work in references to Monty Python.
Python is one of the most popular programming languages in the
world. As a scripting language that can automate a complex series
of tasks, Python is used on the back end of many web applications,
games, and digital and animated special effects. Sites like YouTube
and Instagram are among some of the titans that rely on this
language to support both front-end and back-end functionality.    
        '''
    nb3 = thetext2.replace('Python', 'PYTHON')
    print(nb3)
# ---------------------------------
    return
main()
