#Inspired by the Amazing Race, my version of Pick Your Own Adventure

#allows me to use exit function which exits the user from the game
from sys import exit
#sleep function delayings printing time
from time import sleep

#when player answers incorrectly, prompts the lose function that prints out a lose-statement
def lose(reason):
    print(reason + ' Try again next year.')
    exit(0)
    
#prints the given argument and sleeps for 2 seconds
#def pacing(function):
#    while 
#    function
#    sleep(2)

#prompts user name before starting the game
name = input('Preparing your boarding ticket, name please? ').capitalize()
sleep(1.5)

#user starts in the U.S and must answer quiz correctly to go to the next desintation
def welcome_us():
    print(f'\nWelcome {name}, to your very first Amazing Race!')
    print('On this race around the world, you will be tested of your worldly knowledge.')
    print("And who knows, maybe you'll win the grand prize?\n")
    print('Get ready for your first quiz!\n')
    #sleep(3)
    
    #prompts quiz
    print('Who is considered as the very first programmer?\n')
    #sleep(2)
    print('1) Linus Torvalds')
    #sleep(1)
    print('2) Ada Lovelace')
    #sleep(1)
    print('3) Grace Hopper\n')
    #sleep(1)
    
    #stores user input
    guess = input('Your guess: ')
    #sleep(1)
    
    #if loop is used for answering the quiz
    #if user answers correctly, will prompt the England function
    if guess == '2' or 'two' in guess:
        print(f"\nCongratulations {name}!\n")
        print('Ada Lovelace is known as the first computer programmer with her')
        print('work in Analytical Engine, publishing the first algorithm to be carried out by a machine.\n')
        #sleep(1)
        
        print('Your boarding pass has completed. Take this trip to the city of London, England')
        print('where Ada Lovelace was born.\n')
        #sleep(3)
        welcome_england()
    #if user incorrectly answers, will prompt the lose function and exit the game    
    else:
        lose("That's not quite it. Thanks for playing the game!")

#prompts the welcome speech for England and asks user what route they would like to take
def welcome_england():
    print('WELCOME TO ENGLAND!\n')
    #sleep(2)
    print('The country known for English Breakfasts and historical monuments.')
    print('As you head down to the Thames River, there are two routes you can take.')
    print('There is one sign that points to Buckingham Palace and another that points to SoHo.')
    #sleep(1)
    print('Have you decided where you would like to go?\n')
    
    #two routes that the user has to pick from
    print('1) Take the route towards Buckingham Palace.')
    #sleep(1)
    print('2) Forget the mansions. Take me to Soho!\n')
    #sleep(1)
    
    #stores user input
    user_decision = input("What are you going to do? >> ")
    #sleep(1)
    
    #will prompt a royalty quiz or food quiz depending on user_decision
    #user will fail the game if they do not select either routes provided
    if user_decision == '1' or 'one' in user_decision:
        print()
        royalty_quiz()
    elif user_decision == '2' or 'two' in user_decision:
        print()
        london_food()
    else:
        print("\nYou've wandered aimlessly and fell asleep after a few lagers.")
        lose("Here's your ticket home.")
        
#prints out statements about Queen Victoria and prompts quiz
def royalty_quiz():
    print('Welcome to the British Empire.')
    #sleep(2)
    print('I ruled as the Queen of the United Kingdom and Ireland from 1819-1901,')
    print('leading one of the greatest expansions of the British Empire,')
    print('enforcing the ways of British colonization.')
    print('In fact, I proclaimed myself as the Empress of India.\n')
    
    #pompts quiz
    print('Who am I?\n')
    #sleep(2)
    print('1) King William IV')
    #sleep(1)
    print('2) Queen Victoria')
    #sleep(1)
    print('3) Queen Anne')
    #sleep(1)
    print('4) Queen Elizabeth\n')
    #sleep(1)
    
    #stores user guess
    guess = input("Your guess: ")
    
    #if guess == 2, then execute india function
    if guess == '2' or 'two' in guess:
        print('\nCongratulations! Queen Victoria ruled what is now known as the Victorian Era.\n')
        print('She self-proclaimed herself as the Empress of India after India was incorporated')
        print('into the British Empire. India was colonized for almost 200 years before.')
        print('gaining Independence in 1947.\n')
        print('Here are your tickets and enjoy your trip to the seventh largest country and')
        print('second most populous country in the world. See you in India!\n')
        welcome_india()
    #if user incorrectly guesses, will prompt them to try again until they guess 2
    else:
        print('\nHmmm, try again.')
        royalty_quiz()
        

