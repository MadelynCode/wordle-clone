import random
import time
from rich import print

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
        return False
    if word.lower() == answer.lower():
         return "correct"
    else:
         return "incorrect"

def colors(word, answer):
     splitted = list(word.upper())
     splitted_answer = list(answer.upper())
     result_colors = []
     result = []
     for i in range(0, 5):
        if splitted_answer[i] == splitted[i]:
            result_colors.append("[bold green]")
        elif splitted[i] in splitted_answer:
            result_colors.append("[bold yellow]")
        else:
            result_colors.append("[bold red]")
     
  
     for i in range(0, 5):
        result.append(result_colors[i])
        result.append(splitted[i])

     return "".join(result)




def main():
    words = get_list("./word_list.txt")
    answer = pick_word(words)
    chances = 6
    message = ["Phew", "Good", "Nice!", "Amazing", "Wow...!"]

    print("======STARTING WORDLE ======")
    time.sleep(0.3)
    print("you have 6 chances remaining")

    # loop
    while True:
         guess = input().lower()
         result = check_word(guess, answer, words)
         if result == False:
             continue
         print(colors(guess, answer))
         if result == "correct":
            print(message[chances])
            print("[green]======CORRECT======")
            break
         elif result == "incorrect":
              chances -= 1
              print(f"You have {chances} chances remaning")
              if chances < 1:
                  print("[red]======YOU LOSE======")
                  print(f"The answer was {answer}")
                  break

    

if __name__ == "__main__":
    main()
