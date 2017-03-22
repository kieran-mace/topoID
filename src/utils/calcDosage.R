# ###############################################################################
# # User Modification Section
#
# Progesterone Standard
# stock.concentration = 3180000 #nM
# # Desired 1X Concentrations
# starting.concentration = 15 #nM #1x
# ending.concentration = 0.05 #1x
# # Desired concentration factor
# concentration.factor = 10
# # Number of wells
# wells = 12
# steps = wells - 2
# # Desired Volume
# desired.volume = 5000 #uL

# # Estradiol Standard
stock.concentration = 3670000 #nM
# Desired 1X Concentrations
starting.concentration = 125 #nM #1x
ending.concentration = 3.5 #1x
# Desired concentration factor
concentration.factor = 10
# Number of wells
wells = 8
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

#Calculate Dosages
dosages = numeric()
for(well.num in 1:wells){
dosages[well.num] = (((input.drug.volume*stock.concentration)/(starting.volume))/concentration.factor)*(transfer.volume/starting.volume)^(well.num-1)
}
# Last dosage is always zero
dosages[wells] = 0


print(paste('Desired Volume: ', as.character(desired.volume)))
print(paste('Starting Volume:', as.character(starting.volume)))
print(paste('Drug Volume:', as.character(input.drug.volume)))
print(paste('Transfer Volume:', as.character(transfer.volume)))
print(paste('1 X Dosages:', as.character(paste(rev(dosages), collapse = ', '))))
print(paste('Dosages:', as.character(paste(rev(dosages)*concentration.factor, collapse = ', '))))
