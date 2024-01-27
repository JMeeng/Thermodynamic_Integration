

out_path = '/home/user/Documents/GitHub/Thermodynamic_Integration/CaseStudy_1/Run/out'
data_path = '/home/user/Documents/GitHub/Thermodynamic_Integration/total_energies'

total_energies = []
with open(out_path, 'r') as file:
    lines = file.readlines()
    for line in lines:
        if 'Total energy end of simulation' in line:
            total_energies.append(line.split()[6])

with open(data_path, 'w') as file:
    for energy in total_energies:
        file.write(energy + '\n')
