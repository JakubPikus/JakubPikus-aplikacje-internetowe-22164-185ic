import os
from zipfile import ZipFile


from celery import shared_task

from PIL import Image

from django.conf import settings

@shared_task
def make_thumbnails(file_path, thumbnails=[]):
    os.chdir(settings.IMAGES_DIR)
    path, file = os.path.split(file_path)
    file_name, ext = os.path.splitext(file)

    zip_file = f"{file_name}.zip"
    results = {'archive_path': f"{settings.MEDIA_URL}images/{zip_file}"}
    try:
        img = Image.open(file_path)
        zipper = ZipFile(zip_file, 'w')
        zipper.write(file)
        for w, h in thumbnails:
            img_copy = img.copy()
            img_copy.thumbnail((w, h))
            thumbnail_file = f'{file_name}_{w}x{h}.{ext}'
            img_copy.save(thumbnail_file)
            zipper.write(thumbnail_file)

        img.close()
        zipper.close()
    except IOError as e:
        print(e)

    return results


@shared_task(name='notifiction')
def send_notifiction():
     print('Godzina 20:45')


@shared_task(name='summary1') 
def send_import_summary():
    print('Odśwież co 5 sekund')

@shared_task(name='summary2') 
def send_import_summary():
    print('Odśwież co 10 sekund')

