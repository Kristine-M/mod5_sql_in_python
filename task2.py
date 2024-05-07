from connect_mysql import connect_database

def list_distinct(): #list the distintive trainers for the members
    conn = connect_database()
    if conn is not None:
        try: 
            cursor = conn.cursor()
            
            query = "SELECT DISTINCT trainer_id FROM members;" #rule for action on the table
               
            cursor.execute(query)
            
            print("Here are the following distinct trainer ids")
            for row in cursor.fetchall():
                print(row) #prints the matched data
                
        finally:
            cursor.close()
            conn.close()
            
            
def count_members_per_trainer(): #list the members for each trainer
    conn = connect_database()
    if conn is not None:
        try: 
            cursor = conn.cursor()
            
            
            query = """ 
                SELECT trainer_id, COUNT(*) FROM members 
                GROUP BY trainer_id
            """
            #rule ^ for action on the table
            
            cursor.execute(query)

            
            for row in cursor.fetchall():
                # print(row)
                trainer_id, member_count = row
                print(f"Trainer {trainer_id}: {member_count} members") #prints the respective data
                
        finally:
            cursor.close()
            conn.close()
            
def get_members_in_age_range(start_age, end_age): #list the members with the target age range
    conn = connect_database()
    if conn is not None:
        try: 
            cursor = conn.cursor()
            
            
            query = "SELECT * FROM members WHERE age BETWEEN %s AND %s;" #rule for action on the table
                
            cursor.execute(query, (start_age, end_age)) #executes the rule with the target age range

            print("The following members are within your target age range")
            for row in cursor.fetchall():
                print(row) #prints the matched members with the target age range
            
                
        finally:
            cursor.close()
            conn.close()
            
            
# list_distinct()
# count_members_per_trainer()
# get_members_in_age_range(25, 30)