from litcm import LIT
import ast

lit = LIT(labels=['hin', 'eng'])

with open("testdata/six.csv", 'r') as fp:
	data = fp.readlines()

for i in range(len(data)):
	data[i] = data[i].strip("\r\n")

# count1 = 0
# count2 = 0

valid = 0
oldvalid = 0
ignore = 0
oldignore = 0
match = 0
oldmatch = 0


for i in range(len(data)):

	if data[i].split(",")[1] == "":

		# if count2 != count1:
			# print "damn"

		words = []
		tweet = data[i].split(",")[0]

		detected = lit.identify(tweet).strip("\n")

		words = detected.split(" ")
		
		for j in range(len(words)):
			words[j] = words[j].split("\\")

		try:
			words.remove([''])
		except:
			pass

		# print words

		# count1 = len(words)
		# count2 = 0

	else:
		# print data[i]
		# count2 += 1

		currWord = data[i].split(",")[0]
		old = data[i].split(",")[1]
		correct = data[i].split(",")[2]
		predicted = words[0][1]

		validTags = ["Eng", "Hin"]

		if correct in validTags and predicted in validTags:
			valid += 1


			if words[0][0].lower() == currWord.lower():

				if predicted == correct:
					match += 1

				# print currWord, old, correct, words[0][1]
				pass
			else:
				print "\n\n\n-> -> -> error in alignment!!!!!\n\n\n"


		else:
			ignore += 1


		if correct in validTags and old in validTags:
			oldvalid += 1


			if words[0][0].lower() == currWord.lower():
				# print currWord, old, correct, words[0][1]

				if old == correct:
					oldmatch += 1

			else:
				print "\n\n\n-> -> -> error in alignment!!!!!\n\n\n"


		else:
			oldignore += 1



		words = words[1:]

		

print "old: ", (float(oldmatch)/oldvalid) * 100, (float(oldignore)/oldvalid) * 100
print "new: ", (float(match)/valid) * 100, (float(ignore)/valid) * 100

