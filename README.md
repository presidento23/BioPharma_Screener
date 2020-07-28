# BioPharma Screener

# # How does it work?
The application takes a ~700 company long list and breaks it up into 5 pieces.  It takes those 5 seperate lists and makes an API call to TDAmeritrade. Then the data is processed to calculate % gains for the day and nominal gains for the day. The program is meant for premarket and after hours, however all times of the day work. A tkinter frame is then built to vizualize the data.


# How to get Started 
## Requirements
		pip install tkinter
		pip install pandas
		pip install requests
		pip install pandastable 

## Running the Code
After you have forked and downloaded the repository, enter your API key.

	ApiKey  =  'Enter your api key here'
If you would like to make an authenticated request the  option is also available here. 

	authorization  =  ''

You also need to uncomment the following code.

    # 'Authorization': authorization,

For all authorization codes you will need a new one every 30 minutes as per the TDAmeritrade guidelines. 

