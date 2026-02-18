# python game
import random
while True :
    print(" ")
    print(" ")
    print("Enter what kind of game do you like to play: ")
    print("1. rock, paper")
    print("2. Completing the stories")
    print("3. Question and answers")
    print("If you want to quiet you can enter quiet")
    game=input("Enter :   ").lower().strip()
    if game== "quiet":
       print("____EXIT_____")
       break
    elif game== "completing the stories" or game=="2":
        print("  ")
        print("YOU HAVE SUCCESSFULLY ENTER IN THE GAME")
        print("_________LEVEL 1_________")
        print("STROY 1. ")
        options=["flying","thristy","houses","pot","intelligence","beak","until","pebbles","dropped","rising","refreshed","plastic can","hell","sea"]
        answers=(("flying"),("thirsty"),("houses"),("pot"),("beak"),("pebbles"),("dropped"),("rising"),("until"),("refreshed"),("intelligence"))
    
        score=0
        guess=input("One hot summer afternoon, a small sparrow was {a} in search of water.\n The sun was very bright, and the sparrow was extremely {b}.\n" \
    
           "She flew over fields, trees, and {c}, but she could not find any water. She was tired and almost ready to give up.\n"\

           "Suddenly, she saw a small clay {d} in a garden. She quickly flew down and looked inside.\n"\
           "There was some water in the pot, but the water level was very low. Her {e} could not reach it.\n"\

           "The sparrow thought for a moment. Then she saw some small {f} lying near the pot.\n"\
            "She picked up one pebble and dropped it into the pot. Then she {g} another. And another.\n"\
            "Slowly, the water level started {h}.\n"\
            "The sparrow continued putting pebbles into the pot {i} the water came up high enough.\n"\
            "Finally, she drank the water happily and flew away {j}.\n\n\n" \
            "MORAL= Where there is patience and {k}, there is always a solution.")
        random.shuffle(options)
        print(options)
        user_answers=[]
        for i in range(11):
           print(" ")
           print(" ")
           print(f"enter the words from the given help box in {chr(97+i)}")
           ans=input(" ").lower().strip()
           user_answers.append(ans)
    
        for i in range(11):
           if user_answers[i]==answers[i]:
              print(" ")
              print("Your answer is correct 👍👍😍😍  \n Well done 😁👌👌😎😉😉")
              print()
              print()  
              score +=1
           else :
               print("  ")
               print("SORRY\n Better luck next time")
               print(f"The right answer is {answers[i]} \n Don't worry better luck next time👍👍👍👍☺️☺️😌😌")
        print(" ")
        print(" ")
        print(f"your score is = {score}")
        

        print(f"Now you have successfully completed the LEVEL 1 with your score {score} ")
        print(" ")
        print("If you want solution of the above question then print solution: ")
        print("If you want to continue then enter continue: ")
        print("If you want to exit from the game  then enter exit:  ")
        print("  ")
        user = input("Enter:  ")
        print(" ")
        if user=="solution":
            print("One hot summer afternoon, a small sparrow was flying in search of water.\n"
            " The sun was very bright, and the sparrow was extremely thirsty.\n"\
            "She flew over fields, trees, and houses, but she could not find any water. She was tired and almost ready to give up.\n"\
            "Suddenly, she saw a small clay pot in a garden. She quickly flew down and looked inside.\n"\
            "There was some water in the pot, but the water level was very low. Her beak could not reach it.\n"\
            "The sparrow thought for a moment. Then she saw some small pebbles lying near the pot.\n"\
            "She picked up one pebble and dropped it into the pot. Then she dropped another. And another.\n"\
            "Slowly, the water level started rising.\n"\
            "The sparrow continued putting pebbles into the pot until the water came up high enough.\n"\
            "Finally, she drank the water happily and flew away refreshed.\n"\
            "🌟 Moral:\n"\
            "Where there is patience and intelligence, there is always a solution.")
            print(" ")
        elif user=="exit" :
           print("YOU HAVE EXIT SUCCESSFULLY")
        elif user == "continue":
            user_answers=[]
            score=0
            print(" ")
            print("YOU HAVE SUCCESSFULLY ENTERED IN LEVEL 2")
            guess=input("One summer day, a hardworking ant was busy collecting {A} and storing them in her anthill.\n"\
                   "Nearby, a beetle was resting {B} a leaf.\n"\
                    " He laughed at the ant and said, “Why are you working so hard? Enjoy the {C}”\n"\
                    "The ant replied, “Winter will come soon. I must prepare.”\n"\
                    "The beetle {D} her advice and spent his days playing.\n"\
                    "After a few months, winter arrived. The air became cold, and food was nowhere to be found.\n"\
                    "The beetle was hungry and shivering. He had no {E} for eating and no {F} for spend his night.\n"\
                    "Meanwhile, the ant was {G} inside her warm anthill with plenty of food.\n"\
                    "The beetle understood his mistake and promised to work hard in the future.\n"\
                    "🌟 Moral:\n"\

                    "Work today to stay {H} tomorrow.")
            options=["grains","on","sunshine","ignored","food","shelter","safe","upon","hello","poor","attack"]
            random.shuffle(options)
            print(options)
            print(" ")
            answers=[("grains"),("on"),("sunshine"),("ignored"),("food"),("shelter"),("safe"),("safe")]
            for i in range(8):
                print(" ")
                print(" ")
                print(f"Enter the words in  {chr(65+i)} which complete the story ")
                ans=input(f"{chr(65+i)}=  ").lower().strip()
                user_answers.append(ans)
            for i in range(8):
                if user_answers[i]==answers[i]:
                    print("Your answer is correct 👍👍😍😍  \n Well done 😁👌👌😎😉😉")
                    print()
                    print()  
                    score +=1
                else :
                    print("SORRY\n Better luck next time")
                    print(f"The right answer is {answers[i]} \n Don't worry better luck next time👍👍👍👍☺️☺️😌😌")
                print("  ")    
                print(f"your score is {score}" )
            print(f"Now you have successfully completed the LEVEL 1 with your score {score} ")
            print(" ")
            print("If you want solution of the above question then print solution: ")
            print("If you want to continue then enter continue: ")
            print("If you want to exit from the game  then enter exit:  ")
            print("  ")
            user = input("Enter:  ").lower().strip()
            if user=="solution":
                print("one summer day, a hardworking ant was busy collecting grains and storing them in her anthill.\n"\
                       "Nearby, a beetle was resting on a leaf. He laughed at the ant and said, “Why are you working so hard? Enjoy the sunshine!”\n"\
                       "The ant replied, “Winter will come soon. I must prepare.”\n"\
                       "The beetle ignored her advice and spent his days playing.\n"\
                       "After a few months, winter arrived. The air became cold, and food was nowhere to be found.\n"\
                       "The beetle was hungry and shivering. He had no food and no shelter.\n"\
                       "Meanwhile, the ant was safe inside her warm anthill with plenty of food.\n"\
                       "The beetle understood his mistake and promised to work hard in the future.\n"\
                       "🌟 Moral:\n"\
                       
                       "Work today to stay safe tomorrow.")
            
            elif user=="exit":
                print("____EXIT_____")
                break
            elif user=="continue":
                print("   ")    
                user_answers=[]
                answers=[]
                score=0
                print("----YOU HAVE SUCCESSFULLY ENTERD THE LEVEL 3------")
                print("Last winter, Aarav received a letter that had been sent to him {A} mistake.\n"\
                      "At first, he thought it was nothing {B} an ordinary envelope. " \
                      "However, when he opened it, he realized that it contained information {C} great importance.\n"\
                       "The letter warned him {D} a danger that was approaching his town.\n"\
                        "Although Aarav was confused, he decided to act {E} hesitation.\n"\
                       "He shared the letter {F} his closest friend, Meera, who was known {G} her intelligence and courage.\n"\
                       "Together, they tried to figure {H} what the message truly meant.\n"\
                       "The more they investigated, the more suspicious the situation became.\n"\
                        "It was not {I} easy as they had expected.\n"\
                        "In the end, their bravery prevented a disaster that could have resulted {J} serious consequences.\n"\

                      "🌟 Moral: Wisdom combined {K} courage can overcome any challenge.")
                options = ["hello",
                           "wich",
                           "back",
                           "lover",
                           "love",
                           "with",
                           "of",
                           "in",
                           "from",
                           "by",
                           "without",
                           "for",
                           "into",
                           "as",
                           "more than",
                           "out",
                            "than",
                            "nothing"]
                random.shuffle(options)
                print(options)
                answers=["by",
                         "more than",
                         "of",
                         "of",
                         "without",
                         "with",
                         "for",
                         "out",
                         "as",
                         "in",
                         "with"]
                for i in range(11):
                    print(" ")
                    print(" ")
                    print(f"Enter the words in  {chr(65+i)} which complete the story ")
                    ans=input(f"{chr(65+i)}=  ").lower().strip()
                    user_answers.append(ans)
                for i in range(11):
                    if user_answers[i]==answers[i]:
                      print("Your answer is correct 👍👍😍😍  \n Well done 😁👌👌😎😉😉")
                      print()
                      print()  
                      score +=1
                    else :
                      print("SORRY\n Better luck next time")
                      print(f"The right answer is {answers[i]} \n Don't worry better luck next time👍👍👍👍☺️☺️😌😌")
                      print("  ")    
                    print(f"your score is {score}" )
                print("   ")
                print(f"you have successfully completed the level 3 with score of {score}")
                print("Enter solution if you want answer")
                user=input("Enter:  ").lower().strip()
                if user=="solution":
                    A="by"
                    B="more than"
                    C="of"
                    D="of"
                    E="without"
                    F="with"
                    G="for"
                    H="out"
                    I="as"
                    J="in"
                    K="with"
                    print(f"Last winter, Aarav received a letter that had been sent to him {A} mistake.\n"\
                      f"At first, he thought it was nothing {B} an ordinary envelope. " \
                      f"However, when he opened it, he realized that it contained information {C} great importance.\n"\
                       f"The letter warned him {D} a danger that was approaching his town.\n"\
                        f"Although Aarav was confused, he decided to act {E} hesitation.\n"\
                       f"He shared the letter {F} his closest friend, Meera, who was known {G} her intelligence and courage.\n"\
                       f"Together, they tried to figure {H} what the message truly meant.\n"\
                       "The more they investigated, the more suspicious the situation became.\n"\
                        f"It was not {I} easy as they had expected.\n"\
                        f"In the end, their bravery prevented a disaster that could have resulted {J} serious consequences.\n"\

                      f"🌟 Moral: Wisdom combined {K} courage can overcome any challenge.")
                else:
                    print("-----YOU HAVE SUCCESSFULLY EXIT FORM GAME 2-----")
                    break
    elif game== "question and answers"or game=="3" or game=="questions" or game=="answers":
        print("YOU HAVE SUCCESSFULLY ENTER IN THE GAME")
        print("----------LEVEL 1--------")
        questions=[("What is the capital of India?"," new delhi"),
        ("How many days are there in a week? "," 7"),
        ("Which planet is known as the Red Planet? "," mars"),
        ("Who is known as the Father of the Nation (India)?" ," mahatma gandhi"),
        ("How many continents are there in the world?", "7"),
        ("What is the largest ocean in the world? ", "pacific ocean"),
        ("Which animal is called the King of the Jungle?"," lion"),
        ("What is the national bird of India?","peacock"),
        ("What is H2O commonly known as?","water"),
        ("Which festival is known as the Festival of Lights?" ," diwali"),
        ("How many hours are there in a day?","24"),
        ("Which gas do plants take in from the atmosphere?","carbon dioxide"),
        ("What is the tallest animal in the world?","giraffe"),
        ("Which country is home to the Great Wall?","china"),
        ("How many letters are there in the English alphabet?","26"),
        (" What is the currency of the USA?","dollar"),
        ("Which planet is closest to the Sun?","mercury"),
        ("What do bees make?","honey"),
        ("How many colors are there in a rainbow?","7")]

        selected_question=random.sample(questions,5)
        print("Give the answers of the following questions\n for each question you will get 1 mark")
        
        score=0    
        for question,ans in selected_question:
            print("  ")
            print(question)
            user_answers=input("Enter:  ").lower().strip()
            if user_answers==ans:
                print("Your answer is correct 👍👍😍😍  \n Well done 😁👌👌😎😉😉")
                print("  ")

                score +=1
            else:
                print("your answer is incorrect\n better luck next time")

                print("if you want to see answer then enter answer/solution")
                print("if you want to move next question enter next")
                print(" ")
                user=input("Enter: ").lower().strip()
                if user=="solution" or user=="answer" :
                    print(ans)
        print("  ")
        print(f"Your score is {score}")
        print("   ")
        print("If you want to continue the enter level up ")
        print("If you want to exit enter exit ")
        print("  ")
        user=input("Enter:  ").lower().strip()
        if user=="exit":
            print(" You have successfully exit from the game ")
            break
        elif user=="level up":
            print("  ")
            print(f"YOU HAVE SUCCESSFULLY ENTERED IN LEVEL 2\n with the level 1 score of {score}")
            print(" ")
            score=0
            question=[]
            question=[("Who wrote the book “The Origin of Species”?","Charles Darwin"),
                      ("What is the chemical symbol for Gold?","Au"),
                      ("Which planet has the most moons in the solar system (current record holder)?","Saturn"),
                      ("What is the hardest natural substance on Earth?","Diamond"),
                      ("In which year did World War II end?","1945"),
                      ("What is the capital city of Australia?","Canberra"),
                      ("Who developed the theory of relativity?","Albert Einstein"),
                      ("What is the largest desert in the world?","Antartica "),
                      ("What is the smallest unit of life?","Cell"),
                      ("Which country has the largest population in the world (current)?","India"),
                      ("What is the square root of 144?","12"),
                      ("What gas makes up most of Earth’s atmosphere?","Nitrogen"),
                      ("Who was the first person to step on the Moon?","Neil Armstrong"),
                      ("Which element has atomic number 1?","Hydrogen"),
                      ("What is the currency of Japan?","Yen"),
                      ("Which river is the longest in the world?","Nile"),
                      ("What does DNA stand for?","Deoxyribonucleic Acid")
                      ,("Which organ pumps blood in the human body?","Heart"),
                      ("What is the freezing point of water in Celsius?","0"),
                      ("Who painted the Mona Lisa?","Leonardo da Vinci"),
                      ("What is the powerhouse of the cell?","Mitochondria"),
                      ("Which country invented paper?","China"),
                      ("What is the speed of light (approx in km/s)?","300000"),
                      ("Who was the first President of the United States?","George washington"),
                      ("Which metal is liquid at room temperature?","Mercury")]
            selected_question=random.sample(question,8)
            print("Give the answers of the following questions\n for each question you will get 1 mark")
            for question,ans in selected_question:
              print("  ")
              print(question)
              user_answers=input("Enter:  ").title().strip()
              if user_answers==ans:
                print("Your answer is correct 👍👍😍😍  \n Well done 😁👌👌😎😉😉")
                print("  ")

                score +=1
              else:
                print("your answer is incorrect\n better luck next time")

                print("if you want to see answer then enter answer/solution")
                print("if you want to move next question enter next")
                print(" ")
                user=input("Enter: ").lower().strip()
                if user=="solution" or user=="answer" :
                    print(ans)
            print("  ")
            print(f"Your score is {score}")
            print("   ")
            print("If you want to continue the enter level up ")
            print("If you want to exit enter exit ")
            print("  ")
            user=input("Enter:  ").lower().strip()
        if user=="exit":
             print(" You have successfully exit from the game ")
             break
        elif user=="level up":
            print("    ")
            print(f"YOU HAVE SUCCESSFULLY ENTERED IN LEVEL 3 \n with the score of {score}")
            score=0
            question=[]
            question=[("Who proposed the laws of motion?","Isaac Newton"),
                      ("What is the SI unit of electric current?","Ampere"),
                      ("Which country hosted the first modern Olympic Games in 1896?","Greece"),
                      ("What is the largest internal organ in the human body?","Liver"),
                      ("Who discovered penicillin?","Alexander Fleming"),
                      ("What is the chemical formula of sulfuric acid?","H2SO4"),
                      ("Which strait separates Asia and North America?","Bering Strait"),
                      ("What is the capital of Kazakhstan?","Astana"),
                      ("Who wrote the epic poem “Paradise Lost”?","John Milton"),
                       ("What is the smallest prime number?","2"),
                       ("Which planet rotates on its side?","Uranus"),
                       ("What is the main gas found in the Sun?","Hydrogen"),
                       ("What is the currency of South Korea?","Won"),
                       ("Who was the first woman to win a Nobel Prize?","Marie Curie"),
                       ("What is the term for animals that eat both plants and meat?","Omnivore"),
                       ("What is the capital of Canada?","Ottawa"),
                       ("What is the longest bone in the human body?","Femur"),
                       ("What does CPU stand for?","Central Processing Unit"),
                       ("Which Mughal emperor built the Taj Mahal?","Shah Jahan"),
                       ("Which continent has the most countries?","Africa"),
                       ("What is the study of earthquakes called?","Seismology"),
                       ("Who was the first person to reach the South Pole?","Roald Amundsen"),
                       ("What is the boiling point of water in Celsius at sea level?","100"),
                       ("Which blood group is known as the universal donor?","o negative"),
                       ("What is the largest planet in our solar system?","Jupiter"),
                       ("Who invented the telephone?","Alexander Graham Bell")]
            selected_question=[]
            selected_question=random.sample(questions,8)
            for question,ans in selected_question:
              print("  ")
              print(question)
              user_answers=input("Enter:  ").title().strip()
              if user_answers==ans:
                print("Your answer is correct 👍👍😍😍  \n Well done 😁👌👌😎😉😉")
                print("  ")

                score +=1
              else:
                print("your answer is incorrect\n better luck next time")

                print("if you want to see answer then enter answer/solution")
                print("if you want to move next question enter next")
                print(" ")
                user=input("Enter: ").lower().strip()
                if user=="solution" or user=="answer" :
                    print(ans)
            print("  ")
            print(f"Your score is {score}")
            print("   ")
            print("YOU HAVE SUCCESSFULLY COMPLETED THE GAME WELL DONE ")

    elif game=="1" or game=="rock,paper":
        print("  ")
        player_score=0
        computer_score=0
        running=True
        while running:
    
            print("YOU HAVE SUCCESSFULLY ENTERD IN LEVEL 1 OF GAME")
            print("-------LEVEL 1------")
            for i in range (0,5):
            
                option=("rock","paper","scissor")
                computer=random.choice(option)
                player =input( f"Take a guess to win from computer   {option}:").lower().strip()
                if player not in option :
                    print("INVALID")
                    while player not in option:
                       player =input( f"Take a guess to win from computer   {option}:").lower().strip()

                print(f"computer: {computer}")
                print(f"player: {player}")
                
                if computer==player:
                    print("Tie")
                
                elif( (player == "rock" and computer == "scissor") or
                      (player == "paper" and computer == "rock") or
                      (player == "scissor" and computer == "paper") ):
                    print("You Win")
                    player_score +=1
                else :
                    print("You Loose")
                    computer_score +=1
                
            print(f"your score ={player_score} \n computer score ={computer_score}")
            if player_score>computer_score:
                print("YOU WON")
            elif player_score<computer_score:
                print("YOU LOOSE")
            elif player_score==computer_score:
                print("TIE") 
            print("Enter 'exit' to exit \n skip to continue")
            player=input("Enter: ").lower().strip()
            if player=="exit":
                running=False
            else:
                continue
                
            