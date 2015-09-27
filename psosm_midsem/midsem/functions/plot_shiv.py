
import twitter
import time
import json
import collections
from nvd3 import cumulativeLineChart
from nvd3 import lineChart
from datetime import datetime, timedelta
from json_parser import fileParser
from dateutil import parser
from datetime import datetime, timedelta
import collections
import matplotlib.pyplot as plt
import numpy as np
from nvd3 import lineChart
import time as tm
from json_parser import fileParser_json

def plot(filename):
    array=fileParser_json(filename)
    filename = 'plot.html'
    fw = open(filename, "w")
    type='lineChart'
    # for a date v/s frequency graph
    chart = lineChart(name=type, x_is_date=False, x_axis_format="AM_PM", height=600, width=1000)
    time_dict_days = {}
    for item in array:
        item_json =  json.loads(item)
        # print item_json['id']
        created_at = item_json['created_at']
        time_stamp = time.strftime('%s', time.strptime(created_at, '%a %b %d %H:%M:%S +0000 %Y'))
        date_time = datetime.fromtimestamp(float(time_stamp))
        # date_time = date_time+timedelta(hours=-5, minutes=30)
        day = date_time.day
        if str(day) in time_dict_days.keys():
            list = time_dict_days.get(str(day))
            list.append(date_time)
        else:
            list = []
            list.append(date_time)
            time_dict_days[str(day)] = list
    print time_dict_days.keys()
    for key in time_dict_days.keys():
        list = time_dict_days.get(key)
        time_dict = {}
        for item in list:
            hour = item.hour
            if str(hour) in time_dict.keys():
                time_dict[str(hour)] = time_dict[str(hour)] + 1
            else:
                time_dict[str(hour)] = 1
        time_dict=collections.OrderedDict(sorted(time_dict.items()))
        xdata = []
        ydata = []
        for k in time_dict.keys():
            xdata.append(k)
            ydata.append(time_dict[k])
        chart.add_serie(name=key, y=ydata, x=xdata)

    chart.buildhtml()
    fw.write(chart.htmlcontent)
    fw.close()
