from datetime import date, datetime
import pytz

madrid_timezone = pytz.timezone("Europe/Madrid")
madrid_date = datetime.now(madrid_timezone)
print("Madrid: ", madrid_date.strftime("%d/%m/%Y, %H:%M:%S"))

obregon_timezone = pytz.timezone("America/Phoenix")
obregon_date = datetime.now(obregon_timezone)
print("Obregón: ", obregon_date.strftime("%d/%m/%Y, %H:%M:%S"))