#### ВАЖНО!! Папку с репозиторием после загрузки надо переименовать на 
#### pythonQA_Final **_test** без этого будут ошибки.
 
т.е. убрать дефис в наименовании **pythonQA_Final-test** и запустится без проблем. 
После названия репозитория добавляется наименование ветки репозитория и мешает запуску тестов.


Краткая инструкция по проверке:

- Качаем репозиторий ввиде ZIP файла
- Распаковываем
- Переименовываем в **pythonQA_Final_test**
- Открываем консоль, переходим в папку с репозиторием
- Создаем виртуальное окружение командой virtualenv env
- Запускаем env\Scripts\activate
- После запуска окружения устанавливаем пакеты командой pip install -r requirements.txt
- После установки пакетов убеждаемся, что находимся в окружении (слева от строки пути должно быть написано (env)
- Убеждаемся, что находимся в корне репозитория
- Выполняем команду для запуска тестов pytest -v --tb=line --language=en -m need_review
- Если ошибка не пропадает, удалите файл __init__.py из репозитория.


Если при проверке запуска тестов ругается на несоответствие версий хрома и хромдрайвера, скачайте актуальный
https://github.com/jsnjack/chromedriver/releases?ysclid=lta8k7i5il94205753

и положите его в папку *проверяемый репозиторий*\env\Scripts 

