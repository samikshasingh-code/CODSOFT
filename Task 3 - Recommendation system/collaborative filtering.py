import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import tkinter as tk
from tkinter import ttk, messagebox, filedialog

# Let's load the movie and ratings data. If the files aren't found, we give a friendly error message.
try:
    movies = pd.read_csv("movies.csv")
    ratings = pd.read_csv("ratings.csv")
except FileNotFoundError:
    print("Oops! Looks like 'movies.csv' and 'ratings.csv' are missing. Please make sure they're in the same folder as the script.")
    exit()

# Time to create a user-item matrix from the ratings data. This will help us recommend movies!
user_item_matrix = ratings.pivot_table(index='userId', columns='movieId', values='rating').fillna(0)

# Now let's calculate the similarity between all the movies. Cosine similarity is a smart way to do this.
cosine_sim_item = cosine_similarity(user_item_matrix.T)
cosine_sim_df = pd.DataFrame(cosine_sim_item, index=user_item_matrix.columns, columns=user_item_matrix.columns)

# Here's the function that recommends movies based on the similarity scores.
def get_item_based_recommendations(movie_title):
    try:
        # Get the movie ID based on the title the user entered
        movie_id = movies[movies['title'] == movie_title].iloc[0]['movieId']
        # Grab the similarity scores for that movie
        sim_scores = cosine_sim_df[movie_id]
        # Sort them in descending order to get the most similar movies at the top
        sim_scores = sim_scores.sort_values(ascending=False)
        # Remove the movie itself from the recommendations list
        sim_scores = sim_scores[sim_scores.index != movie_id]
        # Get the top 10 most similar movie IDs
        recommended_movie_ids = sim_scores.head(10).index
        recommended_movies = movies[movies['movieId'].isin(recommended_movie_ids)]
        
        # Return the titles of the recommended movies
        return recommended_movies['title'].tolist()
    except IndexError:
        return ["Oops! I couldn't find that movie. Please double-check the title and try again."]

# Let's save the user's rating when they submit it
def save_user_rating(movie_title, rating):
    try:
        movie_id = movies[movies['title'] == movie_title].iloc[0]['movieId']
        new_rating = {
            'userId': 9999,  # Let's pretend this is a new user (you can assign unique IDs for real users)
            'movieId': movie_id,
            'rating': rating,
            'timestamp': pd.to_datetime('now').timestamp()
        }
        global ratings
        # Append the new rating to our existing dataset
        ratings = ratings.append(new_rating, ignore_index=True)
        # Save the updated ratings back to the CSV
        ratings.to_csv('ratings.csv', index=False)
        # Recalculate the similarity scores with the updated ratings
        update_user_item_matrix()  
        messagebox.showinfo("Rating Saved", f"Nice! Your rating for {movie_title} has been saved!")
    except IndexError:
        messagebox.showwarning("Error", "Hmm... Movie not found. Please make sure the title is correct.")

# Update the user-item matrix after saving a rating, so recommendations stay fresh!
def update_user_item_matrix():
    global user_item_matrix
    user_item_matrix = ratings.pivot_table(index='userId', columns='movieId', values='rating').fillna(0)
    # Recalculate similarity after the new rating
    global cosine_sim_item, cosine_sim_df
    cosine_sim_item = cosine_similarity(user_item_matrix.T)
    cosine_sim_df = pd.DataFrame(cosine_sim_item, index=user_item_matrix.columns, columns=user_item_matrix.columns)

# GUI setup to display everything
def show_recommendations():
    movie_title = combo.get()
    if not movie_title:
        messagebox.showwarning("Oops!", "Please select a movie from the list first.")
        return
    recommendations = get_item_based_recommendations(movie_title)
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, "\n".join(recommendations))

# Save recommendations to a text file for later reading or sharing
def save_recommendations():
    recommendations = result_text.get(1.0, tk.END).strip().split("\n")
    if not recommendations:
        messagebox.showwarning("Oops!", "There are no recommendations to save yet.")
        return
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, 'w') as f:
            f.write("\n".join(recommendations))
        messagebox.showinfo("Saved", f"Your recommendations have been saved to {file_path}. Enjoy!")

# Main window of the application
root = tk.Tk()
root.title("Movie Recommendation System with Your Ratings")

# Let's give some nice text to guide the user
tk.Label(root, text="Hey there! Choose a movie below to get recommendations.", font=("Arial", 12)).pack(pady=10)

# Dropdown menu for movie selection
movie_titles = sorted(movies['title'].dropna().unique())
combo = ttk.Combobox(root, values=movie_titles, width=50, font=("Arial", 12))
combo.pack(pady=5)

# Rating field: Let the user give a movie a rating from 1 to 5
tk.Label(root, text="How would you rate this movie? (1 to 5)", font=("Arial", 12)).pack(pady=5)
rating_entry = tk.Entry(root, width=50, font=("Arial", 12))
rating_entry.pack(pady=5)

# Buttons for actions
tk.Button(root, text="Show Recommendations", command=show_recommendations, font=("Arial", 12), bg="skyblue").pack(pady=10)
tk.Button(root, text="Save Recommendations", command=save_recommendations, font=("Arial", 12), bg="lightgreen").pack(pady=10)
tk.Button(root, text="Save Your Rating", command=lambda: save_user_rating(combo.get(), float(rating_entry.get())), font=("Arial", 12), bg="lightcoral").pack(pady=10)

# Display the recommendations
result_text = tk.Text(root, height=15, width=60, font=("Arial", 12))
result_text.pack(pady=5)

# Exit button to close the app
tk.Button(root, text="Exit", command=root.quit, font=("Arial", 12), bg="lightcoral").pack(pady=10)

# Run the application
root.mainloop()
