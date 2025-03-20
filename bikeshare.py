import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city =input("\nchoose the city(chicago, new york city, washington): ").lower()
    cities=('chicago','new york city','washington')
    while city  not in cities:
       print('please insert valid city.')
       city =input("choose the city:")
    
 
    # TO DO: get user input for month (all, january, february, ... , june)
    month =input("choose the  month: ").lower()
    months =("all","january", "february","march","april","may","june")
    while month  not in months:
       print('please insert valid month.')
       month =input("choose the  month: ").lower()
   
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day =input("choose day: ").lower()
    while day not in  ("all","saturday", "sunday","monday","tuesday","wednesday","thursday"):
        print('please insert valid day.')
        day =input("choose the  day: ").lower()
  
    print('-'*40)
    return city, month, day
    

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    df =pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.day_name()
    df['hour']=df['Start Time'].dt.hour
    # use the index of the months list to get the corresponding int
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month)+1
    
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
     
        df = df[df['day'] == day.title()]
   
    return df
    
def prompt_user_to_raw(df):
    
    raw =input('do you like to see first 5 lines of raw data? yes or no:')
    count=0
    while raw=='yes':
        
        print(df.iloc[count:count+5])              
        raw=input( 'do you like to see next 5 lines of raw data? yes or no:' )
        if raw=='yes':
         count+=5 

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    
     # TO DO: display the most common day of week
    common_day_of_week = df['day'].mode()[0]
    # TO DO: display the most common start hour
    common_start_hour = df['hour'].mode()[0]
    print('the most most common month is :    {}\nand the most common day of week is:   {}\nand the most common start hour is:    {} hour/s'.format(common_month , common_day_of_week , common_start_hour))
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)   
   
    


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    # TO DO: display most frequent combination of start station and end station trip
    df['station combination']=df['Start Station']+ '  to  ' + df['End Station']
    most_frequent_combination=df['station combination'].mode()[0]
    
    print('the most commonly used start station is :   %s' % common_start_station) 
    print('the most commonly used end station is :     %s'% common_end_station)
    print('most frequent combination of start station and end station trip is  :  %s'% most_frequent_combination)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel = df['Trip Duration'].sum()
    print('total travel time :%s   '% total_travel)

    # TO DO: display mean travel time
    mean_travel_time=df['Trip Duration'].mean()
    print('avrage travel time :%s  '%mean_travel_time)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types_counts= df['User Type'].value_counts()
    print('counts of user types :\n%s'%user_types_counts)

    # TO DO: Display counts of gender
   
    if city != 'washington':
        
        user_gender_counts= df['Gender'].value_counts()
        print('counts of user gender :\n%s'%user_gender_counts)
  
            # TO DO: Display earliest, most recent, and most common year of birth
        display_earliest=df['Birth Year'].min()
        print('earliest year of birth : %s' % int(display_earliest))
        most_recent=df['Birth Year'].max()
        print('most recent year of birth : %s' % int(most_recent))
        most_common=df['Birth Year'].mode()[0]
        print('most common year of birth : %s'% int(most_common))
    else :
        
        print('sorry there is no more user data available')
    
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        
        prompt_user_to_raw(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
           print('---------------<GOOD BYE>---------------') 
           break
        else:
            print('ok')
            print('-'*10)
            print('-'*20)
            print('-'*30)
            print('       on it        ')
            print('-'*40)
            print('-'*50)
            print('-'*60)

if __name__ == "__main__":
	main()
    
