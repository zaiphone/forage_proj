from datetime import datetime
import random 
class Car():
    def __init__(self, engine_type, battery, tires):
        self.tires= tires
        self.engine_type = engine_type
        self.battery = battery
    
    def needs_service(self,total_miles,miles_last_service,warning_ind,last_service_date):
        result=False
        self.result=result
        self.new_miles=total_miles-miles_last_service
        self.warning_ind=warning_ind
        tire_wear=[]
        for i in range(4):
            tire_wear.append(random.random()) #auto generate the array 0-1
        self.tire_wear=tire_wear
        print(self.tire_wear)
        match self.engine_type:
            case "capulet":
                if self.new_miles>30000:
                    self.result = True
            case "Willoughby":
                if self.new_miles>60000:
                    self.result = True
            case "sternman":
                if self.warning_ind==True:
                    self.result = True

        if result != True:
            self.last_service_date=last_service_date
            match self.battery:
                case "Spindler":
                    convstr=datetime.strptime(self.last_service_date,'%Y-%m-%d')
                    if (datetime.today()-convstr).days>1095:
                        self.result=True
                case "Nubbin":
                    convstr=datetime.strptime(self.last_service_date,'%Y-%m-%d')
                    if (datetime.today()-convstr).days>1460:
                        self.result=True

        if result != True:
            self.tire_wear=tire_wear
            match self.tires:
                case "Carrigan":
                    for el in self.tire_wear:
                        if el>=0.9:
                            result=True
                case "Octoprime":
                    wear_sum=0
                    for el in self.tire_wear:
                        wear_sum=wear_sum+el
                        if wear_sum>=3:
                            result=True
                            
        return self.result




                
                


