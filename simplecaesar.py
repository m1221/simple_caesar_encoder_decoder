# simplecaesar.py
"""
PRINCIPAL AUTHOR: Mario Portocarrero Jr
AUTHOR EMAIL: m.portocarrero.jr@gmail.com
DATE OF V1.0 RELEASE: 08/11/2015 
AUTHOR OS: Windows 8.1
PYTHON VERSION: 2.7.10
GITHUB ACCOUNT: m1221
CURRENT VERSION: 1.0
CURRENT VERSION DATE: 08/11/2015

NOTE: If you do not know what a Simple Caesar Cipher is, then please consult your
favorite search engine and/or read the README.txt file. Knowing about caesar ciphers
will make reading this code much easier.

TODO:
1. add functionality to initialize_decoder() - make this function return the cipher key(s)
2. add functionality to initialize_decoder() - make this function allow for acceptance of
a cipher key if it is already known.
3. design new algorithm for initialize_decoder() - the current algorithm employs a brute force
method and relies on the end-user to recognize which of the outputs is the deciphered text.
the new algorithm should (i)be a heuristic that relies on a dictionary of the most common words
in the English language. It should (ii)also make use of recursion. 

CHALLENGE:
1. make a program to encode/decode Caesars with a mneumonic device
2. make a program based off of the Jefferson wheel

Please send any bugs to my email or contact me via gitHub.
"""

"""VARIABLE(S)"""
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i",
"j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
"t", "u", "v", "w", "x", "y", "z"]

"""MAIN FUNCTIONS - THERE ARE 2 MAIN FUNCTIONS"""
def initialize_decoder():
  print '''
  **Hello, welcome to this simple caesar DECODER.
  Input SHOULD only contain characters A-Z,
  please no numbers, apostrofes, or other special characters.
  All such characters will be removed.'''
  
  read_file = my_reader() # retrieves and stores a string from a file or from raw_input
  read_file = my_parser(read_file) # removes all characters except for
  #letters of the alphabet and spaces
  
  output = my_decoder(read_file) # output is a list of all of the possible combinations
  # of simple caesar displacement
  messages = ''
  for lines in range(0, len(output)): # make a string from output, 1 line per list item
    messages += (str(lines + 1) + ": " + output[lines] + "\n")
      
  print messages
  
  write_to = my_write_selector() # prompts the user on which file to store the messages
  my_writer(write_to, messages) # writes the messages to specified location
  
def initialize_encoder():
  print '''
  **Hello, welcome to this simple caesar ENCODER.
  Input SHOULD only contain characters A-Z with
  spaces in between words. Please no numbers,
  apostrofes, or other special characters. All 
  such characters will be removed.
  '''
  read_file = my_reader() # retrieves and stores a string from a file or from raw_input
  read_file = my_parser(read_file) # removes all characters except for
  # letters of the alphabet and spaces
  print "Select a number 1-25. This will be your cipher key."
  key_value = my_key_test() # receives and tests the validity of a user-defined key
  output = my_encoder(read_file, key_value) # encodes the string 
  write_to = my_write_selector() # prompts the user on which file to store the message
  print "Here is your encoded message!!!!"
  print output
  my_writer(write_to, output) # writes the message to the specified file
  

"""HELPER FUNCTIONS - LISTED ALPHABETICALLY"""
def my_decoder(msg): # makes a list with all possible combinations of messages
  message_holder = []
  
  for i in range(1, len(alphabet)):
    message_holder.append(my_encoder(msg, i))
  
  return message_holder
  
def my_create_temp_alphabet(key_value): # creates an alphabet 
  temp_alphabet = alphabet[(26-key_value):26] + alphabet[0:(26-key_value)]
  return temp_alphabet
  
def my_encoder(msg, key_value): # converts one message to another based on a key value
  new_msg = ""
  temp_alphabet = my_create_temp_alphabet(int(key_value))
  
  for char in range(0, len(msg)):
    if msg[char] == " ":
      new_msg += " "
    else:
      i = alphabet.index(msg[char])
      new_msg += temp_alphabet[i]
  return new_msg
  
