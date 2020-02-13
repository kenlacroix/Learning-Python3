## Formatting Methods ##

#You’re a programmer working for an organization that is trying to digitize and
#store poetry called Preserve the Verse.
#
#You’ve been given two strings, the title of a poem and it’s author, and have
#been asked to reformat them slightly to fit the conventions of the
#organization’s database.
#
#Make poem_title have title case and save it to poem_title_fixed.

poem_title = "spring storm"
poem_author = "William Carlos Williams"

poem_title_fixed = poem_title.title()
print(poem_title) #spring storm
print(poem_title_fixed) #Spring Storm
poem_author_fixed = poem_author.upper()
print(poem_author) #William Carlos Williams
print(poem_author_fixed) #WILLIAM CARLOS WILLIAMS

## Splitting Strings ##

#In the code editor is a string of the first line of the poem Spring Storm by
#William Carlos Williams.
#
#Use .split() to create a list called line_one_words that contains each word
#in this line of poetry.

line_one = "The sky has given over"
line_one_words = line_one.split()
print(line_one_words) #['The', 'sky', 'has', 'given', 'over']

## Splitting Strings II ##

#Your boss at the Poetry organization sent over a bunch of author names that he
#wants you to prepare for importing into the database. Annoyingly, he sent
#them over as a long string with the names separated by commas.
#
#Using .split() and the provided string, create a list called author_names
#containing each individual author name as it’s own string.

authors = "Audre Lorde, William Carlos Williams, Gabriela Mistral, Jean Toomer,\
 An Qi, Walt Whitman, Shel Silverstein, Carmen Boullosa, Kamala Suraiyya,\
 Langston Hughes, Adrienne Rich, Nikki Giovanni"

author_names = authors.split(',')
#['Audre Lorde', ' William Carlos Williams', ' Gabriela Mistral',
#' Jean Toomer', ' An Qi', ' Walt Whitman', ' Shel Silverstein',
#' Carmen Boullosa', ' Kamala Suraiyya', ' Langston Hughes', ' Adrienne Rich',
#' Nikki Giovanni']

#Great work, but now it turns out they didn’t want poet’s first names
#(why didn’t they just say that the first time!?)
#
#Create another list called author_last_names that only contains the last
#names of the poets in the provided string.

author_last_names = []
for name in author_names:
    author_last_names.append(name.split()[-1])

## Splitting Strings III ##

#The organization has sent you over the full text for William Carlos Williams
#poem Spring Storm. They want you to break the poem up into its individual
#lines.
#
#Create a list called spring_storm_lines that contains a string for each line
#of Spring Storm.

spring_storm_text = \
"""The sky has given over
its bitterness.
Out of the dark change
all day long
rain falls and falls
as if it would never end.
Still the snow keeps
its hold on the ground.
But water, water
from a thousand runnels!
It collects swiftly,
dappled with black
cuts a way for itself
through green ice in the gutters.
Drop after drop it falls
from the withered grass-stems
of the overhanging embankment."""

spring_storm_lines = spring_storm_text.split('\n')

## Joining Strings ##

#You’ve been provided with a list of words from the first line of Jean Toomer’s
#poem Reapers.
#
#Use .join() to combine these words into a sentence and save that sentence as
#the string reapers_line_one.

reapers_line_one_words = ["Black", "reapers", "with", "the", "sound", "of", \
"steel", "on", "stones"]

reapers_line_one = ' '.join(reapers_line_one_words)

## Joining Strings II ##

#You’ve been given a list, winter_trees_lines, that contains all the lines to
#William Carlos Williams poem, Winter Trees. You’ve been asked to join together
#the strings in the list together into a single string that can be used to
#display the full poem. Name this string winter_trees_full.
#
#Print your result to the terminal. Make sure that each line of the poem
#appears on a new line in your string.

winter_trees_lines = ['All the complicated details', 'of the attiring and', \
'the disattiring are completed!', 'A liquid moon', 'moves gently among', \
'the long branches.', 'Thus having prepared their buds', \
'against a sure winter', 'the wise trees', 'stand sleeping in the cold.']

winter_trees_full = '\n'.join(winter_trees_lines)

## Strip ##

#They sent over another list containing all the lines to the Audre Lorde poem,
#Love, Maybe. They want you to join together all of the lines into a single
#string that can be used to display the poem again, but this time, you’ve
#oticed that the list contains a ton of unnecessary whitespace that doesn’t
#appear in the actual poem.
#
#First, use .strip() on each line in the list to remove the unnecessary
#whitespace and save it as a new list love_maybe_lines_stripped.

love_maybe_lines = ['Always    ', '     in the middle of our bloodiest battles  ', 'you lay down your arms', '           like flowering mines    ','\n' ,'   to conquer me home.    ']

love_maybe_lines_stripped = []
for line in love_maybe_lines:
    love_maybe_lines_stripped.append(line.strip())

#.join() the lines in love_maybe_lines_stripped together into one large
#multi-line string, love_maybe_full, that can be printed to display the poem.
#
#Each line of the poem should show up on its own line.

love_maybe_lines_stripped = []
love_maybe_full = []
for line in love_maybe_lines:
    love_maybe_lines_stripped.append(line.strip())
love_maybe_full = '\n'.join(love_maybe_lines_stripped)

#Print love_maybe_full.

print(love_maybe_full)

## Replace ##

#The poetry organization has sent over the bio for Jean Toomer as it currently
#exists on their site. Notice that there was a mistake with his last name and
#all instances of Toomer are lacking one o.
#
#Use .replace() to change all instances of Tomer in the bio to Toomer.
#Save the updated bio to the string toomer_bio_fixed.

