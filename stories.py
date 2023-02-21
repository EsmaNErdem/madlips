"""Madlibs Stories."""


class Story:
    """Madlibs story.

    To  make a story, pass a list of prompts, and the text
    of the template.

        >>> s = Story(["noun", "verb"],
        ...     "I love to {verb} a good {noun}.")

    To generate text from a story, pass in a dictionary-like thing
    of {prompt: answer, promp:answer):

        >>> ans = {"verb": "eat", "noun": "mango"}
        >>> s.generate(ans)
        'I love to eat a good mango.'
    """

    def __init__(self, identification, title, words, text):
        """Create story with words and template text."""
        self.id = identification
        self.title = title
        self.prompts = words
        self.template = text

    def generate(self, answers):
        """Substitute answers into text."""

        text = self.template

        for (key, val) in answers.items():
            text = text.replace("{" + key + "}", val)

        return text


# Here's a story to get you started


story1 = Story(
    "Onceupon",
    "Tell a Story",
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}."""
)

story2 = Story(
    "Macdonald",
    "Sing a Song",
    ["adjective", "noun", "animal", "noise"],
    """{adjective} Macdonald had a {noun}, E-I-E-I-O
        and on that {noun} he had an {animal}, E-I-E-I-O
        with a {noise} {noise} here
        and a {noise} {noise} there,
        here a {noise}, there a {noise},
        everywhere a {noise} {noise},
        {adjective} Macdonald had a {noun}, E-I-E-I-O."""
)

stories = {story.id: story for story in [story1, story2]}
