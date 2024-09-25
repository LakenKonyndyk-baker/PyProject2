import math

while True:
    Year = int(input("Enter Year: "))
    print(f"Approximating Ferrari 250 GTO Value from Year '\033[34m{Year}\033[0m'")
    print("\n")
    if (1962<=Year<=2014):
        print("Year is in Dataset \033[34m(interpolated data)\033[0m:")
        data_years = [1962,1965,1969,1972,1976,1981,1986,2013,2015]
        data_prices = [18500,6000,12000,48000,200000,650000,35000000,52000000]
        year_range = 'empty-empty'
        Cost = 0
        for i,table_year in enumerate(data_years):
            if (Year >= table_year) and not (Year >= data_years[i+1]):
                year_range = str(table_year)+'-'+str(data_years[i+1]-1)
                Cost = data_prices[i]
                break
        print(f"The Ferrari 250 GTO in {year_range} was worth \033[92m${Cost}\033[0m")
    else:
        print("Year is \033[91mNOT\033[0m in Dataset.")
    print('\n')