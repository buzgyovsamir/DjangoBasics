from django.core.management.base import BaseCommand
from categories.models import Category
from notes.models import Note
from notes.choices import PriorityChoices


class Command(BaseCommand):
    help = 'Populates the database with sample categories and notes'

    def handle(self, *args, **options):
        # Clear existing data (optional - comment out if you want to keep existing data)
        # Note.objects.all().delete()
        # Category.objects.all().delete()

        # Create Categories
        categories_data = [
            {
                'name': 'Work',
                'description': 'Notes related to work tasks, meetings, and projects'
            },
            {
                'name': 'Personal',
                'description': 'Personal notes, reminders, and thoughts'
            },
            {
                'name': 'Learning',
                'description': 'Notes about things I\'m learning or studying'
            },
            {
                'name': 'Shopping',
                'description': 'Shopping lists and purchase reminders'
            },
            {
                'name': 'Ideas',
                'description': 'Random ideas and creative thoughts'
            },
        ]

        categories = {}
        for cat_data in categories_data:
            category, created = Category.objects.get_or_create(
                name=cat_data['name'],
                defaults={'description': cat_data['description']}
            )
            categories[cat_data['name']] = category
            if created:
                self.stdout.write(
                    self.style.SUCCESS(f'Created category: {category.name}')
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f'Category already exists: {category.name}')
                )

        # Create Notes
        notes_data = [
            {
                'title': 'Django Project Setup',
                'body': 'Remember to set up virtual environment and install Django. Also configure settings.py properly.',
                'priority': PriorityChoices.HIGH,
                'is_published': True,
                'category': 'Work'
            },
            {
                'title': 'Grocery Shopping',
                'body': 'Need to buy: milk, eggs, bread, chicken, vegetables, and fruits.',
                'priority': PriorityChoices.MEDIUM,
                'is_published': True,
                'category': 'Shopping'
            },
            {
                'title': 'Python Tips',
                'body': 'List comprehensions are faster than loops. Use f-strings for string formatting. Always use virtual environments.',
                'priority': PriorityChoices.MEDIUM,
                'is_published': True,
                'category': 'Learning'
            },
            {
                'title': 'Weekend Plans',
                'body': 'Planning to visit the park, read a book, and catch up with friends.',
                'priority': PriorityChoices.LOW,
                'is_published': False,
                'category': 'Personal'
            },
            {
                'title': 'App Idea',
                'body': 'Create a note-taking app with categories and priorities. Wait, that\'s what we\'re building!',
                'priority': PriorityChoices.LOW,
                'is_published': True,
                'category': 'Ideas'
            },
            {
                'title': 'Meeting Notes',
                'body': 'Discuss project timeline, assign tasks, and review progress. Follow up next week.',
                'priority': PriorityChoices.HIGH,
                'is_published': True,
                'category': 'Work'
            },
            {
                'title': 'Book Recommendations',
                'body': 'Clean Code by Robert Martin, The Pragmatic Programmer, and Design Patterns by Gang of Four.',
                'priority': PriorityChoices.LOW,
                'is_published': True,
                'category': 'Learning'
            },
            {
                'title': 'Birthday Reminder',
                'body': 'Sarah\'s birthday is next month. Need to buy a gift and plan a surprise party.',
                'priority': PriorityChoices.MEDIUM,
                'is_published': False,
                'category': 'Personal'
            },
            {
                'title': 'Django ORM Tips',
                'body': 'Use select_related() for ForeignKey and prefetch_related() for ManyToMany. Avoid N+1 queries.',
                'priority': PriorityChoices.MEDIUM,
                'is_published': True,
                'category': 'Learning'
            },
            {
                'title': 'Project Deadline',
                'body': 'Important: The project deadline is approaching. Need to finish testing and documentation.',
                'priority': PriorityChoices.HIGH,
                'is_published': True,
                'category': 'Work'
            },
        ]

        created_count = 0
        for note_data in notes_data:
            category = categories.get(note_data.pop('category'))
            note, created = Note.objects.get_or_create(
                title=note_data['title'],
                defaults={
                    'body': note_data['body'],
                    'priority': note_data['priority'],
                    'is_published': note_data['is_published'],
                    'category': category
                }
            )
            if created:
                created_count += 1
                self.stdout.write(
                    self.style.SUCCESS(f'Created note: {note.title}')
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f'Note already exists: {note.title}')
                )

        self.stdout.write(
            self.style.SUCCESS(
                f'\nSuccessfully populated database!\n'
                f'Created/Found {len(categories)} categories\n'
                f'Created {created_count} new notes'
            )
        )
