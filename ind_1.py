#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def add(staff):
    # Запросить данные о работнике.
    point1 = input("Откуда? ")
    point2 = input("Куда? ")
    routeNumber = int(input("Номер маршрута? "))

    route = {
        'point1': point1,
        'point2': point2,
        'routeNumber': routeNumber,
    }

    staff.append(route)

    if len(staff) > 1:
        staff.sort(key=lambda item: item.get('routeNumber', ''))

def info(staff, command):
    parts = command.split(' ', maxsplit=2)
    city = str(parts[1])
    line = '+-{}-+-{}-+-{}-+'.format(
        '-' * 5,
        '-' * 20,
        '-' * 20,
    )

    count = 0
    for route in staff:
        if route.get('point1', '') == city or route.get('point2', '') == city:
            print(line)
            print(
                '| {:>5} | {:<20} | {:<20} |'.format(
                    route.get('routeNumber', 0),
                    route.get('point1', ''),
                    route.get('point2', '')
                )
            )
            count += 1

    if count > 0:
        print(line)
    else:
        print('Таких маршрутов нет')


if __name__ == '__main__':
    routes = []

    while True:
        command = input(">>> ").lower()

        if command == 'exit':
            break

        elif command == 'add':
            add(routes)

        elif command.startswith("info "):
            info(routes, command)
