from django.shortcuts import render
from django.http import HttpResponse
from datetime import date

dummy_posts = [
    {
        "slug": "cooking",
        "image": "cooking.jpg",
        "author": "ChatGPT",
        "date": date(2024, 4, 13),
        "excerpt": "In a whirlwind world of fast food, I've rediscovered the joy of slow cooking from scratch.",
        "title": "Rediscovering the Joy of Cooking: A Culinary Journey",
        "content": """In a fast-paced world filled with instant meals and takeout, there's something truly special about spending time in the kitchen, creating delicious dishes from scratch.
                    
                    Lately, I've found myself drawn back to the art of cooking, not just as a means to satisfy hunger, but as a form of creative expression and self-care.
                    
                    There's a unique satisfaction that comes from chopping fresh ingredients, experimenting with flavors, and watching as a recipe comes together into a beautiful, aromatic masterpiece.
                    
                    Whether it's trying out a new recipe inspired by a recent travel adventure or simply whipping up a comforting classic on a lazy Sunday afternoon, each moment spent in the kitchen feels like a journey of discovery.
                    
                    But it's not just about the end result – it's about the process itself. It's about the sizzle of onions hitting a hot pan, the gentle kneading of dough between your fingers, and the heavenly aroma that fills the air as a dish begins to take shape.
                    
                    It's about taking the time to savor each step, to immerse yourself fully in the experience of cooking. In a world that often feels chaotic and unpredictable, there's a sense of comfort and control that comes from creating something delicious with your own two hands.
                    
                    It's a reminder that even in the midst of uncertainty, there are still moments of joy and beauty to be found – often right in our own kitchens.
                    
                    So here's to embracing the simple pleasure of cooking, to slowing down and savoring each moment, and to rediscovering the joy that comes from nourishing both body and soul with homemade meals made with love.""",
    },
    {
        "slug": "nature",
        "image": "nature.jpg",
        "author": "ChatGPT",
        "date": date(2024, 4, 12),
        "excerpt": "Amidst the chaos of daily life, I've found solace in nature's symphony – from the rustle of leaves to the chirping of birdsong.",
        "title": "Embracing Nature's Symphony: Finding Peace Outdoors",
        "content": """In the hustle and bustle of modern life, it's easy to feel disconnected from the natural world around us. But amidst the chaos, there's a symphony playing – the gentle rustle of leaves in the wind, the chirping of birdsong at dawn, the rhythmic patter of rain on the earth.

                    Lately, I've been making a conscious effort to step outside and immerse myself in nature's melody, finding solace and serenity in the great outdoors. There's a certain magic in the way the sunlight filters through the trees, casting dappled shadows on the forest floor.

                    It's a reminder of the beauty and wonder that surrounds us, if only we take the time to look. Whether it's a leisurely stroll through a nearby park or a challenging hike up a rugged mountainside, each moment spent in nature is an opportunity to reconnect with the world around us and find peace amidst the chaos.

                    But it's not just about escaping the noise of the city – it's about embracing the symphony of nature in all its forms. It's about listening to the whispers of the wind as it dances through the trees, feeling the warmth of the sun on your skin, and marveling at the intricate beauty of a single wildflower in bloom.

                    In a world that often feels overwhelming and chaotic, nature offers a sanctuary – a place where we can find refuge from the stresses of everyday life and rediscover a sense of inner calm.

                    So here's to embracing nature's symphony, to finding peace in the great outdoors, and to savoring each moment spent beneath the open sky.""",
    },
    {
        "slug": "cosmos",
        "image": "cosmos.jpg",
        "author": "ChatGPT",
        "date": date(2024, 4, 11),
        "excerpt": "Beneath the starry expanse of night, I've discovered a universe brimming with stories and mysteries.",
        "title": "Exploring the Cosmos: A Stargazer's Odyssey",
        "content": """In the quiet of the night, under the canopy of stars, lies a vast and mysterious universe waiting to be explored. With each twinkle in the sky comes a story, a journey through time and space that captivates the imagination and ignites a sense of wonder.

                    Lately, I've found myself drawn to the heavens above, seeking solace and inspiration in the beauty of the cosmos. There's a certain magic in the way the stars shimmer against the velvet backdrop of the night sky, beckoning us to gaze upwards and ponder the mysteries of the universe.

                    Whether it's tracing the constellations with a telescope or simply lying on a blanket and marveling at the sheer magnitude of it all, each moment spent stargazing is an adventure in itself. But it's not just about the celestial sights – it's about the sense of awe and reverence that comes from contemplating our place in the cosmos.

                    It's about realizing that we are but a small part of something much greater than ourselves, and finding comfort in the knowledge that we are connected to the stars in ways we may never fully understand. In a world that often feels chaotic and uncertain, the night sky offers a sense of perspective – a reminder that we are part of something grand and beautiful, even in our darkest moments.

                    So here's to exploring the cosmos, to seeking inspiration in the stars, and to finding joy in the endless expanse of the universe.""",
    },
    {
        "slug": "creativity",
        "image": "creativity.jpg",
        "author": "ChatGPT",
        "date": date(2024, 4, 10),
        "excerpt": "Within our minds lies a spark of creativity, urging expression through words, colors, or melodies.",
        "title": "Cultivating Creativity: Nurturing the Artist Within",
        "content": """In the quiet corners of our minds lies a spark of creativity waiting to be ignited. It's the force that drives us to express ourselves, to paint with words, colors, or melodies.

                    Lately, I've been on a journey to cultivate this inner artist, to embrace the freedom of creation and explore the depths of imagination. There's a certain joy in the act of creation, whether it's through writing, drawing, or making music.

                    It's a process of discovery, of tapping into something greater than ourselves and allowing it to flow freely onto the canvas of our lives. Whether it's sketching in a notebook, improvising on a musical instrument, or crafting a story from the depths of our imagination, each moment spent in creative pursuit is an opportunity to connect with our true selves and unlock the boundless potential of the human spirit.

                    But it's not just about the end result – it's about the journey of self-discovery that comes with it. It's about embracing imperfection, letting go of fear, and allowing ourselves to be vulnerable in the pursuit of our artistic vision.

                    In a world that often values productivity over creativity, nurturing our inner artist is an act of rebellion – a declaration of our inherent worth and our capacity to create beauty in a world that sorely needs it.

                    So here's to cultivating creativity, to embracing the artist within, and to celebrating the unique gifts that each of us brings to the world.""",
    },
    {
        "slug": "magic",
        "image": "magic.jpg",
        "author": "ChatGPT",
        "date": date(2024, 4, 9),
        "excerpt": "In life's rush, simple joys await - from morning coffee to shared laughter.",
        "title": "Savoring Simple Joys: Embracing Everyday Magic",
        "content": """Amid the rush of daily life, there's a treasure trove of simple joys waiting to be discovered. From the first sip of morning coffee to the laughter shared with loved ones, these moments of everyday magic are the true essence of happiness.

                    Lately, I've been making a conscious effort to slow down and savor these small pleasures, finding beauty in the ordinary and gratitude in the mundane. There's a certain warmth in the glow of candlelight on a cozy evening at home, a sense of peace in the quiet moments spent lost in a good book, and a feeling of contentment in the simple act of sharing a meal with family and friends.

                    Whether it's watching the sunrise from my window or taking a leisurely stroll through the park, each day is filled with opportunities to embrace the beauty of life's simple pleasures. But it's not just about the experiences themselves – it's about the mindset we bring to them.

                    It's about cultivating a sense of mindfulness and gratitude, and finding joy in the present moment, no matter how ordinary it may seem. In a world that often feels overwhelming and chaotic, savoring these simple joys is a powerful reminder that happiness can be found in the here and now.

                    So here's to embracing the magic of everyday life, to finding joy in the little things, and to savoring each moment with an open heart and grateful spirit.""",
    },
]


def get_date(post):
    return post["date"]


def starting_page(request):
    sorted_posts = sorted(dummy_posts, key=get_date)
    latest_post = sorted_posts[:3]
    return render(request, "blog/index.html", {"posts": latest_post})


def posts(request):
    return render(request, "blog/all-posts.html", {"all_posts": dummy_posts})


def post_detail(request, slug):
    post = next(post for post in dummy_posts if post["slug"] == slug)
    return render(request, "blog/post-detail.html", {"post": post})