def initialize(): # begins the interaction with user
  user_select = raw_input('> ')

  if user_select == '1':
    initialize_encoder()
  elif user_select == '2':
    initialize_decoder()
  else:
    print "Please enter 1 or 2."
    initialize()

def my_parser(in_txt): # removes all characters from a string except for alphabet letters and spaces
  out_txt = in_txt.lower()
  to_remove_pos =[]
  
  for i in range(0, len(out_txt)): # adds index positions of characters not
    if out_txt[i] == " ":          # in our alphabet to a to-be-removed to a list
      pass
    else:
      if out_txt[i] not in alphabet:
        to_remove_pos.append(i)
      
  if len(to_remove_pos) > 0: # prints out position and character information for to-be-removed
    print "Your message had characters removed at the following positions."
    print to_remove_pos
    to_remove_char = []
    
    for pos in range(0, len(to_remove_pos)):
      to_remove_char.append(out_txt[to_remove_pos[pos]])
    print "These are the characters that were removed."
    print to_remove_char
      
    
  for j in range(0, len(to_remove_pos)): # removes invalid characters from message
    old_char = out_txt[to_remove_pos[j]]
    out_txt = out_txt.replace(old_char, "")
    
  return out_txt

def my_reader(): # returns a string from a text file or from raw_input
  print '''
  Would you like to enter your message into the prompt or
  enter it into a text file that will be read by this program??
  [1]: Enter a message into the prompt
  [2]: Enter a message from a text file.'''  
  reader_choice_success = False
  
  while reader_choice_success == False: # this while-loop ensures that a valid selection is made
    enter_choice = raw_input('Enter 1 or 2> ')
    if enter_choice == '1':
      read_file = raw_input('Enter your message here > ')
      reader_choice_success = True
    elif enter_choice == '2':
      read_file = my_reader_file_input()
      reader_choice_success = True
    else:
      print "That was not a valid input."
    
  return read_file

def my_reader_file_input(): # returns a string from a file. this fnct is used by my_reader()
  read_success = False
  
  while read_success == False: # this while-loop ensures that an exising file
    # is chosen to read from
    try:
      print '''
      If your message is already in read_in.txt, then press
      enter; otherwise enter the name of the text file that
      contains your message.
      '''
      user_input = raw_input('File name> ')
      if user_input == "":
        user_input = 'read_in.txt'
    
      file_in = open(user_input, 'r')
      read_file = file_in.read()
      file_in.close()
      read_success = True
    except:
      print "That file does not exist."
    finally:
      pass
  return read_file
  
def my_key_test(): # receives and tests the validity of a user-defined key
  cipher_keys = []
  for i in range(1, 26): # the cipher key should be a number 1-25
    cipher_keys.append(str(i))
    
  key_success = False
  
  while key_success == False:
    key_value = raw_input('Enter your number here> ') # asks the user for the cipher key with which to encode the message
    if key_value in cipher_keys:
      key_success = True
    else:
      print "That is not a valid number."
      
  return key_value

def my_write_selector(): # prompts the user on where to write encoded/decoded message(s)
  print '''
  Please enter the name of the file to which you wish to write 
  your message. If you wish to write your file to read_out.txt
  you may leave the line blank and press enter.'''
  
  write_success = False
  while write_success == False: # this while-loop ensures that an existing file is
    write_selection = raw_input('> ') # selected to write to
    if write_selection == "":
      write_to = 'read_out.txt'
    else:
      write_to = write_selection
      
    try: # test if the write_to file exists
      file_out = open(write_to)
      file_out.close()
      write_success = True
    except:
      print "That file does not exist."
    finally:
      pass
  
  return write_to
  
def my_writer(write_to, msg): # writes message to a text file
  file_out = open(write_to, 'w')
  file_out.write(msg)
  file_out.close
  print "Text written to selected file."
  print "Thank you, come again."
  
"""RUN CODE"""
print '''
Hello! Welcome to my simple caesar encoder/decoder.
Would you like to decode a message or encode a message?
[1]: Encode a message
[2]: Decode a message'''
initialize()