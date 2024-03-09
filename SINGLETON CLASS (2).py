#!/usr/bin/env python
# coding: utf-8

# In[19]:


#Creating the class and setting instance as none
class SingletonClass:
    __instance__ = None
    
    @staticmethod
    #Static access method
    def getInstance():
        #If the instance is none we set the instance as the class.This is the only instance of the class
        if SingletonClass.__instance__ == None:
            SingletonClass.__instance__ = SingletonClass()
            #print("Singleton class created",SingletonClass.__instance__)
        #print(SingletonClass.__instance__)
        return SingletonClass.__instance__

    def __init__(self):
        #This is the constructor.One instance is created
        print("init called")
        
    def someFunc(self):
        print("function called")

#The class can be called from anywhere in the program and only one instance is created.    
SingletonClass.getInstance().someFunc()
SingletonClass.getInstance().someFunc()
SingletonClass.getInstance().someFunc()

#SingletonClass.getInstance().someFunc()
#c2=c.getInstance()
#c1=c.someFunc()


# In[ ]:





# In[ ]:




