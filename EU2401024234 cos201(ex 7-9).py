#ex.7
# this print a simple sentence
print("mary had a little lamb.")

#this print another sentence,but the word "snow" is inserted using .format().
print("its fleece was white as{}.".format('snow'))

#this print another line of the rhyme.
print("and everywhere that mary went.")

#this print a period (.) ten times in a row.it result in "..........".
print("." * 10)

# the next line store single letters in a variables
end1="c"
end2="h"
end3="e"
end4="e"
end5="s"
end6="e"
end7="B"
end8="u"
end9="r"
end10="g"
end11="e"
end12="r"

#this print the first group of letters and form the word "cheese"
print(end1 + end2 + end3 + end4 + end5 + end6, end=' ')

#this print the second group of letters and form the word "burger"
print(end7 + end8 + end9 + end10 + end11 + end12)

#Ex.9
#this line creates a formatter string containing four empty placeholders.
formatter= "{} {} {} {}"

#this line print the number 1,2,3, and 4 in place of the four placeholders.
print(formatter.format(1, 2, 3, 4))

#this line print four strings ("one", "two", "three", "four") inside the placeholders.
print(formatter.format("one", "two", "three", "four"))

#this line print four boolean values(True, False,False,True)
print(formatter.format(True, False, False, True))

#this line print the formatter itself four times.
print(formatter.format(formatter, formatter,formatter, formatter))

#this print four lines of text by inserting each string into a placeholder.
print(formatter.format(
    "try your",
    "own text here",
    "maybe a poem",
    "or a song about fear"
))

#Ex.9
# here's some new strange stuff, remember type it exactly

#this variables stores all the days of the week in one string.
days = "mon tue wed thu fri sat sun"

#this variables stores the months of the year, but uses \n to create new lines.
#Each \n makes the next month appear on a new line when printed
months = "Jan\nFeb\nmar\nApr\nMay\nJun\nAug"
#this print the text "here are the days:" followed by the contents of the days variable.
print("here are the days:", days)

#this print the text "here are the months:" followed by month variable.
print("here are the months:", months)

#this print statement uses triple double-quotes.
#triple-quoted string allow us to type multiple lines of text all at once.
print("""
there's something going on here.
with the three double-quotes
we'll be able to type as much as we like.
even 4 lines if we want, or 5, 0r 6.
""")