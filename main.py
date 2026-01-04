import random
import time

words = []

def get_list(path):
       with open("./word_list.txt") as f:
            return f.read().split()



def valid_word(word, words):
    if len(word) == 5 and word in words:
        return True
    else:
        return False


def pick_word(words):
     return words[random.randrange(0, len(words))]
     
     
def check_word(word, answer, words):
    if valid_word(word, words) == False:
        print("Invalid guess")
        return
    if word == answer:
         return "correct"
    else:
         return "incorrect"

def colors(word, answer):
     splitted = list(word)
     splitted_answer = list(answer)
     result_colors = []
     for i in range(0, 5):
        pass
     




def main():
    words = get_list("./word_list.txt")
    answer = pick_word(words)
    chances = 6
    message = ["Phew, barely!", "Good", "Nice!", "Amazing", "Wow...!"]

    print("======STARTING WORDLE ======")
    time.sleep(0.3)
    print("you have 6 chances remaining")

    # loop
    while True:
         guess = input().lower()
         chances -= 1
         result = check_word(guess, answer, words)
         if result == "correct":
            print(message[chances])
            print("======CORRECT======")
            break
         elif result == "incorrect":
              print("do stuffs")
    

    

if __name__ == "__main__":
    main()
