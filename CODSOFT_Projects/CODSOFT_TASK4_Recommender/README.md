# CODSOFT Task 4 - Movie Recommendation System

A content-based recommender. Each movie is described by genre/keyword tags,
turned into a vector, and compared using cosine similarity.

## Run
```
python recommender.py
```

## Try
- Option 1 -> `3 Idiots`
- Option 2 -> `comedy, thriller`

## How it works
1. Build a vocabulary of all tags.
2. Convert each movie into a 0/1 vector.
3. Cosine similarity between vectors = how alike two movies are.
4. Return the top 5 highest scores.
