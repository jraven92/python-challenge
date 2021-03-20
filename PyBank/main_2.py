import os
import csv 
# csv_file= os.path.join( "Desktop", "Python_Challenge", "PyBank", "Resources", "budget_data.csv" )
csv_file= os.path.join("Resources", "budget_data.csv" )

# budget_file = ('Desktop/Python_Challenge/PyBank/Resources/budget_data.csv')

months = []
profit_loss_changes = []

count_months = 0
net_profit_loss = 0
previous_month_profit_loss = 0
current_month_profit_loss = 0
profit_loss_change = 0


with open(csv_file, newline='') as csvfile:
    budget_reader = csv.reader(csvfile, delimiter=',')
    budget_header = next(budget_reader)

    print(f'header: {budget_header}')
    for row in budget_reader:    
        count_months += 1

        # Net total amount of "Profit/Losses" over the entire period
        current_month_profit_loss = int(row[1])
        net_profit_loss += current_month_profit_loss

        if (count_months == 1):
            # Make the value of previous month to be equal to current month
            previous_month_profit_loss = current_month_profit_loss
            continue
        
        

        else:

            # Compute change in profit loss 
            profit_loss_change = current_month_profit_loss - previous_month_profit_loss

            # Append each month to the months[]
            months.append(row[0])

            # Append each profit_loss_change to the profit_loss_changes[]
            profit_loss_changes.append(profit_loss_change)

            # Make the current_month_loss to be previous_month_profit_loss for the next loop
            previous_month_profit_loss = current_month_profit_loss

    #sum and average of the changes in "Profit/Losses" over the entire period
    sum_profit_loss = sum(profit_loss_changes)
    average_profit_loss = round(sum_profit_loss/(count_months - 1), 2)

    # highest and lowest changes in "Profit/Losses" over the entire period
    highest_change = max(profit_loss_changes)
    lowest_change = min(profit_loss_changes)

    # Locate the index value of highest and lowest changes in "Profit/Losses" over the entire period
    highest_month_index = profit_loss_changes.index(highest_change)
    lowest_month_index = profit_loss_changes.index(lowest_change)

    # Assign best and worst month
    best_month = months[highest_month_index]
    worst_month = months[lowest_month_index]

# -->>  Print the analysis to the terminal
print("Financial Analysis")
print("----------------------------")
print(f"Total Months:  {count_months}")
print(f"Total:  ${net_profit_loss}")
print(f"Average Change:  ${average_profit_loss}")
print(f"Greatest Increase in Profits:  {best_month} (${highest_change})")
print(f"Greatest Decrease in Losses:  {worst_month} (${lowest_change})")


# -->>  Export a text file with the results
output_file = os.path.join( "pybank_budget_result.txt")
with open(output_file, "w", newline="") as datafile:

    datafile.write("Financial Analysis")
    datafile.write(f"Total Months:  {count_months}")
    datafile.write(f"Total:  ${net_profit_loss}")
    datafile.write(f"Average Change:  ${average_profit_loss}")
    datafile.write(f"Greatest Increase in Profits:  {best_month} (${highest_change})")
    datafile.write(f"Greatest Decrease in Losses:  {worst_month} (${lowest_change})")
    datafile.write("End of Report")
