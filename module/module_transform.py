def transform(center=[0,0,0],rotation_angle=[0,0,0]):
	import numpy as np
	import math as m
	theta = rotation_angle[0]
	phi = rotation_angle[1]
	psi = rotation_angle[2]
	theta_r = m.radians(theta)
	phi_r = m.radians(phi)
	psi_r = m.radians(psi)
	rotation_theta = np.array([[1,0,0],[0,np.cos(theta_r),-np.sin(theta_r)],[0,np.sin(theta_r),np.cos(theta_r)]])
	rotation_phi = np.array([[np.cos(phi_r),-np.sin(phi_r),0],[np.sin(phi_r),np.cos(phi_r),0],[0,0,1]])
	rotation_psi = np.array([[1,0,0],[0,np.cos(psi_r),-np.sin(psi_r)],[0,np.sin(psi_r),np.cos(psi_r)]])
	rotation_matrix = np.dot(np.dot(rotation_theta,rotation_phi),rotation_psi)
	position_matrix = np.array(center).reshape(1,3)
	#print(rotation_matrix,position_matrix)
	return(rotation_matrix,position_matrix)