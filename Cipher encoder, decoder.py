# Cipher Time #

# https://cryptii.com/pipes/caesar-cipher

# TODO track changed and unchanged letters
# for letter in decoding_text, add to list (indexed substrings) 
# for letter in original_text, add to list too 
# for loop, nested, if x's match: pass

# TODO include example ciphers (YT comments, wikipedia)

# TODO command for candidate list/history
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
candidate_words_prev = [] # updated when restarting decoding


print("Welcome to the Decoder/Encoder")

def start():
    print("What would you like to do?")
    print("1. Decode cipher\n2. Encode cipher (coming soon(TM))")
    #print("3. Test history")
    choice = input("> ")

    if choice == "1":
        decoding_cipher_options()

    elif choice == "2":
        # figure out caesar shift, shift substring by x amount of letters 
        print("Encoding is not available yet (enter anything to continue)")
        input("> ")
        cipher_on_hand()

    else:
        start()

def decoding_cipher_options():
    print("Decode example cipher? y/n (press Enter to skip)")
    choice = input("> ")
    if choice == "y":
        example_ciphers()
        
    elif choice == "n":
        cipher_on_hand()
    elif choice == "":
        cipher_on_hand()

    else:
        decoding_cipher_options()
    
    cipher_on_hand()

def example_ciphers():
    global decoding_text
    print("Take your pick:")
    print("1. Pm ol ohk hufaopun jvumpkluaphs av zhf, ol dyval pa pu jpwoly, aoha pz, if zv johunpun aol vykly vm aol slaalyz vm aol hswohila, aoha uva h dvyk jvbsk il thkl vba. ")
    print("2. P svcl \"wohzl 1\" zv tbjo, zpujl P ruld P olhyk pa pu-nhtl iba ulcly mvbuk pa pu aol tbzpj bwsvhklk pu fvbabil. Av olhy pa uvd jslhysf, pa'z zv hthgpun. Npclz tl nvvzlibtwz hsdhfz")
    choice = input("> ")

    if choice == "1":
        decoding_text = "Pm ol ohk hufaopun jvumpkluaphs av zhf, ol dyval pa pu jpwoly, aoha pz, if zv johunpun aol vykly vm aol slaalyz vm aol hswohila, aoha uva h dvyk jvbsk il thkl vba. "
    elif choice == "2":
        decoding_text = "P svcl \"wohzl 1\" zv tbjo, zpujl P ruld P olhyk pa pu-nhtl iba ulcly mvbuk pa pu aol tbzpj bwsvhklk pu fvbabil. Av olhy pa uvd jslhysf, pa'z zv hthgpun. Npclz tl nvvzlibtwz hsdhfz"

    substitution_time()


def cipher_on_hand():
    print("Please provide text to decode (please use lower case for now)") # if replacing.upper() in text, replacement.upper() for that sp. one
    global original_text
    original_text = input("> ")

    #global encoded_text # same as original text?
    #encoded_text = original_text

    global decoding_text
    decoding_text = original_text

    global decoding_text_prev # for undo
    decoding_text_prev = decoding_text
    
    substitution_time()


def substitution_time():
    global decoding_text
    print("---")
    print(f"Cipher text: {decoding_text}")
    print("Type letter to be replaced (please use lower case for now)")
    print("If you'd like to restart, type \"res\" or \"restart\"")

    global replacing
    replacing = input("> ")

    # BUG > 1 letter restarts decoding, fuck's sake
    if len(replacing) < 1:
        substitution_time()
    elif len(replacing) > 1:
        if replacing == "res" or "restart": # BUG anything between "res" and "restart" triggers this func
            #print(f"restart cond: {replacing}")
            restart_decoding()
        elif replacing == "his" or "history":
            #print(f"history cond: {replacing}")
            show_change_history()
        else:
            #print(f"else cond: {replacing}")
            substitution_time()

    elif replacing not in decoding_text: # failsafe
        print("letter not found in text (enter anything to continue)")
        input("> ")
        substitution_time()


    print("Type a replacement letter (please use lower case for now)")
    global replacement
    replacement = input("> ")

    if len(replacement) < 1:
        substitution_time()
    elif len(replacement) > 1:
        if replacement == "res" or "restart":
            restart_decoding()
        elif replacement == "his" or "history":
            show_change_history()
        else:
            substitution_time()
            
    # OH MY GOD I JUST WANT TO NOT REPLACE OG LETTERS AND MAKE A MESS
    
    decoding_text = decoding_text.replace(replacing, replacement) # BUG not replacing now :)
    print("modified text:", decoding_text) # no seriously there's nothing different why do you do this to me?
    proceed_or_undo()


