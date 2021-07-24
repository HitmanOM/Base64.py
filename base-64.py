import base64
#------------------------------------------------------------------------------
#base64
print('''
██████╗░░█████╗░░██████╗███████╗░█████╗░░░██╗██╗░░░██████╗░██╗░░░██╗
██╔══██╗██╔══██╗██╔════╝██╔════╝██╔═══╝░░██╔╝██║░░░██╔══██╗╚██╗░██╔╝
██████╦╝███████║╚█████╗░█████╗░░██████╗░██╔╝░██║░░░██████╔╝░╚████╔╝░
██╔══██╗██╔══██║░╚═══██╗██╔══╝░░██╔══██╗███████║░░░██╔═══╝░░░╚██╔╝░░
██████╦╝██║░░██║██████╔╝███████╗╚█████╔╝╚════██║██╗██║░░░░░░░░██║░░░
╚═════╝░╚═╝░░╚═╝╚═════╝░╚══════╝░╚════╝░░░░░░╚═╝╚═╝╚═╝░░░░░░░░╚═╝░░░
                                                           By HitmanOM''')
while True:

    print('1 : Encode')
    print('2 : Decode')
    in1 = input('Enter Your Choice: ') 
    if in1 in ('1','2'):
        if in1 == '1':
            text = input('Enter The Text you Want To encode: ')
            encoded_str = base64.b64encode(text.encode())
            print('encoded text:>('' ',(encoded_str),')')    
        elif in1 == '2': 
            text2 = input('Enter The Text you Want To decode: ')                   
            print('decoded base64:>',base64.b64decode(text2).decode())
        else:
            print('error')
    else:
        print('enter a valid choice')
    inp2 = input('En/Decode Again ? (y or n) : ')
    if inp2 == 'n':
        break
            #by HitmanOM
                #insta : lm9k