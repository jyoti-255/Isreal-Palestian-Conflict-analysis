#import lib
import pandas as pd
import matplotlib.pyplot as plt


#load the data
data=pd.read_csv("fatalities.csv")
print(data)

print(data.head(3))
print(data.shape)

#important information
citizenship_counts=data['citizenship'].value_counts()
event_location_region=data['event_location_region'].value_counts()
print(citizenship_counts)
print(event_location_region)
hostilities_counts=data[data['took_part_in_the_hostilities']=='Yes']['citizenship'].value_counts()
print(hostilities_counts)
no_hostilities_counts=data[data['took_part_in_the_hostilities']=='No']['citizenship'].value_counts()
print(no_hostilities_counts)


print(data['type_of_injury'].value_counts().plot(kind='bar'))
plt.show()

print(data['gender'].value_counts().plot(kind='bar'))
plt.show()


#Calculate summary 

data['event_location_region'].value_counts().plot(kind='bar')
plt.show()


data.groupby('event_location_region')['place_of_residence'].nunique().plot(kind='pie',autopct='%1.1f%%')
plt.show()

data['type_of_injury'].value_counts().plot(kind='pie',autopct='%1.1f%%')


data.groupby('citizenship').size().reset_index(name='incident_count')

data[(data['event_location_region']=='West Bank')&(data['type_of_injury']=='gunfire')]


data['date_of_event'] = pd.to_datetime(data['date_of_event'])
data['year'] = data['date_of_event'].dt.year
data['month'] = data['date_of_event'].dt.month_name()

time_events = data.groupby(['year', 'month']).size().reset_index(name='incident_count')
time_events['year_month'] = time_events['month'] + ' ' + time_events['year'].astype(str)

print(time_events)



