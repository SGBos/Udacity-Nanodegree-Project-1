import media
import fresh_tomatoes

AVATAR = media.Movie(
	"AVATAR",
    """A Paraplegic Marine dispatched to the moon Pandora on a unique mission becomes torn
    between following his orders and protecting the world he feels is his home.""",
    "http://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
    "https://www.youtube.com/watch?v=cRdxXPV9GNQ"
)


FURY = media.Movie(
	"FURY",
    """A battle-hardened Army
    sergeant named Wardaddy commands a Sherman tank and his five-man crew
     on a deadly mission behind enemy lines.""",
    "http://upload.wikimedia.org/wikipedia/en/1/17/Fury_2014_poster.jpg",
    "https://www.youtube.com/watch?v=-OGvZoIrXpg"
)


MATRIX = media.Movie(
	"THE MATRIX",
    """A computer hacker learns from mysterious rebels about the true nature of his
    reality and his role in the war against its controllers.""",
    "http://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg",
    "https://www.youtube.com/watch?v=m8e-FF8MsqU"
)


GODFATHER = media.Movie(
	"THE GODFATHER",
    """The aging patriarch of an organized crime dynasty transfers control
     of his clandestine empire to his reluctant son.""",
    "http://upload.wikimedia.org/wikipedia/en/1/1c/Godfather_ver1.jpg",
    "https://www.youtube.com/watch?v=sY1S34973zA"
)


CHARIOTS = media.Movie(
	"CHARIOTS OF FIRE",
    """Two British track athletes, one a determined Jew and the other
     a devout Christian, compete in the 1924 Olympics.""",
    "http://upload.wikimedia.org/wikipedia/en/b/b5/Chariots_of_fire.jpg",
    "https://www.youtube.com/watch?v=QKHPm3BSba8"
)


MAD_MAX = media.Movie(
	"MAD MAX",
    """In a stark desert landscape where humanity is broken, two
     rebels just might be able to restore order.""",
    "http://upload.wikimedia.org/wikipedia/en/2/23/Max_Mad_Fury_Road_Newest_Poster.jpg",
    "https://www.youtube.com/watch?v=YWNWi-ZWL3c"
)


BRAVEHEART = media.Movie(
	"BRAVEHEART",
    """William Wallace begins a revolt and leads Scottish warriors against the
     cruel English tyrant who rules Scotland with an iron fist.""",
    "http://upload.wikimedia.org/wikipedia/en/5/55/Braveheart_imp.jpg",
    "https://www.youtube.com/watch?v=j53_WxqPZ7c"
)


FIGHT_CLUB = media.Movie(
	"FIGHT CLUB",
    """An insomniac office worker looking for a way to change his life crosses paths with a
     devil-may-care soap maker and they form an underground fight club.""",
    "http://upload.wikimedia.org/wikipedia/en/f/fc/Fight_Club_poster.jpg",
    "https://www.youtube.com/watch?v=J8FRBYOFu2w"
)


INCEPTION = media.Movie(
	"INCEPTION",
    """A thief who steals corporate secrets through use of dream-sharing technology is given
    the inverse task of planting an idea into the mind of a CEO.""",
    "http://upload.wikimedia.org/wikipedia/en/7/7f/Inception_ver3.jpg",
    "https://www.youtube.com/watch?v=66TuSJo4dZM"
)


DARK_KNIGHT = media.Movie(
	"THE DARK KNIGHT",
    """The caped crusader must come to terms with one of the greatest
     psychological tests of his ability to fight injustice.""",
    "http://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg",
    "https://www.youtube.com/watch?v=yQ5U8suTUw0"
)


WALL_STREET = media.Movie(
	"WALL STREET",
    """Gordon Gekko works his future son-in-law, an idealistic stock broker,
    when he sees an opportunity to take down a Wall Street enemy and rebuild his empire.""",
    "http://upload.wikimedia.org/wikipedia/en/c/c8/Wall_Street-_Money_Never_Sleeps_film.jpg",
    "https://www.youtube.com/watch?v=5w4VKhjllzs"
)


TOY_STORY = media.Movie(
	"TOY STORY",
    """A cowboy doll is profoundly threatened and jealous when a
     new spaceman figure supplants him as top toy in a boy's room.""",
    "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
    "https://www.youtube.com/watch?v=KYz2wyBy3kc"
)


GLADIATOR = media.Movie(
	"GLADIATOR",
    """When a Roman general is betrayed and his family murdered by an emperor's corrupt son, he
    comes to Rome as a gladiator to seek revenge.""",
    "http://upload.wikimedia.org/wikipedia/en/8/8d/Gladiator_ver1.jpg",
    "https://www.youtube.com/watch?v=owK1qxDselE"
)


GREEN_MILE = media.Movie(
	"THE GREEN MILE",
    "The lives of guards on Death Row are affected by one of their charges.",
    "http://upload.wikimedia.org/wikipedia/en/c/ce/Green_mile.jpg",
    "https://www.youtube.com/watch?v=uDybmxbKf4Y"
)


DEPARTED = media.Movie(
	"THE DEPARTED",
    """An undercover cop and a mole in the police attempt to identify
     each other while infiltrating an Irish gang in South Boston.""",
    "http://upload.wikimedia.org/wikipedia/en/5/50/Departed234.jpg",
    "https://www.youtube.com/watch?v=SGWvwjZ0eDc"
)


APOCALYPSE = media.Movie(
	"APOCALYPSE NOW",
    """Captain Willard is sent on a dangerous mission into Cambodia to assassinate
     a renegade colonel who has set himself up as a god among a local tribe.""",
    "http://upload.wikimedia.org/wikipedia/en/c/c2/Apocalypse_Now_poster.jpg",
    "https://www.youtube.com/watch?v=IkrhkUeDCdQ"
    )



MOVIES = [
    AVATAR, FURY, MATRIX, GODFATHER, WALL_STREET, MAD_MAX, BRAVEHEART, FIGHT_CLUB, INCEPTION,
    DARK_KNIGHT, TOY_STORY, CHARIOTS, GLADIATOR, GREEN_MILE, DEPARTED, APOCALYPSE
    ]


fresh_tomatoes.open_movies_page(MOVIES)
