#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random


# In[17]:


def monty_hall(switcher):
    
    switch_win = 0
    no_switch_win = 0
    
    for i in range(10000):
        
        doors = [1,2,3]   # doors of game
        host_doors = [1,2,3]  # doors host will show

        car_door = random.randint(1,3)  # set car behind random door
        gamer_first_choice = random.randint(1,3)  # gamer choose random door     


        host_doors.remove(gamer_first_choice)  # host doesn`t open door choosen by gamer

        
        while True:
            if car_door in host_doors:
                host_doors.remove(car_door)  # host doesn`t open door of car too
            else:
                host_doors.remove(host_doors[0])  # host show one of the doors which has goat behind that
            break

        if switcher == True:
            # if gamer switch door then we should remove both first choice of him and shown door by host
            
            doors.remove(gamer_first_choice)
            doors.remove(host_doors[0])
            gamer_second_choice = doors[0]  # last door

            if gamer_second_choice == car_door:  # if choice is equal to door of car then he win
                switch_win += 1
              

        else:
            # if gamer doesn`t switch door then we should remove just shown by host
            doors.remove(host_doors[0])
            gamer_second_choice = gamer_first_choice

            if gamer_second_choice == car_door:  # if choice is equal to door of car then he win
                no_switch_win += 1

           
      
    return switch_win, no_switch_win


# In[22]:


result = []
result.append(monty_hall(switcher=True))
print("Probability of winning by switching: ", str(result[0][0] / 10000 * 100), "%")


# In[23]:


result = []
result.append(monty_hall(switcher=False))
print("Probability of winning by without switching: ", str(result[0][1] / 10000 * 100), "%")


# In[ ]:





# In[ ]:




