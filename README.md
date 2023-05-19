# Super_Py
Python-Assignment-final

Please check for the right updates:

python --version
pip --version
pip install rich
pip install pandas
pip install matplotlib


positional arguments:
  {add,sold}            Available commands
    add                 Add a product to the in_stock.csv file
        by --name, -- price, exp-date ( the current date will be profided)

    sold                Add a product to the sold.csv file
        by --name --price

options:
  -h, --help            show this help message and exit
  --report REPORT       Command to execute
        + 'in_stock' = table-report and visualization 
        + 'sold' = table-report and visualization
        + 'total' = tablereport of all revenue
        + 'profit' 

  --expired EXPIRED     Path to the CSV file

        + by adding a date to find out what can be in SALE

  --advance-time ADVANCE_TIME
                        Advance time by specified number of days
