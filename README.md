# 17_sites_monitoring

Скрипт проверяет работоспособность сайтов. Файл со списком урлов является обязательным аргументом (разделитель в файле - новая строка)

## Пример файла с урлами - urls.txt
    http://python.org  
    http://habrahabr.ru
    http://stackoverflow.com

## Примеры использования скрипта
    $python check_sites_health.py urls.txt
    
    
    http://yandex.ru has status OK and ... 
    domain name paid at least a month forward . 
     
    http://python.org has status OK and ... 
    domain name paid at least a month forward . 
     
    http://habrahabr.ru has status OK and ... 
    domain name paid at least a month forward . 
     
    http://stackoverflow.com has status OK and ... 
    domain name paid at least a month forward . 
 
# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
