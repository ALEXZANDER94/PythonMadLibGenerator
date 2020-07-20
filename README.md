# PythonMadLibGenerator
a mad lib generator made in python

This mad lib generator is made in Python using an Object-Oriented Approach and also implements a GUI interface with TKInter. There are 7 different stories that can be loaded up
into the GUI.

Upon loading up the Program, a window appears with a Welcome message and informs the user that they must provide a value in each field to generate the story. Even if the user were
to leave a field blank, there is a checker that runs before the story is generated to ensure that all fields have a value. If there is a field that does not have a value, the user
is notified from the story Text Box.

This was a particularly tricky program to make because of the variety of stories that are included; some have more fields than others; whilst some ask for different quantities of
the same fields. I had to implement a system that would dynamically create these fields, but also had to make it so I could access the entered nouns, verbs, adjectives, etc.

After a value has been entered for each field, the user may hit the "Tell Story" button and then the story will be built with those fields. The Story will appear in the text box 
at the bottom of the form along with the title of the story.

At any time, the user may select the "Load New Mad Lib" button to clear the frame of all widgets and load a whole new mad lib with a different set of fields.
