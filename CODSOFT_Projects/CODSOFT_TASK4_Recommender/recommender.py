"""
CodSoft AI Internship - Task 4: Movie Recommendation System
Content-based filtering: movies are described by genres/keywords,
and similarity is measured with cosine similarity.
No external libraries needed.
"""
import math

MOVIES = {
    "3 Idiots": ["comedy", "drama", "college", "friendship", "inspirational"],
    "Dangal": ["drama", "sports", "family", "inspirational", "biography"],
    "Chak De India": ["drama", "sports", "inspirational", "team"],
    "Bhaag Milkha Bhaag": ["drama", "sports", "biography", "inspirational"],
    "Zindagi Na Milegi Dobara": ["comedy", "drama", "friendship", "travel"],
    "Dil Chahta Hai": ["comedy", "drama", "friendship", "romance"],
    "Kabir Singh": ["drama", "romance"],
    "Jab We Met": ["romance", "comedy", "travel", "drama"],
    "Queen": ["comedy", "drama", "travel", "inspirational"],
    "Sholay": ["action", "adventure", "friendship", "drama"],
    "War": ["action", "thriller", "spy"],
    "Pathaan": ["action", "thriller", "spy"],
    "Baby": ["action", "thriller", "spy", "patriotic"],
    "Uri": ["action", "war", "patriotic", "thriller"],
    "Drishyam": ["thriller", "crime", "family", "mystery"],
    "Andhadhun": ["thriller", "crime", "mystery", "comedy"],
    "Kahaani": ["thriller", "mystery", "crime"],
    "Stree": ["comedy", "horror", "mystery"],
    "Bhool Bhulaiyaa": ["comedy", "horror", "mystery"],
    "PK": ["comedy", "drama", "sci-fi", "satire"],
    "Koi... Mil Gaya": ["sci-fi", "family", "drama"],
    "Krrish": ["sci-fi", "action", "family", "superhero"],
    "Interstellar": ["sci-fi", "adventure", "drama", "space"],
    "Inception": ["sci-fi", "thriller", "action", "mystery"],
    "The Dark Knight": ["action", "crime", "thriller", "superhero"],
    "Avengers: Endgame": ["action", "sci-fi", "superhero", "adventure"],
    "Toy Story": ["animation", "comedy", "adventure", "family"],
    "The Lion King": ["animation", "drama", "adventure", "family"],
}


def build_vocab(movies):
    return sorted({tag for tags in movies.values() for tag in tags})


def to_vector(tags, vocab):
    return [1 if v in tags else 0 for v in vocab]


def cosine_similarity(a, b):
    dot = sum(x * y for x, y in zip(a, b))
    na = math.sqrt(sum(x * x for x in a))
    nb = math.sqrt(sum(y * y for y in b))
    return dot / (na * nb) if na and nb else 0.0


VOCAB = build_vocab(MOVIES)
VECTORS = {title: to_vector(tags, VOCAB) for title, tags in MOVIES.items()}


def recommend_by_movie(title, n=5):
    """Recommend movies similar to a movie the user liked."""
    key = next((t for t in MOVIES if t.lower() == title.lower().strip()), None)
    if key is None:
        return None
    scores = [(t, cosine_similarity(VECTORS[key], v))
              for t, v in VECTORS.items() if t != key]
    scores.sort(key=lambda x: x[1], reverse=True)
    return scores[:n]


def recommend_by_tags(tags, n=5):
    """Recommend movies matching the genres/keywords the user types."""
    tags = [t.strip().lower() for t in tags if t.strip()]
    user_vec = to_vector(tags, VOCAB)
    if not any(user_vec):
        return []
    scores = [(t, cosine_similarity(user_vec, v)) for t, v in VECTORS.items()]
    scores = [s for s in scores if s[1] > 0]
    scores.sort(key=lambda x: x[1], reverse=True)
    return scores[:n]


def show(results):
    if not results:
        print("No recommendations found. Try different input.\n")
        return
    print("\nRecommended for you:")
    for i, (title, score) in enumerate(results, 1):
        print(f"  {i}. {title}  (match: {score * 100:.0f}%)")
    print()


def main():
    print("=== Movie Recommendation System ===")
    while True:
        print("1. Recommend based on a movie I like")
        print("2. Recommend based on genres I like")
        print("3. Show all movies")
        print("4. Exit")
        choice = input("Choose (1-4): ").strip()

        if choice == "1":
            title = input("Enter a movie you like: ")
            res = recommend_by_movie(title)
            if res is None:
                print("Movie not found. Choose option 3 to see the list.\n")
            else:
                show(res)
        elif choice == "2":
            print("Available genres/keywords:", ", ".join(VOCAB))
            tags = input("Enter genres separated by commas (e.g. comedy, thriller): ").split(",")
            show(recommend_by_tags(tags))
        elif choice == "3":
            print()
            for t in MOVIES:
                print(" -", t)
            print()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Please enter 1, 2, 3 or 4.\n")


if __name__ == "__main__":
    main()