def proceed_or_undo():
    global replacing
    global replacement
    print("Proceed with change or undo? \n1. Proceed \n2. Undo")
    choice = input("> ")
    if choice == "1":
        letters_replaced.append(f"replaced: {replacing}, replacement: {replacement}")
        print(letters_replaced[-1]) # not showing whole list each time

        change_checker_list = []
        decoding_text_listifed = list(decoding_text)
        print(f"decode text listified {decoding_text_listifed}")
        
        
        # if replacing affects changed letters and originals
        # so replacing letters diff from original, if originals in same index, change those back

        # for loop list() the decoding text after replacement
        # check index against original text for loop list()-ed
        # if replacing == original at that index, leave it be,
        # isn't over-written then

        # stitch it back together into a string, for x in list, str("" + x)
        

        overwrite_prev()
        # TODO change language here. later, after this feature gets in

    elif choice == "2":
        undo_replacement()
        
    else:
        proceed_or_undo()
    
    
def overwrite_prev():
    global decoding_text
    global decoding_text_prev
    decoding_text_prev = decoding_text
    ask_add_candidate()

def undo_replacement():
    global decoding_text
    global decoding_text_prev
    decoding_text = decoding_text_prev

    substitution_time()


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
    show_change_history()
    input("> ")
    
    substitution_time()


def restart_decoding():
    global decoding_text
    global original_text
    decoding_text = original_text
    
    global letters_replaced
    #letters_replaced.clear() maybe not this, let user know what they've tried
    
    global candidate_words
    global candidate_words_prev
    candidate_words_prev = candidate_words
    candidate_words.clear()
    # only applies for same cipher. new one, just erase
    print("decoding restarted")
    substitution_time()


def show_change_history():
    # TODO option for current/prev attempt's list
    i = 0
    global letters_replaced
    global candidate_words

    for x in candidate_words: # show index, implement as option
        i += 1
        print(f"Candidate {i}: {x}")
        for x in letters_replaced:
            print(x)

    input("> ")
    substitution_time()


start()

test_text = "hi there"
for x in test_text:
    print(x)


# Example ciphers #
"""
Pm ol ohk hufaopun jvumpkluaphs av zhf, ol dyval pa pu jpwoly, aoha pz, if zv johunpun aol vykly vm aol slaalyz vm aol 
hswohila, aoha uva h dvyk jvbsk il thkl vba.
"""
# grab YT comments, wikipedia excerpts


# Spitballing #
# OG-change tracking #
# if letter and index match: pass
# change letter temporarily so it's not caught in .replace()?

# for loop replacing, HEADACHE
"""
for x in decoding_text:
    replaced = x
    for y in original_text:
        original = y

    # oh good lord my brain is melting, re-write this
    if replacing == x in original_text:
        x = "" # fix substring at index
    
    decoding_text_listifed.append(x)
"""

"""
new_letter = ""
    OG_letter = ""
    for x in decoding_text:
        new_letter = x
        for y in original_text:
            OG_letter = y # no fuck, this'll just 
        
        if new_letter == OG_letter:
            if decoding_text != original_text:
                 if x == replacing:
                    x = replacement
                    
"""

"""
    # compare indexes then turn back into string
    OG_text_letters = []
    dec_text_letters = []
    for letter in original_text:
        OG_text_letters.append(letter)
        for letter in decoding_text:
            dec_text_letters.append(letter)
        
        if OG_text_letters[-1] == dec_text_letters[-1]:
            pass
"""


"""
# compare indexes and make it recognise the incoming mess
    decoding_text = decoding_text.replace(replacing, replacement)
    for x in decoding_text:
        new_letter = x
        for y in original_text:
            OG_letter = y
        
        if new_letter == OG_letter:
            if decoding_text != original_text:
                 if x == replacing:
                    x = replacement
"""


# notify user of letter with highest count? like frequency analysis



# EXPLANATION GROUND (/bugs fixed (isnt that what commit history is for?)) #
# blank input bug
# if replacement == " ": # BUG deletes character, dang it
# replacing " " was accepted too
# fixed with len() > or < 1

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