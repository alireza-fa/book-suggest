"""
I use chatgpt for generate test data
"""
from django.core.management import BaseCommand

from apps.book.models import Genre, Author, Book

books = [
    {
        "William Shakespeare": [
            {"title": "Hamlet", "genre": "Tragedy"},
            {"title": "Macbeth", "genre": "Tragedy"},
            {"title": "Romeo and Juliet", "genre": "Tragedy"}
        ]
    },
    {
        "Jane Austen": [
            {"title": "Pride and Prejudice", "genre": "Romance"},
            {"title": "Sense and Sensibility", "genre": "Romance"},
            {"title": "Emma", "genre": "Romance"}
        ]
    },
    {
        "Charles Dickens": [
            {"title": "A Tale of Two Cities", "genre": "Historical Fiction"},
            {"title": "Great Expectations", "genre": "Bildungsroman"},
            {"title": "Oliver Twist", "genre": "Social Novel"}
        ]
    },
    {
        "Mark Twain": [
            {"title": "Adventures of Huckleberry Finn", "genre": "Adventure"},
            {"title": "The Adventures of Tom Sawyer", "genre": "Adventure"},
            {"title": "A Connecticut Yankee in King Arthur's Court", "genre": "Science Fiction"}
        ]
    },
    {
        "Ernest Hemingway": [
            {"title": "The Old Man and the Sea", "genre": "Literary Fiction"},
            {"title": "A Farewell to Arms", "genre": "War Fiction"},
            {"title": "For Whom the Bell Tolls", "genre": "War Fiction"}
        ]
    },
    {
        "F. Scott Fitzgerald": [
            {"title": "The Great Gatsby", "genre": "Tragedy"},
            {"title": "Tender is the Night", "genre": "Tragedy"},
            {"title": "This Side of Paradise", "genre": "Bildungsroman"}
        ]
    },
    {
        "George Orwell": [
            {"title": "1984", "genre": "Dystopian"},
            {"title": "Animal Farm", "genre": "Political Satire"},
            {"title": "Homage to Catalonia", "genre": "Non-fiction"}
        ]
    },
    {
        "J.K. Rowling": [
            {"title": "Harry Potter and the Sorcerer's Stone", "genre": "Fantasy"},
            {"title": "Harry Potter and the Chamber of Secrets", "genre": "Fantasy"},
            {"title": "Harry Potter and the Prisoner of Azkaban", "genre": "Fantasy"}
        ]
    },
    {
        "J.R.R. Tolkien": [
            {"title": "The Hobbit", "genre": "Fantasy"},
            {"title": "The Fellowship of the Ring", "genre": "Fantasy"},
            {"title": "The Two Towers", "genre": "Fantasy"}
        ]
    },
    {
        "Agatha Christie": [
            {"title": "Murder on the Orient Express", "genre": "Mystery"},
            {"title": "The Murder of Roger Ackroyd", "genre": "Mystery"},
            {"title": "And Then There Were None", "genre": "Mystery"}
        ]
    },
    {
        "Leo Tolstoy": [
            {"title": "War and Peace", "genre": "Historical Fiction"},
            {"title": "Anna Karenina", "genre": "Tragedy"},
            {"title": "The Death of Ivan Ilyich", "genre": "Philosophical Fiction"}
        ]
    },
    {
        "Fyodor Dostoevsky": [
            {"title": "Crime and Punishment", "genre": "Psychological Fiction"},
            {"title": "The Brothers Karamazov", "genre": "Philosophical Fiction"},
            {"title": "The Idiot", "genre": "Philosophical Fiction"}
        ]
    },
    {
        "Gabriel Garcia Marquez": [
            {"title": "One Hundred Years of Solitude", "genre": "Magical Realism"},
            {"title": "Love in the Time of Cholera", "genre": "Romance"},
            {"title": "Chronicle of a Death Foretold", "genre": "Mystery"}
        ]
    },
    {
        "Harper Lee": [
            {"title": "To Kill a Mockingbird", "genre": "Southern Gothic"},
            {"title": "Go Set a Watchman", "genre": "Fiction"}
        ]
    },
    {
        "Herman Melville": [
            {"title": "Moby-Dick", "genre": "Adventure"},
            {"title": "Bartleby, the Scrivener", "genre": "Short Story"},
            {"title": "Billy Budd, Sailor", "genre": "Novella"}
        ]
    },
    {
        "Virginia Woolf": [
            {"title": "Mrs Dalloway", "genre": "Modernist"},
            {"title": "To the Lighthouse", "genre": "Modernist"},
            {"title": "Orlando", "genre": "Biographical Fiction"}
        ]
    },
    {
        "James Joyce": [
            {"title": "Ulysses", "genre": "Modernist"},
            {"title": "A Portrait of the Artist as a Young Man", "genre": "Künstlerroman"},
            {"title": "Dubliners", "genre": "Short Stories"}
        ]
    },
    {
        "Franz Kafka": [
            {"title": "The Metamorphosis", "genre": "Absurdist Fiction"},
            {"title": "The Trial", "genre": "Philosophical Fiction"},
            {"title": "The Castle", "genre": "Philosophical Fiction"}
        ]
    },
    {
        "Emily Dickinson": [
            {"title": "The Complete Poems", "genre": "Poetry"},
            {"title": "Selected Poems", "genre": "Poetry"}
        ]
    },
    {
        "Oscar Wilde": [
            {"title": "The Picture of Dorian Gray", "genre": "Philosophical Fiction"},
            {"title": "The Importance of Being Earnest", "genre": "Comedy"},
            {"title": "De Profundis", "genre": "Epistolary"}
        ]
    },
    {
        "John Steinbeck": [
            {"title": "The Grapes of Wrath", "genre": "Historical Fiction"},
            {"title": "Of Mice and Men", "genre": "Tragedy"},
            {"title": "East of Eden", "genre": "Family Saga"}
        ]
    },
    {
        "Stephen King": [
            {"title": "The Shining", "genre": "Horror"},
            {"title": "It", "genre": "Horror"},
            {"title": "Misery", "genre": "Thriller"}
        ]
    },
    {
        "Edgar Allan Poe": [
            {"title": "The Raven", "genre": "Poetry"},
            {"title": "The Tell-Tale Heart", "genre": "Horror"},
            {"title": "The Fall of the House of Usher", "genre": "Gothic"}
        ]
    },
    {
        "Victor Hugo": [
            {"title": "Les Misérables", "genre": "Historical Fiction"},
            {"title": "The Hunchback of Notre-Dame", "genre": "Gothic Fiction"},
            {"title": "The Man Who Laughs", "genre": "Romanticism"}
        ]
    },
    {
        "J.D. Salinger": [
            {"title": "The Catcher in the Rye", "genre": "Bildungsroman"},
            {"title": "Nine Stories", "genre": "Short Stories"},
            {"title": "Franny and Zooey", "genre": "Fiction"}
        ]
    },
    {
        "George R.R. Martin": [
            {"title": "A Game of Thrones", "genre": "Fantasy"},
            {"title": "A Clash of Kings", "genre": "Fantasy"},
            {"title": "A Storm of Swords", "genre": "Fantasy"}
        ]
    },
    {
        "Isaac Asimov": [
            {"title": "Foundation", "genre": "Science Fiction"},
            {"title": "I, Robot", "genre": "Science Fiction"},
            {"title": "The Caves of Steel", "genre": "Science Fiction"}
        ]
    },
    {
        "Arthur Conan Doyle": [
            {"title": "A Study in Scarlet", "genre": "Mystery"},
            {"title": "The Hound of the Baskervilles", "genre": "Mystery"},
            {"title": "The Sign of the Four", "genre": "Mystery"}
        ]
    },
    {
        "Jules Verne": [
            {"title": "Twenty Thousand Leagues Under the Sea", "genre": "Adventure"},
            {"title": "Around the World in Eighty Days", "genre": "Adventure"},
            {"title": "Journey to the Center of the Earth", "genre": "Science Fiction"}
        ]
    },
    {
        "H.G. Wells": [
            {"title": "The War of the Worlds", "genre": "Science Fiction"},
            {"title": "The Time Machine", "genre": "Science Fiction"},
            {"title": "The Invisible Man", "genre": "Science Fiction"}
        ]
    },
    {
        "Toni Morrison": [
            {"title": "Beloved", "genre": "Historical Fiction"},
            {"title": "Song of Solomon", "genre": "Literary Fiction"},
            {"title": "The Bluest Eye", "genre": "Fiction"}
        ]
    },
    {
        "Margaret Atwood": [
            {"title": "The Handmaid's Tale", "genre": "Dystopian"},
            {"title": "Oryx and Crake", "genre": "Science Fiction"},
            {"title": "The Blind Assassin", "genre": "Historical Fiction"}
        ]
    },
    {
        "Kurt Vonnegut": [
            {"title": "Slaughterhouse-Five", "genre": "Science Fiction"},
            {"title": "Cat's Cradle", "genre": "Science Fiction"},
            {"title": "Breakfast of Champions", "genre": "Satire"}
        ]
    },
    {
        "Ray Bradbury": [
            {"title": "Fahrenheit 451", "genre": "Dystopian"},
            {"title": "The Martian Chronicles", "genre": "Science Fiction"},
            {"title": "Something Wicked This Way Comes", "genre": "Fantasy"}
        ]
    },
    {
        "Philip K. Dick": [
            {"title": "Do Androids Dream of Electric Sheep?", "genre": "Science Fiction"},
            {"title": "The Man in the High Castle", "genre": "Science Fiction"},
            {"title": "A Scanner Darkly", "genre": "Science Fiction"}
        ]
    },
    {
        "C.S. Lewis": [
            {"title": "The Lion, the Witch and the Wardrobe", "genre": "Fantasy"},
            {"title": "Prince Caspian", "genre": "Fantasy"},
            {"title": "The Voyage of the Dawn Treader", "genre": "Fantasy"}
        ]
    },
    {
        "Lewis Carroll": [
            {"title": "Alice's Adventures in Wonderland", "genre": "Fantasy"},
            {"title": "Through the Looking-Glass", "genre": "Fantasy"}
        ]
    },
    {
        "Mary Shelley": [
            {"title": "Frankenstein", "genre": "Science Fiction"},
            {"title": "The Last Man", "genre": "Science Fiction"}
        ]
    },
    {
        "Charlotte Brontë": [
            {"title": "Jane Eyre", "genre": "Gothic Fiction"},
            {"title": "Shirley", "genre": "Social Novel"},
            {"title": "Villette", "genre": "Psychological Fiction"}
        ]
    },
    {
        "Emily Brontë": [
            {"title": "Wuthering Heights", "genre": "Gothic Fiction"}
        ]
    },
    {
        "Aldous Huxley": [
            {"title": "Brave New World", "genre": "Dystopian"},
            {"title": "Island", "genre": "Utopian"}
        ]
    },
    {
        "Kazuo Ishiguro": [
            {"title": "Never Let Me Go", "genre": "Science Fiction"},
            {"title": "The Remains of the Day", "genre": "Historical Fiction"}
        ]
    },
    {
        "Chinua Achebe": [
            {"title": "Things Fall Apart", "genre": "Historical Fiction"},
            {"title": "No Longer at Ease", "genre": "Fiction"}
        ]
    }
]


class Command(BaseCommand):
    help = "loading testing data for development state"

    def __init__(self):
        super().__init__()

    @staticmethod
    def get_genre(genre_name: str):
        try:
            return Genre.objects.get(name=genre_name)
        except:
            return Genre.objects.create(name=genre_name)

    @staticmethod
    def get_author(author_name: str):
        try:
            return Author.objects.get(name=author_name)
        except:
            return Author.objects.create(name=author_name)

    def handle(self, *args, **options):
        # we can use exception handling, But I don't use because its just for test
        for author in books:
            for author_name, author_books in author.items():
                author = self.get_author(author_name=author_name)
                for book in author_books:
                    genre = self.get_genre(genre_name=book["genre"])

                    Book.objects.create(
                        title=book["title"],
                        author=author,
                        genre=genre,
                    )

        print("books created")
