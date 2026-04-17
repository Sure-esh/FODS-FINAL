'''
Program to store movie details in dictionary
Asks for 3 movies: title, director, release year, rating
Displays information in well-formatted manner
'''

# Main program
print("="*60)
print("MOVIE INFORMATION STORAGE")
print("="*60)

# Dictionary to store movies
movies = {}

# Input for 3 movies
for i in range(1, 4):
    print(f"\nMovie {i}:")
    title = input("  Enter movie title: ")
    director = input("  Enter director name: ")
    year = input("  Enter release year: ")
    rating = float(input("  Enter rating (0-10): "))
    
    # Store in dictionary
    movies[title] = {
        "director": director,
        "year": year,
        "rating": rating
    }

# Display all movie information
print("\n" + "="*60)
print("MOVIE INFORMATION")
print("="*60)

for movie_title, details in movies.items():
    print(f"\n📽️  {movie_title}")
    print(f"   Director:     {details['director']}")
    print(f"   Release Year: {details['year']}")
    print(f"   Rating:       {details['rating']}/10")

print("\n" + "="*60)
