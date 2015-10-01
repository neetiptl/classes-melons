"""This file should have our melon-type classes in it."""

class MelonOrder(object):

    def get_base_price(self):
        BASE_MELON_PRICE = 5.0
        return BASE_MELON_PRICE

class WatermelonOrder(MelonOrder):
    species = "Watermelon"
    color = "green"
    imported = False
    shape = 'natural'
    seasons = ['Fall', 'Summer']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""
        total = self.get_base_price() * qty
        if qty >= 3:
            total = total *.75
        return total

class CantalopeOrder(MelonOrder):
    species = "Cantalope"
    color = "tan"
    imported = False
    shape = 'natural'
    seasons = ['Spring', 'Summer']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""

        total = self.get_base_price() * qty
        if qty >= 5.0:
            total = total/2
        return total

class CasabaOrder(MelonOrder):
    species = "Casaba"
    color = "green"
    imported = True
    shape = 'natural'
    seasons = ['Spring','Winter', 'Fall', 'Summer']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""
        total =  ((self.get_base_price() +1.0)*1.5)*qty
        return total

class SharlynOrder(MelonOrder):
    species = "Sharlyn"
    color = "tan"
    imported = True
    shape = 'natural'
    seasons = [ 'Summer']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""
        total = (self.get_price()*1.5) * qty
        return total


class SantaClausOrder(MelonOrder):
    species = "SantaClaus"
    color = "green"
    imported = True
    shape = 'natural'
    seasons = ['Winter', 'Spring']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""
        total =  self.get_base_price() *1.5 * qty
        return total

class ChristmasOrder(MelonOrder):
    species = "Christmas"
    color = "green"
    imported = False
    shape = 'natural'
    seasons = ['Winter']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""
        total =  self.get_base_price()* qty
        return total

class HornedMelonOrder(MelonOrder):
    species = "HornedMelon"
    color = "yellow"
    imported = True
    shape = 'natural'
    seasons = [ 'Summer']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""
        total =  self.get_base_price() *1.5 * qty
        return total

class XiguaOrder(MelonOrder):
    species = "Xigua"
    color = "black"
    imported = True
    shape = 'square'
    seasons = ['Summer']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""
        total =  self.get_base_price()*3 *qty
        return total

class OgenOrder(MelonOrder):
    species = "Ogen"
    color = "tan"
    imported = False
    shape = 'natural'
    seasons = ['Spring', 'Summer']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""
        total =  (self.get_base_price() +1) * qty
        return total
