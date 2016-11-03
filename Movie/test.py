#!/usr/bin/python

def main():
    movie_data = {
        "movie": [{
            "Name": "prisoners",
            "Title": "Prisoners",
            "Plot": "A movie about prisoners",
            "Poster": "https://upload.wikimedia.org/wikipedia/en/6/63/Prisoners2013Poster.jpg",
            "Trailer": "https://www.youtube.com/watch?v=bpXfcTF6iVk"
            },
        {
            "Name": "blue_ruin",
            "Title": "Blue Ruin",
            "Plot": "A mysterious outsider's quiet life is turned upside down when he returns to his childhood home to carry out an act of vengeance.",
            "Poster": "https://upload.wikimedia.org/wikipedia/en/9/9f/Blue_Ruin_film_poster.jpg",
            "Trailer": "https://www.youtube.com/watch?v=N9z47Ji0qIk"
            },
        {
            "Name": "kill_list",
            "Title": "Kill List",
            "Plot": "Nearly a year after a botched job, a hitman takes a new assignment with the promise of a big payoff for three killings. What starts off as an easy task soon unravels, sending the killer into the heart of darkness.",
            "Poster": "https://upload.wikimedia.org/wikipedia/en/7/78/Kill-list-poster.jpg",
            "Trailer": "https://www.youtube.com/watch?v=0mkRcuUgLrQ"
        }
    ]
    }

    for obj in movie_data['movie']:
        print obj['Poster']

if __name__ == '__main__':
    main()
