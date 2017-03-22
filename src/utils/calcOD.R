###############################################################################
## User Modification Section
# Starting OD
starting.OD = 0.1
desired.OD = 0.1
# Doubling time (hrs)
doubling.time = 1.5
# Time (hrs)
# Number of wells
wells = 6
steps = wells - 2
# Desired Volume
desired.volume = 5000 #uL
################################################################################
# Calculate Factors:
dilution.factor = 10^((log10(starting.concentration/ending.concentration))/steps)
transfer.volume = (desired.volume)/(dilution.factor - 1)

#Calculate Molarity
starting.volume = desired.volume + transfer.volume
input.drug.volume = (starting.volume*starting.concentration*concentration.factor)/(stock.concentration)

print(paste('Desired Volume: ', as.character(desired.volume)))
print(paste('Starting Volume:', as.character(starting.volume)))
print(paste('Drug Volume:', as.character(input.drug.volume)))
print(paste('Transfer Volume:', as.character(transfer.volume)))
