from csv import reader

title = 'mobile phone analyst'
introduction = ("This project aims to analyze data to help understand what type of apps are likely to acctract more "
                "users. And the goal is practice python jupyter.")

# define two empty list to store data from csv files
# The google play data set
opened_file = open('googleplaystore.csv')
read_file = reader(opened_file)
android = list(read_file)
android_header = android[0]
android = android[1:]

# The App Store data set
opened_file = open('AppleStore.csv')
read_file = reader(opened_file)
ios = list(read_file)
ios_header = ios[0]
ios = ios[1:]

