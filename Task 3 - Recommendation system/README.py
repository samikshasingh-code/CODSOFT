Movie Recommendation System
This project is a movie recommendation system developed using Python. It uses collaborative filtering techniques to recommend movies based on user ratings. The project is split into two main scripts:
main.py – Preprocessing and backend logic for collaborative filtering
collaborative.py – GUI-based movie recommender that interacts with the user

Requirements
Install the required Python libraries before running the project
pip install pandas scikit-learn tkinter

File Descriptions
1. main.py – Preprocessing and Collaborative Filtering Logic
Loads movies.csv and ratings.csv
Merges and processes the data
Applies TF-IDF on movie genres (used for similarity)
Calculates cosine similarity between movies
Returns top 10 recommended movies for a given movie

2. collaborative.py – GUI-Based Collaborative Filtering
Tkinter-based GUI application
Allows users to:

Select a movie
Rate it
Get movie recommendations
Save ratings and recommendations

GUI Features:
Dropdown to select a movie
Input box to rate the movie
Button to get similar movie recommendations
Options to save results and exit

 Dataset
movies.csv: Contains movie ID and title
ratings.csv: Contains user IDs, movie IDs, and ratings
Both files must be present in the project directory.

