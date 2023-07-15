class Worker: #Define class worker
    def __init__(self, name, area, experience = 0): #Starts to define workers
        self.name = name #Name of the worker
        self.experience = experience #How many years of experience
        self.area = area #Where people work
        self.earnings = 0 #Earnings start at zero
    
    def work(self):
        print(f"{self.name} is working in {self.area}")#Where people are working in
        self.earnings = self.earnings + ((self.experience + 1) * 10)#Will add money to earnings

Asa = Worker("Asa", "IT") #Defines a worker
Luciano = Worker("Luciano", "IT", 2)#Defines other workers

# print(Asa.experience)
# print(Luciano.experience) 

# Asa.work()
# Asa.work()
# print(Asa.earnings)

# Luciano.work()
# Luciano.work()
# print(Luciano.earnings)

google = [Asa, Luciano]

# for worker in google:
#     worker.work()

for i in range(len(google)):
    google[i].work() 

highest_earnings_worker = None

for i in range(len(google)):
    if highest_earnings_worker is None:
        highest_earnings_worker = google[i]
    if google[i].earnings > highest_earnings_worker.earnings:
        highest_earnings_worker = google[i]

print(highest_earnings_worker.name)



#Homework: Highest earning worker 
#Hint: You need a for loop, and see #3.py
#Explain in a comment 0-20