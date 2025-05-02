Movie Recommendation System
Project Description
This project is a Movie Recommendation System that suggests movies to users based on Collaborative Filtering. It uses user ratings to find similar users and predict movies that the user might like, based on the preferences of similar users.

Key Features:
Collaborative Filtering: The system predicts movie ratings and recommends movies based on the ratings given by users with similar preferences.

User Ratings: Users can input their ratings for movies, and the system will update its recommendations.

Graphical User Interface (GUI): The system comes with an easy-to-use GUI where users can interact with the system, input ratings, and receive movie recommendations.

Technologies Used:
Python: The main language used for implementing the recommendation system.

Pandas: For managing and processing the movie and rating data.

scikit-learn: Used for calculating Cosine Similarity for collaborative filtering.

Tkinter: Used to build the graphical user interface (GUI).

CSV Files: For storing movie and rating data (movies.csv and ratings.csv).

Installation
To get started with the project, follow these steps:


1. Install required libraries:
Make sure you have Python installed. You can install the required libraries using pip:

pip install pandas scikit-learn
2. Files Required:
movies.csv: Contains the list of movies with movie titles and movie IDs.

ratings.csv: Contains the ratings data for different movies by users.

Make sure to place these CSV files in the same directory as your Python scripts.

How to Run
Launch the application: Run the following command to start the movie recommendation system:

python main.py
Using the GUI:

Choose a movie from the drop-down list.

Rate the movie on a scale of 1-5.

Click "Show Recommendations" to view the recommended movies.

Optionally, you can save the recommendations to a text file for later viewing or sharing.

Add User Ratings:

When you rate a movie, your rating is saved, and recommendations are recalculated based on your preferences.

Example Usage
Example Recommendation:

If you select the movie "Jumanji (1995)", the system will suggest similar movies such as "Ace Ventura: When Nature Calls (1995)", "Lion King, The (1994)", etc.

Save Recommendations:

The system allows you to save the recommended movies to a text file for later viewing or sharing.
