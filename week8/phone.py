# 1. Create 2 instances of the iPhone.
# 2. Change iPhone names through set_name()
# 3. Send a iMessage from phone1 to phone2
# 4. phone2 should be able to check messages. Print the messages on screen.

class iPhone:
  def __init__(self, name, phone_number):
    self.name = name
    self.phone_number = phone_number
    self.storage = []
    self.call_history = []
    self.messages = []
    
  def set_name(self, new_name):
    self.name = new_name
    print(f'Your iPhone name is now {self.name}')
    print("\n-----------------------------\n")
    
  def call(self, to):
    print(f'{self.name} called {to.name}')
    to.receive_call(self)
    self.call_history.append(f"Called -> {to.phone_number}")
    print("\n-----------------------------\n")
    
  def receive_call(self, from_iphone):
    print(f'{self.name} received a call from {from_iphone.name}')
    self.call_history.append(f"Received <- {from_iphone.phone_number}")
    
  def iMessage(self, to, message):
    to.messages.append(message)
    to.receive_message(self, message)
    print("\n-----------------------------\n")
    
  def receive_message(self, from_iphone, message):
    print(f'{self.name} received a message from {from_iphone.name}: {message}')
  
  def check_messages(self, last_n_messages):
    print(f'{self.name} checked messages:')
    print(self.messages[-last_n_messages:])
    print("\n-----------------------------\n")


print("-----------------------------\n")
    
my_phone = iPhone('Itzsyboo', '123-456-7890')
your_phone = iPhone('Annika', '098-765-4321')

my_phone.call(your_phone)
your_phone.call(my_phone)

my_phone.iMessage(your_phone, 'Hey Annika, how are you?')
your_phone.iMessage(my_phone, 'Hey Itzsyboo, I am doing great!')

my_phone.check_messages(1)
your_phone.check_messages(1)