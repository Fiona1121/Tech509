class IPhone:
  
  def __init__(self, name, phone_number):
    self.name = name
    self.phone_number = phone_number
    self.storage = []
    self.call_history = []
    

  def change_name(self, new_name):
    self.name = new_name
    print(f'{self.phone_number} is now {self.name}\n')
    
  
  def call(self, to):
    print(f'{self.name} called {to.name}\n')
    to.receive_call(self)
    self.call_history.append(f"Called -> {to.phone_number}")

  
  def receive_call(self, from_iphone):
    print(f'{self.name} received a call from {from_iphone.name}\n')
    self.call_history.append(f"Received <- {from_iphone.phone_number}")
    
  
  def air_drop(self, to, file):
    to.storage.append(file)
    to.air_receive(self, file)
    
  
  def air_receive(self, from_iphone, file):
    print(f'{self.name} received {file} from {from_iphone.name}\n')
    
  def __str__(self):
    return f'{self.name} - {self.phone_number}'
    
    
itzsyboo_iphone = IPhone('Itzsyboo', '123-456-7890')
annika_iphone = IPhone('Annika', '098-765-4321')

itzsyboo_iphone.call(annika_iphone)
print(itzsyboo_iphone.call_history)
print()

annika_iphone.call(itzsyboo_iphone)
print(annika_iphone.call_history)
print()

itzsyboo_iphone.air_drop(annika_iphone, 'selfie.jpg')
annika_iphone.air_drop(itzsyboo_iphone, 'sunset.jpg')

itzsyboo_iphone.change_name('Itzsyboo the Great')
print(itzsyboo_iphone)