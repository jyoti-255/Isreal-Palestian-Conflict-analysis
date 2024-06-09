import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.sidebar.title("Upload dataset")
Upload_file=st.sidebar.file_uploader("choose Csv file",type='csv')
if  Upload_file is not None:
   data=pd.read_csv(Upload_file)
   
   #sidebar code
   no_event=len(data)
   citizenship_counts=data['citizenship'].value_counts()
   event_location_region=data['event_location_region'].value_counts()
   print(citizenship_counts)
   print(event_location_region)
   hostilities_counts=data[data['took_part_in_the_hostilities']=='Yes']   ['citizenship'].value_counts()
   print(hostilities_counts)
   no_hostilities_counts=data[data['took_part_in_the_hostilities']=='No']['citizenship'].value_counts()
   print(no_hostilities_counts)
   st.sidebar.write("No of Event:",no_event)  

  

   col1,col2=st.sidebar.columns(2)
   col3,col4=st.sidebar.columns(2)
   
   with col1:
      st.subheader("citizenship_counts")
      st.write(citizenship_counts)
   with col2:
      st.subheader("event_location_region")
      st.write(event_location_region)

   with col3:
      st.subheader("hostilities_counts")
      st.write(hostilities_counts)
   with col4:
      st.subheader("no_hostilities_counts")
      st.write(no_hostilities_counts)
  
   weapons_counts=data['ammunition'].value_counts()
   st.sidebar.write("weapon counts",weapons_counts)




#data Analysis part
 
   st.title("Isreal Palestine Conflict Analysis")
   st.write("Dataset Sample",data)

   col1,col2=st.columns(2)
   with col1:
      st.subheader("type of injuries")
      type_of_injury=data['type_of_injury'].value_counts()
      st.bar_chart(type_of_injury)
   with col2:
       st.subheader("MaleFemaleCount")
       MFcounts=data['gender'].value_counts()
       st.bar_chart( MFcounts)


   col1,col2=st.columns(2)
   with col1:
        st.subheader("Age Summary")
        age=data['age'].describe()
        st.write(age)


   with col2:
        st.subheader("Event Location Region Count")
        eventregion=data['event_location_region'].value_counts()
        st.bar_chart(eventregion)

   col1,col2=st.columns(2)
   with col1:
     residencecountryreg=data.groupby('event_location_region')['place_of_residence'].nunique()
     st.subheader("Residence Percentage by Region")
     fig,ax=plt.subplots()
     ax.pie(residencecountryreg,labels=residencecountryreg.index,autopct='%1.1f%%')
     st.pyplot(fig)

   col1,col2=st.columns(2)
   with col1:
     st.subheader("Injury_type")

     injurytype=data['type_of_injury'].value_counts()
     fig,ax=plt.subplots() 
     ax.pie(injurytype,labels=injurytype.index,autopct='%1.1f%%')
     st.pyplot(fig)



   with col2:
    regionavgage=data.groupby('event_location_region')['age'].mean()
    st.subheader("Avg Age by region")
    st.bar_chart(regionavgage)

   col1,col2=st.columns(2)
   with col1:
        IncidentcountbyNationality=     data.groupby('citizenship').size().reset_index(name='incident_count')
        st.subheader('Incident Count by Nationality')
        st.write(IncidentcountbyNationality)

   with col2:
      genderInc=data.groupby('gender').size().reset_index(name="incident_count")
      st.subheader('incident count by Gender')
      st.write(genderInc)
   
    
   data['date_of_event'] = pd.to_datetime(data['date_of_event'])
   data['year'] = data['date_of_event'].dt.year
   data['month'] = data['date_of_event'].dt.month_name()

   time_events = data.groupby(['year', 'month']).size().reset_index(name='incident_count')
   time_events['year_month'] = time_events['month'] + ' ' + time_events['year'].astype(str)
   st.subheader('Time-based Events')
   st.line_chart(time_events.set_index('year_month')['incident_count'])

   

       
  
