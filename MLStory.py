import MLStories
import random
class Story(object):
    """ A Mad Lib Story """

    def __init__(self):
        self.title = ""
        self.story = ""
        self.numberOfNouns = 0
        self.numberOfVerbs = 0
        self.numberOfPTVerbs = 0
        self.numberOfAdjectives = 0
        self.numberOfAdverbs = 0
        self.numberOfPluralNouns = 0
        self.numberOfNumbers = 0
        self.numberOfESTAdjectives = 0
        self.numberOfINGVerbs = 0
        self.numberOfProperNouns = 0
        self.numberOfFNames = 0
        self.numberOfLAnimals = 0
        self.numberOfSAnimals = 0
        self.numberOfGirlNames = 0

    def createStory(self):
        chosenStory = random.choice(MLStories.MLSTORIES)
        self.title = chosenStory["title"]
        self.story = chosenStory["story"]
        self.numberOfAdjectives = chosenStory["adjectiveCount"]
        self.numberOfAdverbs = chosenStory["adverbCount"]
        self.numberOfNouns = chosenStory["nounCount"]
        self.numberOfPTVerbs = chosenStory["ptverbCount"]
        self.numberOfVerbs = chosenStory["verbCount"]
        self.numberOfPluralNouns = chosenStory["pNounCount"]
        self.numberOfNumbers = chosenStory["numCount"]
        self.numberOfESTAdjectives = chosenStory["estadjectiveCount"]
        self.numberOfINGVerbs = chosenStory["ingVerbCount"]
        self.numberOfProperNouns = chosenStory["propNounCount"]
        self.numberOfFNames = chosenStory["fNameCount"]
        self.numberOfLAnimals = chosenStory["lAnimalCount"]
        self.numberOfSAnimals = chosenStory["sAnimalCount"]
        self.numberOfGirlNames = chosenStory["girlNameCount"]
        return self

    def __str__(self):
        rep = ""
        rep += "title:\t\t" + self.title
        rep += "\nnounCount:\t" + str(self.numberOfNouns)
        rep += "\nverbCount:\t" + str(self.numberOfVerbs)
        rep += "\nptverbCount:\t" + str(self.numberOfPTVerbs)
        rep += "\nadjectiveCount:\t" + str(self.numberOfAdjectives)
        rep += "\nadverbCount:\t" + str(self.numberOfAdverbs)
        rep += "\npluralNounsCount:\t" + str(self.numberOfPluralNouns)
        rep += "\nnumbersCount:\t" + str(self.numberOfNumbers)
        rep += "\nestadjectiveCount:\t" + str(self.numberOfESTAdjectives)
        rep += "\ningverbCount:\t]t" + str(self.numberOfINGVerbs)
        rep += "\npropNounCount:\t\t" + str(self.numberOfProperNouns)
        rep += "\nstory:\t\t" + self.story
        return rep