#prints out statements about food in London and prompts quiz
def london_food():
    print('After the waning power of the Portugese in India, the Dutch and English')
    print('seized this opportunity to gain power in the spice trade world.')
    print('Britain eventually won total power over India, thus controlling the spice trade by the 1800s.\n')
    
    #prompts quiz
    print('What two main spices did Britain, Holland and Portual go to war over from India?\n')
    print('1) Salt and Black Pepper')
    print('2) Cayenne and Paprika')
    print('3) Saffron and Pink Himalayan Salt')
    print('4) Black Pepper and Cinnamon\n')
    
    #stores user guess
    guess = input('Your guess: ')
    
    #if user guesses correctly, will prompt India function
    if guess == '4' or 'four' in guess:
        print(f"\nCongrats, {name}! That's correct!\n")
        print('Food has and continues to be a political trade war.')
        print('Are you aware of the current food trade wars that is going on today?')
        print("Well, why don't you take this next trip to learn more about the country")
        print('that continues to fight Agricultural Monopolies from other countries.\n')
        
        print('Here are your tickets and enjoy your trip to the seventh largest country and')
        print('second most populous country in the world. See you in India!\n') 
        welcome_india()
    #user will have to try again until guess == 4.    
    else:
        print('\nHmmm, try again.')
        london_food()

#prompts welcome speech for India and provides two routes for user to take
def welcome_india():
    print('WELCOME TO INDIA!\n\nA country filled with dynamic history and culture.')
    print('Before you exit the airport in Kolkata, you must decide where you will take your next quiz.')
    print('One takes you to the local streets of Kolkata and another takes you to a historical landmark.\n')
    
    #prompts user to decide which route to take
    print('Where are you going to go?\n')
    print('1) Take me to the streets!')
    print("2) I just want a glimpse of this landmark you're talking aobut.\n")
    
    #stores user input into choice
    choice = input('I choose: ')
    
    #will prompt a food quiz or invention quiz depending on user_decision
    #user will fail the game if they do not select either routes provided
    if choice == '1' or 'one' in choice:
        india_food()
    elif choice == '2' or 'two' in choice:
        india_inventions()
    else:
        print('You got distracted by an Indian wedding that passed by and missed your exit.')
        lose('This is your ticket home.')

#prints out India invention facts and prompts quiz
def india_inventions():
    print('\nDid you know that India was the first civilization that carburising steel?')
    print('Anicient India discovered the carburising technique that would heat up metals and')
    print("produce high quality iron and steel. Without this inventions, we wouldn't have cars.\n")
    
    #prompts quiz
    print('What other inventions did Ancient India make that changed the way we live today?')
    print('1) Coffee')
    print('2) Paper')
    print('3) Math')
    print('4) Astrology\n')
    
    #stores user input in guess
    guess = input('Your answer: ')
    
    #if guess == 3, will execute Japan function 
    if guess == '3' or 'three' in guess:
        print(f"\nCongratulatioms, {name}! That's correct.\n")
        print('Although Egypt was the first to create a numeral system, it is a system we do not used today.')
        print('Ancient India invented the Indian/Hindu numeral system--the numbers that we all use today!')
        print('This is often referred to as Arabic numerals, after the Arab traders brought the Indian')
        print('mathmatical concept to the West, thus replacing the Roman numeral system used at the time.')
        print('Ancient India also created zero, 0, thus setting the foundation of calculus.\n')
        
        print('If you really think about it, we are more connected than we realize.')
        print('Take your boarding ticket and we will see you in Tokyo, Japan!\n')
        welcome_japan()
        
    #if user inputs any other numbers from 1-4, except for 3, quiz is reprompted until 3 is guessed    
    elif guess == '4' or 'four' in guess:
        print('\nActually, the Mayans were the ones who studied the sun, moon and stars, thus')
        print('creating the Haab Mayan calendar with 365.2420 days. It is even more accurate than the')
        print('Gregorian calendar that we use today.')
        print("Now that you're aware that Mayans first studied Astrology, let's try this quiz again.\n")
        india_inventions()
    elif guess == '2' or 'two' in guess:
        print('\nIt is believed that the invention of paper was discovered accidentally after leaving clothes')
        print('out too long after washing in China. Clothes were originally made out of hemp, therefore,')
        print('the original papers were made out of hemp as well before it became what it is now.')
        print("Now that you're aware that the Chinese first created paper, let's try tis quiz again.\n")
        india_inventions()
    elif guess == '1' or 'one' in guess:
        print("\nAlthough coffee is grown worldwide, we can trace the heritage of coffee to Ethiopia.")
        print('Legend has it that a goat herder named Kaldi discovered coffee after his goats ate berries')
        print('from a certain tree and shared it with his local monastery. This led to the spread of')
        print("coffee bean trade throughout the world.")
        print("Now that you're aware that coffee came from Ethiopia, let's try this quiz again.")
        india_inventions()
    #if user inputs anything other than 1-4, they will lose and exit the game
    else:
        print("\nAnswering the quiz like that is not appropriate.")
        lose('Here is your ticket home.')

