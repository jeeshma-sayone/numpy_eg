import datetime
import numpy as np

start = datetime.date(2022, 7, 22)
end = datetime.datetime.today().date()

days = np.busday_count(start, end)
print('Number of business days is:', days)
