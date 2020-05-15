"""
File Name: bank.py
This Main Module Defines The Bank Class
"""

"""Importing our main modules/features of this Bank"""
import pickle
import time as tm
import datetime as dt
from customer import Customer
from advantagesavings import AdvantageSavings
from safebalancechecking import SafeBalanceChecking
from advantagepluschecking import AdvantagePlusChecking
from advantagerelationshipchecking import AdvantageRelationshipChecking


class Bank():
	"""This class represents the collection of
	Safe Balance Checking Class,
	Advantage Relationship Checking Class,
	Advantage plus Checking Class and 
	Advantage Savings Class."""
	print('')

	def __init__(self, username):

		self.delta = dt.timedelta(days = 30)

		print('1- Do you want to register with bank account\n2- If you have, proceed further\n')
		user_choice = input('Choose from above and Enter: ')
		self.username = username

		file = open('accounts.pickle', 'rb')
		self.accounts = pickle.load(file)
		file.close()

		"""Asking for creating an account"""
		if user_choice=='1':

			while True:
				print('\n1- Safe Balance Checking\n2- Advantage Relationship Checking\n3- Advantage plus Checking')
				print('4- Advantage Savings\n5- Exit\n')
				account_choice = input('Choose from above and Enter: ').lower()
				print('')
				if account_choice=='1':
					self.add_account(1, input("Enter new Pin: "), int(input('Initial balance: ')), input("Enter Name: "))
					
				elif account_choice=='2':
					self.add_account(2, input("Enter new Pin: "), int(input('Initial balance: ')), input("Enter Name: "))
					
				elif account_choice=='3':
					self.add_account(3, input("Enter new Pin: "), int(input('Initial balance: ')), input("Enter Name: "))
					
				elif account_choice=='4':
					self.add_account(4, input("Enter new Pin: "), int(input('Initial balance: ')), input("Enter Name: "))
					
				elif account_choice=='5':
					print("****************Thanks for using the bank of America*****************")
					break
				if input('Do you want to register another Account (y/n): ')=='n':
					print('\n***************Thanks for using the Bank of America***************')
					break

		elif user_choice=='2':
			print('\n********Which account you want to Use*********\n')
			print('1- Safe Balance Checking\n2- Advantage Relationship Checking\n3- Advantage plus Checking')
			print('4- Advantage Savings\n')
			account_choice = input('Choose from above and Enter: ')
			print('')

			"""Checking if account exists or not"""
			self.result = self.checking(account_choice)
			if self.result=='n':
				print('\n********This Bank Account does not Exist!********')
				raise SystemExit

			self.maintenance()
			
			"""Actions that user can perform"""
			while True:
				"""Printing out the actions that user can perform"""
				print('1- Do you want to remove your account\n2- Do you want to deposit money')
				print('3- Do you want to withdraw\n4- Do you want to transfer money')
				print('5- Do you want to see your Account Info\n6- Cancel\n')
				further_choice = input('Choose from above and Enter: ')
				print('')
				if further_choice=='1':
					self.remove_account(account_choice)
					print('\n******This Bank account has been Deleted!******')
					break
				elif further_choice=='2':
					self.deposit(int(input('Enter Amount i.e 54000: ')))

				elif further_choice=='3':
					self.withdraw(int(input('Enter Amount i.e 54000: ')))

				elif further_choice=='4':
					amount = int(input('Enter Amount i.e 54000: '))
					username = input('Please Enter username of account you want to transfer: ')
					account_type = input('Please enter Account type i.e (sbc, apc, arc, as): ').lower()
					self.transfer(amount, username, account_type)

				elif further_choice=='5':
					self.information(account_choice)

				elif further_choice=='6':
					print('\n***************Thanks for using the Bank of America*******************')
					raise SystemExit

	def maintenance(self):
		"""This is deducting the monthly maintenance fee
		for all the accounts if it exists"""
		file = open('accounts.pickle', 'rb')
		accounts = pickle.load(file)
		file.close()

		name = accounts[self.result][self.username][0]
		pin = accounts[self.result][self.username][1]
		balance = accounts[self.result][self.username][2]
		time = accounts[self.result][self.username][3]

		if (time+self.delta)<=dt.date.today():

			if self.result=='sbc':
				obj = SafeBalanceChecking(name, pin, balance)
				new_balance = obj.monthly_maintenance()

			elif self.result=='arc':
				obj = AdvantageRelationshipChecking(name, pin, balance)
				new_balance = obj.monthly_maintenance()

			elif self.result=='apc':
				obj = AdvantagePlusChecking(name, pin, balance)
				new_balance = obj.monthly_maintenance()

			elif self.result=='as':
				obj = AdvantageSavings(name, pin, balance)
				new_balance = obj.monthly_maintenance()

			accounts[self.result][self.username][3] = dt.date.today()
			accounts[self.result][self.username][2] = new_balance
			file = open('accounts.pickle', 'wb')
			pickle.dump(accounts, file)
			file.close()
			print('\n********Monthly maintenance fee deducted Successfully********\n')

		else:
			current = (self.delta+time)-dt.date.today()
			print(f'\n*******{current.days} days are remaining for monthly maintenance fee******\n')




	def transfer(self, amount, username, account_type):
		"""Transfering the amount from one account to another account"""

		file = open('accounts.pickle', 'rb')
		accounts = pickle.load(file)
		file.close()

		"""Checking if username exists or not"""
		if  username in accounts[account_type].keys():

			name = accounts[self.result][self.username][0]
			pin = accounts[self.result][self.username][1]
			balance = accounts[self.result][self.username][2]
			another_account_balance = accounts[account_type][username][2]

			if self.result=='sbc':
				obj = SafeBalanceChecking(name, pin, balance)
				new_balance = obj.transfer(another_account_balance, amount)

			elif self.result=='arc':
				obj = AdvantageRelationshipChecking(name, pin, balance)
				new_balance = obj.transfer(another_account_balance, amount)

			elif self.result=='apc':
				obj = AdvantagePlusChecking(name, pin, balance)
				new_balance = obj.transfer(another_account_balance, amount)

			elif self.result=='as':
				obj = AdvantageSavings(name, pin, balance)
				new_balance = obj.transfer(another_account_balance, amount)

			if new_balance!=None:
				accounts[self.result][self.username][2] = new_balance[1]
				accounts[account_type][username][2] = new_balance[0]
				file = open('accounts.pickle', 'wb')
				pickle.dump(accounts, file)
				file.close()
				print('\n************Transfer Successfully!**************\n')
		else:
			print('*********There is no one exist with such Username***********')

	def withdraw(self, amount):
		file = open('accounts.pickle', 'rb')
		accounts = pickle.load(file)
		file.close()

		name = accounts[self.result][self.username][0]
		pin = accounts[self.result][self.username][1]
		balance = accounts[self.result][self.username][2]

		if self.result=='sbc':
			obj = SafeBalanceChecking(name, pin, balance)
			new_balance = obj.transaction(amount)

		elif self.result=='arc':
			obj = AdvantageRelationshipChecking(name, pin, balance)
			new_balance = obj.transaction(amount)

		elif self.result=='apc':
			obj = AdvantagePlusChecking(name, pin, balance)
			new_balance = obj.transaction(amount)

		elif self.result=='as':
			obj = AdvantageSavings(name, pin, balance)
			new_balance = obj.transaction(amount)

		if new_balance!=None:
			accounts[self.result][self.username][2] = new_balance
			file = open('accounts.pickle', 'wb')
			pickle.dump(accounts, file)
			file.close()
			print('\n************Withdraw Successfully!**************\n')


	def deposit(self, amount):

		file = open('accounts.pickle', 'rb')
		accounts = pickle.load(file)
		file.close()

		name = accounts[self.result][self.username][0]
		pin = accounts[self.result][self.username][1]
		balance = accounts[self.result][self.username][2]

		if self.result=='sbc':
			obj = SafeBalanceChecking(name, pin, balance)
			new_balance = obj.deposit(amount)

		elif self.result=='arc':
			obj = AdvantageRelationshipChecking(name, pin, balance)
			new_balance = obj.deposit(amount)

		elif self.result=='apc':
			obj = AdvantagePlusChecking(name, pin, balance)
			new_balance = obj.deposit(amount)

		elif self.result=='as':
			obj = AdvantageSavings(name, pin, balance)
			new_balance = obj.deposit(amount)

		accounts[self.result][self.username][2] = new_balance
		file = open('accounts.pickle', 'wb')
		pickle.dump(accounts, file)
		file.close()
		print('\n************Amount Deposited Successfully!**************\n')

	def checking(self, choice):

		"""Returning Y in case account exists otherwise
		returning n"""
		if choice=='1':
			if self.username in self.accounts['sbc'].keys():
				return 'sbc'

		elif choice=='2':
			if self.username in self.accounts['arc'].keys():
				return 'arc'

		elif choice=='3':
			if self.username in self.accounts['apc'].keys():
				return 'apc'

		elif choice=='4':
			if self.username in self.accounts['as'].keys():
				return 'as'
		return 'n'

	def add_account(self, choice, pin, balance, name):
		"""Adding the account to the bank"""
		if choice==1:
			self.accounts['sbc'][self.username]=[name, pin, balance, dt.date.today()]

		elif choice==2:
			self.accounts['arc'][self.username]=[name, pin, balance, dt.date.today()]

		elif choice==3:
			self.accounts['apc'][self.username]=[name, pin, balance, dt.date.today()]

		elif choice==4:
			self.accounts['as'][self.username]=[name, pin, balance, dt.date.today()]
		
		file = open('accounts.pickle', 'wb')
		pickle.dump(self.accounts, file)
		file.close()
		print('\n**************Created Successfully!************\n')
		print("You can also register another account!\n")



	def remove_account(self, account_choice):
		"""Removing account if it exists"""
		if account_choice=='1':
			del self.accounts['sbc'][self.username]

		elif account_choice=='2':
			del self.accounts['arc'][self.username]

		elif account_choice=='3':
			del self.accounts['apc'][self.username]

		elif account_choice=='4':
			del self.accounts['as'][self.username]

		file = open('accounts.pickle', 'wb')
		pickle.dump(self.accounts, file)
		file.close()


	def information(self, choice):
		"""Getting your bank account information"""
		read = open('accounts.pickle', 'rb')
		data = pickle.load(read)
		read.close()
		#print(type(choice))

		if choice=='1':
			obj = SafeBalanceChecking(data['sbc'][self.username][0], data['sbc'][self.username][1], data['sbc'][self.username][2])

		elif choice=='2':
			obj = SafeBalanceChecking(data['arc'][self.username][0], data['arc'][self.username][1], data['arc'][self.username][2])

		elif choice=='3':
			obj = SafeBalanceChecking(data['apc'][self.username][0], data['apc'][self.username][1], data['apc'][self.username][2])

		elif choice=='4':
			obj = SafeBalanceChecking(data['as'][self.username][0], data['as'][self.username][1], data['as'][self.username][2])

		print(obj)

def main():
	print('**********Welcome to Bank of America***********\n')
	print('1- Do you want to signup as a customer\n2- Do you want to Login as a customer\n')
	user_choice = input('Choose from above and Enter: ')
	username = input('\nEnter your username: ')
	if user_choice=='2':
		file = open('signup.pickle', 'rb')
		signup = pickle.load(file)
		file.close()

		if username in signup.keys():
			if signup[username][0]==input('Enter your account Password: '):
				print('\n************Login Successfully!**********\n')
				decision = input('Do you want to see your Personal Information (y/n): ').lower()
				if decision=='y':
					obj = Customer()
					obj.view_personal_information(username)
					Bank(username)
				elif decision=='n':
					Bank(username)
				else:
					print('\n**********Invalid Input**********\n\n*****Exiting!******')
			else:
				print('\n**********Invalid Password!**********')

		else:
			print('\n**********Invalid username!************')

	elif user_choice=='1':
		new_customer = Customer()
		new_customer.get_personal_information(username)
		print('*********You are automatically logged in**************\n')
		Bank(username)

if __name__=='__main__':
	main()