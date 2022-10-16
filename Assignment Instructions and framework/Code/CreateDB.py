
import pandas as pd
import sqlite3

df = pd.read_csv("penalty_data_set_2.csv", low_memory=False)
conn = sqlite3.connect('OffenceDB.db')
c = conn.cursor()
c.execute('''
          CREATE TABLE IF NOT EXISTS Offences
          ([Index] INTEGER PRIMARY KEY, [OFFENCE_FINYEAR] TEXT, [OFFENCE_MONTH] TEXT,[OFFENCE_CODE] TEXT, [OFFENCE_DESC] TEXT, [LEGISLATION] TEXT, [SECTION_CLAUSE] TEXT, [FACE_VALUE] INTEGER, [CAMERA_IND] TEXT, [CAMERA_TYPE] TEXT, [LOCATION_CODE] TEXT, [LOCATION_DETAILS] TEXT, [SCHOOL_ZONE_IND] TEXT, [SPEED_BAND] TEXT, [SPEED_IND] TEXT, [POINT_TO_POINT_IND] TEXT, [RED_LIGHT_CAMERA_IND] TEXT, [SPEED_CAMERA_IND] TEXT, [SEATBELT_IND] TEXT, [MOBILE_PHONE_IND] TEXT, [PARKING_IND] TEXT, [CINS_IND] TEXT, [FOOD_IND] TEXT, [BICYCLE_TOY_ETC_IND] TEXT, [TOTAL_NUMBER] INTEGER, [TOTAL_VALUE] INTEGER)
          ''')
df.to_sql('Offences', conn, if_exists='replace', index = True)
conn.commit()
