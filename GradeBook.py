#David Casarrubias-Mena
# COSC 251
# 2/26/16
# In this program I initialize a list of students(roster) and each student is part of his own list that holds the number of absences and current grade average
# In the call roll method, I go down the roster in alphabetical order asking the user if they are here or not, attendance for each student is then recorded as a number of classes missed
# and added to the appropriate student in their list.
# In the input grades method, I go down the roster in alphabetical order and ask the user to enter a grade. That grade is then added to their current grade in their list and then divided by 2
# because this is the second grade being entered. The new average then replaces the initial average. 
class GradeBook:
    

    #using the constructor I take in a roster(name) and store it in a list
    def __init__(self):
        #each list contains name, number of absences, and average grade. Each student starts off with 0 absences, and each student starts off with a different average.
       self.l = [['David', 0, 78], ['Julian', 0, 81], ['Kenny', 0 , 65], ['Chris', 0, 92], ['John', 0, 95], ['Kyle', 0, 89], ['Cartman', 0, 73]] 

   
    def callRoll(self):
        self.l.sort() # sort list in alphabetical order
        print('Current roster(name, number of absences, current average): ', self.l)
        absent = GradeBook() # create GradeBook object called absent
        
        for i in range(len(self.l)): # for loop that loops from 0 to the size of the list
            answer = input('Are you present') #prompts user if they are here or no
            
            if(answer == 'no'): # if user is absent
               self.l[i][1] += 1 # increment the absent counter by 1 to every student that is absent. Column 1 will always be where number of absences is recorder. [i] is the row.

        print(self.l) #prints the list        
  

    def inputGrades(self):
       self.l.sort() # sort in alphabetical order
       average = GradeBook()
       

       for i in range(len(self.l)): # for loop to traverse list
          grade = int(input('\nEnter grade')) #prompts user to enter grade
          self.l[i][2] += grade # column 2 is always the average grade
          self.l[i][2] = self.l[i][2] / 2 #currently has one grade average, then each student is being prompted for another grade  
       print(self.l)  #prints the list  
       
   
        
p = GradeBook() # creates GradeBook object
p.callRoll() #calls callRollMethod
p.inputGrades() #calls inputGrades method.
        
    
