#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np
import matplotlib.pyplot as plt


# In[7]:


#Line color and marker
x = np.linspace(0, 10, 100)
plt.plot(x, np.sin(x - 0), color='blue', marker ='+')   # color by name
plt.plot(x, np.sin(x - 1), color='g', marker = '*')      # short color code (rgbcmyk) 
plt.plot(x, np.sin(x - 2), color='0.75', marker = 's')  # Grayscale between 0 and 1
plt.plot(x, np.sin(x - 4), color=(1.0,0.2,0.3), marker = 'd') # RGB tuple, values 0 and 1 
plt.show()


# In[58]:


import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 10, 100)
plt.plot(x, np.sin(x))
#plt.axis('tight')
#plt.axis('equal')   #sets the x-axis and y-axis equal
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Sine Graph')
plt.savefig('plot.png')   #saves the fig

from IPython.display import Image
Image('plot.png')
#plt.show()    


# In[59]:


import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 10, 100)
plt.plot(x, np.sin(x))
plt.axis('tight')
#plt.axis('equal')   #sets the x-axis and y-axis equal
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Sine Graph')
plt.savefig('plot.png')   #saves the fig

from IPython.display import Image
Image('plot.png')
#plt.show()    


# In[63]:


import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 10, 100)
plt.plot(x, np.sin(x))
#plt.axis('tight')
plt.axis('equal')   #sets the x-axis and y-axis equal
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Sine Graph')
plt.savefig('plot.png')   #saves the fig

from IPython.display import Image
Image('plot.png')
#plt.show()    


# In[20]:


#Subplots in Matplotlib
plt.style.use('seaborn-whitegrid') 
import numpy as np
x = np.arange(5)          #a numpy array [0,1,2,3,4]
#plt.subplot(nrow, ncol, pos)
plt.subplot(1,2,1)     #Divides the figure window into 1 row and 2 columns, polt goes to position 1
plt.plot(x, x, label='linear')    # plot x versus x
plt.subplot(1,2,2)
plt.plot(x, x*x, label='square')


# In[21]:


#Subplots in Matplotlib
plt.style.use('seaborn-whitegrid') 
import numpy as np
x = np.arange(5)          #a numpy array [0,1,2,3,4]
#plt.subplot(nrow, ncol, pos)
plt.subplot(1,1,1)     #Divides the figure window into 1 row and 2 columns, polt goes to position 1
plt.plot(x, x, label='linear')    # plot x versus x
plt.subplot(1,2,2)
plt.plot(x, x*x, label='square')


# In[22]:


#Subplots in Matplotlib
plt.style.use('seaborn-whitegrid') 
import numpy as np
x = np.arange(5)          #a numpy array [0,1,2,3,4]
#plt.subplot(nrow, ncol, pos)
plt.subplot(1,1,1)     #Divides the figure window into 1 row and 2 columns, polt goes to position 1
plt.plot(x, x, label='linear')    # plot x versus x
plt.subplot(1,1,1)
plt.plot(x, x*x, label='square')


# In[57]:


#Subplots in Matplotlib
plt.style.use('seaborn-whitegrid') 
import numpy as np
x = np.arange(5)          #a numpy array [0,1,2,3,4]
#plt.subplot(nrow, ncol, pos)
plt.subplot(2,2,1)     #Divides the figure window into 1 row and 2 columns, polt goes to position 1
plt.plot(x, x, color='red', label='linear')    # plot x versus x
plt.legend()
plt.subplot(2,2,2)
plt.plot(x, x*x, color='blue', label='square')
plt.legend()
plt.subplot(2,2,3)
plt.plot(x, x*x*x, color='green', label='cube')
plt.legend()
plt.subplot(2,2,4)
plt.plot(x, x*x*x*x, color='brown', label='fourth')
plt.legend()
plt.show()


# In[25]:


#grid of subplots
for i in range(1, 7):
    plt.subplot(2, 3, i)
    plt.text(0.5, 0.5, str((2,3,i)), fontsize = 18, ha = 'center')


# In[29]:


#grid of subplots
for i in range(1, 7):
    plt.subplot(1, 2, i)
    plt.text(0.4, 0.2, str((1,2,i)), fontsize = 18, ha = 'center')


# In[31]:


#grid of subplots
for i in range(1, 7):
    plt.subplot(1, 3, i)
    plt.text(0.2, 0.5, str((1,2,i)), fontsize = 18, ha = 'center')


