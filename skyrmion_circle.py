import math as m
import numpy as np

# Initialize
file_out_name = 'skyrmion_circle.vtk'
text_head = '# vtk DataFile Version 3.0\n\nASCII\n\nDATASET UNSTRUCTURED_GRID\n'
number_points = 0
number_cells = 0
number_cells_all = 0
number_cell_types = 0
text_cells = ''
text_cell_types = ''
text_cell_data_all = ''
file_out = open(file_out_name,'w')
file_out.write(text_head)
file_out.close()

# Define Parameters
cone_height = 3
cone_radius = 1.5
cone_grid = 60
cylinder_height = 3
cylinder_radius = 0.75
cylinder_grid = 60
position = [0,0,0]
start_point = 0
rotation_angle = [0,0,0]
radius = 40

r = [0,6.6,13.2,20,26.6,33.2,40]
theta = [1,8,12,16,24,32,40]

x = []
y = []

for i in range(len(r)):
	for j in range(0,theta[i]):
		x.append(r[i]*np.cos(360/theta[i]*j/180*m.pi))
		y.append(r[i]*np.sin(360/theta[i]*j/180*m.pi))


# Calculate Number of Points and Connections
from module.module_arrow import arrow_number
for k in range(len(x)):
	i = x[k]
	j = y[k]
	number_point,number_cell,number_cell_all,number_cell_type,text_cell,text_cell_type = arrow_number(start_point=start_point,cone_grid=cone_grid,cylinder_grid=cylinder_grid)
	number_points += number_point
	start_point += number_point
	number_cells += number_cell
	number_cells_all += number_cell_all
	number_cell_types += number_cell_type
	text_cells += text_cell
	text_cell_types += text_cell_type


# Write Points
file_out = open(file_out_name,'a')
text_point_head = '\nPOINTS\t' + str(number_points) + '\tfloat\n'
file_out.write(text_point_head)
file_out.close()

from module.module_arrow import arrow_point,arrow_data
for k in range(len(x)):
	i = x[k]
	j = y[k]
	position = [i,j,0]
	if i**2+j**2<=2500:
		if i!= 0:
			rotation_angle = [-(i**2+j**2)**0.5/radius*180,-m.atan(j/i)/m.pi*180+np.sign(i)*90+180,0]
		else:
			rotation_angle = [-(i**2+j**2)**0.5/radius*180,np.sign(j)*90-90,0]
	else:
		rotation_angle = [-180,0,0]
	arrow_point(file_out_name=file_out_name,cone_height=cone_height,cone_radius=cone_radius,cone_grid=cone_grid,cylinder_height=cylinder_height,cylinder_radius=cylinder_radius,cylinder_grid=cylinder_grid,position=position,rotation_angle=rotation_angle)
	#print(rotation_angle)
	text_cell_data = arrow_data(cone_grid=cone_grid,cylinder_grid=cylinder_grid,rotation_angle=rotation_angle)
	text_cell_data_all += text_cell_data


# Write Cells
file_out = open(file_out_name,'a')
text_cell_head = '\nCELLS\t' + str(number_cells) + '\t' + str(number_cells_all) +'\n'
file_out.write(text_cell_head)
file_out.write(text_cells)
file_out.close()

# Write Cell Types
file_out = open(file_out_name,'a')
text_cell_type_head = '\nCELL_TYPES\t' + str(number_cell_types) + '\n'
file_out.write(text_cell_type_head)
file_out.write(text_cell_types)
file_out.close()

# Write Cell Data
file_out = open(file_out_name,'a')
text_cell_data_head = '\nCELL_DATA\t' + str(number_cell_types) +'\nSCALARS\tz_angle\tfloat\t1\nLOOKUP_TABLE\tdefault\n'
file_out.write(text_cell_data_head)
file_out.write(text_cell_data_all)
file_out.close()
