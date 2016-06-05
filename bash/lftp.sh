#!/bin/bash

# lftp -e 'mirror -e каталог-на-сервере локальный-каталог; bye;' -u логин,пароль удалённый.хост
# lftp -e 'mirror -R локальный-каталог каталог-на-сервере; bye;' -u логин,пароль удалённый.хост

# lftp -e 'mirror -e ~/ ~/img; bye;' ftp.narod.ru
lftp -e 'mirror -R ~/projects/web/narod/ /; bye;' ftp.narod.ru

