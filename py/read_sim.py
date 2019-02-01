import numpy as np

def avg_data(gg, alpha, Ctp, ud, folder):
    # averages the last period of the simulation
    A = np.loadtxt('../../sim/%s/%dm-a%0.2f/Ctp%0.2f/turbine/turbine_1.dat'%(folder, gg, alpha, Ctp))
    s = '%dm-a%0.2f-Ctp%0.2f'%(gg, alpha, Ctp)
    ud[s] = np.mean(A[450:,4])
    return ud

def write_data_file(folder):
    # Create empty dictionary
    d = dict()

    # Read data
    Ctps = np.array([0.25, 0.5, 0.75, 1, 1.25, 1.5, 1.75, 2.0])
    for Ctp in Ctps:
        avg_data(12, 0.75, Ctp+0.05, d, folder)
        avg_data(12, 1.50, Ctp,      d, folder)
        avg_data(12, 3.00, Ctp-0.05, d, folder)

        avg_data(6, 0.75, Ctp+0.05, d, folder)
        avg_data(6, 1.50, Ctp,      d, folder)
        avg_data(6, 3.00, Ctp-0.05, d, folder)
        avg_data(6, 6.00, Ctp-0.10, d, folder)

    Ctps = np.array([0.25, 0.75, 1.25, 1.75])
    for Ctp in Ctps:
        avg_data(3, 0.75, Ctp+0.05, d, folder)
        avg_data(3, 1.50, Ctp,      d, folder)
        avg_data(3, 3.00, Ctp-0.05, d, folder)
        avg_data(3, 6.00, Ctp-0.10, d, folder)

    # Write to file
    f = open('../data/%s.dat'%folder,'w')
    for key in d:
        f.write('%s %0.16f\n'%(key,d[key]))
    f.close()

# Write data files for uncorrected and corrected cases
write_data_file('uncorrected')
write_data_file('corrected')
