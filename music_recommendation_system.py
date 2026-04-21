import json
import os
import random

FILE_NAME = "songs.json"


default_songs = [
    {
        "title": "Blinding Lights",
        "artist": "The Weeknd",
        "genre": "pop",
        "mood": "energetic",
        "language": "english",
        "year": 2020
    },
    {
        "title": "Perfect",
        "artist": "Ed Sheeran",
        "genre": "pop",
        "mood": "calm",
        "language": "english",
        "year": 2017
    },
    {
        "title": "God's Menu",
        "artist": "Stray Kids",
        "genre": "kpop",
        "mood": "energetic",
        "language": "korean",
        "year": 2020
    },
    {
        "title": "MANIAC",
        "artist": "Stray Kids",
        "genre": "kpop",
        "mood": "dark",
        "language": "korean",
        "year": 2022
    },
    {
        "title": "Magic",
        "artist": "TXT",
        "genre": "kpop",
        "mood": "happy",
        "language": "english",
        "year": 2021
    },
    {
        "title": "Anti-Romantic",
        "artist": "TXT",
        "genre": "kpop",
        "mood": "sad",
        "language": "korean",
        "year": 2021
    },
    {
        "title": "Someone Like You",
        "artist": "Adele",
        "genre": "pop",
        "mood": "sad",
        "language": "english",
        "year": 2011
    },
    {
        "title": "Believer",
        "artist": "Imagine Dragons",
        "genre": "rock",
        "mood": "energetic",
        "language": "english",
        "year": 2017
    },
    {
        "title": "Radioactive",
        "artist": "Imagine Dragons",
        "genre": "rock",
        "mood": "dark",
        "language": "english",
        "year": 2012
    },
    {
        "title": "Stay",
        "artist": "The Kid LAROI & Justin Bieber",
        "genre": "pop",
        "mood": "happy",
        "language": "english",
        "year": 2021
    },
    {
        "title": "Dynamite",
        "artist": "BTS",
        "genre": "kpop",
        "mood": "happy",
        "language": "english",
        "year": 2020
    },
    {
        "title": "Spring Day",
        "artist": "BTS",
        "genre": "kpop",
        "mood": "sad",
        "language": "korean",
        "year": 2017
    }
]


def load_songs():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r", encoding="utf-8") as file:
                songs = json.load(file)
                print("Songs loaded from file.")
                return songs
        except (json.JSONDecodeError, FileNotFoundError):
            print("Error loading file. Default song list loaded.")
            return default_songs.copy()
    else:
        print("File not found. Default song list loaded.")
        return default_songs.copy()


def save_songs(song_list):
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(song_list, file, indent=4, ensure_ascii=False)
    print("Songs saved to file.")


def show_menu():
    print("\n===== MUSIC RECOMMENDATION SYSTEM =====")
    print("1. Show all songs")
    print("2. Get music recommendations")
    print("3. Search by artist")
    print("4. Add a new song")
    print("5. Remove a song")
    print("6. Save songs to file")
    print("7. Exit")


def show_all_songs(song_list):
    if not song_list:
        print("No songs in the database.")
        return

    print("\n===== ALL SONGS =====")
    for index, song in enumerate(song_list, start=1):
        print(
            f"{index}. {song['title']} - {song['artist']} | "
            f"Genre: {song['genre']} | Mood: {song['mood']} | "
            f"Language: {song['language']} | Year: {song['year']}"
        )


def recommend_songs(song_list, genre, mood, language):
    recommendations = []

    for song in song_list:
        if (
            song["genre"] == genre
            and song["mood"] == mood
            and song["language"] == language
        ):
            recommendations.append(song)

    return recommendations


def search_by_artist(song_list, artist_name):
    results = []

    for song in song_list:
        if artist_name.lower() in song["artist"].lower():
            results.append(song)

    return results


