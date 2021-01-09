import pandas as pd

df = pd.read_csv('Traffic_Crashes_-_Crashes.csv', header=0)

# 1. Remove column CRASH_RECORD_ID
print('1. Remove column CRASH_RECORD_ID')
df.drop('CRASH_RECORD_ID', 1, inplace=True)

# 2. Remove column RD_NO
print('2. Remove column RD_NO')
df.drop('RD_NO', 1, inplace=True)


# 3. Set CRASH_DATE_EST_I = N when empty and remove CRASH_DATE
print('3. Set CRASH_DATE_EST_I = N when empty and remove CRASH_DATE')
df['CRASH_DATE_EST_I'].fillna('N', inplace=True)
df.drop('CRASH_DATE', 1, inplace=True)

# 4. Discretization POSTED_SPEED_LIMIT
print('4. Discretization POSTED_SPEED_LIMIT')
discretization_posted_speed_limit = lambda x: '1. 30' if x <= 30 else '2. 30-60' if x <= 60 else '3. 60'
df.loc[:, 'POSTED_SPEED_LIMIT'] = df['POSTED_SPEED_LIMIT'].apply(discretization_posted_speed_limit)

# 5. Remove column LANE_CNT (too much missing data to considered)
print('5. Remove column LANE_CNT (too much missing data to considered)')
df.drop('LANE_CNT', 1, inplace=True)

# 6. Set INTERSECTION_RELATED_I = N when empty
print('6. Set INTERSECTION_RELATED_I = N when empty')
df['INTERSECTION_RELATED_I'].fillna('N', inplace=True)

# 7. Set NOT_RIGHT_OF_WAY_I = N when empty
print('7. Set NOT_RIGHT_OF_WAY_I = N when empty')
df['NOT_RIGHT_OF_WAY_I'].fillna('N', inplace=True)

# 8. Set HIT_AND_RUN_I = N when empty
print('8. Set HIT_AND_RUN_I = N when empty')
df['HIT_AND_RUN_I'].fillna('N', inplace=True)

# 9. Set INTERSECTION_RELATED_I = N when empty
print('9. Set INTERSECTION_RELATED_I = N when empty')
df['INTERSECTION_RELATED_I'].fillna('N', inplace=True)

# 10. Remove DATE_POLICE_NOTIFIED 
print('10. Remove DATE_POLICE_NOTIFIED ')
df.drop('DATE_POLICE_NOTIFIED', 1, inplace=True)

# 11. Remove column SEC_CONTRIBUTORY_CAUSE
print('11. Remove column SEC_CONTRIBUTORY_CAUSE')
df.drop('SEC_CONTRIBUTORY_CAUSE', 1, inplace=True)

# 12. Remove Street's columns (STREET_*). Not usefuls
print('12. Remove Street\'s columns (STREET_*). Not usefuls')
df.drop('STREET_NO', 1, inplace=True)
df.drop('STREET_DIRECTION', 1, inplace=True)
df.drop('STREET_NAME', 1, inplace=True)

# 13. Remove column BEAT_OF_OCCURRENCE 
print('13. Remove column BEAT_OF_OCCURRENCE')
df.drop('BEAT_OF_OCCURRENCE', 1, inplace=True)

# 14. Remove columns PHOTOS_TAKEN_I and STATEMENTS_TAKEN_I (too much missing data)
print('14. Remove columns PHOTOS_TAKEN_I and STATEMENTS_TAKEN_I (too much missing data)')
df.drop('PHOTOS_TAKEN_I', 1, inplace=True)
df.drop('STATEMENTS_TAKEN_I', 1, inplace=True)

# 15. Set DOORING = N when empty
print('15. Set DOORING = N when empty')
df['DOORING_I'].fillna('N', inplace=True)

# 16. Remove WORK_ZONE_* columns / WORKERS_PRESENT (too much missing data)
print('16. Remove WORK_ZONE_* columns / WORKERS_PRESENT (too much missing data)')
df.drop('WORK_ZONE_I', 1, inplace=True)
df.drop('WORK_ZONE_TYPE', 1, inplace=True)
df.drop('WORKERS_PRESENT_I', 1, inplace=True)

# 17. Discretization NUM_UNITS ( 1, 2, 3+)
print('17. Discretization NUM_UNITS')
discretization_num_units = lambda x: '1 Unit' if x == 1 else '2 Units' if x == 2 else '3+ Units'
df.loc[:, 'NUM_UNITS'] = df['NUM_UNITS'].apply(discretization_num_units)

