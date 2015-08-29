from datetime import date
from random import randint, sample
from django.core.management.base import BaseCommand
from optparse import make_option
from students.models import Student, Group
from django.contrib.auth.models import User


class Command(BaseCommand):
    args = '<model_name model_name ...>'
    help = "It creates a specified number of objects of a particular type in the database"
    option_list = BaseCommand.option_list + (
        make_option('--students',
            action='store',
            dest='students',
            default=False,
            help='Add student to database'),
        )

    def handle(self, *args, **options):
        if options['students']:
            population = 'abcdefghijklmnopqrstuvwxyz'
            name = ''
            groups = Group.objects.all()

            for _ in xrange(int(options['students'])):
                first_name = name.join(sample(population, 4)).capitalize()
                last_name = name.join(sample(population, 5)).capitalize()
                birthday = date.today()
                ticket = randint(1, 1000)
                group = groups[randint(0, len(groups)-1)]

                data = {'first_name': first_name,
                        'last_name': last_name,
                        'birthday': str(birthday),
                        'ticket': ticket,
                        'student_group': group}
                student = Student(**data)
                student.save()
