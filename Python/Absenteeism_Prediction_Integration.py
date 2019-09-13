from absenteeism_module import *
import pymysql
# load the model
model = absenteeism_model('model', 'scaler')
model.load_and_clean_data("Absenteeism_new_data.csv") # PPC the whoel dataset
df_new_obs= model.predicted_outputs() # fit the cleaned data into the model

# the probabity that givem individual to be absent
# prediction to extent probaility column as a reault driven column (absent vs no)
df_new_obs.head()

# Then we are itegrating the python processed/predicted data into MySQL, then visualziae it in tableau
# first of all we need to go to MySQL to create a corresponded database
# Then we should create a connection between the database inside of MySQL and Jupyer notebook
# Create a Connectoon and Cursor
# cursur is the indication to inside MySQL where t write the code
conn= pymysql.connect(database= "predicted_output", user ="root", password ="Laifu_xow5108")
# assign the conn to curor and invode the cursor
cursor = conn.cursor()
# sending data to MySQL DB using one multiple row statement
insert_query = "INSERT INTO predicted_outputs VALUES"
df_new_obs.columns.values

for i in range(df_new_obs.shape[0]):
    insert_query += "("
    
    for j in range(df_new_obs.shape[1]):
#         print(str(df_new_obs[df_new_obs.columns.values[j]][i]))
        if j == 12:
            Cell = str(df_new_obs[df_new_obs.columns.values[j]][i])
#             print (Cell)
            insert_query = insert_query + "{}),".format(Cell)
        else:
            cell = str(df_new_obs[df_new_obs.columns.values[j]][i])
            insert_query += cell + ","
          
insert_query = insert_query[:-2] + ");"
# print(insert_query)
# execute 
cursor.execute(insert_query)
conn.commit()
conn.close()