import re

# \(adj\)|\(noun\)|\(verb\)|
story = """
I walk through the color jungle. I take out my \n
(adj) canteen. There's a\n
(adj) parrot with a (adj) \n
(noun) in his mouth right in front of me in the\n
(adj) trees! I gaze at his (adj)\n
(noun) . A sudden sound awakes me from my\n
daydream! A panther "s" (verb) in front of my\n
head! I (verb) his (adj) \n
breath. I remember I have a packet of (noun)\n
that makes go into a deep slumber! I (verb) it\n
away in front of the (noun) . Yes he's eating\n
it! I (verb) away through the\n
(adj) jungle. I meet my parents at the tent.\n
Phew; It’s been an exciting day in the jungle."""

# CONSTANTS
delimiter = ' '
LINE = '-'*40
WELCOME_MSG = 'Welcome to this Modular Madlibs game'
INTRO = 'Choose a story and follow the prompts to see what you end up with.'


# input stuff
# creates a list with the required input from the user in the proper order as in the story string
def word_input(found_words):
    fills = []

    for i in found_words:
        if i == '(adj)':
            user_adj = input("Enter an Adjective: ")
            fills.append(user_adj)
        elif i == '(noun)':
            user_noun = input("Enter a Noun: ")
            fills.append(user_noun)
        elif i == '(verb)':
            user_verb = input("Enter an Verb: ")
            fills.append(user_verb)
    return fills


# fills the user input into their respective positions in the story
def word_replace(found_words, filled_words, story_split):
    counter = 0
    for word in story_split:
        if word in found_words:
            story_split[story_split.index(word)] = filled_words[counter]
            counter += 1
    return story_split


# re joins the formerly split story string
def join_story(split_story):
    new_story = delimiter.join(split_story)
    return new_story


def main():
    # setup stuff
    print(LINE)
    print(WELCOME_MSG)
    print(INTRO)
    print(LINE)

    # regex search through story string for nouns, verbs and adjectives
    wordsRe = re.compile(r'\(adj\)|\(noun\)|\(verb\)')
    fnd_words = wordsRe.findall(story)

    # split story to be able to replace individual list/string elems with user input
    story_split = story.split()

    # creates a list with the required input from the user in the proper order as in the story string
    filld_words = word_input(fnd_words)

    # fills the user input into their respective positions in the story
    new_story_data = word_replace(fnd_words, filld_words, story_split)

    # re joins the formerly split story string
    new_story = join_story(new_story_data)

    print(new_story)


main()

#
# words to quickly test program = ['dnsk', 'sgre', 'fdsf', 'sdf', 'fsd', 'acsd', 'saf', 'dsf', 'rger', 'nyt',
# 'myuyh', 'eafe', 'mtyr', 'ny5t', 'efj4rj']
