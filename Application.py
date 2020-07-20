import tkinter as tk
import MLStory

class Application(tk.Frame):
    """ a Python TKInter Application """

    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.Nouns = []
        self.Verbs = []
        self.Adjectives = []
        self.Adverbs = []
        self.PTVerbs = []
        self.PluralNouns = []
        self.Numbers = []
        self.ESTAdjectives = []
        self.INGVerbs = []
        self.propNouns = []
        self.fNames = []
        self.lAnimals = []
        self.sAnimals = []
        self.girlNames = []
        self.rowCount = 0
        self.storyText = ""
        self.populateFrame()
        


    def changeStory(self):
        for widget in self.winfo_children():
            widget.destroy()
        self.story.destroy()
        self.grid_forget()
        self.grid()
        self.Nouns = []
        self.Verbs = []
        self.Adjectives = []
        self.Adverbs = []
        self.PTVerbs = []
        self.PluralNouns = []
        self.Numbers = []
        self.ESTAdjectives = []
        self.INGVerbs = []
        self.propNouns = []
        self.fNames = []
        self.lAnimals = []
        self.sAnimals = []
        self.girlNames = []
        self.rowCount = 0
        self.storyText = ""
        self.populateFrame()

    def buildStory(self):
        """ takes the input from each field and places them into the story """
        storyText = self.MadLib.story
        for nouns in self.Nouns:
            storyText = storyText.replace("*noun*", nouns.get(), 1)

        for verbs in self.Verbs:
            storyText = storyText.replace("*verb*", verbs.get(), 1)

        for adjectives in self.Adjectives:
            storyText = storyText.replace("*adjective*", adjectives.get(), 1)

        for adverbs in self.Adverbs:
            storyText = storyText.replace("*adverb*", adverbs.get(), 1)

        for ptverbs in self.PTVerbs:
            storyText = storyText.replace("*ptverb*", ptverbs.get(), 1)

        for estadj in self.ESTAdjectives:
            storyText = storyText.replace("*estadj*", estadj.get(), 1)

        for number in self.Numbers:
            storyText = storyText.replace("*number*", number.get(), 1)

        for pnouns in self.PluralNouns:
            storyText = storyText.replace("*pnoun*", pnouns.get(), 1)

        for ingverbs in self.INGVerbs:
            storyText = storyText.replace("*ingverb*", ingverbs.get(), 1)

        for propnouns in self.propNouns:
            storyText = storyText.replace("*propnouns*", propnouns.get(), 1)

        for fnames in self.fNames:
            storyText = storyText.replace("*fname*", fnames.get(), 1)

        for lanimals in self.lAnimals:
            storyText = storyText.replace("*lanimal*", lanimals.get(), 1)

        for sanimals in self.sAnimals:
            storyText = storyText.replace("*sanimal*", sanimals.get(), 1)

        for girlnames in self.girlNames:
            storyText = storyText.replace("*girlname*", girlnames.get(), 1)

        self.story.tag_config("title", justify="center")
        self.story.tag_config("storyText", justify="left")
        self.story.tag_add("title", "1.0", "2.0")
        self.story.tag_add("storyText", "2.0", tk.END)
        self.story.insert("1.0", self.MadLib.title + "\n", "title")
        self.story.insert("3.0", "\n" + storyText, "storyText")
    
    def checkFields(self):
        """ Checks the fields to see if they are empty """
        emptyFields = ""
        self.story["state"] = tk.NORMAL
        self.story.delete("0.0", tk.END)
        for nouns in range(len(self.Nouns)):
            if(self.Nouns[nouns].get() == ""):
                emptyFields += "Please fill out Noun #" + str(nouns+1) +"\n"

        for verbs in range(len(self.Verbs)):
            if(self.Verbs[verbs].get() == ""):
                emptyFields += "Please fill out Verb #" + str(verbs+1) +"\n"

        for adjectives in range(len(self.Adjectives)):
            if(self.Adjectives[adjectives].get() == ""):
                emptyFields += "Please fill out Adjective #" + str(adjectives+1) +"\n"

        for adverbs in range(len(self.Adverbs)):
            if(self.Adverbs[adverbs].get() == ""):
                emptyFields += "Please fill out Adverb #" + str(adverbs+1) +"\n"

        for ptverbs in range(len(self.PTVerbs)):
            if(self.PTVerbs[ptverbs].get() == ""):
                emptyFields += "Please fill out Past Tense Verb #" + str(ptverbs+1) +"\n"

        for pnouns in range(len(self.PluralNouns)):
            if(self.PluralNouns[pnouns].get() == ""):
                emptyFields += "Please fill out Plural Noun #" + str(pnouns+1) +"\n"
        
        for number in range(len(self.Numbers)):
            if(self.Numbers[number].get() == ""):
                emptyFields += "Please fill out Number #" + str(number+1) +"\n"

        for estadj in range(len(self.ESTAdjectives)):
            if(self.ESTAdjectives[estadj].get() == ""):
                emptyFields += "Please fill out Adjective ending in -est #" + str(estadj+1) +"\n"

        for ingverbs in range(len(self.INGVerbs)):
            if(self.INGVerbs[ingverbs].get() == ""):
                emptyFields += "Please fill out Verb ending in -ing #" + str(ingverbs+1) +"\n"

        for propnouns in range(len(self.propNouns)):
            if(self.propNouns[propnouns].get() == ""):
                emptyFields += "Please fill out Proper Noun #" + str(propnouns+1) +"\n"

        for fnames in range(len(self.fNames)):
            if(self.fNames[fnames].get() == ""):
                emptyFields += "Please fill out First Name #" + str(fnames+1) +"\n"

        for lanimals in range(len(self.lAnimals)):
            if(self.lAnimals[lanimals].get() == ""):
                emptyFields += "Please fill out Large Animal #" + str(lanimals+1) +"\n"

        for sanimals in range(len(self.sAnimals)):
            if(self.sAnimals[sanimals].get() == ""):
                emptyFields += "Please fill out Small Animal #" + str(sanimals+1) +"\n"

        for girlnames in range(len(self.girlNames)):
            if(self.girlNames[girlnames].get() == ""):
                emptyFields += "Please fill out Girl Name #" + str(girlnames+1) +"\n"
                
        if(emptyFields == ""):
            self.buildStory()
        else:
            self.story.insert(0.0, emptyFields)
        self.story["state"] = tk.DISABLED

    def populateFrame(self):
        """ Populates the frame of the window with each field and the story Box"""
        rowCount = 0
        self.story = tk.Text(width=100, height=20, wrap=tk.WORD)
        self.MadLib = MLStory.Story().createStory()
        tk.Label(self, 
                 text="Welcome to the Python Mad Lib Generator\nPlease fill out the respective fields to generate your mad lib").grid(row=rowCount,
                                                                                                                                      column=1,
                                                                                                                                      columnspan=2)
        rowCount += 1
        for index in range(self.MadLib.numberOfNouns):
            self.Nouns.append(tk.Entry(self))
            self.Nouns[index].grid(row=rowCount,column=1)
            tk.Label(self,
                    text="Noun #" + str(index+1)).grid(row=rowCount, column=0, sticky=tk.W)
            rowCount += 1

        if(self.MadLib.numberOfNouns > 0):
            tk.Label(self, text="").grid(row=rowCount, columnspan=2)
            rowCount+=1
        
        for index in range(self.MadLib.numberOfVerbs):
            self.Verbs.append(tk.Entry(self))
            self.Verbs[index].grid(row=rowCount,column=1)
            tk.Label(self,
                    text="Verb #" + str(index+1)).grid(row=rowCount, column=0, sticky=tk.W)
            rowCount += 1
        
        if(self.MadLib.numberOfVerbs > 0):
            tk.Label(self, text="").grid(row=rowCount, columnspan=2)
            rowCount+=1

        for index in range(self.MadLib.numberOfAdverbs):
            self.Adverbs.append(tk.Entry(self))
            self.Adverbs[index].grid(row=rowCount,column=1)
            tk.Label(self,
                    text="Adverb #" + str(index+1)).grid(row=rowCount, column=0, sticky=tk.W)
            rowCount += 1
        
        if(self.MadLib.numberOfAdverbs > 0):
            tk.Label(self, text="").grid(row=rowCount, columnspan=2)
            rowCount+=1
        
        for index in range(self.MadLib.numberOfAdjectives):
            self.Adjectives.append(tk.Entry(self))
            self.Adjectives[index].grid(row=rowCount,column=1)
            tk.Label(self,
                    text="Adjective #" + str(index+1)).grid(row=rowCount, column=0, sticky=tk.W)
            rowCount += 1
        
        if(self.MadLib.numberOfAdjectives > 0):
            tk.Label(self, text="").grid(row=rowCount, columnspan=2)
            rowCount+=1

        for index in range(self.MadLib.numberOfPluralNouns):
            self.PluralNouns.append(tk.Entry(self))
            self.PluralNouns[index].grid(row=rowCount,column=1)
            tk.Label(self,
                    text="Plural Noun #" + str(index+1)).grid(row=rowCount, column=0, sticky=tk.W)
            rowCount += 1
        
        if(self.MadLib.numberOfPluralNouns > 0):
            tk.Label(self, text="").grid(row=rowCount, columnspan=2)
            rowCount+=1
        
        for index in range(self.MadLib.numberOfNumbers):
            self.Numbers.append(tk.Entry(self))
            self.Numbers[index].grid(row=rowCount,column=1)
            tk.Label(self,
                    text="Number #" + str(index+1)).grid(row=rowCount, column=0, sticky=tk.W)
            rowCount += 1
        
        if(self.MadLib.numberOfNumbers > 0):
            tk.Label(self, text="").grid(row=rowCount, columnspan=2)
            rowCount+=1

        for index in range(self.MadLib.numberOfESTAdjectives):
            self.ESTAdjectives.append(tk.Entry(self))
            self.ESTAdjectives[index].grid(row=rowCount,column=1)
            tk.Label(self,
                    text="Adjective ending in -est #" + str(index+1)).grid(row=rowCount, column=0, sticky=tk.W)
            rowCount += 1
        
        if(self.MadLib.numberOfESTAdjectives > 0):
            tk.Label(self, text="").grid(row=rowCount, columnspan=2)
            rowCount+=1

        for index in range(self.MadLib.numberOfINGVerbs):
            self.INGVerbs.append(tk.Entry(self))
            self.INGVerbs[index].grid(row=rowCount,column=1)
            tk.Label(self,
                    text="Verb ending in -ing #" + str(index+1)).grid(row=rowCount, column=0, sticky=tk.W)
            rowCount += 1
        
        if(self.MadLib.numberOfINGVerbs > 0):
            tk.Label(self, text="").grid(row=rowCount, columnspan=2)
            rowCount+=1

        for index in range(self.MadLib.numberOfProperNouns):
            self.propNouns.append(tk.Entry(self))
            self.propNouns[index].grid(row=rowCount,column=1)
            tk.Label(self,
                    text="Proper Noun #" + str(index+1)).grid(row=rowCount, column=0, sticky=tk.W)
            rowCount += 1
        
        if(self.MadLib.numberOfProperNouns > 0):
            tk.Label(self, text="").grid(row=rowCount, columnspan=2)
            rowCount+=1

        for index in range(self.MadLib.numberOfFNames):
            self.fNames.append(tk.Entry(self))
            self.fNames[index].grid(row=rowCount,column=1)
            tk.Label(self,
                    text="First Name #" + str(index+1)).grid(row=rowCount, column=0, sticky=tk.W)
            rowCount += 1
        
        if(self.MadLib.numberOfFNames > 0):
            tk.Label(self, text="").grid(row=rowCount, columnspan=2)
            rowCount+=1

        for index in range(self.MadLib.numberOfLAnimals):
            self.lAnimals.append(tk.Entry(self))
            self.lAnimals[index].grid(row=rowCount,column=1)
            tk.Label(self,
                    text="Large Animal #" + str(index+1)).grid(row=rowCount, column=0, sticky=tk.W)
            rowCount += 1
        
        if(self.MadLib.numberOfLAnimals > 0):
            tk.Label(self, text="").grid(row=rowCount, columnspan=2)
            rowCount+=1

        for index in range(self.MadLib.numberOfSAnimals):
            self.sAnimals.append(tk.Entry(self))
            self.sAnimals[index].grid(row=rowCount,column=1)
            tk.Label(self,
                    text="Small Animal #" + str(index+1)).grid(row=rowCount, column=0, sticky=tk.W)
            rowCount += 1
        
        if(self.MadLib.numberOfSAnimals > 0):
            tk.Label(self, text="").grid(row=rowCount, columnspan=2)
            rowCount+=1

        for index in range(self.MadLib.numberOfGirlNames):
            self.girlNames.append(tk.Entry(self))
            self.girlNames[index].grid(row=rowCount,column=1)
            tk.Label(self,
                    text="Girl Name #" + str(index+1)).grid(row=rowCount, column=0, sticky=tk.W)
            rowCount += 1
        
        if(self.MadLib.numberOfGirlNames > 0):
            tk.Label(self, text="").grid(row=rowCount, columnspan=2)
            rowCount+=1

        for index in range(self.MadLib.numberOfPTVerbs):
            self.PTVerbs.append(tk.Entry(self))
            self.PTVerbs[index].grid(row=rowCount,column=1)
            tk.Label(self,
                    text="Past Tense Verb #" + str(index+1)).grid(row=rowCount, column=0, sticky=tk.W)
            rowCount += 1

        tk.Button(self, text="Tell Story", command=self.checkFields).grid(row=rowCount, column=0, sticky=tk.W)
        tk.Button(self, text="Load New Mad Lib", command=self.changeStory).grid(row=rowCount, column=1, sticky=tk.W)
        rowCount += 1
        
        tk.Label(self, text="").grid(row=rowCount, columnspan=2)
        rowCount+=1
        
        self.story["state"] = tk.DISABLED
        self.story.grid(row=rowCount, column=0, columnspan=2)
        
        
