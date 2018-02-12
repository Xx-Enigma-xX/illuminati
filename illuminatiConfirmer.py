import random

toBeIlluminated = "lol"

illuminatiList = [("One. The Illuminati's symbol, the triangle has one eye!", 0),
("Two. Two is even.\n\nDo you know what else is even?\nThat's right.\nSix.", 6),
("Three. A triangle contains 3 sides.\n\nDo you know what else contains three sides?\nThat's right. Illuminati's sign!", 0),
("Four. In chinese numbers, four sounds same as death!\n\nDo you know what else likes death?\nYes. Devils.\n\nDevils are six letters long.", 6),
("Five. Humans have five fingers on one hand.\n\nDo you know what humans like?\nCorrect.\nThey like eating.\n\nDo you know what else likes eating?\nThat's right!\nPigs.\n\nPigs are four letters long.", 4),
("Six.\n\nSix... six... six...\n\n.\n.\n.\n\n666!\n666 is a demon number.\n\nDo you know what demons do?\nCorrect.\nThey take humans to hell.\n\nHell is horrible.\n\nDo you know what else is horrible?\nYes.\nAliens.\n\nAliens are also six letters long.\n\nCoincidence?\nI think not.\n\nThe symbol of the Illuminati is triangle.\nAn triangle as 3 sides and 3 vertices.\n3 + 3 = 6", 0),
("Seven. People say it's lucky.\n\nBut is it lucky?\nLet us see.\n\nSeven. Seven sounds like Steven.\n\nSteven Universe. Steven Universe is an animation made by Cartoon Network.\n\nCartoon Network makes Cartoons that are televised.\nBut, are they brainwashing us with their shows?\nMost likely.\n\nCartoon Network was launched on 1992.\nThe year 1992 was a leap year.\nDo you know what else is a leap year?\nThat's right.\nThe year 2012.\n\nDo you know what happended on the year 2012?\nYes. The 2012 phenominon.\n\nWhat is 2012 phenominon?\nThe 2012 phenomenon was a range of eschatological beliefs that cataclysmic or otherwise transformative events would occur on or around 21 December 2012.\n\nWow. Cataclysmic is 11 letters long.", 11),
("Eight. If you turn eight into sideways, you see the infinity sign.\n\nDo you know what else has infinity in it?\nThat's right.\nThe Samsung Infinity Display.\n\nThe Samsung Infinity Display was first implemented in the Samsung Galaxy S8.\n\nWoah!\n8! Again! Coincidence? I think not.\nIs Samsung trying to tell us something?\nMost likely.\n\nSamsung. Samsung originated in Korea. Korea is five letters long.", 5),
("Nine. People tell the tale of the nine tail fox.\n\nBut is it real?\nYou gotcha!\nYes. The nine tail fox exists.\nWhy would people even think of it?\n\nThe nien tail fox is a fox.\nFox is three letters long.", 3),
("Ten. When people thought Microsoft was about to release Windows 9, they released Windows 10.\nWoah.\n\nDid Windows 7 ate(8) Windows 9?\nYou got it!\nWindows 7 obviously were hungry.\n\nDoes that mean Windows 7 was self-aware?\nIs Microsoft tring to tell us something?\nMost likely.\n\nWhat else did Microsoft made that was self-aware?\nCorrect.\nMicrosoft Tay.\n\nMicrosoft Tay was a Twitter Bot that was a racist.\nRacist. Racist is 6 letters long.", 6),
("Eleven. In Stranger Things, Eleven is a girl that have super powers.\nShe suffered child abuse at Hawkins Labratory.\n\nDo you know what else does experiments?\nThat's right!\nThe Illuminati!", 0)]

def illuminate(item):
	story = ""
	num = len(item.replace(" ", ""))
	if num > 11:
		if num % 2 == 0:
			nextNum = random.randint(1, 5) * 2
			story = "%s contains %i letters.\n%i is even.\n\nDo you know what else is even?\nYes.\n%i.\n\n" % (item, num, num, nextNum)
		else:
			nextNum = random.randint(1, 6) * 2 - 1
			story = "%s contains %i letters.\n%i is odd.\n\nDo you know what else is odd?\nYes.\n%i.\n\n" % (item, num, num, nextNum)
	else:
		nextNum = num
		story = "%s. %s contains %i letters.\n\n" % (item, item, num)
	while not nextNum == 0:
		# print(nextNum)
		story = story + illuminatiList[nextNum - 1][0] + "\n\n"
		nextNum = illuminatiList[nextNum - 1][1]
	return story + "Therefore %s is Illuminati confirmed.\n\nThank you to the LuckOfTheClaw on Scratch for inspiring Enigma to make this project.\nYou can see LuckOfTheClaw's Random Illuminati Conspiracy theory generator here:\nhttps://scratch.mit.edu/projects/117836320/" % item

if __name__ == '__main__':
	print(illuminate(toBeIlluminated))
