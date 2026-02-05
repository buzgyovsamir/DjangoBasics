from django.core.management.base import BaseCommand
from django.db import transaction

from books.models import Book
from reviews.models import Review


class Command(BaseCommand):
    help = "Seed the database with sample books and reviews (5 books, 3 reviews each)."

    @transaction.atomic
    def handle(self, *args, **options):
        # Clear existing sample data that matches our ISBNs so the command is idempotent
        isbns = {
            "9780000000001",
            "9780000000002",
            "9780000000003",
            "9780000000004",
            "9780000000005",
        }
        Review.objects.filter(book__isbn__in=isbns).delete()
        Book.objects.filter(isbn__in=isbns).delete()

        books_data = [
            {
                "title": "The Silent Library",
                "price": "14.99",
                "isbn": "9780000000001",
                "genre": "Mystery",
                "publishing_date": "2021-03-15",
                "description": (
                    "When a rare manuscript goes missing from an old university library, "
                    "an introverted archivist must uncover a decades-old conspiracy "
                    "buried between the stacks."
                ),
                "image_url": "https://example.com/images/the-silent-library.jpg",
                "pages": 352,
                "publisher": "inkwell-press",
            },
            {
                "title": "Stars Beyond Canvas",
                "price": "18.50",
                "isbn": "9780000000002",
                "genre": "Science",
                "publishing_date": "2020-11-02",
                "description": (
                    "A popular-science journey through the history of astronomy told through "
                    "the artists who painted the night sky long before telescopes could "
                    "prove them right."
                ),
                "image_url": "https://example.com/images/stars-beyond-canvas.jpg",
                "pages": 278,
                "publisher": "orion-house",
            },
            {
                "title": "Clockwork Kingdom",
                "price": "22.00",
                "isbn": "9780000000003",
                "genre": "Fantasy",
                "publishing_date": "2019-07-21",
                "description": (
                    "In a city powered by gears and guarded by automatons, a young mechanic "
                    "discovers that the royal clock has been lying about time—and their fate—"
                    "for centuries."
                ),
                "image_url": "https://example.com/images/clockwork-kingdom.jpg",
                "pages": 410,
                "publisher": "brass-owl-press",
            },
            {
                "title": "Footnotes to History",
                "price": "16.75",
                "isbn": "9780000000004",
                "genre": "History",
                "publishing_date": "2018-09-10",
                "description": (
                    "A collection of little-known episodes that quietly changed the world: "
                    "the misprints, side letters, and forgotten meetings that never made it "
                    "into the textbooks."
                ),
                "image_url": "https://example.com/images/footnotes-to-history.jpg",
                "pages": 320,
                "publisher": "lantern-press",
            },
            {
                "title": "Coffee Shop Algorithms",
                "price": "19.95",
                "isbn": "9780000000005",
                "genre": "Non-Fiction",
                "publishing_date": "2022-01-05",
                "description": (
                    "An accessible introduction to algorithms and problem‑solving, "
                    "explained through everyday scenarios—queues, orders, and regulars—"
                    "in a bustling city cafe."
                ),
                "image_url": "https://example.com/images/coffee-shop-algorithms.jpg",
                "pages": 260,
                "publisher": "riverside-press",
            },
        ]

        reviews_data = {
            "9780000000001": [
                {
                    "author": "Alex Morgan",
                    "body": (
                        "Beautifully written and full of atmosphere. I loved how the mystery "
                        "unfolded entirely within the library—every room felt real."
                    ),
                    "rating": "4.50",
                    "is_spoiler": False,
                },
                {
                    "author": "Priya Das",
                    "body": (
                        "Slow start but the last third is impossible to put down. "
                        "The final reveal is clever without feeling cheap."
                    ),
                    "rating": "4.00",
                    "is_spoiler": False,
                },
                {
                    "author": "James Carter",
                    "body": (
                        "As a librarian, the details made me smile. One scene in the archive "
                        "basement actually gave me chills."
                    ),
                    "rating": "4.75",
                    "is_spoiler": True,
                },
            ],
            "9780000000002": [
                {
                    "author": "Nora Klein",
                    "body": (
                        "Great blend of art and astronomy. The explanations stay clear even "
                        "when it gets into heavier science."
                    ),
                    "rating": "4.25",
                    "is_spoiler": False,
                },
                {
                    "author": "Luis Herrera",
                    "body": (
                        "I picked this up for the illustrations and stayed for the stories. "
                        "Perfect if you like science but hate equations."
                    ),
                    "rating": "4.00",
                    "is_spoiler": False,
                },
                {
                    "author": "Maya Thompson",
                    "body": (
                        "A couple of chapters drag, but the section on early star maps "
                        "is fantastic."
                    ),
                    "rating": "3.75",
                    "is_spoiler": False,
                },
            ],
            "9780000000003": [
                {
                    "author": "Elias Park",
                    "body": (
                        "Exactly the kind of immersive fantasy I love. "
                        "The city itself feels like a main character."
                    ),
                    "rating": "4.80",
                    "is_spoiler": False,
                },
                {
                    "author": "Sara Velasquez",
                    "body": (
                        "Some of the plot twists are predictable, but the world‑building "
                        "and gadgets more than make up for it."
                    ),
                    "rating": "4.10",
                    "is_spoiler": False,
                },
                {
                    "author": "Tom Richter",
                    "body": (
                        "There is a late‑book reveal about the royal clock that completely "
                        "recontextualizes the opening chapters."
                    ),
                    "rating": "4.60",
                    "is_spoiler": True,
                },
            ],
            "9780000000004": [
                {
                    "author": "Hana Kim",
                    "body": (
                        "Short, sharp chapters that make it easy to dip in and out. "
                        "Learned a lot without feeling lectured."
                    ),
                    "rating": "4.20",
                    "is_spoiler": False,
                },
                {
                    "author": "Daniel Osei",
                    "body": (
                        "Great reminder that history is often decided in the margins. "
                        "I kept googling events as I went."
                    ),
                    "rating": "4.00",
                    "is_spoiler": False,
                },
                {
                    "author": "Emily Ross",
                    "body": (
                        "A few chapters feel like extended footnotes, but that’s kind of "
                        "the point. Niche but fascinating."
                    ),
                    "rating": "3.60",
                    "is_spoiler": False,
                },
            ],
            "9780000000005": [
                {
                    "author": "Chris Nguyen",
                    "body": (
                        "If you’ve ever tried to explain big‑O to a non‑technical friend, "
                        "this is the book you wish you had."
                    ),
                    "rating": "4.70",
                    "is_spoiler": False,
                },
                {
                    "author": "Rita Silva",
                    "body": (
                        "Clever analogies and concrete examples. The coffee shop setting "
                        "keeps it light without dumbing anything down."
                    ),
                    "rating": "4.30",
                    "is_spoiler": False,
                },
                {
                    "author": "Mohammed Al‑Khalid",
                    "body": (
                        "Some chapters repeat ideas, but the exercises at the end of each "
                        "section are surprisingly practical."
                    ),
                    "rating": "3.90",
                    "is_spoiler": False,
                },
            ],
        }

        created_books = []
        created_reviews = 0

        for book_data in books_data:
            isbn = book_data["isbn"]
            book = Book.objects.create(
                title=book_data["title"],
                price=book_data["price"],
                isbn=isbn,
                genre=book_data["genre"],
                publishing_date=book_data["publishing_date"],
                description=book_data["description"],
                image_url=book_data["image_url"],
                pages=book_data["pages"],
                publisher=book_data["publisher"],
            )
            created_books.append(book)

            for review_data in reviews_data[isbn]:
                Review.objects.create(
                    author=review_data["author"],
                    body=review_data["body"],
                    rating=review_data["rating"],
                    book=book,
                    is_spoiler=review_data["is_spoiler"],
                )
                created_reviews += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"Created {len(created_books)} books and {created_reviews} reviews."
            )
        )

