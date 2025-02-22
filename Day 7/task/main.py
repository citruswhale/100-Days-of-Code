
# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word. Then print it.

# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

# TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word. Print "Right" if it
#  is, "Wrong" if it's not.

# actual word to guess
# array of guessed word
# number of wrong guesses
# freq array to verify whether the word has been guessed or not.

#vars
import random
word_list = ["aardvark", "baboon", "camel"]
has_won = False
chosen_word = word_list[random.randint(0, len(word_list)-1)]
guessed_word = []
wrong_guesses = 0
right_guesses = 0
total_guesses = 6
letter_verification = [False]*26
letter_indices = [[] for _ in range(26)]
wrong_guess_pics = [
    '''
      +---+
      |   |
          |
          |
          |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========
    '''
]

# pre-req
for i in range (0, len(chosen_word)):
    guessed_word += '_'

for i in range (0, len(chosen_word)):
    letter_indices[ord(chosen_word[i])-ord('a')].append(i)

# launch
while wrong_guesses < total_guesses:
    print("Word to guess: " + ''.join(guessed_word) + "\n")
    letter = input("Guess a letter: ")
    if len(letter_indices[ord(letter)-ord('a')]) > 0:
        if letter_verification[ord(letter)-ord('a')]:
            print("You've already guessed " + letter + "." + "\n")
        else:
            letter_verification[ord(letter)-ord('a')] = True
            indices = letter_indices[ord(letter)-ord('a')]
            print(indices)
            for i in range(0, len(indices)):
                right_guesses += 1
                guessed_word[indices[i]] = letter
            if right_guesses == len(chosen_word):
                has_won = True
        print(''.join(guessed_word) + "\n")
        if has_won:
            break
    else:
        wrong_guesses += 1
        print("You guessed " + letter + ", that's not in the word. You lose a life." + "\n")
    print(wrong_guess_pics[wrong_guesses] + "\n")
    print("****************************" + str(6-wrong_guesses) + "/6 LIVES LEFT****************************" + "\n")

if not has_won:
    print("***********************IT WAS " + chosen_word + "! YOU LOSE**********************" + "\n")
else:
    print("You win." + "\n")

# CPP Version
# #include<bits/stdc++.h>
# using namespace std;
#
# int main() {
#
#     // vars
#     bool has_won = false;
#     string chosen_word = "karthik";
#     string guessed_word = "";
#     int wrong_guesses = 0;
#     int right_guesses = 0;
#     int total_guesses = 6;
#     vector<bool> letter_verification(26, 0);
#     vector<vector<int>> letter_indices(26, vector<int>(0));
#     vector<string> wrong_guess_pics = {"N/A", "W", "WR", "WRO", "WRON", "WRONG", "X_X"};
#
#     // pre-req
#     for (int i = 0; i < chosen_word.size(); i++) {
#         guessed_word.push_back('_');
#     }
#
#     for (int i = 0; i < chosen_word.size(); i++) {
#         letter_indices[chosen_word[i]-'a'].push_back(i);
#     }
#
#     // launch
#     while (wrong_guesses < total_guesses) {
#         char letter;
#         cout << "Word to guess: " << guessed_word << endl;
#         cout << "Guess a letter: ";
#         cin >> letter;
#         if (letter_indices[letter-'a'].size() > 0) {
#             if (letter_verification[letter-'a']) {
#                 cout << "You've already guessed " << letter << "." << endl;
#             }
#             else {
#                 letter_verification[letter-'a'] = 1;
#                 vector<int> indices = letter_indices[letter-'a'];
#                 for (int i = 0; i < indices.size(); i++) {
#                     right_guesses++;
#                     guessed_word[indices[i]] = letter;
#                 }
#                 if (right_guesses == chosen_word.size()) has_won = true;
#             }
#             cout << guessed_word << endl;
#             if (has_won) break;
#         }
#         else {
#             wrong_guesses++;
#             cout << "You guessed " << letter << ", that's not in the word. You lose a life." << endl;
#         }
#         cout << wrong_guess_pics[wrong_guesses] << endl;
#         cout << "****************************" << 6-wrong_guesses << "/6 LIVES LEFT****************************" << endl;
#     }
#
#     if (!has_won) cout << "***********************IT WAS " << chosen_word << "! YOU LOSE**********************" << endl;
#     else cout << "You win." << endl;
# }