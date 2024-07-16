# Natural Language Processing (NLP)

Natural Language Processing (NLP) is a field of artificial intelligence that focuses on the interaction between computers and humans through natural language. The goal is to enable computers to understand, interpret, and generate human language in a way that is both meaningful and useful.

## Key Concepts

### Tokenization
Tokenization is the process of breaking down text into smaller units called tokens, which can be words, subwords, or characters.

- **Word Tokenization:** Splitting text into words.
- **Sentence Tokenization:** Splitting text into sentences.
- **Subword Tokenization:** Splitting words into smaller units (useful for handling out-of-vocabulary words).

### Lemmatization and Stemming
- **Lemmatization:** Reducing words to their base or root form (lemma), considering the context.
- **Stemming:** Reducing words to their root form by removing suffixes, without considering the context.

### Stop Words
Stop words are common words (e.g., "and", "the", "is") that are often removed from text before processing because they do not carry significant meaning.

### Part-of-Speech (POS) Tagging
POS tagging involves assigning parts of speech (e.g., noun, verb, adjective) to each token in a text.

### Named Entity Recognition (NER)
NER is the process of identifying and classifying named entities (e.g., person names, locations, organizations) in text.

### N-grams
N-grams are contiguous sequences of N items (e.g., words, characters) from a given text.

- **Unigrams:** Single words.
- **Bigrams:** Pairs of consecutive words.
- **Trigrams:** Triplets of consecutive words.

## Common NLP Tasks

### Text Classification
Text classification involves assigning predefined categories to text documents. Common approaches include:

- **Bag of Words (BoW):** Representing text as a set of word frequencies.
- **TF-IDF (Term Frequency-Inverse Document Frequency):** Weighing words by their frequency and rarity.
- **Word Embeddings:** Representing words as dense vectors (e.g., Word2Vec, GloVe).

### Sentiment Analysis
Sentiment analysis is the process of determining the sentiment or emotional tone of a text (e.g., positive, negative, neutral).

### Machine Translation
Machine translation involves automatically translating text from one language to another.

- **Sequence-to-Sequence Models:** Models that take a sequence of words in the source language and output a sequence of words in the target language (e.g., using LSTM, GRU).
- **Transformer Models:** Advanced models that use self-attention mechanisms to handle long-range dependencies (e.g., BERT, GPT).

### Text Summarization
Text summarization involves creating a concise summary of a longer text.

- **Extractive Summarization:** Selecting key sentences from the original text.
- **Abstr
