#!/usr/bin/env python3

class Vehicle(object):

    def __init__(self, vin, cat, mileage=0, drivers=[]):
        self.vin = vin
        self.cat = cat
        self.mileage = mileage
        self.drivers = drivers

    def __str__(self):
        slist = []
        slist.append('ID: {}'.format(self.vin))
        slist.append('Category: {}'.format(self.cat))
        slist.append('Mileage: {}'.format(self.mileage))
        slist.append('Drivers: {}'.format(', '.join(self.drivers)))
        return '\n'.join(slist)


class Fleet(object):

    def __init__(self):
        self.f = {}

    def add(self, v):
        self.f[v.vin] = v

    def remove(self, v):
        if v in self.f:
            del self.f[v]

    def lookup(self, v):
        if v in self.f:
            return self.f[v]
        return None

    def get_drivers_by_category(self, scat):
        alist = []
        for v in self.f.values():
            if scat in v.cat:
                for d in v.drivers:
                    if d not in alist:
                        alist.append(d)
        #need to get names out the obj in alist
        return len(alist)
