import decoder
import encoder
def start():
    try:
        userInput = input("You want to Encode(E) or Decode(D): " )
        if userInput == "D":
            user_string = input("Please enter the encoded string: ")
            print("Decoded String: ", decoder.decode(user_string))
        elif userInput == "E":
            user_string = input("Please input the string to encode: ")
            print("Encoded String: ", encoder.encoder(user_string))
        else:
            raise ValueError("Please try again")
    except:
        start()
start()
