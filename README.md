# The Cauchy Sequence Game

This is a computer partner for the Cauchy Sequence Game.

A javascript version of this game is available at https://github.com/kisonecat/cauchy.quest

## Recorded demos

You can watch a couple short games being played at

  https://asciinema.org/a/t2aKDyS3Q3OL5sqmKGUrNieAn

  https://asciinema.org/a/v6RaGBvgtxrKaNZ62e131uEHF

or a longer game at

  https://asciinema.org/a/cPiPD0ciqjQ9ngU3PVy8T0Ez5

## Rules of the game

The goal of the game is to say the same word at the same time.

In each round, the two players say a word outloud.  They may not say a
word that either player has said previously.  Ideally, the word that
they say is "related" (somehow!) to the previous pair of words said.
In this way, the players are saying words which move closer to each
other, until they finally say the same word at the same time.

## word2vec

The code in `game.py` depends on a gensim model stored in `en.model`
and a list of words stored in `/usr/share/dict/american-english`.  The
code is designed to account for some vocabulary items being in the
DBPEDIA form.