# 18. Remove not used INJURIES_* (too much imbalance)
print('18. Remove INJURIES_* (too much imbalance)')
df.drop('INJURIES_INCAPACITATING', 1, inplace=True)
df.drop('INJURIES_NON_INCAPACITATING', 1, inplace=True)
df.drop('INJURIES_REPORTED_NOT_EVIDENT', 1, inplace=True)
df.drop('INJURIES_NO_INDICATION', 1, inplace=True)
df.drop('INJURIES_UNKNOWN', 1, inplace=True)

# 18.1 INJURIES_TOTAL discretization
print('18.1 Discretization INJURIES_TOTAL')
discretization_injuries_total = lambda x: '1. 0' if x == 0 else '2. 1' if x == 1 else '3. 2' if x == 2 else '4. 3+'
df.loc[:, 'INJURIES_TOTAL'] = df['INJURIES_TOTAL'].apply(discretization_injuries_total)


# 18.2 INJURIES_FATAL discretizaion
print('18.2 Discretization INJURIES_FATAL')
discretization_injuries_fatal = lambda x: 'N' if x == 0 else 'Y'
df.loc[:, 'INJURIES_FATAL'] = df['INJURIES_FATAL'].apply(discretization_injuries_fatal)


# 19. Discretization CRASH_HOUR (0-8 / 8 - 16 / 16 - 24)
print('19. Discretization CRASH_HOUR')
discretization_crash_hour = lambda x: '1. 0-8' if x <= 8 else '2. 9-16' if x <= 16 else '3. 17-24'
df.loc[:, 'CRASH_HOUR'] = df['CRASH_HOUR'].apply(discretization_crash_hour)

# 20. Add WEEKEND from CRASH_DAY_OF_WEEK and remove it
print('20. Add WEEKEND from CRASH_DAY_OF_WEEK and remove it')
format = lambda x: 'Y' if x == 1 or x == 7 else 'N'
df['WEEKEND'] = df['CRASH_DAY_OF_WEEK'].apply(format)
df.drop('CRASH_DAY_OF_WEEK', 1, inplace=True)

# 21. Remove CRASH_MONTH (not useful)
print('21. Remove CRASH_MONTH (not useful)')
df.drop('CRASH_MONTH', 1, inplace=True)

# 22. Remove GEO_DATA (LATITUDE, LONGITUDE, LOCATION)
print('22. Remove GEO_DATA (LATITUDE, LONGITUDE, LOCATION)')
df.drop('LATITUDE', 1, inplace=True)
df.drop('LONGITUDE', 1, inplace=True)
df.drop('LOCATION', 1, inplace=True)

to_null_values = ['N', 'UNKNOWN', 'NO CONTROLS']
negative_to_missing = lambda x: None if [s for s in to_null_values if x in s] else x

# df_filtered = df.query('INJURIES_FATAL == "Y" | HIT_AND_RUN_I=="Y"')
df.loc[:, 'TRAFFIC_CONTROL_DEVICE'] = df['TRAFFIC_CONTROL_DEVICE'].apply(negative_to_missing)
df.loc[:, 'DEVICE_CONDITION'] = df['DEVICE_CONDITION'].apply(negative_to_missing)
df.loc[:, 'WEATHER_CONDITION'] = df['WEATHER_CONDITION'].apply(negative_to_missing)
df.loc[:, 'LIGHTING_CONDITION'] = df['LIGHTING_CONDITION'].apply(negative_to_missing)
df.loc[:, 'TRAFFICWAY_TYPE'] = df['TRAFFICWAY_TYPE'].apply(negative_to_missing)
df.loc[:, 'ROADWAY_SURFACE_COND'] = df['ROADWAY_SURFACE_COND'].apply(negative_to_missing)
df.loc[:, 'ROAD_DEFECT'] = df['ROAD_DEFECT'].apply(negative_to_missing)
df.loc[:, 'NOT_RIGHT_OF_WAY_I'] = df['NOT_RIGHT_OF_WAY_I'].apply(negative_to_missing)
df.loc[:, 'HIT_AND_RUN_I'] = df['HIT_AND_RUN_I'].apply(negative_to_missing)
df.loc[:, 'DOORING_I'] = df['DOORING_I'].apply(negative_to_missing)
df.loc[:, 'INJURIES_FATAL'] = df['INJURIES_FATAL'].apply(negative_to_missing)


df.drop('CRASH_HOUR', 1, inplace=True)
df.drop('POSTED_SPEED_LIMIT', 1, inplace=True)
df.drop('CRASH_DATE_EST_I', 1, inplace=True)

# End preprocessing
df.to_csv('Traffic_Crashes-forRA.csv', index=False, quotechar='"')

print("Export done!")