#prints statements about street food in India and will prompt quiz
def india_food():
    print('Ahh, the pleasant street market vendors are all waving at you to try their local delights.')
    print('You can find puchkas, kathi rolls, samosas, momos and more on these streets.')
    print('Close to Bengali, you are bound to run into Bengali-style dishes as well!\n')
    
    #prompt quiz
    print("Kolkata's food scene is heavily influenced by Bengali and what other culture?\n")
    print('1) Chinese')
    print('2) Bhutanese')
    print('3) Italian')
    print('4) English\n')
    
    #stores user input in guess variable
    guess = input('Your guess: ')
    
    #if user guesses 1, prompts the Japan function
    if guess == '1' or 'one' in guess:
        print("\nThat's correct!\n")
        print('In the 18th century, the first wave of Chinese immigrants worked on the sugar plantations.')
        print('Chinese immigrants settled in Tangra, Kolkata for almost 230 years and established their')
        print('very own Chinatown in Tiretta Bazaar, central Kolkata. You can find dishes like the')
        print('dragon chicken, rice dumplings and soup, and other authentic Chinese dishes.\n')
        
        print('If you really think about it, we are more connected than we realize.')
        print('Take your boarding ticket and we will see you in Tokyo, Japan!\n')
        welcome_japan()
        
    #if user inputs numbers 2-4, quiz will prompt again until they answer as 1
    elif guess == '2' or 'two' in guess:
        print('\nAlthough India and Bhutan neighboring countries, there are other cultures with a')
        print("heavier influence in Kolkata street food. Why don't you try again.")
        india_food()
    elif guess == '3' or 'three' in guess:
        print('\nNot quite. The India and Italy relationship goes back to the Roman Empire, but')
        print("political relations reduced during the British colonization. Why don't you try again.")
        india_food()
    elif guess == '4' or 'four' in guess:
        print('\nThis is a good guess as the term "curry" was used by the English to describe all Indian dishes.')
        print('Unfortunately, the term curry and curry powder has little meaning in India.')
        print("Why don't you try again.")
        india_food()
    #if user inputs anything other than 1-4, they will fail and exit the game
    else:
        print('\nInteresting.. but not even close.')
        lose("Sorry, but seems like you've ran out of time.")

#prints Japan welcome speech and prompt location for next mini quiz    
def welcome_japan():
    print('Welcome to Japan!\n')
    print('This country will determine the ultimate winner and bring an end to the Amazing Race.')
    print('A small country made up of clustering islands with colonizing history and power,')
    print("Japan's relationship with other countries have been a complex one.")
    print('While you are here, you can take the JR line to Hiroshima or visit the local vendor markets.\n')
    
    print("Have you decided where you'd like to go?\n")
    print("1) I've had too much food. What's in Hiroshima?")
    print("2) There's no such thing as too much food!\n")
    
    #stores input into decision variable
    decision = input('Your decision: ')
    
    #depending on what the user inputs, will prompt next function
    if decision == '1' or 'one' in decision:
        Hiroshima()
    elif decision == '2' or 'two' in decision:
        japan_food()
    else:
        print('\nHmmm... sounds like you spent too much time wondering around the subway lines.')
        lose("Unfortunately, it's the end of the game for you.")

