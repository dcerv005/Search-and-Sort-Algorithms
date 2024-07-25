#Question 1
from flask import Flask


app = Flask(__name__)
 


@app.route("/")

def movieTitleSearch():
    movie_titles=[ "The Art of Coding", 
    "Exploring the Cosmos",
    "Cooking Masterclass: Italian Cuisine",
    "History Uncovered: Ancient Civilizations",
    "Fitness Fundamentals: Strength Training",
    "Digital Photography Essentials",
    "Financial Planning for Beginners",
    "Nature's Wonders: National Geographic",
    "Artificial Intelligence Revolution",
    "Travel Diaries: Discovering Europe"
    ]
    movie_titles= sorted(movie_titles.copy())
    movie=input("Which movie are you looking for? ")
    low = 0
    high = len(movie_titles)-1

    while low <= high:
        mid = (low+high)//2
        if movie_titles[mid] == movie:
            return f"Movie: {movie} is on the list of movies."
        elif movie_titles[mid] < movie:
            low = mid+1
        else:
            high=mid-1
    return f"Movie: {movie} is not on the list of movies."

@app.route("/sortedlist")
def sortedMovieList(movie_titles=[ "The Art of Coding", 
    "Exploring the Cosmos",
    "Cooking Masterclass: Italian Cuisine",
    "History Uncovered: Ancient Civilizations",
    "Fitness Fundamentals: Strength Training",
    "Digital Photography Essentials",
    "Financial Planning for Beginners",
    "Nature's Wonders: National Geographic",
    "Artificial Intelligence Revolution",
    "Travel Diaries: Discovering Europe"
    ]):
    
    if len(movie_titles) > 1:
        mid = len(movie_titles) // 2
        left_half = movie_titles[:mid]
        right_half = movie_titles[mid:]

        sortedMovieList(left_half)
        sortedMovieList(right_half)

        i=j=k=0

        while i<len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                movie_titles[k] = left_half[i]
                i+=1
            else: 
                movie_titles[k] = right_half[i]
                j+=1
            k += 1
        while i < len(left_half):
            movie_titles[k] = left_half[i]
            i += 1
            j += 1

        while j < len(right_half):
            movie_titles[k] = right_half[j]
            j += 1
            k += 1

    return movie_titles
 
if __name__ == '__main__':  
   app.run(debug=True)