import pandas as pd


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
    processFile(file1)

    file2 = 'dataset2.csv'
    processFile(file2)


if __name__ == "__main__":
    main()
