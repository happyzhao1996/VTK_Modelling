def cone_number(grid=60):
	number_point = grid+2
	number_cell = grid+1
	number_cell_all = grid*5+2
	number_cell_type = grid+1
	return(number_point,number_cell,number_cell_all,number_cell_type)

def cone_point(file_out_name='draw.vtk',height=2,radius=1,grid=60,position=[0,0,0],rotation_angle=[0,0,0]):
	import numpy as np
	import math as m
	from module.module_transform import transform
	a = np.zeros([1,3],dtype = float)
	b = np.zeros([grid+1,3],dtype = float)
	a[0] = [0,0,height]
	for i in range(0,grid+1):
		b[i] = [radius*np.sin(m.radians(360/grid*i)),radius*np.cos(m.radians(360/grid*i)),0]
	rotation_matrix,position_matrix = transform(position,rotation_angle)
	for i in range(len(a)):
		a[i] = np.dot(a[i],rotation_matrix)+position_matrix
	for i in range(len(b)):
		b[i] = np.dot(b[i],rotation_matrix)+position_matrix
	with open(file_out_name,'a') as file_out:
		np.savetxt(file_out,a)
		np.savetxt(file_out,b)

def cone_cell(start_point=0,grid=60):
	text_cell = ''
	text_cell_type = ''
	for i in range(1,grid+1):
		text_cell += '3\t'+str(start_point)+'\t'+str(start_point+i)+'\t'+str(start_point+i+1)+'\n'
	text_cell += str(grid+1)+'\t'+'\t'.join([str(x) for x in range(start_point+1,start_point+grid+2)])+'\n'
	for i in range(1,grid+1):
		text_cell_type += '5\n'
	text_cell_type += '7\n'
	#print(text_cell,text_cell_type)
	return(text_cell,text_cell_type)

def cone_data(grid=60,rotation_angle=[0,0,0]):
	text_data = ''
	for i in range(0,grid+1):
		text_data += str(rotation_angle[0]) + '\n'
	return(text_data)