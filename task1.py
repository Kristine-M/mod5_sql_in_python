from connect_mysql import connect_database

def print_data(): #prints the table
    conn = connect_database()
    if conn is not None:
        try: 
            cursor = conn.cursor() #look through the table
            
            query = "SELECT * FROM workoutsessions" #rule
            
            cursor.execute(query) #goes and look through the table with the rule
            
            for row in cursor.fetchall(): #prints the found data
                print(row)
                
        finally:
            cursor.close()
            conn.close()


def add_member(id, name, age, trainer_id): #adds a member
    
    conn = connect_database()
    if conn is not None:
        try: 
            cursor = conn.cursor()
            
            new_member = (id, name, age, trainer_id) #new member info
            
            query = "INSERT INTO members (id, name, age, trainer_id) VALUES (%s, %s, %s, %s)"
            #rule ^ for action on the table
            
            cursor.execute(query, new_member) #executes the rule with the new member info
            conn.commit()
            
            print("New member added")
            return conn
            
        except Exception as e:
            print(f"Error: {e}") #prints errors
            return None
           
        finally:
            cursor.close()
            conn.close()
            
            
            
def add_workout_session(session_id, member_id, session_time):#adds a workout session
    conn = connect_database()
    if conn is not None:
        try: 
            cursor = conn.cursor()
            
            new_session = (session_id, member_id, session_time) #new session info
            
            query = "INSERT INTO WorkoutSessions (session_id, member_id, session_time) VALUES (%s, %s, %s)"
            #rule ^ for action on the table
            
            cursor.execute(query, new_session) #executes the rule with the new session info
            
            conn.commit()
            print("New session added")
            return conn
            
         
        except Exception as e:
            print(f"Error: {e}") #prints errors
            return None
        
        
        finally:
            cursor.close()
            conn.close()

def update_member_age(member_id, new_age): #updates the member's age
    conn = connect_database()
    if conn is not None:
        try: 
            cursor = conn.cursor()
            
            updated_member = (new_age, member_id) #updated info
            
            query = "UPDATE members SET age = %s WHERE id = %s" #rule for action on the table
            
            cursor.execute(query, updated_member) #executes the rule with the updated member info
            conn.commit()
            print("Updated member age")
            return conn
            
         
        except Exception as e:
            print(f"Error: {e}") #prints errors
            return None
        
        
        finally:
            cursor.close()
            conn.close()

def delete_workout_session(session_id): #deletes the specified workout session
    
    conn = connect_database()
    if conn is not None:
        try: 
            cursor = conn.cursor()
            
            del_session = (session_id, ) #session to delete
            
            query_check = "SELECT * FROM workoutsessions WHERE session_id = %s" 
            # rule to check if the session is available to delete
            
            cursor.execute(query_check, del_session) #executes the rule to check the info
            
            members = cursor.fetchall() #list of matched data
            
            
            if members: #if the list wasn't empty then  proceed with deleting
                
                query = "DELETE FROM workoutsessions WHERE session_id = %s"
                #rule ^ for action on the table
                
                cursor.execute(query, del_session) #executes the rule to delete the session
                conn.commit()
                print("Deleted session")
                return conn
            else:    
                print("No workout session to delete") #otherwise print the respective message
            
         
        except Exception as e:
            print(f"Error: {e}") #prints errors
            return None
        
        
        finally:
            cursor.close()
            conn.close()
            
            
            
# add_member(1234, 'John Doe', 30, 5)
# add_workout_session(5, 3, "evening")
# update_member_age(1, 21)
# delete_workout_session(1)
# print_data()