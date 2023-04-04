print("""

           88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88  
"""
)

def caesar_cipher(input_string, shift_number, decode_or_encode):
    return_message = ""
    for charac in input_string:
        if decode_or_encode == "decode":
            if charac.isalpha():
                return_message += chr((ord(charac)-shift_number-97) % 26 + 97) 
                
            else:
                return_message += charac  
        else:
            if charac.isalpha():
                return_message += chr((ord(charac)+shift_number-97) % 26 + 97)
                
            else:
                return_message += charac  
    return return_message


Yes_Or_No = "yes"
while Yes_Or_No == "yes":
    decode_or_encode = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")
    input_string = input("Type your message: ").lower()
    shift_number = int(input("Type the shift number: ")) 
    print(f"Here is your {decode_or_encode}d message: ", caesar_cipher(input_string, shift_number, decode_or_encode))
    Yes_Or_No = input("Type 'yes' if you want to go again. Otherwise type 'no': ")
