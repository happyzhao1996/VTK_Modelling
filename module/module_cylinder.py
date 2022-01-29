def cylinder_number(grid=60):
	number_point = grid*2+2
	number_cell = grid+2
	number_cell_all = grid*7+4
	number_cell_type = grid+2
	return(number_point,number_cell,number_cell_all,number_cell_type)

def cylinder_point(file_out_name='draw.vtk',height=1,radius=0.5,grid=60,position=[0,0,0],rotation_angle=[0,0,0]):
	import numpy as np
	import math as m
	from module.module_transform import transform
	c = np.zeros([grid+1,3],dtype = float)
	d = np.zeros([grid+1,3],dtype = float)
	for i in range(0,grid+1):	
		c[i] = [radius*np.sin(m.radians(360/grid*i)),radius*np.cos(m.radians(360/grid*i)),height]
		d[i] = [radius*np.sin(m.radians(360/grid*i)),radius*np.cos(m.radians(360/grid*i)),0]
	rotation_matrix,position_matrix = transform(position,rotation_angle)
	for i in range(len(c)):
		c[i] = np.dot(c[i],rotation_matrix)+position_matrix
	for i in range(len(d)):
		d[i] = np.dot(d[i],rotation_matrix)+position_matrix
	with open(file_out_name,'a') as file_out:
		np.savetxt(file_out,c)
		np.savetxt(file_out,d)

def cylinder_cell(start_point=0,grid=60):
	text_cell = ''
	text_cell_type = ''

	text_cell += str(grid+1)+'\t'+'\t'.join([str(x) for x in range(start_point,start_point+grid+1)])+'\n'
	for i in range(0,grid):
		text_cell += '4\t'+str(start_point+i)+'\t'+str(start_point+i+1)+'\t'+str(start_point+grid+i+1)+'\t'+str(start_point+grid+i+2)+'\n'
	text_cell += str(grid+1)+'\t'+'\t'.join([str(x) for x in range(start_point+grid+1,start_point+grid*2+2)])+'\n'

	text_cell_type += '7\n'
	for i in range(1,grid+1):
		text_cell_type += '8\n'
	text_cell_type += '7\n'
	#print(text_cell,text_cell_type)
	return(text_cell,text_cell_type)

def cylinder_data(grid=60,rotation_angle=[0,0,0]):
	text_data = ''
	for i in range(0,grid+2):
		text_data += str(rotation_angle[0]) + '\n'
	return(text_data)