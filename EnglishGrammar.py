from parsimonious import Grammar
grammar1=Grammar(
    """ 
    sentence= (pron space verb space noun mark) / (pron space verb space noun space preposition space noun mark) / (pron space adverb space verb space noun mark) / (pron space verb space pron space noun mark) / (pron space verb space pron mark)

    pron= "i" / "they" / "who" / "themselves" / "each other" / "my" / "we" / "you"
    verb= "love" / "like" / "show" / "act" / "persuade" / "tolerate" / "exist" / "want" / "chase" / "watch" / "wear" / "care" / "stare" / "think" / "judge" / "call"
    noun= "python" / "steak" / "food" / "coffee" / "animals" / "cats" / "dogs"/ "money" / "movies" / "tv" / "pets" / "burgers" / "chicken" / "people" / "friends" / "eggs"
    preposition= "aboard" / "about" / "across" / "after" / "down" / "near" / "to" / "in" / "straight" / "behind" / "with" / "and"
    adjective= "blue"/ "pink" / "little" / "red" / "square" / "triangular" / "short" / "tall" / "big" / "little" / "bad" / "good" / "neutral" 
    article= "a" / "an" / "the"
    space=' '
    adverb = "angrily" / "anxiously" / "badly" / "correctly" / "eagerly" / "hardly"
    mark= "." / "!" / "?"

    """
)