def add_song(song_list):
    print("\n===== ADD NEW SONG =====")

    title = input("Enter song title: ").strip()
    artist = input("Enter artist name: ").strip()
    genre = input("Enter genre (pop/rock/kpop): ").strip().lower()
    mood = input("Enter mood (happy/sad/energetic/calm/dark): ").strip().lower()
    language = input("Enter language (english/korean): ").strip().lower()

    while True:
        year_input = input("Enter release year: ").strip()
        if year_input.isdigit():
            year = int(year_input)
            break
        else:
            print("Invalid year. Enter a number.")

    new_song = {
        "title": title,
        "artist": artist,
        "genre": genre,
        "mood": mood,
        "language": language,
        "year": year
    }

    song_list.append(new_song)
    print("Song added successfully.")


def remove_song(song_list):
    if not song_list:
        print("No songs to remove.")
        return

    show_all_songs(song_list)

    while True:
        choice = input("Enter the number of the song to remove: ").strip()

        if choice.isdigit():
            choice = int(choice)

            if 1 <= choice <= len(song_list):
                removed_song = song_list.pop(choice - 1)
                print(f"Removed: {removed_song['title']} - {removed_song['artist']}")
                break
            else:
                print("Invalid number.")
        else:
            print("Enter a valid number.")


def get_user_choice(prompt_text, allowed_values):
    while True:
        user_input = input(prompt_text).strip().lower()

        if user_input in allowed_values:
            return user_input
        else:
            print("Invalid choice. Try again.")
            print("Available options:", ", ".join(allowed_values))


def show_recommendations(recommendations):
    print("\n===== RECOMMENDATIONS =====")
    if recommendations:
        for index, song in enumerate(recommendations, start=1):
            print(
                f"{index}. {song['title']} - {song['artist']} | "
                f"Genre: {song['genre']} | Mood: {song['mood']} | "
                f"Language: {song['language']} | Year: {song['year']}"
            )

        random_choice = input("\nDo you want one random recommendation? (yes/no): ").strip().lower()
        if random_choice == "yes":
            chosen_song = random.choice(recommendations)
            print(
                f"\nRandom recommendation: {chosen_song['title']} - {chosen_song['artist']} "
                f"({chosen_song['year']})"
            )
    else:
        print("No matching songs found.")


def main():
    songs = load_songs()

    while True:
        show_menu()
        choice = input("Choose an option (1-7): ").strip()

        if choice == "1":
            show_all_songs(songs)

        elif choice == "2":
            print("\n===== RECOMMENDATION FORM =====")

            genre = get_user_choice(
                "Choose genre (pop, rock, kpop): ",
                ["pop", "rock", "kpop"]
            )

            mood = get_user_choice(
                "Choose mood (happy, sad, energetic, calm, dark): ",
                ["happy", "sad", "energetic", "calm", "dark"]
            )

            language = get_user_choice(
                "Choose language (english, korean): ",
                ["english", "korean"]
            )

            recommendations = recommend_songs(songs, genre, mood, language)
            show_recommendations(recommendations)

        elif choice == "3":
            artist_name = input("Enter artist name: ").strip()
            results = search_by_artist(songs, artist_name)

            print("\n===== SEARCH RESULTS =====")
            if results:
                for index, song in enumerate(results, start=1):
                    print(
                        f"{index}. {song['title']} - {song['artist']} | "
                        f"Genre: {song['genre']} | Mood: {song['mood']} | "
                        f"Language: {song['language']} | Year: {song['year']}"
                    )
            else:
                print("No songs found for this artist.")

        elif choice == "4":
            add_song(songs)

        elif choice == "5":
            remove_song(songs)

        elif choice == "6":
            save_songs(songs)

        elif choice == "7":
            save_before_exit = input("Do you want to save before exit? (yes/no): ").strip().lower()
            if save_before_exit == "yes":
                save_songs(songs)

            print("Goodbye!")
            break

        else:
            print("Invalid option. Choose a number from 1 to 7.")


main()