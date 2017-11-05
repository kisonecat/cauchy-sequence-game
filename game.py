import re
import hashlib
import readline
import random
import sys
from gensim.models import Word2Vec
from colorama import init, Fore, Back, Style
init()

def to_canonical(word):
    if (len(word.split(' ')) > 1):
        return re.sub("^","DBPEDIA_ID/",re.sub(" ","_",word))
    return word
    
def from_canonical(word):
    if re.match("^DBPEDIA_ID", word):
        return re.sub("_"," ",re.sub("^DBPEDIA_ID/","",word))
    return word

################################################################
print("Loading model... (this takes a moment)... ", end="")
sys.stdout.flush()
model = Word2Vec.load("en.model")
print("Done!")

yours = None
mine = None
already_said = []

################################################################
def random_line(afile):
    line = next(afile)
    for num, aline in enumerate(afile):
      if random.randrange(num + 2): continue
      line = aline
    return line

# pick words from the system dictionary which I know and which are
# lowercase; there are lots of weird words in the model, so this
# ensures that we are only starting with words that the player is
# likely to know
while (mine == None) or (not (mine in model.wv.vocab)) or (not re.match('^[a-z]*', mine)):
    mine = from_canonical(random_line(open("/usr/share/dict/american-english")).strip())

################################################################
round = 1

while True:
    print()
    print(Fore.RED + "Round",round)
    print(Style.RESET_ALL)

    # Commit to say a specific word
    h = hashlib.sha1(mine.encode('utf-8')).hexdigest()
    print(Fore.BLUE + "    I will say a word with sha1 =", h,Style.RESET_ALL)

    # The player can say any word that I know which hasn't been said previously
    while True:
        yours = input('  You say ')
        if not to_canonical(yours) in model.wv.vocab:
            print("  I don't know '" + yours + "'.  Try something else.")
        else:
            if (yours in already_said):
                print("  That word has already been said!")
            else:
                break

    print("    I say",mine)
    
    if mine == yours:
        print(Fore.GREEN + "\nWe win!  We win!",Style.RESET_ALL)
        break
    
    print(Fore.BLUE + " ...I'm thinking..." + Style.RESET_ALL)
    
    # Find a word that I haven't said but is similar to the words we just said
    already_said.append( mine )
    already_said.append( yours )
          
    acceptable = [pair[0] for pair in model.most_similar(positive=[to_canonical(mine),to_canonical(yours)]) if not (from_canonical(pair[0]) in already_said)]
          
    if len(acceptable) == 0:
        print(" I can't think of anything!")
        break
    mine = from_canonical(acceptable[0])
          
    round = round + 1
    
