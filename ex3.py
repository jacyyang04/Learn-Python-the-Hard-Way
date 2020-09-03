name = 'Jolly Fellow'
age = 26
height = 59 #inches
weight = 140 #lbs
eyes = 'brown'
hair = 'black'

heightcm = height * 2.54

weightkg = weight * 0.45392

print "Let's talk about %s." % name
print "She is %d inches tall. That's about %d in cm!" % (height, heightcm)
print "That's considered short in the United States. Yikes!"
print "She is %r years old." % age
print "%s weighs about %r lbs. That's about %r in kg!" % (name, weight, weightkg)
print "She has %s eyes and %s hair." % (eyes, hair)

#trying something new new new
print "If I add %d, %d, and %d, I'd get %d." % (age, weightkg, heightcm, age + weightkg + heightcm)
