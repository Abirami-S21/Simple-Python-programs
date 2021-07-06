#!/usr/bin/env python
# coding: utf-8

# In[15]:


#Pangram program
#A Pangram is a sentence having all letters of the alphabet atleast once in the sentence.

import string

#Input the string
print("Enter the string")
given_string=str(input())

alphabet=set(string.ascii_lowercase) #get all alphabets in lowercase and form a set

if set(given_string.lower()) < alphabet:
    print('The given string is not a pangram')
else:
    print('The given string is a pangram')


# In[ ]:





# In[ ]:





# In[ ]:




