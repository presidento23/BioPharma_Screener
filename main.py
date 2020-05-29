from datetime import datetime, time
from tkinter import *
from tkinter import ttk

import numpy as np
import pandas as pd
import requests as requests
from pandastable import Table

# Intially sets the variable showing.Vital because you can not reuse a variable typically when a function is run.
# Without it the function show_details would throw an error.
showing = False

# Creates the gui
root = Tk()


dfinal = pd.read_pickle("./biotechfinalv1.pkl")

#### doutput needs to be sanitazed throughout the various functions so that it doesn't get deleted everytime and only print the last price of the chunks
doutput = dfinal
global df1
global increment
global loopcount


def StockQuotesCall():
    QuotesURl = 'https://api.tdameritrade.com/v1/marketdata/quotes'
    ApiKey =  'Enter your api key here'
    # API CALL HAS A  500 symbol limit
    # Sorts by Ticker so it is easier to debug.

    dfinal.sort_values(by ='Ticker',inplace = True)

    # The for loops divides the dataframe by 5 and then extracts the necessary information for each chunk.
    # the dataframe gets divided up because the api can't handle large batch requests in a consistent manner.
    global loopcount
    loopcount = 0
    for chunk in np.array_split(dfinal,5):
        # Simple list comprenhension to convert the dataentries into a string sepereate by a common.
        stocksToCall = ','.join([str(chunk.Ticker.iloc[x])for x in range(len(chunk.Ticker))])


        # Authorization key isn't necessary but needs to be updated every 30 minutes if you plan to use it.
        # You can add it i you like.
        authorization = ''
        params = {'apikey' : ApiKey,
                  # 'Authorization': authorization,
                  'symbol': stocksToCall}
        r = requests.get(url = QuotesURl,params= params)
        data = r.json()
        # uses function to strip necessary data out of the json and puts it in a new dictionary
        # All functions below returns a dictionary and also adds it to doutput.
        # I store the data as a dictionary instead of a json to make it easier to handle large dictionaries.
        lastPrice = stockParse('lastPrice',data)
        closePrice = stockParse('closePrice',data)
        netChange = stockSubtraction(lastPrice,closePrice)
        MakeAPercentage(netChange,closePrice)

        # I'm using 'A' because I know its the first ticker in the pandas list. Just need to grab the time one time
        # python only reads up to the second while epoch time is in miliseconds
        try:
            datetimeofquote = datetime.fromtimestamp(data[chunk.Ticker.iloc[0]]['tradeTimeInLong']/1000)

        except:
            continue
        notAfterHours = is_time_between(time(9, 30),time(16, 30),datetimeofquote)

        print(dfinal.Ticker[0])
        global df1
        df1 = doutput
        loopcount += 1
    # The after method tells the function to run again  every x milisecs once the program begins
    if showing:
        return doutput

    else:
        root.after(10000, StockQuotesCall)
        return doutput

# stockParse(string, json object)

def stockParse(requestValue, dataset):
    # Function makes a new dictionary to add to
    # and adds to a pandas library so that way I don't have to keep extracting data from a pandas datafram in every
    # function.
    nameRequestvalue ={}

    for x in dataset:
        try:
            print(dataset[x][requestValue])
            nameRequestvalue[x] = dataset[x][requestValue]

        except TypeError:
            continue

    if loopcount == 0:
        doutput.loc[:, requestValue] = doutput['Ticker'].map(nameRequestvalue)

    else:
        m = doutput[requestValue].isna()
        # Need to figure out how to always update it. if ran.
        doutput.loc[m, requestValue] = doutput.Ticker.map(nameRequestvalue)
    return nameRequestvalue

# The parameters for the StockSubtraction should be dictionaries


def stockSubtraction(value1, value2):
    stockSubtractionResults = {}
    for x in value1:
        stockSubtractionResults[x] = value1[x] - value2[x]

    if loopcount == 0:
        doutput.loc[:, 'Change'] = doutput['Ticker'].map(stockSubtractionResults)

    else:
        m = doutput['Change'].isna()
        doutput.loc[m, 'Change'] = doutput.Ticker.map(stockSubtractionResults)
    return stockSubtractionResults


def MakeAPercentage(numerator, denominator):
    percentageResults = {}
    for x in numerator:
        if denominator[x] == 0:
            percentageResults[x] = 0
        else:
            percentageResults[x] = (numerator[x]/denominator[x]) *100

    if loopcount == 0:
        doutput.loc[:, '%Change'] = doutput['Ticker'].map(percentageResults)

    else:
        m = doutput['%Change'].isna()
        doutput.loc[m, '%Change'] = doutput.Ticker.map(percentageResults)

    return percentageResults

# It takes integers time(intgers) for all of the inputs.  It returns False if market is after hours


def is_time_between(begin_time, end_time, check_time=None):
    # If check time is not given, default to current UTC time
    # Check time is a datetime object in this example
    # returns false if it is the weekend or outside of normal market hours. 9:30 am to 4:30 pm

    dayofweek = check_time.weekday()
    if dayofweek == 5 or dayofweek == 6:
        return False
    else:
        check_time = datetime.time(check_time)

    if begin_time < end_time:
        return check_time >= begin_time and check_time <= end_time
    else: # crosses midnight
        return check_time >= begin_time or check_time <= end_time


# sets a variable to be used as the dataframe for the tables in the function, calls a function which returns a dataframe
# df1 = StockQuotesCall()

def show_details():
    # declares that showing will refer to the global variable mentioned above instead of to a local variable for this function
    global showing

    # toggles on or off by testing whether or not the details are already showing
    if showing == False:
        # flips the switch to on.
        showing = True

        # declares all of these future variables as global ones so they can be refered to the next time the function runs.
        global dt
        # Simply creates a block of text and appends it to the Mainframe(See below for more details) for each variable.
        # .grid just forces a positon for the newly created label.
        dt = Table(mainframe, dataframe= StockQuotesCall())
        dt.grid(column=10, row=0, sticky=(N, W, E, S))
        dt.show()
        dt.redraw()




    else:
        # No matter what I use, dt.close(), dt.grid_forget, dt.pack_forget, dt.pack_remove, dt.grid_remove, dt.destroy, none of them works properly with the table.
        # Must be mod error
        showing = False
        #
        dt.grid_forget()


# Gives a title to the gui
root.title("Final Proyecto")

# Creates a box or a frame and appends it to the gui.
mainframe = ttk.Frame(root, padding="3 3 12 12")
# Positions the mainframe in the gui
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

# Makes the gui expand on resize. The GUI and Mainframe are two distinct elements.
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)




### creates buttons and appends them to the tkinter frame caleld "MainFrame", assigns functions to each button with the
# command parameter and assigns the butto..n a poisiton on the MainFrame in one line. Sticky = W appens it to the west side of the
# Grid cell.

# root.destroy just deletes the gui and cleans whatver cache has built over time.
ttk.Button(mainframe,text = "BioPharma Screener", command = show_details).grid(column= 2, row= 2, sticky=(W))



# Calls Tkinter method that runs the gui and make sure its constantly on the screen hence the loop aspect.
root.mainloop()
