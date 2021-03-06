import pandas as pd
import schedule
import time


def processFile(fileName):
    # Read csv file
    df = pd.read_csv(fileName)

    # Delete rows which do not have a name (Row has no value under name column)
    df = df.dropna(axis=0, subset=['name'])

    # Remove salutations from names
    df.name = df.name.replace(['Miss ', 'Mr\. ', 'Ms\. ', 'Dr\. ',
                               'Mrs\. ', 'MD', 'PhD', 'DVM', 'DDS'], '', regex=True)

    # Split name field into first_name and last_name
    df[['first_name', 'last_name']] = df.name.str.split(' ', n=1, expand=True,)

    # Remove leading zeros by converting to numeric type
    df.price = pd.to_numeric(df.price)

    # Add column to return true if the price is strictly greater than 100
    df['above_100'] = df.price.ge(100)

    print(df)

    # Output CSV file including header containing field names
    df.to_csv('processed_' + fileName, index=False)


def main():
    file1 = 'dataset1.csv'
    # processFile(file1)

    file2 = 'dataset2.csv'
    # processFile(file2)

    # Scheduled to run at 1am every day
    schedule.every().day.at("01:00").do(processFile, fileName=file1)
    schedule.every().day.at("01:00").do(processFile, fileName=file2)

    # Uncomment this to run all jobs now regardless of scheduling
    # schedule.run_all()

    # Comment this to stop waiting for the scheduled job to run
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()
