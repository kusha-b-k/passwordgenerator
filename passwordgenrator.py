import random

def passwrodGenerator(strength):
    passwoord_charactors_list ="1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
    if strength in range(0, 8):
     print( "password strength is normal" )
    elif strength in range(8,16):
     print( "password strength is GOOD" )
    elif strength in range(15, 26):
     print( "password strength is strong" )
    else:
     print( "UNBRACKBLE PAASWORD" )
    return "".join(random.sample(passwoord_charactors_list, strength))

print("YOUR PASSWORD IS :", passwrodGenerator(20))
