from json_parser import fileParser
from dateutil import parser
from datetime import datetime, timedelta
import collections
import matplotlib.pyplot as plt
import numpy as np
from nvd3 import lineChart
import time as tm

def plot_line(x,y,x_label,y_label,title,xtick_labels):
	width=1/1.5
	fig,ax=plt.subplots()
	plt.plot(x,y,'ro',color="lightskyblue",ls='-')
	plt.xlabel(x_label)
	plt.ylabel(y_label)
	plt.axhline(y=5,linewidth=2, color='lightcoral', ls='--')
	plt.axhline(y=10,linewidth=2, color='orange', ls='--')
	plt.axhline(y=20,linewidth=2, color='red', ls='--')
	ind=np.arange(len(y))
	if(xtick_labels is not None):
		ax.set_xticks(ind+width)
		ax.set_xticklabels(xtick_labels,rotation=90,fontsize=8)
	plt.title(title)

	plt.show()

def chart_line(ydata,xdata,filename):
	output_file = open(filename, 'w')
	type = 'lineChart'
	chart = lineChart(name=type, x_is_date=True, color_category='category20c', height=450, width=900)
	chart.set_containerheader("\n\n<h2>" + type + "</h2>\n\n")
	chart.add_serie(y=ydata, x=xdata)
	chart.buildhtml()
	output_file.write(chart.htmlcontent)

def parseData(all_data,filename):
	tweet_time={}
	retweet_time={}
	# print all_data[0].keys()
	for data in all_data:
		# print data['created_at']
		dt = parser.parse(data['created_at'])
		dt=dt+timedelta(hours=5,minutes=30)
		time_label=str(dt).split(":")[0]
		if time_label not in tweet_time.keys():
			tweet_time[time_label]=1
		else:
			tweet_time[time_label]=tweet_time[time_label]+1

		if time_label not in retweet_time.keys():
			if 'retweet_count' in data.keys():
				retweet_time[time_label]=data['retweet_count']
		else:
			if 'retweet_count' in data.keys():
				retweet_time[time_label]=retweet_time[time_label]+data['retweet_count']

	tweet_time=collections.OrderedDict(sorted(tweet_time.items()))
	add=0
	for key in tweet_time.keys():
		tweet_time[key]=tweet_time[key]+add
		add=tweet_time[key]
	xtick_labels=[tm.mktime(datetime.strptime(time, "%Y-%m-%d %H").timetuple())*1000 for time in tweet_time.keys()]
	# plot_line(x=range(len(tweet_time.values())),y=tweet_time.values(),x_label="Time",y_label="No. of Posts",xtick_labels=xtick_labels,title=filename)
	# print tweet_time
	chart_line(tweet_time.values(),xtick_labels,filename="tweet_cdf.html")

	retweet_time=collections.OrderedDict(sorted(retweet_time.items()))
	add=0
	for key in retweet_time.keys():
		retweet_time[key]=retweet_time[key]+add
		add=retweet_time[key]
	xtick_labels=[tm.mktime(datetime.strptime(time, "%Y-%m-%d %H").timetuple())*1000 for time in retweet_time.keys()]
	# plot_line(x=range(len(retweet_time.values())),y=retweet_time.values(),x_label="Time",y_label="No. of Posts",xtick_labels=xtick_labels,title=filename)
	# print retweet_time
	chart_line(retweet_time.values(),xtick_labels,filename="retweet_cdf.html")

if __name__=="__main__":
	filename="gujarat riot_search.json"
	data=fileParser(filename)
	# print data
	parseData(data,filename)

	filename="karnataka bandh_search.json"
	data=fileParser(filename)
	# print data
	parseData(data,filename)