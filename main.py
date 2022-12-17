import os
path = "books/"
dir_list = os.listdir(path)

def display_books(bookshelf):
  print("__________________________________\nBooks available in our library:\n")
  for book in bookshelf:
    index = book.find(".txt")
    book = book[0:index]
    print("-> " + book.title())
  print("__________________________________")

def get_book_text(book_name):
  book_path = f"books/{book_name}.txt"
  with open(book_path) as book:
    return book.read()

def check_existence(dictionary, letter_or_word):
  if letter_or_word in dictionary:
    return dictionary[letter_or_word]
  else:
    return "Not found"

def count_all_words(book):
  return len(book.split())

def dict_char_count(book):
  letters_in_book_dict = {}
  all_words = book.split()
  
  for word in all_words:
    for letter in word:
      letter = letter.lower()
      if letter.isalpha() and letter in letters_in_book_dict.keys():
        letters_in_book_dict[letter] += 1   
      elif letter.isalpha():
        letters_in_book_dict[letter] = 1

  ordered_characters = sorted(letters_in_book_dict.items())

  return {k:v for k,v in ordered_characters}

def count_char(book, character):
  dict_of_chars = dict_char_count(book)
  return check_existence(dict_of_chars, character)

def report_alphabets(book, book_name):
  list_of_chars = dict_char_count(book)
  list_of_words = count_all_words(book)
  print(f"--- Begin report of {book_name.upper()}---")
  print(f"{list_of_words} words found in the document")
  for letter in list_of_chars:
    print(f"The '{letter}' character was found {list_of_chars[letter]} times")
  print(f"--- END REPORT ---")

def dict_word_count(book):
  words_in_book = {}
  all_words = book.split()
  for word in all_words:
    word = word.lower()
    if word in words_in_book.keys():
      words_in_book[word] += 1   
    else:
      words_in_book[word] = 1
  
  return words_in_book

def word_count(book, word):
  dict_of_words = dict_word_count(book)
  return check_existence(dict_of_words, word)

#input
def ask_book():
  books_available = ['frankenstein']
  book = input("Which book do you want to do a lookup on?\n>>>").lower()
  if book not in books_available:
    print(f"{book} is not found in the library. Pick an available book.")
    return ask_book()
  return book

def ask_stat():
  chosen_stat = input("What type of stat are you interested in knowing? [word] or [letter]?\n>>>")
  if chosen_stat == "word" or chosen_stat == "letter":
    return chosen_stat
  else:
    print("Input 'word' or 'letter'")
    return ask_stat()

def ask_char_to_count():
  chosen_char = input("What letter are you interested in looking up?\n>>>")
  if len(chosen_char) > 1:
    print("Input valid letter. Cannot exceed 1 character.")
    return ask_char_to_count()
  return chosen_char

def ask_word_to_count():
  chosen_word = input("What word are you interested in looking up?\n>>>")
  if len(chosen_word) < 1:
    print("Please input valid word")
    return ask_word_to_count()
  return chosen_word

#display
def display_stat(letter_or_word, choice, book):
  if letter_or_word == "letter":
    integer = count_char(book, choice)
  elif letter_or_word == "word":
    integer = word_count(book, choice)
  if integer == "Not found":
    print(f"{choice.upper()} was not found in the book")
  else:
    print(f"Your book contains {integer} {choice.upper()} {letter_or_word}s")

def ask_letter_report_type():
  full_report = input('''Would you like to view all the alphabet and their
corresponding occurence [report]?
or perform an individual letter lookup? [letter]?\n>>>''').lower()
  if full_report == "report" or full_report == "letter":
    return full_report
  else:
    print("Please type 'report' or 'letter'")
    return ask_letter_report_type()

def perform_report(book):
  full_book_text = get_book_text(book)
  report_alphabets(full_book_text, book)

def ask_again(fn):
  lookup_again = input("Do you want to perform another lookup? [y/n]\n>>>").lower()
  if lookup_again == "yes" or lookup_again == "y":
    print("Lets head back to the libary...")
    return fn()
  elif lookup_again == "no" or lookup_again == "n":
    print("Thank you for using our service")

# lookup program
def lookup():
  display_books(dir_list)
  ask_book_name = ask_book()
  chosen_book = get_book_text(ask_book_name)
  letter_or_word = ask_stat()
  if letter_or_word == "letter":
    report_or_letter = ask_letter_report_type()
    if report_or_letter == "report":
      perform_report(ask_book_name)
    elif report_or_letter == "letter":
      character = ask_char_to_count()
      display_stat(letter_or_word, character, chosen_book)
  elif letter_or_word == "word":
    word = ask_word_to_count()
    display_stat(letter_or_word, word, chosen_book)

  ask_again(lookup)

lookup()