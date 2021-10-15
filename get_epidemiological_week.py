
import pandas as pd
from epiweeks import Week



# Main function
def main(dataset, my_date_header, date_format):
    
    temp_date = string_to_date(dataset, my_date_header, date_format)
    date_to_epiweek(dataset, temp_date).to_csv('new_epidataset.csv', index=False)
    
    

# Convert string to date
def string_to_date(dataset, my_date_header, date_format):
    
    temp_date = pd.to_datetime(dataset[my_date_header], 
                                   format = date_format)
    return temp_date



# Returns year and epidemiological week in two columns
def date_to_epiweek(dataset, temp_date):
    
    epi_date = temp_date.apply(lambda date_name : Week.fromdate(date_name).weektuple())
    dataset[["epi_year","epi_week"]] = pd.DataFrame(epi_date.tolist())
    return dataset
    


df = pd.read_csv("dataset.csv")
main(df, "important_date", "%d/%m/%Y")