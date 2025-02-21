#include<bits/stdc++.h>
using namespace std;

int main() {

    // vars
    bool has_won = false;
    string chosen_word = "karthik";
    string guessed_word = "";
    int wrong_guesses = 0;
    int right_guesses = 0;
    int total_guesses = 6;
    vector<bool> letter_verification(26, 0);
    vector<vector<int>> letter_indices(26, vector<int>(0));
    vector<string> wrong_guess_pics = {"N/A", "W", "WR", "WRO", "WRON", "WRONG", "X_X"};

    // pre-req
    for (int i = 0; i < chosen_word.size(); i++) {
        guessed_word.push_back('_');
    }

    for (int i = 0; i < chosen_word.size(); i++) {
        letter_indices[chosen_word[i]-'a'].push_back(i);
    }

    // launch
    while (wrong_guesses < total_guesses) {
        char letter;
        cout << "Word to guess: " << guessed_word << endl;
        cout << "Guess a letter: ";
        cin >> letter;
        if (letter_indices[letter-'a'].size() > 0) {
            if (letter_verification[letter-'a']) {
                cout << "You've already guessed " << letter << "." << endl;
            }
            else {
                letter_verification[letter-'a'] = 1;
                vector<int> indices = letter_indices[letter-'a'];
                for (int i = 0; i < indices.size(); i++) {
                    right_guesses++;
                    guessed_word[indices[i]] = letter;
                }
                if (right_guesses == chosen_word.size()) has_won = true;
            }
            cout << guessed_word << endl;
            if (has_won) break;
        }
        else {
            wrong_guesses++;
            cout << "You guessed " << letter << ", that's not in the word. You lose a life." << endl;
        }
        cout << wrong_guess_pics[wrong_guesses] << endl;
        cout << "****************************" << 6-wrong_guesses << "/6 LIVES LEFT****************************" << endl;
    }

    if (!has_won) cout << "***********************IT WAS " << chosen_word << "! YOU LOSE**********************" << endl;
    else cout << "You win." << endl;
}