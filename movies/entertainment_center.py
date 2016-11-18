import media

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life.",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar",
                        "Dances with Smurfs.",
                        "http://t0.gstatic.com/images?q=tbn:ANd9GcQCfmvrE4fMo2cd8esc7mDZPtFSJThAujddMPkRtti1_ij6u-jp",
                        "https://youtu.be/cRdxXPV9GNQ?t=1m47s")

dark_knight = media.Movie("The Dark Knight",
                        "Batman vs. The Joker.",
                        "http://www.bolegaindia.com/images/gossips/dark_knight_post_1324468213.jpg",
                        "https://youtu.be/EXeTwQWrcwY?t=1m35s")

dark_knight.show_trailer()

