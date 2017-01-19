#!/usr/bin/python2.7
import numpy as np

def get_all_table(matrice_a):
	#on part du principe que la matrice est de taille n * n
	table_c=[]
	table_l=[]
	table_i=[]
	matrice_size = matrice_a.shape[0]
	element_courant = 0
	element_courant_tmp=0
	for i in range(matrice_size):
		table_l.append(element_courant)
		for j in range(matrice_size):
			
			if(matrice_a[i][j]!=0):
				table_c.append(matrice_a[i][j])
				element_courant+=1		
				table_i.append(j)
	table_l.append(len(table_c))
	return table_c,table_l,table_i

def 


def multiplie_matrice(matrice_a,matrice_b):
	print(matrice_a)
	print(matrice_b)


def init_res_empty_matrix(matrice_a,matrice_b):
	matrix_a_size_information = matrice_a.shape
	matrix_b_size_information = matrice_b.shape
	res=""
	max_line = max(matrix_b_size_information[0],matrix_a_size_information[0])
	#on considere que la matrice est carree de taille n
	max_column = max(matrix_b_size_information[1],matrix_b_size_information[1])
	matrix_size = max(max_column,max_line)
	print(max_line,max_column)
	res+='['
	for i in range(matrix_size):
		res+='['
		for j in range(matrix_size):
			if j == matrix_size-1:
				res+="0"
			else:
				res+="0,"
		if i == matrix_size-1:
			res+="]"
		else:
			res+="],"
	res+=']'
	empty_matrix = np.array(res)
	return empty_matrix


b = np.array([[0,3,5,8],[1,0,2,0],[0,0,0,0],[0,3,0,0]])
a = np.array([[0,0,1,0],[2,3,0,4],[0,5,6,7],[0,0,0,0]])
print(get_all_table(b))
print(get_all_table(a))
#multiplie_matrice(a,a)
print(init_res_empty_matrix(a,a))

