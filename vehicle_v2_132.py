#!/usr/bin/env python3

class Vehicle(object):

    def __init__(self, vin, cat, mileage=0, drivers=[]):
        self.vin = vin
        self.cat = cat
        self.mileage = mileage
        self.drivers = drivers

    def add_driver(self, d):
        if d not in self.drivers:
            self.drivers.append(d)
        else:
            return 'The driver {} has already been added'.format(d)

    def __str__(self):
        slist = []
        slist.append('ID: {}'.format(self.vin))
        slist.append('Category: {}'.format(self.cat))
        slist.append('Mileage: {}'.format(self.mileage))
        slist.append('Drivers: {}'.format(', '.join(self.drivers)))
        return '\n'.join(slist)
