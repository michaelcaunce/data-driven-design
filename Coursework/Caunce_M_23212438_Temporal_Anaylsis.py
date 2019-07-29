#A range of packages imported from various libraries.
import seaborn
from pandas import DataFrame
from csv import DictReader
from matplotlib import pyplot
from datetime import datetime

#Created dictionary ({}). These are mapings from keys to values.
#This dictionary contains three keys, all with empty arrays.
#This allows complexed analysis of the 'category', time of day 'time', and which day 'day'.
#The dictionary is assigned to Variable 'data'.
data = {'category': [],
        'day': [],
        'time': []}

#Open the "cleaned_log.csv" file that we read the log data from.Next we create a DictReader
#that will read the lines from the "cleaned_log.csv".
with open('cleaned_log.csv') as in_f:
    reader = DictReader(in_f)
    for line in reader:

        #datetime.strptime function.This function takes two parameters. The first is the string to parse (the "time_received_isoformat") and the second is the pattern that the string uses.
        #In this case we specify the pattern to be '%Y-%m-%dT%H:%M:%S', indicating that first we have the year, then the month, and day.
        #A "T" separates the date and time and the time is formatted hour, colon, minute, colon, second.
        timestamp = datetime.strptime(line['time_received_isoformat'], '%Y-%m-%dT%H:%M:%S')
        data['day'].append(timestamp.day)
        data['time'].append(timestamp.hour * 60 + timestamp.minute)

        #if, elif statements are used to determine whether or not various keywords are present in each line of cleaned_log, specifically if they are present within 'request_url_path'.
        #If these keywords are present they are then assigned their specific category inside category key inside 'data'. Any remaining requests are categorised as 'other'.
        if 'sitesearch' in line ['request_url_path']:
            data['category'].append('Search')
        elif 'onlineshop/' in line['request_url_path']:
            data['category'].append('Shopping')
        elif 'ism/'in line['request_url_path']:
            data['category'].append('International Slavery Museum')
        elif 'maritime/' in line['request_url_path']:
            data['category'].append('Merseyside Maritime Museum')
        elif 'kids' in line['request_url_path']:
            data['category'].append('Educational')
        elif 'sudley/' in line['request_url_path']:
            data['category'].append('Sudley House')
        elif 'walker/' in line['request_url_path']:
            data['category'].append('Walker Art Gallery')
        elif 'ladylever/' in line['request_url_path']:
                data['category'].append('Lady Lever Art Gallery')
        elif 'mol/' in line['request_url_path']:
            data['category'].append('Museum of Liverpool')
        else:
            data['category'].append('Other')
            print(line['request_url_path'])

data = DataFrame(data)

#Start of plotting Data using seaborn. A variety of charts are created providing different analytic views on then
# logged data. Within each saved plot you'll find, data obtained from the DataFrame(data), with each of 'time', 'day' and 'category' included.
#Additional features include setting the size of the charts, issues arose when trying to plot charts involving categories, they were displaying
# far too tight. Also, each plot is given a title, with either or both axis labeled. Finally, font size and colours are personalised providing esaier to read
# charts.

plot = seaborn.stripplot(data=data, y='day', color="#A14255")
plot.figure.set_size_inches(14,10)
seaborn.despine()
plot.axes.set_title('Days Of The Month Accessed', fontsize=28,color="#4A5762")
plot.set_ylabel("June 2015",size = 24, color="#7B8FA2")
plot.tick_params(labelsize=12,labelcolor="#4A5762")
plot.get_figure().savefig('days_accessed_stripplot.png')
pyplot.close()


plot = seaborn.stripplot(data=data, y='time', color="#A14255")
plot.figure.set_size_inches(14,10)
seaborn.despine()
plot.axes.set_title('Time Of Day Accessed', fontsize=28,color="#4A5762")
plot.set_ylabel("Time Of Day (Divide by 60)",size = 24, color="#7B8FA2")
plot.tick_params(labelsize=12,labelcolor="#4A5762")
plot.get_figure().savefig('time_accessed_stripplot.png')
pyplot.close()


