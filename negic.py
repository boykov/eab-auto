#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# (eepitch-shell)

"""

import hronlib
import os,shutil
import time,datetime,re
import csv
import sys
import hronlib
import random

segments = {
"mvpc":
    [["Хабаровск - MAXI Plus (гор/фед) (КТП) (SS)"        ,"01.01.09 00:00","31.12.09 23:59"],
     ["Хабаровск - MAXI Super (гор/фед) (КТП) (SS)"       ,"01.01.09 00:00","31.12.09 23:59"],
     ["Хабаровск - Много звонков (гор/фед) (КТП) (SS)"    ,"01.01.09 00:00","31.12.09 23:59"],
     ["Хабаровск - Говори свободно (гор/фед) (КТП) (SS)"  ,"01.01.09 00:00","31.12.09 23:59"],
     ["Хабаровск - МТС Коннект-2 (гор/фед) (КТП) (SS)"    ,"01.01.09 00:00","31.12.09 23:59"],
     ["Хабаровск - Эксклюзив07 (гор/фед) (КК) (SS)"       ,"01.01.09 00:00","31.12.09 23:59"],
     ["Хабаровск - Эксклюзив (гор/фед) (КК) (SS)"         ,"01.01.09 00:00","31.12.09 23:59"],
     ["Хабаровск - MAXI (гор/фед) (КТП) (SS)"             ,"01.01.09 00:00","31.12.09 23:59"],
     ["Хабаровск - MAXI Active (гор/фед) (КТП) (SS)"      ,"01.01.09 00:00","31.12.09 23:59"],
     ["Хабаровск - Удачный ход (гор/фед) (КТП) (SS)"      ,"01.01.09 00:00","31.12.09 23:59"],
     ["Хабаровск - Бизнес без границ (гор/фед) (КК) (SS)" ,"01.01.09 00:00","31.12.09 23:59"]],
"mass":
    [
["Хабаровск - i-Онлайнер (фед) (ПРП) (SS)"                                 ,"01.01.09 00:00","31.12.09 23:59"],
["Хабаровск - RED07 (фед) (ПРП) (IN)"                                      ,"01.01.09 00:00","31.12.09 23:59"],
["Хабаровск - RED Energy (гор/фед) (ПРП) (IN)"                             ,"01.01.09 00:00","31.12.09 23:59"],
["Хабаровск - RED New (фед) (ПРП) (IN)"                                    ,"01.01.09 00:00","31.12.09 23:59"],
["Хабаровск - RED_text (фед) (ПРП) (IN)"                                   ,"01.01.09 00:00","31.12.09 23:59"],
["Хабаровск - RED (фед) (ПРП) (IN)"                                        ,"01.01.09 00:00","31.12.09 23:59"],
["Хабаровск - SIM (фед) (ПРП) (SS)"                                        ,"01.01.09 00:00","31.12.09 23:59"],
["Хабаровск - Базовый09 (фед) (ПРП) (IN)"                                  ,"01.01.09 00:00","31.12.09 23:59"],
["Хабаровск - Базовый (фед) (ПРП) (IN)"                                    ,"01.01.09 00:00","31.12.09 23:59"],
["Хабаровск - Все свои (фед) (ПРП) (IN)"                                   ,"01.01.09 00:00","31.12.09 23:59"],
["Хабаровск - Все свои + (фед) (ПРП) (IN)"                                 ,"01.01.09 00:00","31.12.09 23:59"],
["Хабаровск - Гостевой (гор/фед) (ПРП) (IN)"                               ,"01.01.09 00:00","31.12.09 23:59"],
["Хабаровск - Джинс 007 поминутно 2009_1 (фед) (ПРП) (IN)"                 ,"01.01.09 00:00","31.12.09 23:59"],
["Хабаровск - Джинс 007 поминутно 2009_61 (фед) (ПРП) (IN)"                ,"01.01.09 00:00","31.12.09 23:59"],
["Хабаровск - Длинные разговоры (гор/фед) (ПРП) (IN)"                      ,"01.01.09 00:00","31.12.09 23:59"],
["Хабаровск - Заботливый (гор/фед) (ПРП) (IN)"                             ,"01.01.09 00:00","31.12.09 23:59"],
["Хабаровск - Классный (гор/фед) (ПРП) (IN)"                               ,"01.01.09 00:00","31.12.09 23:59"],
["Хабаровск - Любимый (фед) (ПРП) (IN)"                                    ,"01.01.09 00:00","31.12.09 23:59"],
["Хабаровск - Мы (фед) (ПРП) (IN)"                                         ,"01.01.09 00:00","31.12.09 23:59"],
["Хабаровск - Новогодний (фед) (ПРП) (IN)"                                 ,"01.01.09 00:00","31.12.09 23:59"],
["Хабаровск - Онлайнер (гор/фед) (ПРП) (IN)"                               ,"01.01.09 00:00","31.12.09 23:59"],
["Хабаровск - Первый07 (фед) (ПРП) (IN)"                                   ,"01.01.09 00:00","31.12.09 23:59"],
["Хабаровск - Первый (фед) (ПРП) (IN)"                                     ,"01.01.09 00:00","31.12.09 23:59"],
["Хабаровск - Подарок (фед) (ПРП) (IN)"                                    ,"01.01.09 00:00","31.12.09 23:59"],
["Хабаровск - Подружки (гор/фед) (ПРП) (IN)"                               ,"01.01.09 00:00","31.12.09 23:59"],
["Хабаровск - Рубль (фед) (ПРП) (IN)"                                      ,"01.01.09 00:00","31.12.09 23:59"],
["Хабаровск - Свободный (фед) (ПРП) (IN)"                                  ,"01.01.09 00:00","31.12.09 23:59"],
["Хабаровск - Сотовый мир (фед) (ПРП) (IN)"                                ,"01.01.09 00:00","31.12.09 23:59"],
["Хабаровск - Стимул07 (фед) (ПРП) (IN)"                                   ,"01.01.09 00:00","31.12.09 23:59"],
["Хабаровск - Стимул09 (гор/фед) (ПРП) (IN)"                               ,"01.01.09 00:00","31.12.09 23:59"],
["Хабаровск - Супер Город (гор/фед) (ПРП) (IN)"                            ,"01.01.09 00:00","31.12.09 23:59"],
["Хабаровск - Супер Джинс поминутно 2009_1 (фед) (ПРП) (IN)"               ,"01.01.09 00:00","31.12.09 23:59"],
["Хабаровск - Супер Джинс поминутно 2009_61 (фед) (ПРП) (IN)"              ,"01.01.09 00:00","31.12.09 23:59"],
["Хабаровск - Супер Ноль (гор/фед) (ПРП) (IN)"                             ,"01.01.09 00:00","31.12.09 23:59"],
["Хабаровск - Супер-Первый (фед) (ПРП) (IN)"                               ,"01.01.09 00:00","31.12.09 23:59"],
["Хабаровск - Универсальный (фед) (ПРП) (IN)"                              ,"01.01.09 00:00","31.12.09 23:59"],
["Хабаровск - Хот Джинс поминутно 2009_61 (фед) (ПРП) (IN)"                ,"01.01.09 00:00","31.12.09 23:59"],
    ]                                                                      ,
"hvpc":
[
["Хабаровск - MAXI корпоративный (гор/фед) (КОРП) (SS)"                    ,"01.01.09 00:00","31.12.09 23:59"],
["Хабаровск - Авиатор (фед) (КОРП) (SS)"                                   ,"01.01.09 00:00","31.12.09 23:59"],
["Хабаровск - Бизнес online (гор/фед) (КОРП) (SS)"                         ,"01.01.09 00:00","31.12.09 23:59"],
["Хабаровск - Бизнес без границ корпоративный (гор/фед) (КОРП) (SS)"       ,"01.01.09 00:00","31.12.09 23:59"],
["Хабаровск - Бизнес-класс (гор/фед) (КОРП) (SS)"                          ,"01.01.09 00:00","31.12.09 23:59"],
["Хабаровск - Бизнес-модель (гор/фед) (КОРП) (SS)"                         ,"01.01.09 00:00","31.12.09 23:59"],
["Хабаровск - Бизнес общение (гор/фед) (КОРП) (SS)"                        ,"01.01.09 00:00","31.12.09 23:59"],
["Хабаровск - Бизнес сеть (гор/фед) (КОРП) (SS)"                           ,"01.01.09 00:00","31.12.09 23:59"],
["Хабаровск - Команда07 (гор/фед) (КОРП) (SS)"                             ,"01.01.09 00:00","31.12.09 23:59"],
["Хабаровск - Команда (гор/фед) (КОРП) (SS)"                               ,"01.01.09 00:00","31.12.09 23:59"],
["Хабаровск - Корпоративная сеть (гор/фед) (КОРП) (SS)"                    ,"01.01.09 00:00","31.12.09 23:59"],
["Хабаровск - Корпоративный мобайл07 (гор/фед) (КОРП) (SS)"                ,"01.01.09 00:00","31.12.09 23:59"],
["Хабаровск - Корпоративный мобайл (гор/фед) (КОРП) (SS)"                  ,"01.01.09 00:00","31.12.09 23:59"],
["Хабаровск - Корпоративный мобайл + (гор/фед) (КОРП) (SS)"                ,"01.01.09 00:00","31.12.09 23:59"],
["Хабаровск - Корпоративный национальный (гор/фед) (КОРП) (SS)"            ,"01.01.09 00:00","31.12.09 23:59"],
["Хабаровск - Корпоративный Эксклюзив (гор/фед) (КОРП) (SS)"               ,"01.01.09 00:00","31.12.09 23:59"],
["Хабаровск - Корпорация I (гор/фед) (КОРП) (SS)"                          ,"01.01.09 00:00","31.12.09 23:59"],
["Хабаровск - МТС. Команда' (гор/фед) (КОРП) (SS)"                         ,"01.01.09 00:00","31.12.09 23:59"],
["Хабаровск - МТС-Коннект (гор/фед) (КОРП) (SS)"                           ,"01.01.09 00:00","31.12.09 23:59"],
["Хабаровск - Престиж  (гор/фед) (КОРП) (SS)"                              ,"01.01.09 00:00","31.12.09 23:59"],
["Хабаровск - Свой бизнес (гор/фед) (КОРП) (SS)"                           ,"01.01.09 00:00","31.12.09 23:59"],
["Хабаровск - Свой круг (гор/фед) (КОРП) (SS)"                             ,"01.01.09 00:00","31.12.09 23:59"],
["Хабаровск - Территория бизнеса (гор/фед) (КОРП) (SS)"                    ,"01.01.09 00:00","31.12.09 23:59"],
["Хабаровск - Эксклюзив07 корпоративный (гор/фед) (КОРП) (SS)"             ,"01.01.09 00:00","31.12.09 23:59"],
["Хабаровск - Экспресс (гор/фед) (КОРП) (SS)"                              ,"01.01.09 00:00","31.12.09 23:59"]],
"except":
[
["Благовещенск - MAXI07' корпоративный (гор/фед) (КОРП) (SS)"              ,"01.01.80 00:00","31.12.09 23:59"],
["Еврейский АО - Команда07 (фед) (КОРП) (SS)"                              ,"01.01.80 00:00","31.12.09 23:59"],
["Еврейский АО - МТС Коннект-2 (фед) (КТП) (SS)"                           ,"01.01.80 00:00","31.12.09 23:59"],
["МР ДВ - RED (фед) (ТЕСТ) (SCP)"                                          ,"01.01.80 00:00","31.12.09 23:59"],
["МР ДВ - Дилер GPRS (фед) (КТП) (SS)"                                     ,"01.01.80 00:00","31.12.09 23:59"],
["МР ДВ - Корпоративный Индивидуальный (кроме Читы) (гор/фед) (КОРП) (SS)" ,"01.01.80 00:00","31.12.09 23:59"],
["МР ДВ - Корпоративный локальный (кроме Читы) (гор/фед) (КОРП) (SS)"      ,"01.01.80 00:00","31.12.09 23:59"],
["МР ДВ - Корпоративный Стандарт (кроме Читы) (гор/фед) (КОРП) (SS)"       ,"01.01.80 00:00","31.12.09 23:59"],
["МР ДВ - Льготный безлимит (кроме Читы) (гор/фед) (КК) (SS)"              ,"01.01.80 00:00","31.12.09 23:59"],
["МР ДВ - СОРМ-1 (гор/фед) (КК) (SS)"                                      ,"01.01.80 00:00","31.12.09 23:59"],
["МР ДВ - Технический (гор/фед) (СПЕЦ) (SS)"                               ,"01.01.80 00:00","31.12.09 23:59"],
["Приморье - MAXI (гор/фед) (КТП) (SS)"                                    ,"01.01.80 00:00","31.12.09 23:59"],
["Приморье - Команда07 (гор/фед) (КОРП) (SS)"                              ,"01.01.80 00:00","31.12.09 23:59"],
["Приморье - Много звонков (гор/фед) (КТП) (SS)"                           ,"01.01.80 00:00","31.12.09 23:59"],
["Приморье - МТС Коннект-2 (гор/фед) (КТП) (SS)"                           ,"01.01.80 00:00","31.12.09 23:59"],
["Хабаровск - Корпорация II (гор/фед) (КОРП) (SS)"                         ,"01.01.80 00:00","31.12.09 23:59"],
["Хабаровск - Корпорация III (гор/фед) (КОРП) (SS)"                        ,"01.01.80 00:00","31.12.09 23:59"],
["Хабаровск - Корпорация III + Теам (гор/фед) (КТП) (SS)"                  ,"01.01.80 00:00","31.12.09 23:59"],
["Хабаровск - Стандарт корп (гор/фед) (КОРП) (SS)"                         ,"01.01.80 00:00","31.12.09 23:59"],
["Хабаровск - Тестовый 3G (гор/фед) (ПРП) (SS)"                            ,"01.01.80 00:00","31.12.09 23:59"],
["Хабаровск - Профессионал (гор/фед) (КТП) (SS)"                           ,"01.01.80 00:00","31.12.09 23:59"]],
 "1jan09":
     [
["Хабаровск - Удачный ход (гор/фед) (КТП) (SS)"                            ,"01.01.80 00:00","31.12.09 23:59"],
["Хабаровск - MAXI (гор/фед) (КТП) (SS)"                                   ,"01.01.80 00:00","31.12.09 23:59"],
["Хабаровск - MAXI Active (гор/фед) (КТП) (SS)"                            ,"01.01.80 00:00","31.12.09 23:59"],
["Хабаровск - MAXI Plus (гор/фед) (КТП) (SS)"                              ,"01.01.80 00:00","31.12.09 23:59"],
["Хабаровск - MAXI Super (гор/фед) (КТП) (SS)"                             ,"01.01.80 00:00","31.12.09 23:59"],
["Хабаровск - MAXI корпоративный (гор/фед) (КОРП) (SS)"                    ,"01.01.80 00:00","31.12.09 23:59"],
["Хабаровск - RED Energy (гор/фед) (ПРП) (IN)"                             ,"01.01.80 00:00","31.12.09 23:59"],
["Хабаровск - RED New (фед) (ПРП) (IN)"                                    ,"01.01.80 00:00","31.12.09 23:59"],
["Хабаровск - SIM (фед) (ПРП) (SS)"                                        ,"01.01.80 00:00","31.12.09 23:59"],
["Хабаровск - Авиатор (фед) (КОРП) (SS)"                                   ,"01.01.80 00:00","31.12.09 23:59"],
["Хабаровск - Бизнес без границ (гор/фед) (КК) (SS)"                       ,"01.01.80 00:00","31.12.09 23:59"],
["Хабаровск - Бизнес общение (гор/фед) (КОРП) (SS)"                        ,"01.01.80 00:00","31.12.09 23:59"],
["Хабаровск - Бизнес-модель (гор/фед) (КОРП) (SS)"                         ,"01.01.80 00:00","31.12.09 23:59"],
["Хабаровск - Говори свободно (гор/фед) (КТП) (SS)"                        ,"01.01.80 00:00","31.12.09 23:59"],
["Хабаровск - Дилер (гор/фед) (ПРП) (IN)"                                  ,"01.01.80 00:00","31.12.09 23:59"],
["Хабаровск - Длинные разговоры (гор/фед) (ПРП) (IN)"                      ,"01.01.80 00:00","31.12.09 23:59"],
["Хабаровск - Заботливый (гор/фед) (ПРП) (IN)"                             ,"01.01.80 00:00","31.12.09 23:59"],
["Хабаровск - Классный (гор/фед) (ПРП) (IN)"                               ,"01.01.80 00:00","31.12.09 23:59"],
["Хабаровск - Команда07 (гор/фед) (КОРП) (SS)"                             ,"01.01.80 00:00","31.12.09 23:59"],
["Хабаровск - Корпоративный Эксклюзив (гор/фед) (КОРП) (SS)"               ,"01.01.80 00:00","31.12.09 23:59"],
["Хабаровск - Корпоративный мобайл (гор/фед) (КОРП) (SS)"                  ,"01.01.80 00:00","31.12.09 23:59"],
["Хабаровск - Корпоративный мобайл07 (гор/фед) (КОРП) (SS)"                ,"01.01.80 00:00","31.12.09 23:59"],
["Хабаровск - Корпоративный национальный (гор/фед) (КОРП) (SS)"            ,"01.01.80 00:00","31.12.09 23:59"],
["Хабаровск - МТС Коннект-2 (гор/фед) (КТП) (SS)"                          ,"01.01.80 00:00","31.12.09 23:59"],
["Хабаровск - Много звонков (гор/фед) (КТП) (SS)"                          ,"01.01.80 00:00","31.12.09 23:59"],
["Хабаровск - Мы (фед) (ПРП) (IN)"                                         ,"01.01.80 00:00","31.12.09 23:59"],
["Хабаровск - Новогодний (фед) (ПРП) (IN)"                                 ,"01.01.80 00:00","31.12.09 23:59"],
["Хабаровск - Онлайнер (гор/фед) (ПРП) (IN)"                               ,"01.01.80 00:00","31.12.09 23:59"],
["Хабаровск - Подружки (гор/фед) (ПРП) (IN)"                               ,"01.01.80 00:00","31.12.09 23:59"],
["Хабаровск - Свой бизнес (гор/фед) (КОРП) (SS)"                           ,"01.01.80 00:00","31.12.09 23:59"],
["Хабаровск - Свой круг (гор/фед) (КОРП) (SS)"                             ,"01.01.80 00:00","31.12.09 23:59"],
["Хабаровск - Сотовый мир (фед) (ПРП) (IN)"                                ,"01.01.80 00:00","31.12.09 23:59"],
["Хабаровск - Стимул07 (фед) (ПРП) (IN)"                                   ,"01.01.80 00:00","31.12.09 23:59"],
["Хабаровск - Стимул09 (гор/фед) (ПРП) (IN)"                               ,"01.01.80 00:00","31.12.09 23:59"],
["Хабаровск - Супер Город (гор/фед) (ПРП) (IN)"                            ,"01.01.80 00:00","31.12.09 23:59"],
["Хабаровск - Супер Ноль (гор/фед) (ПРП) (IN)"                             ,"01.01.80 00:00","31.12.09 23:59"],
["Хабаровск - Супер-Первый (фед) (ПРП) (IN)"                               ,"01.01.80 00:00","31.12.09 23:59"],
["Хабаровск - Эксклюзив (гор/фед) (КК) (SS)"                               ,"01.01.80 00:00","31.12.09 23:59"],
["Хабаровск - Эксклюзив07 (гор/фед) (КК) (SS)"                             ,"01.01.80 00:00","31.12.09 23:59"],
["Хабаровск - Эксклюзив07 корпоративный (гор/фед) (КОРП) (SS)"             ,"01.01.80 00:00","31.12.09 23:59"],
["Хабаровск - Экспресс (гор/фед) (КОРП) (SS)"                              ,"01.01.80 00:00","31.12.09 23:59"],
     ]                                                                     ,
"closed":
    [["Хабаровск - Бизнес 200 (гор/фед) (КТП) (SS)"                        ,"01.01.80 00:00","31.12.08 23:59"],
["Хабаровск - Любимый (фед) (ПРП) (IN)"                                    ,"01.01.80 00:00","31.12.08 23:59"],
["Хабаровск - RED07 (фед) (ПРП) (IN)"                                      ,"01.01.80 00:00","31.12.08 23:59"],
["Хабаровск - Бизнес 400 (гор/фед) (КТП) (SS)"                             ,"01.01.80 00:00","31.12.08 23:59"],
["Хабаровск - Оптима 100 (гор/фед) (КТП) (SS)"                             ,"01.01.80 00:00","31.12.08 23:59"],
["Хабаровск - Оптима 50 (гор/фед) (КТП) (SS)"                              ,"01.01.80 00:00","31.12.08 23:59"],
["Хабаровск - Оптима День (гор/фед) (КТП) (SS)"                            ,"01.01.80 00:00","31.12.08 23:59"],
["Хабаровск - Оптима День* (гор/фед) (КТП) (SS)"                           ,"01.01.80 00:00","31.12.08 23:59"],
["Хабаровск - Профи 300.07 (гор/фед) (КТП) (SS)"                           ,"01.01.80 00:00","31.12.08 23:59"],
["Хабаровск - Профи 60 (гор/фед) (КТП) (SS)"                               ,"01.01.80 00:00","31.12.08 23:59"],
["Хабаровск - Профи 60.07 (гор/фед) (КТП) (SS)"                            ,"01.01.80 00:00","31.12.08 23:59"],
["Хабаровск - Профи 700.new VIP (гор/фед) (КК) (SS)"                       ,"01.01.80 00:00","31.12.08 23:59"],
["Хабаровск - Свободный (гор/фед) (КТП) (SS)"                              ,"01.01.80 00:00","31.12.08 23:59"],
["Хабаровск - Свободный - И (гор/фед) (КТП) (SS)"                          ,"01.01.80 00:00","31.12.08 23:59"],
["Хабаровск - Универсальный (фед) (ПРП) (IN)"                              ,"01.01.80 00:00","31.12.08 23:59"],
# ["Хабаровск - Хот Джинс поминутно 2009_61 (фед) (ПРП) (IN)"              , "01.01.80 00:00","31.12.08 23:59"],
["Хабаровск - Супер Джинс поминутно 2009_1 (фед) (ПРП) (IN)"               ,"01.01.80 00:00","31.12.08 23:59"],
["Хабаровск - Супер Джинс поминутно 2009_61 (фед) (ПРП) (IN)"              ,"01.01.80 00:00","31.12.08 23:59"],
# ["Хабаровск - Рубль (фед) (ПРП) (IN)"                                    ,"01.01.80 00:00","31.12.08 23:59"],
["Хабаровск - Свободный (фед) (ПРП) (IN)"                                  ,"01.01.80 00:00","31.12.08 23:59"],
["Хабаровск - Первый (фед) (ПРП) (IN)"                                     ,"01.01.80 00:00","31.12.08 23:59"],
["Хабаровск - Подарок (фед) (ПРП) (IN)"                                    ,"01.01.80 00:00","31.12.08 23:59"],
["Хабаровск - Джинс 007 поминутно 2009_1 (фед) (ПРП) (IN)"                 ,"01.01.80 00:00","31.12.08 23:59"],
["Хабаровск - Джинс 007 поминутно 2009_61 (фед) (ПРП) (IN)"                ,"01.01.80 00:00","31.12.08 23:59"],
["Хабаровск - Базовый09 (фед) (ПРП) (IN)"                                  ,"01.01.80 00:00","31.12.08 23:59"],
["Хабаровск - Базовый (фед) (ПРП) (IN)"                                    ,"01.01.80 00:00","31.12.08 23:59"],
["Хабаровск - Все свои (фед) (ПРП) (IN)"                                   ,"01.01.80 00:00","31.12.08 23:59"],
["Хабаровск - Все свои + (фед) (ПРП) (IN)"                                 ,"01.01.80 00:00","31.12.08 23:59"],
["Хабаровск - RED_text (фед) (ПРП) (IN)"                                   ,"01.01.80 00:00","31.12.08 23:59"],
["Хабаровск - МТС. Команда' (гор/фед) (КОРП) (SS)"                         ,"01.01.80 00:00","31.12.08 23:59"],
["Хабаровск - Команда (гор/фед) (КОРП) (SS)"                               ,"01.01.80 00:00","31.12.08 23:59"],
["Хабаровск - Корпорация I (гор/фед) (КОРП) (SS)"                          ,"01.01.80 00:00","31.12.08 23:59"],
["Хабаровск - Престиж  (гор/фед) (КОРП) (SS)"                              ,"01.01.80 00:00","31.12.08 23:59"],
["Хабаровск - Территория бизнеса (гор/фед) (КОРП) (SS)"                    ,"01.01.80 00:00","31.12.08 23:59"],
["Хабаровск - RED (фед) (ПРП) (IN)"                                        ,"01.01.80 00:00","31.12.08 23:59"],
["Хабаровск - Первый07 (фед) (ПРП) (IN)"                                   ,"01.01.80 00:00","31.12.08 23:59"],
        ]                                                                  ,
"emptydate":
 [["" ,"01.01.80 00:00","01.01.80 00:00"],
 ["" ,"01.01.10 00:00","31.12.10 23:59"]],
 "arpu0-135old":
 [["" ,"01.01.80 00:00","31.12.08 23:59",0,135]],
 "arpu0-135new":
 [["" ,"01.01.09 00:00","31.12.09 23:59",0,135]],
 "arpu136-350":
 [["" ,"01.01.80 00:00","31.12.09 23:59",136,350]],
 "arpu351-750":
    [["" ,"01.01.80 00:00","31.12.09 23:59",351,750]],
 "arpu751-999999":
    [["" ,"01.01.80 00:00","31.12.09 23:59",751,999999]]
}


def splitFile(inputFile,restFile,matchedFile,processFile,pattern):
    """
    Split inputFile to matchedFile and restFile with using conditions in processFile and pattern.
    """
    ifl = open(inputFile,"rb")
    rdr = csv.reader(ifl)
    rp = open(restFile,"wb")
    mp = open(matchedFile,"wb")    
    wrtrRP = csv.writer(rp,dialect = 'excel')
    wrtrMP = csv.writer(mp,dialect = 'excel')
    processFile(rdr,wrtrRP,wrtrMP,pattern)
    rp.close()
    mp.close()
    ifl.close()

def tarif(rdr,wrtrY,wrtrN,patlst):
    """
    """
    for rec in rdr:
        wrtrY.writerow([rec[0]])

def identy(rdr,wrtrY,wrtrN,patlst):
    """
    Identical processing. Input = Output
    """
    for rec in rdr:
        wrtrY.writerow(rec)

def changeColumns(rdr,wrtrY,wrtrN,patlst):
    for rec in rdr:
        wrtrY.writerow([rec[1],rec[0],rec[2],rec[3],rec[4],rec[5]])

def addColumns(rdr,wrtrY,wrtrN,patlst):
    for rec in rdr:
        rc.append(str(arpu+arpuAP))
        rc.append(str(arpu))
        rc.append(str(arpuAP))
        rc.append(str(dactiv.isoformat()))
        wrtrY.writerow(rc)
        arpu = 0
        arpuAP = 0
        try:
            arpu = arpu + int(rec[3])
            arpuAP = arpuAP + int(rec[4])
        except:
            pass

def addcat(rdr,wrtrY,wrtrN,patlst):
    for rec in rdr:
        rc = rec
        rc.append(patlst[0])
        wrtrY.writerow(rc)

def colupto3(rdr,wrtrY,wrtrN,patlst):
    tmp = [1,2]
    tmpoct=[]
    tmpdec=[]
    tmpnov=[]
    arpu = 0
    arpuAP = 0
    flg = False
    for rec in rdr:
        rc = []
        if (tmp[1]<>rec[1]) and flg:
            if tmpoct<>[]:
                rc.append(str(dactiv.isoformat()))            
                rc.append(str(arpu+arpuAP))
                rc.append(str(arpu))
                rc.append(str(arpuAP))
                rc.extend(tmpoct)
                wrtrY.writerow(rc)
                rc = []
            # else:
            #     rc.extend(["","","","","",""])
            if tmpnov<>[]:
                rc.append(str(dactiv.isoformat()))            
                rc.append(str(arpu+arpuAP))
                rc.append(str(arpu))
                rc.append(str(arpuAP))
                rc.extend(tmpnov)
                wrtrY.writerow(rc)
                rc = []
            # else:
            #     rc.extend(["","","","","",""])
            if tmpdec<>[]:
                rc.append(str(dactiv.isoformat()))            
                rc.append(str(arpu+arpuAP))
                rc.append(str(arpu))
                rc.append(str(arpuAP))
                rc.extend(tmpdec)
                wrtrY.writerow(rc)
                rc = []
            # else:
            #     rc.extend(["","","","","",""])            
            # wrtrY.writerow(rc)
            tmpoct=[]
            tmpnov=[]
            tmpdec=[]
            arpu = 0
            arpuAP = 0
        flg = True
        tmp = rec
        if tmp[5]=="dec":
            try:
                arpu = arpu + int(tmp[3])
                arpuAP = arpuAP + int(tmp[4])
            except:
                pass
            dactiv = hronlib.string2date(str(tmp[2]))
            tmpdec=tmp
        if tmp[5]=="oct":
            try:
                arpu = arpu + int(tmp[3])
                arpuAP = arpuAP + int(tmp[4])
            except:
                pass
            dactiv = hronlib.string2date(str(tmp[2]))
            tmpoct=tmp
        if tmp[5]=="nov":
            try:
                arpu = arpu + int(tmp[3])
                arpuAP = arpuAP + int(tmp[4])
            except:
                pass
            dactiv = hronlib.string2date(str(tmp[2]))
            tmpnov=tmp


def makeRandomSample(rdr,rest,matched,patlst):
    """
    """
    pat = str(random.randint(10,24)) + ":" + str(random.randint(10,59))
    for rec in rdr:
        if rec[2].find(pat) <> -1:
            matched.writerow(rec)

def diffTest(inp,out):
    """
    Read file and write. Diff results.
    """
    if not os.system("diff " + inp + " " + out):
        return "diff test success."
    else:
        return "diff test failed."

def splitTest(inputFile,restFile,matchedFile):
    print "lines"
    os.system("wc -l " + inputFile)
    print "lines"
    os.system("wc -l " + restFile)
    print "lines"
    os.system("wc -l " + matchedFile)
    

def patternSplit(rdr,rest,matched,patternsList):
    """
    """
    s2d = hronlib.string2date
    for rec in rdr:
        activ = s2d(rec[2])
        flg = True
        for pat in patternsList:
            ldate = sd2(pat[1])
            rdate = s2d(pat[2])
            try:
                larpu = int(pat[3])
                rarpu = int(pat[4])
            except:
                pass
            if (rec[0].find(pat[0]) <> -1):
                flg = not flg
                break
                if activ>=ldate and activ<=rdate:
                    try:
                        if toggleAP:
                            arpu = int(rec[4]) # ARPU AP
                        else:
                            arpu = int(rec[3]) # ARPU without AP
                        if arpu>=larpu and arpu<=rarpu:
                            flg = not flg
                            break
                    except:
                        flg = not flg
                        break
        if not flg:
            matched.writerow([rec[0],rec[1],rec[2],rec[3],rec[4],rec[5],hronlib.timelive(rdate,activ)/30.,globPAT])
        else:
            rest.writerow([rec[0],rec[1],rec[2],rec[3],rec[4],rec[5]])

def averageDate(rdr,rest,matched,patternsList):
    """
    """
    s2d = hronlib.string2date
    minDate = s2d("01.01.80 00:00")
    maxDate = s2d("01.01.20 00:00")
    maxDateForPattern = []
    minDateForPattern = []     
    for pat in patternsList:
        maxDateForPattern.append([pat[0],minDate])
        minDateForPattern.append([pat[0],maxDate])        
    maxDateForPattern = dict(maxDateForPattern)
    minDateForPattern = dict(minDateForPattern)
    
    for rec in rdr:
        activationDate = s2d(rec[2])
        maxDP = maxDateForPattern[rec[0]]
        minDP = minDateForPattern[rec[0]]
        matched = False
        for pat in patternsList:
            lowLimitDate = s2d(pat[1])
            highLimitDate = s2d(pat[2])
            try:
                larpu = int(pat[3])
                rarpu = int(pat[4])
            except:
                pass
            if (rec[0].find(pat[0]) <> -1):
                if activationDate>=lowLimitDate and activationDate<=highLimitDate:
                    if activationDate>maxDP:
                        maxDP = activationDate
                    if activationDate<minDP and activationDate<>minDate:
                        minDP = activationDate
                    matched = not matched
                    break
        if matched:
            timelive = hronlib.timelive(highLimitDate,activationDate)/30.
            matched.writerow([rec[0],rec[1],rec[2],rec[3],rec[4],rec[5],timelive,globPAT])
        else:
            rest.writerow(rec[0:6])
    for pat in patternsList:
        maxDP = maxDateForPattern[pat[0]]
        minDP = minDateForPattern[pat[0]]
        averageDate = minDP + datetime.timedelta((hronlib.timelive(maxDP,minDate) -
                                                  hronlib.timelive(minDP,minDate))/2.)
        matched.writerow([pat[0], maxDP, minDP, str(averageDate)])


def patnoempty(rdr,wrtrY,wrtrN,patlst):
    """
    """
    datesclosed = {
"Хабаровск - Бизнес 200 (гор/фед) (КТП) (SS)":"08.03.02 14:39",
"Хабаровск - Любимый (фед) (ПРП) (IN)":"06.12.03 18:03",
"Хабаровск - RED07 (фед) (ПРП) (IN)":"06.10.04 02:30",
"Хабаровск - Бизнес 400 (гор/фед) (КТП) (SS)":"30.05.01 16:33",
"Хабаровск - Оптима 100 (гор/фед) (КТП) (SS)":"04.07.02 02:33",
"Хабаровск - Оптима 50 (гор/фед) (КТП) (SS)":"20.04.02 15:13",
"Хабаровск - Оптима День (гор/фед) (КТП) (SS)":"05.05.03 03:48",
"Хабаровск - Оптима День* (гор/фед) (КТП) (SS)":"02.04.03 02:58",
"Хабаровск - Профи 300.07 (гор/фед) (КТП) (SS)":"19.09.03 16:29",
"Хабаровск - Профи 60 (гор/фед) (КТП) (SS)":"08.03.03 16:03",
"Хабаровск - Профи 60.07 (гор/фед) (КТП) (SS)":"07.10.03 04:36",
"Хабаровск - Профи 700.new VIP (гор/фед) (КК) (SS)":"11.10.03 00:48",
"Хабаровск - Свободный (гор/фед) (КТП) (SS)":"24.05.02 12:05",
"Хабаровск - Свободный - И (гор/фед) (КТП) (SS)":"05.07.05 15:02",
"Хабаровск - Универсальный (фед) (ПРП) (IN)":"12.09.03 11:52",
"Хабаровск - Супер Джинс поминутно 2009_1 (фед) (ПРП) (IN)":"02.02.03 20:45",
"Хабаровск - Супер Джинс поминутно 2009_61 (фед) (ПРП) (IN)":"22.06.03 03:01",
"Хабаровск - Свободный (фед) (ПРП) (IN)":"25.06.04 14:58",
"Хабаровск - Первый (фед) (ПРП) (IN)":"31.01.04 04:30",
"Хабаровск - Подарок (фед) (ПРП) (IN)":"09.07.04 15:19",
"Хабаровск - Джинс 007 поминутно 2009_1 (фед) (ПРП) (IN)":"09.01.03 06:31",
"Хабаровск - Джинс 007 поминутно 2009_61 (фед) (ПРП) (IN)":"11.11.02 15:53",
"Хабаровск - Базовый09 (фед) (ПРП) (IN)":"07.08.04 05:46",
"Хабаровск - Базовый (фед) (ПРП) (IN)":"11.05.06 00:29",
"Хабаровск - Все свои (фед) (ПРП) (IN)":"17.11.04 03:48",
"Хабаровск - Все свои + (фед) (ПРП) (IN)":"08.10.03 05:05",
"Хабаровск - RED_text (фед) (ПРП) (IN)":"27.09.04 12:41",
"Хабаровск - МТС. Команда' (гор/фед) (КОРП) (SS)":"26.06.03 16:47",
"Хабаровск - Команда (гор/фед) (КОРП) (SS)":"20.10.03 15:50",
"Хабаровск - Корпорация I (гор/фед) (КОРП) (SS)":"16.10.03 01:18",
"Хабаровск - Престиж  (гор/фед) (КОРП) (SS)":"11.09.04 15:54",
"Хабаровск - Территория бизнеса (гор/фед) (КОРП) (SS)":"24.05.04 15:01",
"Хабаровск - RED (фед) (ПРП) (IN)":"02.09.04 01:37",
"Хабаровск - Первый07 (фед) (ПРП) (IN)":"30.06.04 18:16"
}
    for rec in rdr:
        activ = hronlib.string2date(rec[2])
        flg = True
        for pat in patlst:
            ldate = hronlib.string2date(pat[1])
            rdate = hronlib.string2date(pat[2])
            if (rec[0].find(pat[0]) <> -1):
                flg = not flg
                break
        if not flg:
            if rec[2]=="":
                rdate = hronlib.string2date("31.12.09 23:59")
                if rec[0] in datesclosed:
                    wrtrN.writerow([rec[0],rec[1],datesclosed[rec[0]],rec[3],rec[4],rec[5],hronlib.timelive(rdate,hronlib.string2date(datesclosed[rec[0]]))/30.])
                else:
                    wrtrN.writerow([rec[0],rec[1],"01.01.09 00:00",rec[3],rec[4],rec[5],hronlib.timelive(rdate,hronlib.string2date("01.01.09 00:00"))/30.])
            else:
                # no empty entries move to rest
                wrtrY.writerow([rec[0],rec[1],rec[2],rec[3],rec[4],rec[5],hronlib.timelive(rdate,hronlib.string2date("01.01.09 00:00"))/30.])
        else:
            wrtrY.writerow([rec[0],rec[1],rec[2],rec[3],rec[4],rec[5]])


def month3(rdr,wrtrY,wrtrN,patlst):
    flg = False
    tmp = [1]
    tmpoct=[]
    tmpdec=[]
    tmpnov=[]
    arpu3low = 999999
    for rec in rdr:
        rc = []
        if (tmp[0]<>rec[0]) and flg:
            if tmpoct<>[] and tmpnov<>[] and tmpdec<>[]:
                arpu3low = int(tmpoct[3])+int(tmpnov[3])+int(tmpdec[3])
            else:
                arpu3low = 999999
        rc.append(tmp[1])
        rc.extend(tmpoct)
        rc.extend(tmpnov)
        rc.extend(tmpdec)
        wrtr.writerow(rc)
        tmpoct=[]
        tmpnov=[]
        tmpdec=[]
        
        flg = True
        tmp = rec
        if tmp[5]=="dec":
            tmpdec=tmp
        if tmp[5]=="oct":
            tmpoct=tmp
        if tmp[5]=="nov":
            tmpnov=tmp

    if tmpoct<>[] and tmpnov<>[] and tmpdec<>[]:
        arpu3low = int(tmpoct[3])+int(tmpnov[3])+int(tmpdec[3])
    else:
        arpu3low = 999999

    rc.extend(tmpoct)
    rc.extend(tmpnov)
    rc.extend(tmpdec)
    wrtrY.writerow(rc)


def makeSegmentation(inputFile,pattern):
    """
    """
    patternsList = segments[pattern]
    restFile = inputFile + "-" + pattern
    matchedFile = pattern + "-from-" + inputFile
    splitFile(inputFile,restFile,matchedFile,patternSplit,patternsList)
    # splitFile(inputFile,restFile,matchedFile,patnoempty,patternsList)
    splitTest(inputFile,restFile,matchedFile)

if __name__ == '__main__':
    """
    ./do.py
    ./do.py input.csv output &
    ps -e | grep bash
    """
    finput = sys.argv[1]
    # patterns = ["except","emptydate","arpu0-135new","mvpc","mass","hvpc","arpu0-135old","arpu136-350","arpu351-750","arpu751-999999"]
    patterns = ["except"]
    toggleAP = False
    addSegmentName = ""
    for pattern in patterns:
        globPAT = pattern
        makeSegmentation(finput + addSegmentName,pattern)
        addSegmentName = addSegmentName + "-" + pattern
    # print "only splited"
        print "split ", pattern + "-from-" + finput + addSegmentName

    # splitFile(finput,"fileY","fileN",makeRandomSample,[])
    
    
    # forced out make global var
    # toggleAP = True
    # patterns = ["arpu0-135old","arpu0-135new","arpu136-350","arpu351-750","arpu751-999999"]
    # finput = finput + "-emptydate-except-mvpc-mass-hvpc"
    # os.system("mv " + finput + " " + finput + "-AP")
    # finput = finput + "-AP"
    # addSegmentName = ""
    # for pattern in patterns:
    #     makeSegmentation(finput + addSegmentName,pattern)
    #     addSegmentName = addSegmentName + "-" + pattern

    # # makeSegmentation(finput,"emptydate")    
    # # makeSegmentation("emptydate","except")
    # # makeSegmentation(finput+"-emptydate-except","mvpc")
    # # makeSegmentation(finput+"-emptydate-except-mvpc","mass")
    # # makeSegmentation(finput+"-emptydate-except-mvpc-mass","hvpc")
    # splitFile(finput,finput+"-up3","tmp",colupto3,[])    
    # splitFile(finput,finput+"-tarif","tmp",tarif,[])
    # # os.system("sort -r " + finput+"-up3 > "+finput+"-up3-sort")
    # # os.system("sort -n " + finput+"-up3 > "+finput+"-up3-sort")
    # tarifs = open("tarif-sort","rb").readlines()
    # i = 100
    # for tar in tarifs:
    #     filt = tar.split(" (")[0]
    #     os.system("grep -e \"" + filt + " (\" \""+finput + "-up3\" > \"" + str(i)+"\"")
    #     # os.system("grep -e \"" + "dec" + "\" \""+str(i) + "\" > \"" + str(i) + "-dec\"")
    #     # os.system("grep -e \"" + "nov" + "\" \""+str(i) + "\" > \"" + str(i) + "-nov\"")
    #     # os.system("grep -e \"" + "oct" + "\" \""+str(i) + "\" > \"" + str(i) + "-oct\"")
    #     i = i + 1
        
    # splitFile(finput,finput + "-category","tmp",addcat,[sys.argv[2]])        
        
        
 
