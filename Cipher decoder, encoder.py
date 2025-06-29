# Cipher Time #

# https://cryptii.com/pipes/caesar-cipher

# Dictionary, {replaced:replacement}
letter_replacements = {} # can update, no dupes, pairs. perfect for this

# Text
original_text = ""
decoding_text = ""
decoding_text_prev = ""
#decoded_text = ""

# Letter vars
replacing = ""
replacement = ""

# Candidate words
candidate_words = []


print("Welcome to the Decoder/Encoder")


def start():
    print("What would you like to do?")
    print("1. Decode cipher\n2. Encode cipher")
    choice = input("> ")

    if choice == "1":
        #decoding_cipher_options()
        cipher_on_hand()
    elif choice == "2":
        print("encoding not availble atm (enter anything to continue)")
        input("> ")
        cipher_on_hand()

    else:
        start()

def decoding_cipher_options():
    print("Decode example cipher? y/n (press Enter to skip)")
    choice = input("> ")
    if choice == "y":
        # grab YT comments, wikipedia excerpts
        print("no examples yet (enter anything to continue)")
        input("> ")
        
    elif choice == "n":
        cipher_on_hand()
    elif choice == "":
        cipher_on_hand()

    else:
        decoding_cipher_options()
    
    cipher_on_hand()


def cipher_on_hand():
    # give example ciphers option, Enter to skip
    print("Please provide text to decode (please use lower case for now)") # code breaks here
    global original_text
    original_text = input("> ")

    global encoded_text
    encoded_text = original_text

    global decoding_text
    decoding_text = encoded_text

    global decoding_text_prev # for undo
    decoding_text_prev = decoding_text
    
    substitution_time()


def substitution_time():
    global decoding_text
    print("---")
    print(f"Cipher text: {decoding_text}")
    print("Type letter to be replaced (please use lower case for now)")

    global replacing
    replacing = input("> ")

    if replacing == " ": # just "" is interpreted as str()
        substitution_time()
    elif len(replacing) > 1:
        substitution_time()
    elif replacing not in decoding_text: # unlikely, failsafe anyway
        print("letter not found in text (enter anything to continue)")
        input("> ")
        substitution_time()


    print("Type a replacement letter (please use lower case for now)")
    global replacement
    replacement = input("> ")

    if replacement == " ":
        substitution_time()
    elif len(replacement) > 1:
        substitution_time()

    global decoding_text_prev
    decoding_text = decoding_text.replace(replacing, replacement)
    print("modified text:", decoding_text)
    proceed_or_undo()


def proceed_or_undo():
    global replacing
    global replacement
    print("Proceed with change or undo? \n1. Proceed \n2. Undo")
    choice = input("> ")
    if choice == "1":
        letter_replacements["replaced: " + replacing] = ("replacement: " + replacement) # success :D
        print(letter_replacements)
        overwrite_prev()

    elif choice == "2":
        undo_replacement()
        #print("choice:",choice)
        
    else:
        proceed_or_undo()
    

def overwrite_prev():
    global decoding_text
    global decoding_text_prev
    decoding_text_prev = decoding_text
    ask_add_candidate()


def ask_add_candidate():
    # testing, how branches work, merge back etc.
    print("Store candidate words containing the replacement letter? y/n")
    choice2 = input("> ")

    if choice2 == "y":
        add_candidate_words()      

    elif choice2 == "n":
        print("no candidate found")
        substitution_time()
    
    else:
        ask_add_candidate()



def add_candidate_words():
    text_copy = ""
    global decoding_text
    text_copy = decoding_text

    global replacement

    # ask user for each word? select which numbers they want to keep? # feature creep?
    for x in text_copy.split(" "):
        if replacement in x:
            candidate_words.append(x) # hell yeah first try

    print(candidate_words)
    input("> ")

    # candidate list, var name to keep parity with replacement dict?
    
    #print(f"candidate words: {candidate_words}")
    substitution_time()


def undo_replacement():
    #print("UNDO coming soon")
    global decoding_text
    global decoding_text_prev
    decoding_text = decoding_text_prev

    # leapfrog vars, revert text to prev version

    substitution_time()



start()

# TODO include example ciphers
"""
Pm ol ohk hufaopun jvumpkluaphs av zhf, ol dyval pa pu jpwoly, aoha pz, if zv johunpun aol vykly vm aol slaalyz vm aol 
hswohila, aoha uva h dvyk jvbsk il thkl vba.

"""

# notify user of letter with highest count? like frequency analysis

# BUG can change letters into one that's still encoded (e.g a->h) and uhhh shit
# TODO undo change, store candidate pairs, restart decoding
# dictionary and a candidate word

# realising this ^ is a UI huh




# dict list? #
#decoded_text_step = ""
#global decoded_text = decoded_text_step


# DUMPING GROUND #

# Y/N BUG #
# Y code doesn't print anything at all, N code uses Y code with choice: n???

#if choice == "y" or "Y": # taking out "or Y" fixed it for some reason
#       replaced_by_candidates.append(replacing)
#        replacement_candidates.append(replacement)
#        print("success candidate:", replacement_candidates, "letter replaced:",replaced_by_candidates) # list grows??
#        print("choice:",choice) # code runs when N

# encoded_text.replace(replacing, replacement) # wasnt updating global, so... encoded_text = encoded_text.replace() 

# #letters_replacing.pop() if bad input # restarting would've added to prev list and desync