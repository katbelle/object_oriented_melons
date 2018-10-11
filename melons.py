"""Classes for melon orders."""

class AbstractMelonOrder():
	"""Generic Melon Order"""

	def __init__(self, species, qty):
		"""Initialize melon order attributes."""

		self.species = species
		self.qty = qty
		self.shipped = False
		self.order_type = ""
		self.tax = None

	def get_total(self):
		"""Calculate price, including tax."""
		base_price = 5
		
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
