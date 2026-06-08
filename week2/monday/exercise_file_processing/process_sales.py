"""
Week 2 Exercise — CSV processing with context managers.

TODO:
1. Read starter_code/data/sales.csv using csv.DictReader and with open(...).
2. Compute rows count, grand total (sum of units * unit_price), average line revenue.
3. Find SKU with max line revenue (tie: first in file).
4. Write output/summary.txt using with open(..., "w", encoding="utf-8").
"""

from __future__ import annotations
from pathlib import Path 
import csv

file_name="sales.csv"
output_file_name="summary.txt"
dir_name = "output"


def main() -> None:
    # Your implementation here

    rows = 0
    grand_total = 0
    top_sku = None
    top_line_rev = 0

    try:
    
        with open(file_name, 
                mode='r',
                encoding="utf-8",
                newline="") as file:
            reader=csv.DictReader(file)

       

            for row in reader:
                #print(row["units"],row["unit_price"])
                units = int(row["units"])
                price=float(row["unit_price"])

                line_rev= units * price
                grand_total += line_rev

                rows+=1

                if line_rev>top_line_rev:
                    top_line_rev=line_rev
                    top_sku=row["sku"]

            average_line_rev = grand_total / rows

                
        
    except FileNotFoundError:
        print(f"File {file_name} was not found ")
        #add logger
    except Exception as e:
        print(f"Missing bad row",e)
        #add logger
        
    #check if output dir exsist, if not then create one
    Path(dir_name).mkdir(exist_ok=True)

    # writes to file summary.txt in the output dir
    with open(dir_name + '/' + output_file_name, 
                    mode='w',
                    encoding="utf-8",
                    newline="") as ofile:
        
        ofile.write(f"rows={rows}\n")
        ofile.write(f"grand_total={grand_total}\n")
        ofile.write(f"average_line_revenue={average_line_rev:.2f}\n")
        ofile.write(f"top_sku={top_sku}\n")
        ofile.write(f"top_line_revenue={top_line_rev}")
        
            
        

            



    #raise NotImplementedError("Complete this exercise")



if __name__ == "__main__":
    main()