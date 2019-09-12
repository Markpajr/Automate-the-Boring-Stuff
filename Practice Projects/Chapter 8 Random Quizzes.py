#! python3
# randomQuizGenerator.py - Creates quizzes with questions and answers in
# random order, along with the answer key.

import random, os
os.chdir('.\\Practice Projects\\ch 8 Quiz Files')
# State names and capitals are stored in capitals dictionary
capitals = {
    "Alabama": "Montgomery",
    "Alaska": "Juneau",
    "Arizona": "Phoenix",
    "Arkansas": "Little Rock",
    "California": "Sacramento",
    "Colorado": "Denver",
    "Connecticut": "Hartford",
    "Delaware": "Dover",
    "Florida": "Tallahassee",
    "Georgia": "Atlanta",
    "Hawaii": "Honolulu",
    "Idaho": "Boise",
    "Illinois": "Springfield",
    "Indiana": "Indianapolis",
    "Iowa": "Des Moines",
    "Kansas": "Topeka",
    "Kentucky": "Frankfort",
    "Louisiana": "Baton Rouge",
    "Maine": "Augusta",
    "Maryland": "Annapolis",
    "Massachusetts": "Boston",
    "Michigan": "Lansing",
    "Minnesota": "Saint Paul",
    "Mississippi": "Jackson",
    "Missouri": "Jefferson City",
    "Montana": "Helena",
    "Nebraska": "Lincoln",
    "Nevada": "Carson City",
    "New Hampshire": "Concord",
    "New Jersey": "Trenton",
    "New Mexico": "Santa Fe",
    "New York": "Albany",
    "North Carolina": "Raleigh",
    "North Dakota": "Bismarck",
    "Ohio": "Columbus",
    "Oklahoma": "Oklahoma City",
    "Oregon": "Salem",
    "Pennsylvania": "Harrisburg",
    "Rhode Island": "Providence",
    "South Carolina": "Columbia",
    "South Dakota": "Pierre",
    "Tennessee": "Nashville",
    "Texas": "Austin",
    "Utah": "Salt Lake City",
    "Vermont": "Montpelier",
    "Virginia": "Richmond",
    "Washington": "Olympia",
    "West Virginia ": " Charleston ",
    " Wisconsin ": " Madison ",
    " Wyoming ": " Cheyenne ",
}

for quizNum in range(5):
   # TODO: Create quize and answer key
   fileNum = quizNum + 1
   quizFile = open(f"capitalsQuiz{fileNum}.txt", "w")
   answerFile = open(f"CapitalsQuiz_Answers{fileNum}.txt", "w")

   # TODO: Write Quiz Header

   quizFile.write("Name:\n\nDate:\n\nPeriod:\n\n")
   quizFile.write((" " * 20) + f"State Capitals Quiz (Form {fileNum})")
   quizFile.write("\n\n")

   # TODO: Shuffle order of states

   states = list(capitals.keys())
   random.shuffle(states)

   # TODO: Loop the creation of question for all 50 states

   for questionNum in range(50):
      correctAnswer = capitals[states[questionNum]]
      wrongAnswers = list(capitals.values())
      del wrongAnswers[wrongAnswers.index(correctAnswer)]
      wrongAnswers = random.sample(wrongAnswers, 3)
      answerOptions = wrongAnswers + [correctAnswer]
      random.shuffle(answerOptions)
      quizFile.write(f'{questionNum + 1}. What is the capital of {states[questionNum]}?\n')              
      for i in range(4):
         ansLet = 'ABCD'[i]
         quizFile.write(f'{ansLet}. {answerOptions[i]}\n')
      quizFile.write('\n')
      CorrAnsLet = 'ABCD'[answerOptions.index(correctAnswer)]
      answerFile.write(f'{questionNum + 1}. {CorrAnsLet}\n')
   quizFile.close()
   answerFile.close()