# In[35]:


# Bar Plots
#When both x and Y are discrete or categorical
x=[2,8,10]                   #x takes discrete values 
y=[11,15,9]     #height or frequency of each bar
plt.bar(x,y, color='r', label='red')


# In[37]:


# Bar Plots
#When both x and Y are discrete or categorical
x=[2,9,10]                   #x takes discrete values 
y=[11,15,9]     #height or frequency of each bar
plt.bar(x,y, color='r', label='red')
plt.legend()


# In[38]:


# Bar Plots
#When both x and Y are discrete or categorical
x=['A','B','C']                   #x takes discrete values 
y=[11,15,9]     #height or frequency of each bar
plt.bar(x,y, color='r', label='red')
plt.legend()


# In[40]:


# Bar Plots
#When both x and Y are discrete or categorical
x=[2,4,10]                   #x takes discrete values 
y=[11,15,9]     #height or frequency of each bar
plt.bar(x,y, color='r', label='red')
plt.legend()
# Bar Plots
#When both x and Y are discrete or categorical
x=[12,5,15]                   #x takes discrete values 
y=[6,8,10]     #height or frequency of each bar
plt.bar(x,y, color='g', label='green')
plt.legend()
plt.show()

plt.title("Bar plot")
plt.xlabel("X axis")
plt.ylabel("Y axis")


# In[44]:


# Bar Plots
#When both x and Y are discrete or categorical
x=[2,8,10]                   #x takes discrete values 
y=[11,15,9]     #height or frequency of each bar
plt.bar(x,y, color='r', label='red')

x2=[12,5,15]
y2=[6,8,10]
plt.bar(x2,y2,color='g', label ='green')
plt.legend()        # use this whenever  labels are used
plt.title("Bar plot")
plt.xlabel("X axis")
plt.ylabel("Y axis")


# In[41]:


# Simple bar plot
import numpy as np
import matplotlib.pyplot as plt
cities=['Delhi','Mumbai','Bangalore','Hydrabad']
population=[23456123,10083104,18456123,13411093]
plt.bar(cities,population,width=[.3,.1,.7,.4],color=['r','b','g','y'])


# In[43]:


# Simple bar plot
import numpy as np
import matplotlib.pyplot as plt
cities=['Delhi','Mumbai','Bangalore','Hydrabad']
population=[23456123,10083104,18456123,13411093]
plt.bar(cities,population,width=0.8,color='yellow')


# In[50]:


# Simple bar plot
import numpy as np
import matplotlib.pyplot as plt
cities=['Delhi','Mumbai','Bangalore','Hydrabad']
population=[23456123,10083104,18456123,13411093]
plt.barh(cities,population,color=['r','b','g','y'])
plt.xlabel("population")
plt.ylabel("cities")


# In[51]:


# Simple bar plot
import numpy as np
import matplotlib.pyplot as plt
cities=['Delhi','Mumbai','Bangalore','Hydrabad']
population=[23456123,10083104,18456123,13411093]
plt.barh(cities,population,color=['r','b','g','y'])
plt.xlabel("cities")
plt.ylabel("population")


# In[56]:


# Simple bar plot
import numpy as np
import matplotlib.pyplot as plt
cities=['Delhi','Mumbai','Bangalore','Hydrabad']
population=[23456123,10083104,18456123,13411093]
plt.bar(cities,population,width=[0.2,0.4,0.6,0.8],color=['r','b','g','y'])
#plt.barh(cities,population,width=[0.2,0.4,0.6,0.8],color=['r','b','g','y'])
plt.xlabel("population")
plt.ylabel("cities")


# In[64]:


# Simple bar plot
import numpy as np
import matplotlib.pyplot as plt
cities=['Delhi','Mumbai','Bangalore','Hydrabad']
population=[23456123,10083104,18456123,13411093]
#plt.bar(cities,population,width=[0.2,0.4,0.6,0.8],color=['r','b','g','y'])
plt.barh(cities,population,width=[0.2,0.4,0.6,0.8],color=['r','b','g','y'])
plt.xlabel("population")
plt.ylabel("cities")


# In[54]:


#Recall of Univariate Line plot 
plt.plot([1, 2, 3, 4, 8])   #default values on x-axis are 0,1,2,3,4


# In[66]:


