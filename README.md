Generate misspelled words and word variations as YAML for espanso
The goal of this application is to be able to take any local file and transform it into a dictionary of possible word misspellings.
Instead of copying the entire dictionary (thus creating tons of uneccessary word combiniations), this app will only generate mispellings of the words that you directly use, reflecting your specific langauges
This application is language-agnostic - English, German, Italian, French, Spanish, just to name a few!

## Use Cases:

    - grab words from .bash_history, correct common mispellings on the command line
    - grab words from markdown docs, correcting common mispellings of unusual words in technical documentation
    -

Output needs to look like:

```yaml
matches:
  - trigger: announcment
    replace: announcement
    propagate_case: true
    word: true
  - trigger: maanagement
    replace: management
    propagate_case: true
    word: true
```

In general, looks like:

```yaml
matches:
  - trigger: { { MISPELLED WORD } }
    replace: { { CORRECT WORD } }
    propagate_case: true
    word: true
```

## Step 1: get word list

Read words from file
Remove punctuation
Filter out unique words

> Requires manual verification that words are correctly spelled

Sanitize mispellings if they collide with existing words (ex: 'there' mispelled as 'here', which collides with the actual word 'here')

Put words into array (or temp file)

## Step 2: init output file

echo 'matches:' > incremental.yml

## Step 3: Generate mispellings and append to output

For each word:

- create new results array
  - for each letter
    - remove that letter and add mispelled word to results
      - append to results
    - also swap all adjacent letters from word, append each mispelling to results
      - append to results
- remove duplicates in results
- for each word in results:
  - append to incremental.yml as:

```
  - trigger: {{mispelled_word}}
    replace: {{original_word}}
    propagate_case: true
    word: true
```

## Step 5: get espanso config dir

ESPANSO_CONFIG
ESPANSO_CONFIG=$(espanso path | grep Config)
Check that espanso is installed

- if ESPANSO_CONFIG contains like 'not found', throw error
  espanso_path = ESPANSO_CONFIG.split(':')[0].strip()
  print(espanso_path)

## Step 6: Copy output file to espanso_path/match

## Feature roadmap:

- [] remove duplicates after generating all mispellings
- [] generate more advanced misspellings

  - [] bump multiple letters around (ex: annoucmemnet, both e's have been swapped to the right)
  - [] bump letters around further (ex: annoucenment, n has been shifted right by 2)
  - [] generate mispellings by removing multiple vowels
  - [] generate mispellings of letter pairs (ex: spuppport)
  - [] handle mispellings from extra keystrokes (ex: storrage, spuport)

- [] ML approach: query LLM for variety of common mispellings