toomer_bio = \
"""
Nathan Pinchback Tomer, who adopted the name Jean Tomer early in his literary \
career, was born in Washington, D.C. in 1894. Jean is the son of Nathan Tomer \
was a mixed-race freedman, born into slavery in 1839 in Chatham County, \
North Carolina. Jean Tomer is most well known for his first book Cane, which \
vividly portrays the life of African-Americans in southern farmlands.
"""

toomer_bio_fixed = toomer_bio.replace('Tomer', 'Toomer')

## Find ##

#In the code editor is the first line of Gabriela Mistral’s poem God Wills It.
#
#At what index place does the word “disown” appear? Save that index place to
#the variable disown_placement.

god_wills_it_line_one = "The very earth will disown you"

disown_placement = god_wills_it_line_one.find('disown')

## Format ##

#Write a function called poem_title_card that takes two inputs poet and title.
#The function should use .format() to return the following string:
#
# The poem "[TITLE]" is written by [POET].
#
#For example, if the function is given the inputs
#
#poem_title_card("Walt Whitman", "I Hear America Singing")
#
#It should return the string
#
#The poem "I Hear America Singing" is written by Walt Whitman.

def poem_title_card(poet, title):
    return "The poem \"{}\" is written by {}.".format(title, poet)

poem_title_card("Walt Whitman", "I Hear America Singing")


## Format II ##

#The function poem_description is supposed to use .format() to print out
#some quick information about a poem, but it seems to be causing some errors
#currently.
#
#Fix the function by using keywords in the .format() method.

#def poem_description(publishing_date, author, title, original_work):
#  poem_desc = "The poem {title} by {author} was originally published in \
#  {original_work} in {publishing_date}.".format(publishing_date, author, \
#  title, original_work)
#  return poem_desc

def poem_description(publishing_date, author, title, original_work):
  poem_desc = "The poem {title} by {author} was originally published in \
  {original_work} in {publishing_date}.".format(\
  publishing_date = publishing_date, author = author, \
  title = title, original_work = \
  original_work)
  return poem_desc

my_beard_description = poem_description("1974", "Shel Silverstein",\
 "My Beard", "Where the Sidewalk Ends")

print(my_beard_description)

## Review ##

#.upper(), .title(), and .lower() adjust the casing of your string.

#.split() takes a string and creates a list of substrings.

#.join() takes a list of strings and creates a string.

#.strip() cleans off whitespace, or other noise from the beginning and end of
#a string.

#.replace() replaces all instances of a character/string in a string with
#another character/string.

#.find() searches a string for a character/string and returns the index
#value that character/string is found at.

#.format() and f-strings allow you to interpolate a string with variables.

#Preserve the Verse has one final task for you. They have delivered you a string
#that contains a list of poems, titled highlighted_poems, they want to highlight
#on the site, but they need your help to parse the string into something that
#can display the name, title, and publication date of the highlighted poems on
#the site.
#
#First, start by printing highlighted_poems to the terminal and see how it
#displays.

highlighted_poems = "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos \
Williams:1915, Ecstasy:Gabriela Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   \
Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, \
Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico City:Carmen \
Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston \
Hughes:1994, Dreamwood:Adrienne Rich:1987"

print(highlighted_poems)

#The information for each poem is separated by commas, and within this
#information is the title of the poem, the author, and the date of publication.
#
#Start by splitting highlighted_poems at the commas and saving it to
#highlighted_poems_list.

highlighted_poems_list = highlighted_poems.split(',')

#Print highlighted_poems_list, how does the structure of the data look now?

print(highlighted_poems_list)


#Notice that there is inconsistent whitespace in highlighted_poems_list.
#Let’s clean that up.
#
#Start by creating a new empty list, highlighted_poems_stripped.
#
#Then, iterate through highlighted_poems_list using a for loop and for each
#poem strip away the whitespace and append it to your new list,
#highlighted_poems_stripped.

highlighted_poems_stripped = []
for i in highlighted_poems_list:
    highlighted_poems_stripped.append(i.strip())

#Print highlighted_poems_stripped.
#
#Looks good! All the whitespace is cleaned up.

print(highlighted_poems_stripped)

#Next we want to break up all the information for each poem into it’s own list,
#so we end up with a list of lists.
#
#Create a new empty list called highlighted_poems_details.

highlighted_poems_details = []

#Iterate through highlighted_poems_stripped and split each string around the :
#characters and append the new lists into highlighted_poems_details.

highlighted_poems_details = []
for i in highlighted_poems_stripped:
    split = i.split(':')
    highlighted_poems_details.append(split))
print(highlighted_poems_details)

#Great! Now we want to separate out all of the titles, the poets, and the
#publication dates into their own lists.
#
#Create three new empty lists, titles, poets, and dates.

titles = []
poets = []
dates = []

#Iterate through highlighted_poems_details and for each list in the list
#append the appropriate elements into the lists titles, poets, and dates.
#
#For example, for the poem The Shadow (1915) by William Carlos Williams your
#code should be adding "The Shadow" to titles, "William Carlos Williams" to
#poets, and "1915" to dates.

for i in highlighted_poems_details:
    titles.append(i[0])
    poets.append(i[1])
    dates.append(i[2])

#Finally, write a for loop that uses either f-strings or .format() to prints
#out the following string for each poem:
#
#The poem TITLE was published by POET in DATE.

increment = 0
for i in range(len(titles)):
    print("The poem " + titles[increment] + " was published by " + \
    poets[increment] + " in " + dates[increment])
    increment += 1
