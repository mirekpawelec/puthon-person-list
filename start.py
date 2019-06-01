import csv
import string
import random
from model.osoba import Osoba

osoby = []

def wczytaj_osoby():
    try:
        plik = open('osoby.csv', 'r')
        csv_reader = csv.reader(plik)
        for row in csv_reader:
            if len(row) != 3:
                continue
            osoba = Osoba(row[0], row[1], row[2])
            osoby.append(osoba)
    except FileNotFoundError:
        plik = open('osoby.csv', 'w')
        plik.close()

def wygeneruj_haslo():
    haslo = ''
    string_set = string.ascii_letters + string.digits
    for sign in range(10):
        haslo += random.choice(string_set)
    return haslo

def dodaj_osobe():
    imie = input('Podaj imie: ')
    while len(imie) < 1:
        imie = input('Niepoprawna wartość. Podaj imie ponownie: ')
    nowa_osoba = Osoba(len(osoby), imie, wygeneruj_haslo())
    plik = open('osoby.csv', 'a')
    csv_writer = csv.writer(plik, delimiter=',')
    csv_writer.writerow(nowa_osoba.get_row())
    print('dodałeś osobe')
    plik.close()

def zapytaj_czy_pokazac_osoby():
    if input('Czy wczytać listę? [T/N]').lower() == 't':
        for osoba in osoby:
            print(osoba.__str__())

def zapytaj_czy_dodac_osobe():
    if input('Czy chcesz dodać nową osobę? [T/N]').lower() == 't':
        dodaj_osobe()

wczytaj_osoby()
zapytaj_czy_pokazac_osoby()
zapytaj_czy_dodac_osobe()
