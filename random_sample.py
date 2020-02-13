import pandas as pd
import datetime

NOW = datetime.datetime.now()

def main():
    #Get data and figure out if we need to split the data by group
    data, header, group_flag = param_prompt()
    if group_flag:
        #Then ask how many per group
        column_index, sample_size = get_group_sample_size(header)
        #print(header[column_index], sample_size)
        grouped = data.groupby(by=header[column_index])
        sampled = grouped.apply(lambda x: x.sample(n=sample_size))
    else:
        #Get sample size
        sample_size = get_sample_size()
        #Sample data set and set to new variable.
        sampled = data.sample(n=sample_size)
    sampled.to_csv("output_%s.csv" % (NOW))

#Open .csv, return data as pandas dataframe and header (column names)
def preview_csv(file):
    data = pd.read_csv(file)
    header = data.columns
    return data, header

#Prompt user to choose if they want to randomly sample the entire sheet or sample by groups first.
def group_by_prompt():
    flag = input("Would you like to sample tasks per group? y/n: ")
    flag = flag.lower()
    print("flag: %s" % (flag))
    if flag == 'y':
        return True
    elif flag == 'n':
        return False
    else:
        group_by_prompt()

def get_group_sample_size(header):
    print("Which column would you like to group by?")
    for i in range(len(header)):
        print("%s. %s" % (i+1, header[i]))
    column_index = input("Please select a column number: ")
    column_index = int(column_index) - 1
    sample_size = input("How many tasks per group would you like to sample? (Sample size must be less than or equal to the number of tasks per group) ")
    sample_size = int(sample_size)
    return column_index, sample_size

def get_sample_size():
    sample_size = input("How many tasks would you like to sample? ")
    sample_size = int(sample_size)
    return sample_size

#Prompt user to figure out all of the necessary inputs in order to randomly sample.
#Need to know:
#   -# of tasks to sample
#   -Sample by group?
#   -Group by which column?
#   -If yes, # of tasks to sample per group.
def param_prompt():
    filepath = input("Please paste the filepath of the .csv you wish to randomly sample.")
    data, header = preview_csv(filepath)
    #Column names
    print(header)
    #Row count
    print(data.shape[0])
    group_flag = group_by_prompt()
    return data, header, group_flag


if __name__ == '__main__':
    main()
