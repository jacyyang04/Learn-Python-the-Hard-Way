#Functions and Variables

#setting up the funtion
#def cheese_and_crackers(cheese_count, boxes_of_crackers):
#    print "You have %d cheese!" % cheese_count
#    print "You have %d boxes of crackers!" % boxes_of_crackers
#    print "That's enough for a party.\n"

#executing the functions in multiple ways


#print "We can give the numbers directly."
#cheese_and_crackers(20, 30)

#print "Or, we can use variables from our script."
#amount_of_cheese = 10
#amount_of_crackers = 50

#cheese_and_crackers(amount_of_cheese, amount_of_crackers)


#print "We can also do math inside."
#cheese_and_crackers(10 + 20, 15 + 5)

#print "We can combine the two, math and variable."
#cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 100)



#my function

def covid_history():
    covid_movies = int(raw_input("How many movies did you watch over COIVD? "))
    covid_lbs = int(raw_input("How much lbs did you lose over COVID? "))
    covid_python = int(raw_input("How long did you spend studying over COVID? "))
    print """
Perfect. So you watched %d movies, lost %d lbs and spent %d minutes studying
over the COVID pandemic.
    """ % (covid_movies, covid_lbs, covid_python)
    
covid_history()


