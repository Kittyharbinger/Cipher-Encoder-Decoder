# Cipher Time #

# https://cryptii.com/pipes/caesar-cipher

# TODO include example ciphers (YT comments, wikipedia)

# TODO restart decoding option (type "restart", "res"?)
# TODO match candidate_words index with letter_replacements
# history of changes? pages? what's the most helpful?

# (realising this ^ is a UI, huh?)


# Cipher text
original_text = ""
decoding_text = ""
decoding_text_prev = ""
#decoded_text = ""

# Letter vars
# TODO change language, brevity
replacing = ""
replacement = ""
letters_replaced = [] # changed to list, dict keys overwritten. bad idea

# Candidate words
candidate_words = []


print("Welcome to the Decoder/Encoder")

def start():
    print("What would you like to do?")
    print("1. Decode cipher\n2. Encode cipher")
    choice = input("> ")

    if choice == "1":
        decoding_cipher_options()

    elif choice == "2":
        # figure out caesar shift, shift substring by x amount of letters 
        print("encoding not availble atm (enter anything to continue)")
        input("> ")
        cipher_on_hand()

    else:
        start()

def decoding_cipher_options():
    print("Decode example cipher? y/n (press Enter to skip)")
    choice = input("> ")
    if choice == "y":
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
    print("Please provide text to decode (please use lower case for now)") # replacing.upper()?
    global original_text
    original_text = input("> ")

    global encoded_text # same as original text?
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
    elif replacing not in decoding_text: # failsafe
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
        letters_replaced.append(f"replaced: {replacing}, replacement: {replacement}")
        print(letters_replaced)
        overwrite_prev()

    elif choice == "2":
        undo_replacement()
        
    else:
        proceed_or_undo()
    

def overwrite_prev():
    global decoding_text
    global decoding_text_prev
    decoding_text_prev = decoding_text
    ask_add_candidate()


def ask_add_candidate():
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

    # ask user for each word? select which indices they want to keep? # feature creep?
    for x in text_copy.split(" "):
        if replacement in x:
            
            candidate_words.append(x) # works now, missed split(" ") before
            

    print(f"candidate words: {candidate_words}") # TODO match index with letter_replacements
    input("> ")
    
    substitution_time()


def undo_replacement():
    global decoding_text
    global decoding_text_prev
    decoding_text = decoding_text_prev

    substitution_time()


start()


# Spitballing
# notify user of letter with highest count? like frequency analysis


# Example ciphers #
"""
Pm ol ohk hufaopun jvumpkluaphs av zhf, ol dyval pa pu jpwoly, aoha pz, if zv johunpun aol vykly vm aol slaalyz vm aol 
hswohila, aoha uva h dvyk jvbsk il thkl vba.
"""
# grab YT comments, wikipedia excerpts




# EXPLANATION GROUND (/bugs fixed (isnt that what commit history is for?)) #
# Undo feature #
# leapfrog vars, revert text to prev version


# Y/N BUG #
# Y code doesn't print anything at all, N code uses Y code with choice: n???

#if choice == "y" or "Y": # taking out "or Y" fixed it for some reason
#       replaced_by_candidates.append(replacing)
#        replacement_candidates.append(replacement)
#        print("success candidate:", replacement_candidates, "letter replaced:",replaced_by_candidates) # list grows??
#        print("choice:",choice) # code runs when N

# encoded_text.replace(replacing, replacement) # wasnt updating global, so... encoded_text = encoded_text.replace() 

# #letters_replacing.pop() if bad input # restarting would've added to prev list and desync