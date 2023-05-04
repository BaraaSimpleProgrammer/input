from getch import getch
def Input(prompt, mask=None, is_invisible=False):
    Delete_Char = "\x7f"
    print (prompt, end="", flush=True)
    value = []
    if not is_invisible:
        while True:
            symbol = getch()
            if symbol in ["\n","\r"]:break
            elif symbol == Delete_Char and len(value)>0:
                print ("\b \b",end="",flush=True )
            elif len(value)==0 and symbol == Delete_Char:
                pass
            else:print (mask if mask else symbol,end="", flush =True )
            if not (symbol == Delete_Char):value += symbol
            elif (symbol == Delete_Char):
                try:
                    del value[len(value)-1]
                except IndexError:
                    value=[]
    elif is_invisible:
        while True:
            symbol = getch()
            if symbol in ["\n","\r"]:break
            if not (symbol == Delete_Char):value += symbol
            elif (symbol == Delete_Char):
                try:
                    del value[len(value)-1]
                except IndexError:
                    value=[]
    print ()
    return ''.join(value)