#HistoGram
# Histogram shows the quantitave values
ages = [32, 67, 113, 89, 65, 102, 93, 54, 69, 103, 74, 87, 105, 78, 116, 28, 92, 108, 29, 118, 135, 76, 84, 78, 23, 104, 75, 81]
age_groups = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140]
plt.hist(ages, age_groups, rwidth = 0.9)

plt.xlabel('age_groups')
plt.ylabel('population_ages')
plt.title("Histogram")


# In[68]:


data=np.random.randn(100) # number which follows normal distribution
plt.hist(data)
bins=[-3,-2,-1,1,2,3]   #integer or sequence or ‘auto’, optional these nos are on the left of the bin
plt.hist(data, bins=bins, color='blue',  edgecolor='green') 


# In[70]:


data=np.random.randn(100) # number which follows normal distribution
plt.hist(data,histtype='bar')
#bins=[-3,-2,-1,1,2,3]   #integer or sequence or ‘auto’, optional these nos are on the left of the bin
#plt.hist(data, bins=bins, color='blue',  edgecolor='green') 


# In[72]:


data=np.random.randn(100) # number which follows normal distribution
#plt.hist(data,histtype='bar')
bins=[-3,-2,-1,1,2,3]   #integer or sequence or ‘auto’, optional these nos are on the left of the bin
plt.hist(data, bins=bins, color='blue',  edgecolor='red') 


# In[73]:


data=np.random.randn(100) # number which follows normal distribution
#plt.hist(data,histtype='bar')
#bins=[-3,-2,-1,1,2,3]   #integer or sequence or ‘auto’, optional these nos are on the left of the bin
plt.hist(data, bins=bins, color='blue',  edgecolor='red') 


# In[74]:


data=np.random.randn(100) # number which follows normal distribution
#plt.hist(data,histtype='bar')
#bins=[-3,-2,-1,1,2,3]   #integer or sequence or ‘auto’, optional these nos are on the left of the bin
plt.hist(data, bins=25, color='blue',  edgecolor='red') 


# In[75]:


data=np.random.randn(100) # number which follows normal distribution
#plt.hist(data,histtype='bar')
#bins=[-3,-2,-1,1,2,3]   #integer or sequence or ‘auto’, optional these nos are on the left of the bin
plt.hist(data, bins=10, color='blue',  edgecolor='red') 


# In[78]:


data=np.random.randn(100) # number which follows normal distribution
#plt.hist(data,histtype='bar')
#bins=[-3,-2,-1,1,2,3]   #integer or sequence or ‘auto’, optional these nos are on the left of the bin
plt.hist(data, bins=10, histtype='step', color='blue',  edgecolor='red') 


# In[77]:


#hist function has many options to tune calculations and display
data=np.random.randn(100)
plt.hist(data,bins=30, histtype='stepfilled',color='steelblue',alpha=0.5) 
 #alpha lightens the color of hist


# In[80]:


np.random.seed(100)
n_bins = 5
x = np.random.randn(100, 3)    #three data could be say Revenue Profit and Sales of a Company
print(x.shape)
colors = ['red', 'tan', 'lime']
plt.hist(x, n_bins, density= None, histtype='bar', color = colors, label = colors)
#plt.hist(x, n_bins, density= None, histtype='bar',  color = colors, label = colors, stacked = True)
plt.legend()
plt.xlabel("Stocks")
plt.ylabel("revenue and profit")
#plt.show()


# In[114]:


np.random.seed(20)
n_bins = 5
x = np.random.randn(100, 3)    #three data could be say Revenue Profit and Sales of a Company
print(x.shape)
colors = ['red', 'tan', 'lime']
#plt.hist(x, n_bins, density= None, histtype='bar', color = colors, label = colors)
plt.hist(x, n_bins, density= None, histtype='bar',  color = colors, label = colors, stacked = True)
plt.legend()
plt.xlabel("Stocks")
plt.ylabel("revenue and profit")
#plt.show()


# In[81]:


np.random.seed(100)
n_bins = 5
x = np.random.randn(100, 3)    #three data could be say Revenue Profit and Sales of a Company
print(x.shape)
colors = ['red', 'tan', 'lime']
#plt.hist(x, n_bins, density= None, histtype='bar', color = colors, label = colors)
plt.hist(x, n_bins, density= None, histtype='bar',  color = colors, label = colors, stacked = True)
plt.legend()
plt.xlabel("Stocks")
plt.ylabel("revenue and profit")
#plt.show()