#prints Hiroshima history and mini quiz
def Hiroshima():
    print('\nWelcome to Hiroshima!\n')
    print('Hiroshima is in the prefacture of Peace.')
    print('Located in what used to be the commercial district of Hiroshima before the United States')
    print('dropped an atomic bomb above it in 1945, currently resides the Peace Memorial Park.')
    print('There are over 70 monuments in this park, including the Atomic Bomb Dome--a building that was')
    print('once the Prefectural Industrial Promotion Hall, and is now a UNESCO World Heritage.')
    print('It is also the only building standing that "survived" the atomic bomb.\n')
    
    print('Have you read the book about Sadako Sasaki?\n')
    print('She believe that if she made 1000 paper cranes, it would grant her wish to live.')
    print("Answer these questions to collect 1000 paper cranes to add to the Children's Peace Monument.\n")
    
    cranequestions()
    

#while loop that will stop when cranes = 1000
def cranequestions():
    total_cranes = 0
    print(total_cranes)
    print('You are starting with "0" total cranes.\n')
    
    while total_cranes < 1000:
        Q1cranes = CQ1()
        total_cranes = total_cranes + Q1cranes
        print(f"You currently have {total_cranes} cranes.\n")
        Q2cranes = CQ2()
        total_cranes = total_cranes + Q2cranes
        print(f"You now have {total_cranes} cranes.\n")
        Q3cranes = CQ3()
        total_cranes = total_cranes + Q3cranes
        print(f"Your current total is {total_cranes} cranes.\n")
        Q4cranes = CQ4()
        total_cranes = total_cranes + Q4cranes
        print(f"Almost there. One more question.\n") 
        Q5cranes = CQ5()
        total_cranes = total_cranes + Q5cranes
        print(f"You now have {total_cranes} cranes.\n")
        break
        
    #prints according to total crane
    if total_cranes == 1000:
        print(f"Congrats {name.upper()}! You just finished collecting 1000 cranes!")
    else:
        print(f"You have {total_cranes} cranes.")
        lose('You almost made it.')

#defines crane question1 and returns 200 cranes if user enters a number equal or higher to 70
def CQ1():
    print('Q1) How many monuments are in the Peace Memorial Park?\n')
    #stores user input
    number_monuments = int(input('> '))
    if number_monuments >= 70:
        print(f"Correct! As mentioned above, there are over 70 monuments. You have obtained 200 cranes!\n")
    #for loop will continue until user guesses correctly.
    else:
        print('Reread the information given and try again.\n')
        CQ1()
    #returns Q1cranes
    Q1cranes = 200
    return Q1cranes

#defines crane question2 and returns 200 cranes if user inputs true
def CQ2():
    print('Q2) The atomic bomb that was dropped on Hiroshima by the Americans was called the "Little Boy".\n')
    #stores user input
    answer = input('True or False? > ')
    
    if 'T' in answer or 't' in answer:
        print(f"Nice. You just gained 200 cranes.")
    else:
        print('Try again.')
        CQ2()
    #returns Q2cranes    
    Q2cranes = 200
    return(Q2cranes)

#defines question3 and returns 200 cranes if user inputs Nagasaki
def CQ3():
    print('What is the name of the other well known Japanese city the United States dropped bombs on?')
    city = input('> ').capitalize()
    if 'Nagasaki' in city:
        print("Sounds like you are well informed aobut the United States atomic warfare.")
    #will reprompt the question if user inputs anything with the letter n
    elif 'N' in city or 'n' in city:
        print("I think your spelling is a bit off. Try again.")
        CQ3()
    #returns 0 cranes if user answers incorrectly
    else:
        print("Hmm.. That's not quite it. No cranes for you.")
        Q3cranes = 0
        return(Q3cranes)
        
    #returns Q3cranes
    Q3cranes = 200
    return(Q3cranes)
    
#defines question4, prints out history of Laos and returns 0 or 200 cranes
def CQ4():
    print('What country is the most heavily bombed nation in the history?')
    country = input('Your guess: ')
    if country == 'Laos' or country == 'laos':
        print('\nSpot on! Although Laos was the offical neutral country, it became a battle ground')
        print('during the Cold War between the Unites States and the Soviety Union.')
        print('America dropped over 2 million tons of cluster bombs on this small country.')
        print('That is more bombs dropped during World War II combined. Today, 30% of the bombs dropped')
        print('from Americans still remain on Laotian soil as a result of failing to explose upon impact,')
        print('killing and injuring over 20,000 people with the 80 million bombs left behind.')
        print('President Barack Obama was the first president to visit Laos, pledging $90 million in aid')
        print('to remove and locate unexploded bombs.\n')
        print('200 cranes collected.')

    else:
        print('\nNot quite. Laos is actually the most bombed country in the world.')
        print('Although Laos was the offical neutral country, it became a battle ground')
        print('during the Cold War between the Unites States and the Soviety Union.')
        print('America dropped over 2 million tons of cluster bombs on this small country.')
        print('That is more bombs dropped during World War II combined. Today, 30% of the bombs dropped')
        print('from Americans still remain on Laotian soil as a result of failing to explode upon impact,')
        print('killing and injuring over 20,000 people with the 80 million bombs left behind.')
        print('President Barack Obama was the first president to visit Laos, pledging $90 million in aid')
        print('to remove and locate unexploded bombs.\n')
        
        print('You can read more about it here: ')
        print('https://www.history.com/news/laos-most-bombed-country-vietnam-war\n')
        #returns 0 cranes if answers is NOT Laos
        Q4cranes = 0
        return(Q4cranes)
        
    #returns Q2cranes    
    Q4cranes = 200
    return(Q4cranes)

#defines question5 and returns 200 cranes if user answers correctly
#I would like to add an option to bet cranes but will have to come back for this
#prompts user input for number(x) and returns twice the number(x) input
#user can choose to opt out of bet, with a return of 200
#if user fails to succeed in question, user will lose x number of cranes or return with 0 cranes 
def CQ5():
    
    #print("Last question, why don't you bet some cranes?")
    #print("Don't worry, if you choose to not bet any cranes, you can still get 200 cranes.")
    
    #x = int(input('How many cranes would you like to bet? > '))
    
    #if x >= 0:
    #    cranes = x * 2
    #    print(f"Perfect, you've bet {bet} cranes. If you answer the question right, you'll get {cranes} cranes.")
    #else:
    #    cranes = 200
    #    print('Okay, we will go ahead with no bets.')
    
    #starting the questions
    print('\nQ5) What is the name of the peace activist who protested against nuclear arms in front of the')
    print('\tWhite House in her peace camp until 2016?\n')
    
    print('1) Setsuko Thurlow')
    print('2) Wangari Maathai')
    print('3) Concepcion (Connie or Conchita) Picciotto')
    print('4) Dolores Huerta')
    guess = input('Your guess: ')
    
    if guess == "3" or guess == "three":
        print("\nNice! Yes, Picciotto was the one and only person who carried out the longest")
        print('continous act of political protest in the United States (35 years!).\n')
        
    elif guess == "1" or guess == "one":
        print('\nSetsuko Thurlow is actually a Japanese Canadian peace activist.')
        print('She is a survivor of the atomic bomb in Hiroshima and is known for her work')
        print('in anti-nuclear weapons after the United States dropped a hydrogen bomb in the Marshal Islands,')
        print('10 years after the bombing in Hirshima. The hydrogen bomb is 10x more powerful than the')
        print('bomb dropped in Hiroshma. Setsuko went on to advocate for anti-nuclear weapons and became')
        print('an active member in the ratification of the United Nations treaty on prohibition of nulcear')
        print("weapons. Let us learn from Setsuko Thurlow in her efforts for a more peaceful world.\n")
        print('Try again.\n')
        CQ5()
    elif guess == "2" or guess == "two":
        print('\nWangari Maathai is actually a Kenyan social, environmental and political activist and the')
        print('first African woman to win a Nobel Peace Prize. Maathai founded the Green Belt Movement,')
        print('an environment NGO organization that planted trees, pushed for enviornmental conservation,')
        print("and women's rights. The Wanagri Garden in Washington D.C honors her legacy in community")
        print('engagement and environmental protection.\n')
        print('Try again. \n')
        CQ5()
    elif guess == "4" or guess == "four":
        print('\nDolores Huerta, an American labor leader and civil rights activist who coined, "Si, se puede".')
        print('Cofounded with Cesar Chavez, of the Natoinal Farmworkers Association, Huerta helped')
        print("organize the Delano grape strike in 1965 in California and negotiated in the workers'")
        print("contract after the strike. Known for her activism in workers', women's, and immirgrant rights,")
        print('Huerta is a name we should all know.\n')
        print('Try again.\n')
        CQ5()
    else:
        print("Hmmm, it looks like you didn't even try.\n")
        Q5cranes = 0
        return(Q5cranes)

    #returns Q2cranes    
    Q5cranes = 200
    return(Q5cranes)

cranequestions()


