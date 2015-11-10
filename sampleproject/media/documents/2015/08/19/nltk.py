import nltk
import csv

def leaves(tree):
    """Finds NP (nounphrase) leaf nodes of a chunk tree."""
    for subtree in tree.subtrees(filter = lambda t: t.label()=='NP'):
        print(subtree.leaves)
        yield subtree.leaves()


def get_terms(tree):
    for leaf in leaves(tree):
        term = leaf
        print(term)
        yield term


# nltk.download('punkt')
# nltk.download('maxent_treebank_pos_tagger');
# nltk.download('maxent_ne_chunker');
# nltk.download('words')

sentence = "I went to New York with John Smith and went to London";
tokens = nltk.word_tokenize(sentence)
# print(tokens)
pos_tags = nltk.pos_tag(tokens)
print(pos_tags)
length= len(pos_tags)

namedEnt = nltk.ne_chunk(pos_tags)
print(namedEnt)

pattern = "NP:  {<NNP>+}"

NPChunker = nltk.RegexpParser(pattern)
result = NPChunker .parse(pos_tags)
print(result)


print(get_terms(result));
