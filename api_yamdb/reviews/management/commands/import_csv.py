
from django.core.management import BaseCommand

from .utils import (check_files, get_path, get_models_and_files, load_data)


class Command(BaseCommand):
    help = "Загрузка данных из csv-файлов"

    def add_arguments(self, parser) -> None:
        parser.add_argument(
            '--path',
            default='static/data',
            help='Путь к папке с csv файлами'
        )

    def handle(self, *args, **options):
        path = get_path(options)
        files = check_files(path)
        models_files = get_models_and_files(path, files)
        load_data(models_files)
