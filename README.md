# ShapiroGaymeMeneveau-arXiv-2019
LaTeX and source for paper on filtered actuator disks (https://arxiv.org/abs/1901.10056)

## Simulations
Simulations were performed using LESGO with uniform inflow. The version of the code used in this communication is available at: https://github.com/lesgo-jhu/lesgo/releases/tag/ShapiroGaymeMeneveau-arXiv-2019. Example configuration files for the three resolutions used are available in the *sim* folder.

Various combinations of grid sizes, filter widths, and local thrust coefficients are used. The data files in *data* will list the combinations in the format (Δx/D)m-a(α)-Ctp(C′<sub>T</sub>). The Grid sizes used are:
* Δx = 3D, Δy = 3D, Δz = 3D/4
* Δx = 6D, Δy = 6D, Δz = 3D/2
* Δx = 12D, Δy = 12D, Δz = 3D

## LaTeX source code
The LaTeX source code is available in the folder *ltx*

## Figure files
The Figure files are available in the folder *fig*. They can be generated using the Python code in the folder *py*.