# In[82]:


np.random.seed(100)
n_bins = 8
x = np.random.randn(100, 3)    #three data could be say Revenue Profit and Sales of a Company
print(x.shape)
colors = ['red', 'tan', 'lime']
plt.hist(x, n_bins, density= None, histtype='bar', color = colors, label = colors)
#plt.hist(x, n_bins, density= None, histtype='bar',  color = colors, label = colors, stacked = True)
plt.legend()
plt.xlabel("Stocks")
plt.ylabel("revenue and profit")
#plt.show()


# In[110]:


#explain 3 arrays and bin intervals in output
#scatter plot(15)
import matplotlib.pyplot as plt
import numpy as np
x = np.random.randn(10)
y = np.random.randn(10)
print(x,y)
plt.scatter(x,y)             # Just marks the coordinates on the x-axis. 
#Understand why we dont use a Line plot here
#plt.plot(x,y)


# In[111]:


#explain 3 arrays and bin intervals in output
#scatter plot(15)
import matplotlib.pyplot as plt
import numpy as np
x = np.random.randn(10)
y = np.random.randn(10)
#print(x,y)
plt.scatter(x,y)             # Just marks the coordinates on the x-axis. 
#Understand why we dont use a Line plot here
#plt.plot(x,y)


# In[112]:


x = np.random.randn(10)
y = np.random.randn(10)
#print(x,y)
plt.scatter(x,y)             # Just marks the coordinates on the x-axis. 


# In[113]:


x=[1,2,3,4,5,6,7,8]
y=[4,5,8,7,4,9,2,3]
y= [2,4,6,8,10,13,15,16]
plt.scatter(x,y)
#plt.scatter(x,y,label='cat',color='k',, s=130,  marker='^')  # sis a marker size


# In[109]:


# Scatter plot using plt.plot()
x = np.linspace(0, 10, 50) # 50 numbers
y = np.sin(x)
plt.plot(x, y, 'o', color = 'blue')


# In[86]:


plt.plot(x , y, '-og')


# In[87]:


plt.plot(x, y, '-p', color='gray',
         markersize=15, linewidth=4,  
         markerfacecolor='white', 
         markeredgecolor='gray',
         markeredgewidth=2)    
plt.ylim(-1.2, 1.2);


# In[88]:


x = [1, 2, 3, 4, 5, 6, 7, 8]
#y = [5, 2, 4, 2, 1, 4, 5, 2]
y=[2,4,6,8,10,13,15,16]
plt.scatter(x, y, label = 'cat', color = 'k', s=130 , marker = "^")  # s is marker size
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Scatter Plot")
plt.legend()
plt.show()


# In[96]:


#x = [1, 2, 3, 4, 5, 6, 7, 8]
y = [5, 2, 4, 2, 1, 4, 5, 2]
y=[2,4,6,8,10,13,15,16]
plt.scatter(x, y, label = 'cat', color = 'k', s=130 , marker = "^")  # s is marker size
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Scatter Plot")
plt.legend()
plt.show()


# In[97]:


x = [1, 2, 3, 4, 5, 6, 7, 8]
y = [5, 2, 4, 2, 1, 4, 5, 2]
y=[2,4,6,8,10,13,15,16]
plt.scatter(x, y, label = 'cat', color = 'k', s=130 , marker = "^")  # s is marker size
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Scatter Plot")
plt.legend()
plt.show()


# In[98]:


#Pie Chart/Pie Plot
import matplotlib.pyplot as plt, numpy
plt.figure(figsize=(3,3))
x=(40,20,5)
labels=['Bikes', 'Cars', 'Buses']    #what is the % of each vehicle in the whole
plt.pie(x, labels = labels)   #plot x with labels given
plt.show()


# In[1]:


#Pie Chart/Pie Plot
import matplotlib.pyplot as plt, numpy
plt.figure(figsize=(3,3))
x=(40,20,5)  # total 65
labels=['Bikes', 'Cars', 'Buses']    #what is the % of each vehicle in the whole
plt.pie(x, labels = labels,autopct='%1.2f%%')   #plot x with labels given
plt.show()


# In[91]:


