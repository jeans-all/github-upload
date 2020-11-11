import pandas
import numpy
import os
import matplotlib.pyplot as plt

#df = pandas.read_csv('data.csv', header= None, low_memory=False)
#df.value_counts()


new_names = ['year', 'id', 'agency', 'load_type', 'property_type', 'loan_purpose', 'occupancy', 'loan_amount', 'preapproval', 'action_type', 'msa_md', 'state', 'county', 'census_track', 'applicant_ethnicity', 'co_ethnicity', 'applicant_race1', 'applicant_race2', 'applicant_race3', 'applicant_race4', 'applicant_race5', 'co_race1', 'co_race2', 'co_race3', 'co_race4', 'co_race5', 'applicant_sex', 'co_sex', 'applicant_income', 'purchase_type', 'denial_reason1', 'denial_reason2', 'denial_reason3', 'rate_spread', 'hoepa_status', 'lien_status', 'edit_status', 'population', 'minority_population', 'median_family_income', 'msa_md_income', 'num_owner_unit', 'num_family_unit', 'application_data_indicator']  

df = pandas.read_csv('utah.csv', names=new_names)

topCounty =df.groupby('county').count()

A = df['applicant_ethnicity'].plot(kind='hist', bins=50, figsize=(12,6))


df2 = pandas.read_csv('utah.csv', names=new_names)

B = df2["state"].value_counts().plot(kind='bar')




topCounty = df.groupby('state')[['county']].count()
topCounty.sort_values('county').reset_index()
topCounty.colums=['Number of County']
df3 = pandas.read_csv('utah.csv', names=new_names)

C = df3.plot(kind='scatter',x='applicant_ethnicity',y='occupancy')


plt.show()

