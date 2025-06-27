# Cipher Time #

# https://cryptii.com/pipes/caesar-cipher

# .replace("replacement","replacing?")

# Lists
letters_replacing = []
letter_replacements = []
replacement_candidates = []
replaced_by_candidates = []

# Text
original_text = ""
decoding_text = ""
decoded_text = ""

# Letter vars
replacing = ""
replacement = ""


print("Welcome to the decoder/encoder")


def start():
    print("What would you like to do?")
    print("1. Decode cipher\n2. Encode cipher")
    choice = input("> ")

    if choice == "1":
        decode_start()
    elif choice == "2":
        print("encoding not availble atm")
        decode_start()

    else:
        start()


def decode_start():
    print("Please provide text to decode (please use lower case for now)") # code breaks here
    global encoded_text
    encoded_text = input("> ")

    global original_text
    original_text = encoded_text

    global decoding_text
    decoding_text = encoded_text
    
    substitution_time()


def substitution_time():
    #decoded_text_step = ""
    #global decoded_text = decoded_text_step
    print("---")
    print("Type letter to be replaced (please use lower case for now)")
    global replacing
    replacing = input("> ")
    #print("replacing:",replacing)

    if replacing == " ": # i think just "" is interpreted as str()
        substitution_time()
    elif len(replacing) > 1:
        substitution_time() # missing bracket

    print(replaced_by_candidates)


    print("Type letter to replace it with (please use lower case for now)")
    global replacement
    replacement = input("> ")
    #print("replacement:",replacement)

    if replacement == " ":
        substitution_time()
    elif len(replacement) > 1:
        substitution_time()

    print(replacement_candidates)

    letters_replacing.append(replacing)
    letter_replacements.append(replacement)

    global decoding_text # messy atm
    decoding_text = decoding_text.replace(replacing, replacement) # not reverting changes any more?
    print("modified text:", decoding_text)
    letter_rating()


def letter_rating():
    print("store letter as possible success? Y/N (please use lower case for now)")
    choice = input("> ")
    if choice == "y":
        replaced_by_candidates.append(replacing)
        replacement_candidates.append(replacement)
        print("success candidate:", replacement_candidates, "letter replaced:",replaced_by_candidates) # list grows??
        #print("choice:",choice)

    elif choice == "n":
        print("no candidate found")
        #print("choice:",choice)
        

    # BUG Y code doesn't print anything at all, N code uses Y code with choice: n???

    substitution_time()



start()

# notify user of letter with highest count? like frequency analysis


# BUG can change letters into one that's still encoded (e.g a->h) and uhhh shit
# TODO store successful pairs, restart decoding
# cycle back through pairings, or list with indexes attached, add to success list
# or letter menu: mark replacement success, fail, replace a letter
# get index of "x" in list, if not, say "hasn't been used"

# dictionary to store pairs?

# realising this ^ is a UI huh


#print(replacing)
#print(replacement)

# here's a cipher to use, ceasar shift
"""
Pm ol ohk hufaopun jvumpkluaphs av zhf, ol dyval pa pu jpwoly, aoha pz, if zv johunpun aol vykly vm aol slaalyz vm aol 
hswohila, aoha uva h dvyk jvbsk il thkl vba.

"""


# DUMPING GROUND #
#if choice == "y" or "Y": # taking out "or Y" fixed it for some reason
#       replaced_by_candidates.append(replacing)
#        replacement_candidates.append(replacement)
#        print("success candidate:", replacement_candidates, "letter replaced:",replaced_by_candidates) # list grows??
#        print("choice:",choice) # code runs when N

# encoded_text.replace(replacing, replacement) # wasnt updating global, so... encoded_text = encoded_text.replace() 

# #letters_replacing.pop() if bad input # restarting would've added to prev list and desync