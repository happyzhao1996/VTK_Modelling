def arrow_number(start_point=0,cone_grid=60,cylinder_grid=60):
	number_points = 0
	number_cells = 0
	number_cells_all = 0
	number_cell_types = 0
	text_cells = ''
	text_cell_types = ''

	from module.module_cone import cone_number,cone_cell
	number_point,number_cell,number_cell_all,number_cell_type = cone_number(grid=cone_grid)
	text_cell,text_cell_type = cone_cell(start_point,grid=cone_grid)
	number_points += number_point
	start_point += number_point
	number_cells += number_cell
	number_cells_all += number_cell_all
	number_cell_types += number_cell_type
	text_cells += text_cell
	text_cell_types += text_cell_type

	from module.module_cylinder import cylinder_number,cylinder_cell
	number_point,number_cell,number_cell_all,number_cell_type = cylinder_number(grid=cylinder_grid)
	text_cell,text_cell_type = cylinder_cell(start_point,grid=cylinder_grid)
	number_points += number_point
	start_point += number_point
	number_cells += number_cell
	number_cells_all += number_cell_all
	number_cell_types += number_cell_type
	text_cells += text_cell
	text_cell_types += text_cell_type

	return(number_points,number_cells,number_cells_all,number_cell_types,text_cells,text_cell_types)


def arrow_point(file_out_name='draw.vtk',cone_height=2,cone_radius=1,cone_grid=60,cylinder_height=3,cylinder_radius=0.5,cylinder_grid=60,position=[0,0,0],rotation_angle=[0,0,0]):
	import numpy as np
	import math as m

	from module.module_transform import transform
	cylinder_position = np.dot(np.asarray([0,0,-(cylinder_height+cone_height)/2]),transform([0,0,cylinder_height],rotation_angle)[0])+np.asarray(position)
	cone_position = np.dot(np.asarray([0,0,(cylinder_height-cone_height)/2]),transform([0,0,cylinder_height],rotation_angle)[0])+np.asarray(position)
	
	from module.module_cone import cone_point
	cone_point(file_out_name=file_out_name,height=cone_height,radius=cone_radius,grid=cone_grid,position=cone_position,rotation_angle=rotation_angle)
	from module.module_cylinder import cylinder_point
	cylinder_point(file_out_name=file_out_name,height=cylinder_height,radius=cylinder_radius,grid=cylinder_grid,position=cylinder_position,rotation_angle=rotation_angle)


def arrow_data(cone_grid=60,cylinder_grid=60,rotation_angle=[0,0,0]):
	#print(rotation_angle)
	text_data = ''
	text_data_all = ''
	from module.module_cone import cone_data
	text_data = cone_data(grid=cone_grid,rotation_angle=rotation_angle)
	text_data_all += text_data
	from module.module_cylinder import cylinder_data
	text_data = cylinder_data(grid=cylinder_grid,rotation_angle=rotation_angle)
	text_data_all += text_data
	return text_data_all