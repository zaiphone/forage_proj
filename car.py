from datetime import datetime
class Car():
    def __init__(self, engine_type, battery):
        self.engine_type = engine_type
        self.battery = battery
    def years_past(original_date, years_to_add):
        dateholder = datetime.replace(original_date,year=datetime.year(original_date) + years_to_add)
        return dateholder
    
    def needs_service(self,total_miles,miles_last_service,warning_ind,last_service_date):
        result=False
        self.new_miles=total_miles-miles_last_service
        match self.engine_type:
            case "capulet":
                if self.new_miles>30000:
                    result = True
            case "Willoughby":
                if self.new_miles>60000:
                    result = True
            case "sternman":
                if warning_ind==True:
                    result = True
        if result != True:
            self.last_service_date=last_service_date
            match self.battery:
                case "Spindler":
                    if datetime.year(datetime.today()-datetime.strptime(self.last_service_date,'%Y/%m/%d'))>2:
                        result=True
                case "Nubbin":
                    service_date = years_past   (self.last_service_date, 4)
                    if date_which_battery_should_be_serviced_by < self.current_date:
                        return True
        return result
mycar=Car('sternman','Nubbin')
mycar.needs_service(2000,1000,False,'2017/10/11')   

                
                


