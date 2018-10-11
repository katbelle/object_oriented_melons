"""Classes for melon orders."""
import random
from datetime import datetime


class TooManyMelonsError(ValueError):
	pass
	# def __init__(self, expression):
	# 	self.expression = expression
	# 	self.message = "That's too many melons!"

class AbstractMelonOrder():
	"""Generic Melon Order"""

	def __init__(self, species, qty):
		"""Initialize melon order attributes."""
		if qty > 100:
			raise TooManyMelonsError
		self.species = species
		self.qty = qty
		self.shipped = False
		self.order_type = ""
		self.tax = 0
		self.order_time = datetime.now()
		# self.order_time = datetime(2018, 10, 13, 8,30,0,0)

	def get_base_price(self):
		"""Determine the base price of melon"""
		
		baseprice = random.randint(5,10)
		# print("baseprice from get_base_price method is originally {}".format(baseprice))
		
		#check for weekday and check for time
		#if mon-fri and in the rush hour time, then baseprice is 4+baseprice
		weekday = self.order_time.weekday()
		hour = self.order_time.time().hour
		if weekday >=0 and weekday <5:
			if hour >=8 and hour <=11:
				baseprice += 4
				# print("baseprice from get_base_price method is now changed to {}".format(baseprice))

		return baseprice

	def get_total(self):
		"""Calculate price, including tax."""
		base_price = self.get_base_price()
		# print("base_price from the get total method is {}".format(base_price))
		
		if self.species == "christmas":
			base_price = 1.5*base_price

		total = (1 + self.tax) * self.qty * base_price

		return total

	def mark_shipped(self):
		"""Record the fact than an order has been shipped."""

		self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder):
	"""A melon order within the USA."""
	def __init__(self, species, qty):
		super().__init__(species,qty)
		self.order_type = "domestic"
		self.tax = 0.08



class InternationalMelonOrder(AbstractMelonOrder):
	"""An international (non-US) melon order."""

	def __init__(self, species, qty, country_code):
		"""Initialize melon order attributes."""

		super().__init__(species,qty)
		self.country_code = country_code
		self.order_type = "international"
		self.tax = 0.17

	def get_total(self):
		total = super().get_total()
		if self.qty < 10:
			total += 3

		return total


	def get_country_code(self):
		"""Return the country code."""

		return self.country_code


class GovernmentMelonOrder(AbstractMelonOrder):

	def __init__(self, species, qty):

		super().__init__(species,qty)
		self.tax = 0
		self.passed_inspection = False

	def mark_inspection(self, passed):
		self.passed_inspection = passed
