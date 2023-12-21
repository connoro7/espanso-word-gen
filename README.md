# Genspanso

Generate misspellings and word variations from any file and output as .yaml for Espanso!

The goal of this application is to be able to take any local file and transform it into a dictionary of possible word misspellings.
Instead of using the entire dictionary (thus creating tons of uneccessary word combiniations), this app will only generate mispellings of the words that you directly use, reflecting your specific vocabulary, industry terms, and writing style.

<!-- This application is language-agnostic - English, German, Italian, French, Spanish, just to name a few! -->

## Use Cases:

- Grab words from .bash_history, correct common mispellings on the command line
- Grab words from markdown docs, correcting common mispellings of unusual words in technical documentation

In general, Espanso matches look like:

```yaml
matches:
  - trigger: MISPELLED WORD
    replace: CORRECT WORD
    propagate_case: true
    word: true
  - trigger: MISPELLED WORD
    replace: CORRECT WORD
    propagate_case: true
    word: true
  ...
```

## Feature roadmap:

- [x] remove duplicates after generating all mispellings
  - [] generate more advanced misspellings
  - [x] bump single letters around (ex: annouecment)
- [x] remove single letters (ex: annoucment)
  - [] bump multiple letters around (ex: annoucmemnet, both e's have been swapped to the right)
  - [] bump letters around further (ex: annoucenment, n has been shifted right by 2)
  - [] generate mispellings by removing multiple vowels (ex: annoucmnt)
  - [] generate mispellings of letter pairs (ex: ammouncement)
  - [] handle mispellings from extra keystrokes (ex: annnoucement)
- [] remember previously generated words, skip them (or overwrite)
  - [] add option to append to existing yaml file
  - [] ML approach: query LLM for variety of common mispellings

## v1.x MVP Features:

- [x] Get words from files (.txt, .md, .sh), process them
- [x] From processed word list, generate misspellings
- [x] Output .yaml file for Espanso consumption

## Step 5: get espanso config dir

ESPANSO_CONFIG=$(espanso path | grep Config)
Check that espanso is installed

- if ESPANSO_CONFIG contains like 'not found', throw error
  espanso_path = ESPANSO_CONFIG.split(':')[0].strip()
  print(espanso_path)

## Step 6: Copy output file to espanso_path/match
