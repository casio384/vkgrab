# vkgrab
Простая скачивалка музыки из контакта. Для загрузки файлов используется wget.

# Установка
Для начала необходимо:
* зарегистрировать standalone-приложения(https://vk.com/dev) и вставить его в код скрипта(заменить строку YOUR-APP-ID)
* установить библиотеку vk для Python: https://github.com/dimka665/vk


#Usage
```bash
Usage: vkgrab.py -l login [OPTIONS]

Options:
  -h, --help            show this help message and exit
  -l LOGIN, --login=LOGIN
                        your login
  -s SEARCH_TITLE, --search_title=SEARCH_TITLE
                        Search audio with this title
  -o OWNERID, --owner_id=OWNERID
                        grab data from this id;
  --album_name=ALBUM_NAME
                        Name of album for download;
```
