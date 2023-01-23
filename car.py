from datetime import datetime
from dateutil.parser import parse, parserinfo
class Car():
    def __init__(self, engine_type, battery):
        self.engine_type = engine_type
        self.battery = battery
    
    def needs_service(self,total_miles,miles_last_service,warning_ind,last_service_date):
        result=False
        self.new_miles=total_miles-miles_last_service
        self.warning_ind=warning_ind
        match self.engine_type:
            case "capulet":
                if self.new_miles>30000:
                    result = True
            case "Willoughby":
                if self.new_miles>60000:
                    result = True
            case "sternman":
                if self.warning_ind==True:
                    result = True
        if result != True:
            self.last_service_date=last_service_date
            match self.battery:
                case "Spindler":
                    convstr=datetime.strptime(self.last_service_date,'%Y/%m/%d')
                    if dateutil.relativedelta(datetime.today(),convstr).years>2:
                        result=True
                case "Nubbin":
                    convstr=datetime.strptime(self.last_service_date,'%Y/%m/%d')
                    if dateutil.relativedelta(datetime.today(),convstr).years>4:
                        result=True
        return result
mycar=Car('sternman','Nubbin')
mycar.needs_service(2000,1000,False,'2016/10/11')   

                
                