plot = seaborn.violinplot(data=data, y='time', color="#A14255")
plot.figure.set_size_inches(14,10)
seaborn.despine()
plot.axes.set_title('Time Density Plot', fontsize=28,color="#4A5762")
plot.set_ylabel("Time Of Day (Divide by 60)",size = 24, color="#7B8FA2")
plot.tick_params(labelsize=12,labelcolor="#4A5762")
plot.get_figure().savefig('time_accessed_violinplot.png')
pyplot.close()


plot = seaborn.stripplot(data=data, x='category', y='day')
plot.figure.set_size_inches(30,10)
seaborn.despine()
plot.axes.set_title('Categories Accessed On Days Of The Month', fontsize=28,color="#4A5762")
plot.set_ylabel("June 2015",size = 24, color="#7B8FA2")
plot.set_xlabel("Categories",size = 24, color="#7B8FA2")
plot.tick_params(labelsize=12,labelcolor="#4A5762")
plot.get_figure().savefig('category_day_stripplot.png')
pyplot.close()


plot = seaborn.violinplot(data=data, x='category', y='day')
plot.figure.set_size_inches(30,10)
seaborn.despine()
plot.axes.set_title('Categories Accessed On Days Of The Month', fontsize=28,color="#4A5762")
plot.set_ylabel("June 2015",size = 24, color="#7B8FA2")
plot.set_xlabel("Categories",size = 24, color="#7B8FA2")
plot.tick_params(labelsize=12,labelcolor="#4A5762")
plot.get_figure().savefig('category_day_violinplot.png')
pyplot.close()


plot = seaborn.violinplot(data=data, x='category', y='time')
plot.figure.set_size_inches(30,10)
seaborn.despine()
plot.axes.set_title('Time Density Plot', fontsize=28,color="#4A5762")
plot.set_ylabel("Time Of Day (Divide by 60)",size = 24, color="#7B8FA2")
plot.set_xlabel("Categories",size = 24, color="#7B8FA2")
plot.tick_params(labelsize=12,labelcolor="#4A5762")
plot.get_figure().savefig('category_time_violinplot.png')
pyplot.close()


plot = seaborn.kdeplot(data=data.time[data.category=='Search'] / 60.0, label='Search')
plot = seaborn.kdeplot(data=data.time[data.category=='Shopping'] / 60.0, label='Shopping')
plot = seaborn.kdeplot(data=data.time[data.category=='International Slavery Museum'] / 60.0, label='International Slavery Museum')
plot = seaborn.kdeplot(data=data.time[data.category=='Educational'] / 60.0, label='Educational')
plot = seaborn.kdeplot(data=data.time[data.category=='Sudley House'] / 60.0, label='Sudley House')
plot = seaborn.kdeplot(data=data.time[data.category=='Merseyside Maritime Museum'] / 60.0, label='Merseyside Maritime Museum')
plot = seaborn.kdeplot(data=data.time[data.category=='Walker Art Gallery'] / 60.0, label='Walker Art Gallery')
plot = seaborn.kdeplot(data=data.time[data.category=='Lady Lever Art Gallery'] / 60.0, label='Lady Lever Art Gallery')
plot = seaborn.kdeplot(data=data.time[data.category=='Museum of Liverpool'] / 60.0, label='Museum of Liverpool')
plot.figure.set_size_inches(18,10)
seaborn.despine()
plot.axes.set_title('Categorised Requests - Time KDE Plot', fontsize=28,color="#4A5762")
plot.set_xlabel("Time Of day",size = 24, color="#7B8FA2")
plot.tick_params(labelsize=12,labelcolor="#4A5762")
plot.get_figure().savefig('time_density_categories.png')
pyplot.close()


plot = seaborn.kdeplot(data=data.time / 60.0, label='Category Access', color="#A14255")
plot.figure.set_size_inches(14,10)
seaborn.despine()
plot.axes.set_title('Categories Time Density Plot', fontsize=28,color="#4A5762")
plot.set_xlabel("time Of time",size = 24, color="#7B8FA2")
plot.tick_params(labelsize=12,labelcolor="#4A5762")
plot.get_figure().savefig('time_density.png')
pyplot.close()
