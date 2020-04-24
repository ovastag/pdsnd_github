import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

CITIES = ['chicago', 'new york city', 'washington']
MONTHS = ['january', 'february', 'march', 'april', 'may', 'june']
DAYS = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday' ]

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
    while True:
            city = input("What city are you looking for? Please specify for Chicago, New York City or Washington: ").lower()
            if city in CITIES:
                break
            else: print('Oops, something went wrong. That is not a valid input. You might misspelled Chicago, New York City or Washington. Please try again.')

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("Are you interested in a specific month? Please insert all or a specific month: ").lower()
        if month in MONTHS or month == 'all':
            break
        else: print('Oops, something went wrong. That is not a valid input. You might misspelled the month from January until June. Please try again.')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Are you interested in a specific day of the week? Please insert all or a specific day of the week: ").lower()
        if day in DAYS or day == 'all':
            break
        else: print('Oops, something went wrong. That is not a valid input. Yout might misspelled the weekday from Sunday till Saturday. Please try again.')

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
    # create data frame based on csv
    df = pd.read_csv(CITY_DATA[city])

    # convert start time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month, day of week and hour from start time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour


    # filter by month if applicable
    if month != 'all':
    # use index of months list to get corresponding int
        month = MONTHS.index(month) + 1

    # filter by month to create new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].value_counts().idxmax()
    print('The most common month is: \n', popular_month)

    # TO DO: display the most common day of week
    popular_day = df['day'].value_counts().idxmax()
    print('The most common day of week is (if filtered for a specific day, that day is shown): \n', popular_day)

    # TO DO: display the most common start hour
    popular_hour = df['hour'].value_counts().idxmax()
    print('The most common start hour is: \n', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating the most popular stations and trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_startstation = df['Start Station'].value_counts().idxmax()
    print('The most commonly used start station is: \n', popular_startstation)

    # TO DO: display most commonly used end station
    popular_endstation = df['End Station'].value_counts().idxmax()
    print('The most commonly used used end station is: \n', popular_endstation)

    # TO DO: display most frequent combination of start station and end station trip
    popular_combistation = (df['Start Station'] + ' to ' + df['End Station']).value_counts().idxmax()
    print('The most frequent combination of start station and end station is: \n', popular_combistation)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('The total travel time is: \n', total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('The mean travel time is: \n', mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('The ounts of user types: \n', user_types)


    while True:
        try:
            # TO DO: Display counts of gender exit

            gender = df['Gender'].value_counts()
            print('The counts of gender: \n', gender)

            # TO DO: Trip duration per gender
            trip_per_gender = df.groupby(['Gender'])['Trip Duration'].mean()
            print('The trip duration on average for male and female: \n', trip_per_gender)

            # TO DO: Display earliest, most recent, and most common year of birth
            earliest = df['Birth Year'].min()
            most_recent = df['Birth Year'].max()
            most_common = df['Birth Year'].value_counts().idxmax()
            print('The earliest birth year is {} while the most recent one is {} - the most common birth year is {}.\n'.format(earliest, most_recent, most_common))

            # TO DO: Trip duration per year
            trip_per_year = df.groupby(['Birth Year'])['Trip Duration'].mean()
            print('Per year, the following trip duration average: \n',trip_per_year)
            break
        except:
            print('For Washington, no data availabe regarding gender and year of birth  \n')
            break

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