from matplotlib import pyplot as plt
import numpy as np
plt.figure(figsize=(4,4))
langs = ['C', 'C++', 'Java', 'Python', 'PHP']
students = [23,17,35,29,12]
cols = ['c', 'm', 'r', 'b', 'g']
#plt.pie(students, labels = langs, colors = cols, explode = (0, 0.1, 0, 0,0), autopct='%1.2f%%')
plt.pie(students , labels = langs, colors = cols, startangle = 90, shadow = False, explode = (0, 0.1, 0, 0,0), autopct = '%1.1f%%')
plt.show()


# In[2]:


from matplotlib import pyplot as plt
import numpy as np
plt.figure(figsize=(4,4))
langs = ['C', 'C++', 'Java', 'Python', 'PHP']
students = [23,17,35,29,12]
cols = ['c', 'm', 'r', 'b', 'g']
#plt.pie(students, labels = langs, colors = cols, explode = (0, 0.1, 0, 0,0), autopct='%1.2f%%')
plt.pie(students , labels = langs, colors = cols, startangle = 90, explode = (0, 0.1, 0, 0,0), autopct = '%1.1f%%')
plt.show()


# In[99]:


#BoxPlot(22)
#Generating two random normal variates
#We use the numpy.random.normal() function to create the fake data.
#arguments are mean and standard deviation of the normal distribution, and the number of values desired.
np.random.seed(10)
data1 = np.random.normal(100, 10, 200)  
data2 = np.random.normal(80, 30, 200)
data3 = np.random.normal(100, 20, 200)
# Create the boxplot
data=[data1, data2, data3]
plt.boxplot(data)
plt.show()
#Observe the mean and standard deviation in the graph


# In[108]:


#BoxPlot(22)
#Generating two random normal variates
#We use the numpy.random.normal() function to create the fake data.
#arguments are mean and standard deviation of the normal distribution, and the number of values desired.
np.random.seed(10)
data1 = np.random.normal(100, 10, 200)   #mean,variance,outliers 
data2 = np.random.normal(80, 10, 200)    #mean,variance,outliers 
data3 = np.random.normal(120, 30, 200)   #mean,variance,outliers 
# Create the boxplot
data=[data1, data2, data3]
plt.boxplot(data)
plt.show()
#Observe the mean and standard deviation in the graph


# In[6]:


#Error Bar(23)
#Error Bar added to line plot
plt.style.use('seaborn-whitegrid')
x = np.arange(10)/10  # values will be 0 to 0
y = (x + 0.1)**2     # instead of x2 we have x+0.1 to power 2 also x*2 + 2x*0.1 + 0.01
# defing our error  
y_error = np.linspace(0.05, 0.2, 10)    #error is between 0.05 and 0.2 in the square 
plt.errorbar(x,y,yerr=y_error, fmt='-og')


# In[106]:


# ploting our function and  error bar 
#plt.plot(x, y)  
plt.errorbar(x, y, yerr = y_error, fmt ='or') 
plt. xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Line plot with error bars')


# In[107]:


# Error can be added to the x-value too then the error bars are horizontal
x = np.arange(10)/10 
x_error=0.1
y = (x)**2     # instead of x2 we have x+0.1 to power 2
# defing our error  
#y_error = np.linspace(0.05, 0.2, 10)    #error is between 0.05 and 0.2 in the square 
# ploting our function and  error bar 
plt.plot(x, y)  
plt.errorbar(x, y, xerr = x_error, fmt ='or') 
plt. xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Line plot with error bars')


# In[8]:


# Error can be added to the x-value too then the error bars are horizontal
x = np.arange(10)/10 
x_error=0.1
y = (x)**2     # instead of x2 we have x+0.1 to power 2
# defing our error  
#y_error = np.linspace(0.05, 0.2, 10)    #error is between 0.05 and 0.2 in the square 
# ploting our function and  error bar 
plt.plot(x, y)  
plt.errorbar(x, y, xerr = x_error, fmt ='*g') 
plt. xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Line plot with error bars')


# In[9]:


# Error can be added to the x-value too then the error bars are horizontal
x = np.arange(10)/10 
x_error=0.1
y = (x)**2     # instead of x2 we have x+0.1 to power 2
# defing our error  
y_error = np.linspace(0.05, 0.2, 10)    #error is between 0.05 and 0.2 in the square 
# ploting our function and  error bar 
plt.plot(x, y)  
plt.errorbar(x, y, xerr = x_error, fmt ='*g') 
plt. xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Line plot with error bars')


# In[ ]:





# In[ ]:




