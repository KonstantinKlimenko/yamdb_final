import csv
from os import listdir
from os.path import exists, isfile, join
from pathlib import Path
from typing import Any, Dict, Tuple, Type

from django.apps import apps
from django.conf import settings
from django.db.models import Model


def get_path(options: Dict[str, Any]) -> str:
    """Получение относительного пути к директории с файлами."""
    input_path = Path(options['path'])
    path = join(settings.BASE_DIR, input_path)
    print(f'Введена директория: {path}')
    if exists(path):
        return path
    else:
        raise FileNotFoundError('Директория НЕ найдена!')


def check_files(path: str) -> Dict[str, str]:
    """Проверка наличия всех файлов."""
    files_dict = {
        'user': 'users.csv',
        'category': 'category.csv',
        'comment': 'comments.csv',
        'genre': 'genre.csv',
        'review': 'review.csv',
        'title': 'titles.csv',
        'title_genre': 'genre_title.csv',
    }
    access_files = {}
    files_list = [f for f in listdir(path) if isfile(join(path, f))]
    for model_name, files in files_dict.items():
        if files in files_list:
            print(f'Для модели {model_name} найден файл {files}')
            access_files[model_name] = files
        else:
            print(f'*Для модели {model_name} файл НЕ найден!')
    if len(files_dict) != len(access_files):
        raise FileNotFoundError('Найдены не все файлы!')
    return access_files


def get_models_and_files(
        path: str,
        files: Dict[str, str]) -> Dict[str, Tuple[Type[Model], str]]:
    """Создание словаря {Модель: Путь к файлу}."""
    models = {**apps.all_models['reviews'], **apps.all_models['users']}
    models_files = {}
    for model_name, file_name in files.items():
        if model_name in models:
            model = models[model_name]
        else:
            raise TypeError('Такой модели не найдено')
        file_path = join(path, file_name)
        models_files[model_name] = model, file_path
    return models_files


def load_data(
        models_files: Dict[str, Tuple[Type[Model], str]]) -> None:
    """Загрузка данных в модели"""
    models_names_list = [
        'user',
        'category',
        'genre',
        'title',
        'review',
        'comment',
        'title_genre',
    ]
    replace_field = [
        'author',
        'category',
    ]
    for model_name in models_names_list:
        model, file = models_files[model_name]
        count_obj_before = model.objects.all().count()
        with open(file, encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file, delimiter=',')
            for index, field in enumerate(reader.fieldnames):
                if field in replace_field:
                    reader.fieldnames[index] += '_id'
            print(f'Импорт данных в модель {model.__name__}')
            count_row = 0
            for count_row, row in enumerate(reader, start=1):
                object, created = model.objects.get_or_create(**row)
        count_obj_after = model.objects.all().count()
        print(f'Добавлено {count_obj_after - count_obj_before} из {count_row}')
