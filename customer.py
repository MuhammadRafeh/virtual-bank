"""
File Name: customer.py
Here Defines The customer Class 
"""
import pickle

class Customer():
	"""This class will sign up/creates the new customers. If someone is registered then he can
	view her details."""

	def __init__(self):
		"""I have set username for uniqueness or differentiate between customers.
		Loading a signup.pickle file to load our registered customers dictionary"""
		file = open('signup.pickle', 'rb')
		self.signup = pickle.load(file)
		file.close()

		"""If username is already registered then we are offering a user to view her detail"""
		#if username in self.signup.keys():
		#	flag = False
		#	print('You are already Registered!')
		#	if input('Enter Password for login: ')==self.signup[username][0]:
		#		if input('Do you want to view your information (y/n): ').lower()=='y':
		#			self.view_personal_information(username)
		#	else:
		#		print('Invalid Password!')

		"""If username is not registered then we are offering a user to register"""
		#if  flag and input('Do you want to sign up (y/n): ').lower()=='y':
		#	self.get_personal_information(username)

	def get_personal_information(self, username):
		"""[password, name, addressline1, addressline2, city, state, zipcode, country, phonenumber,
		phonenumbertype, email, are-you-a-us-citizen, do-you-have-double-citizenship,
		countryofresidence, dateofbirth, source-of-income] that's a order of an array"""

		self.username = username
		self.password = input('Enter Password: ')
		self.name = input('Enter Full name: ')
		self.address_line_1 = input('Enter Address Line 1: ')
		self.address_line_2 = input('Enter Address Line 2: ')
		self.city = input('Enter City: ')
		self.state = input('Enter State: ')
		self.zip_code = input('Enter Zip Code: ')
		self.country = input('Enter Country: ')
		self.phone_number = input('Enter Phone Number: ')
		self.phone_number_type = input('Enter Phone Number Type: ')
		self.email = input('Enter Email: ')
		self.are_you_a_us_citizen = input('Are you a US citizen (y/n): ')
		self.do_you_have_double_citizenship = input('Do you have double Citizenship (y/n): ')
		self.country_of_residence = input('Where are you currently living: ')
		self.date_of_birth = input('Enter your date of birth (MM/DD/YY): ')
		self.source_of_income = input('Source of Income: ')
		print('\n***********************Sign Up Successful!********************************\n')


		"""Creating a list of the new Customer """
		self.list_of_new_customer = [self.password, self.name, self.address_line_1, self.address_line_2, self.city, self.state, self.zip_code,
		self.country, self.phone_number, self.phone_number_type, self.email, self.are_you_a_us_citizen,
		self.do_you_have_double_citizenship, self.country_of_residence, self.date_of_birth, self.source_of_income]

		"""Adding above list to the dictionary and serializing"""
		self.signup[username] = self.list_of_new_customer
		file = open('signup.pickle', 'wb')
		pickle.dump(self.signup, file)
		file.close()

	def view_personal_information(self, username):
		"""Printing out the personal information of the User"""

		printable_guidance = ['Password: ', 'Name: ', 'Address line1: ', 'Address line2: ', 'City: ', 'State: ', 'Zipcode: ', 'Country: ',
		'phone number: ', 'Phone number type: ', 'Email: ', 'Are you a us citizen: ', 'Do you have double citizenship: ',
		'Country of residence: ', 'Date of birth: ', 'Source of income: ']
		file = open('signup.pickle', 'rb')
		signup = pickle.load(file)
		print('')
		for i, j in zip(printable_guidance, signup[username]):
			print(i, j)
		print('')
		file.close()



