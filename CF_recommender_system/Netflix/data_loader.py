import os
import os.path
import numpy as np
import random
import itertools as ite

# (original) dataset content: user id/ item id /rating /timestamp
# (data_loader.py) dataset content: user id/ item id /rating

# Usage Example:
# import data_loader as dl
# dataset=dl.loader_1M()
# splitted_dataset=dl.split_dataset( dataset )

def loader_1M():

	# load 1M dataset from the directory
	# no input
	# returns 2D ndarray type dataset

	f = open(os.path.dirname(__file__) + '/../../dataset/MovieLens/1M_dataset/ratings.dat',"r")
	text=f.read().split('\n')
	new_text=np.asarray([np.asarray([np.float(element) for element in row.split("::")[0:3]]) for row in text[0:-1]])
	return new_text

def loader_100k():

	# load 100k dataset from the directory
	# no input
	# returns 2D ndarray type dataset

	f = open(os.path.dirname(__file__) + '/../../dataset/MovieLens/100k_dataset/u.data',"r")
	text=f.read().split('\n')
	new_text=np.asarray([np.asarray([np.float(element) for element in row.split("\t")[0:3]]) for row in text[0:-1]])
	return new_text


def split_dataset(dataset, num_fold=5):

	# split the given dataset
	# dataset and number of folds(default 5) as input
	# returns 4D ndarray type dataset :   [ [trainset, testset] * num_fold ] with trainset and testset being 2D ndarray dataset
	
	if(num_fold<2 or num_fold==None):
		print("error in num_fold argument")
		return -1
	data_length=len(dataset)
	index_array=np.arange(data_length)
	random.shuffle(index_array)
	start=stop=0
	resulting_set=[]
	for i in range(num_fold):
		start = stop
		stop += len(index_array) // num_fold
		if i < len(index_array) % num_fold:
			stop += 1

		trainset = np.asarray([dataset[j] for j in ite.chain(index_array[:start],index_array[stop:])],dtype=object)
		testset = np.asarray([dataset[j] for j in index_array[start:stop]],dtype=object)
		resulting_set.append(np.asarray([trainset,testset],dtype=object))
	return np.asarray(resulting_set,dtype=object)
		



# train_set given by 100k
def loader_100k_1():
	f = open(os.path.dirname(__file__) + '/../../dataset/MovieLens/100k_dataset/u1.base',"r")
	text=f.read().split('\n')
	new_text=np.asarray([np.asarray([np.float(element) for element in row.split("\t")[0:3]]) for row in text[0:-1]])
	return new_text

def loader_100k_2():
	f = open(os.path.dirname(__file__) + '/../../dataset/MovieLens/100k_dataset/u2.base',"r")
	text=f.read().split('\n')
	new_text=np.asarray([np.asarray([np.float(element) for element in row.split("\t")[0:3]]) for row in text[0:-1]])
	return new_text

def loader_100k_3():
	f = open(os.path.dirname(__file__) + '/../../dataset/MovieLens/100k_dataset/u3.base',"r")
	text=f.read().split('\n')
	new_text=np.asarray([np.asarray([np.float(element) for element in row.split("\t")[0:3]]) for row in text[0:-1]])
	return new_text

def loader_100k_4():
	f = open(os.path.dirname(__file__) + '/../../dataset/MovieLens/100k_dataset/u4.base',"r")
	text=f.read().split('\n')
	new_text=np.asarray([np.asarray([np.float(element) for element in row.split("\t")[0:3]]) for row in text[0:-1]])
	return new_text

def loader_100k_5():
	f = open(os.path.dirname(__file__) + '/../../dataset/MovieLens/100k_dataset/u5.base',"r")
	text=f.read().split('\n')
	new_text=np.asarray([np.asarray([np.float(element) for element in row.split("\t")[0:3]]) for row in text[0:-1]])
	return new_text



# test_set given by 100k
def loader_100k_t1(): 
	f = open(os.path.dirname(__file__) + '/../../dataset/MovieLens/100k_dataset/u1.test',"r")
	text=f.read().split('\n')
	new_text=np.asarray([np.asarray([np.float(element) for element in row.split("\t")[0:3]]) for row in text[0:-1]])
	return new_text

def loader_100k_t2():
	f = open(os.path.dirname(__file__) + '/../../dataset/MovieLens/100k_dataset/u2.test',"r")
	text=f.read().split('\n')
	new_text=np.asarray([np.asarray([np.float(element) for element in row.split("\t")[0:3]]) for row in text[0:-1]])
	return new_text

def loader_100k_t3():
	f = open(os.path.dirname(__file__) + '/../../dataset/MovieLens/100k_dataset/u3.test',"r")
	text=f.read().split('\n')
	new_text=np.asarray([np.asarray([np.float(element) for element in row.split("\t")[0:3]]) for row in text[0:-1]])
	return new_text

def loader_100k_t4():
	f = open(os.path.dirname(__file__) + '/../../dataset/MovieLens/100k_dataset/u4.test',"r")
	text=f.read().split('\n')
	new_text=np.asarray([np.asarray([np.float(element) for element in row.split("\t")[0:3]]) for row in text[0:-1]])
	return new_text

def loader_100k_t5(): 
	f = open(os.path.dirname(__file__) + '/../../dataset/MovieLens/100k_dataset/u5.test',"r")
	text=f.read().split('\n')
	new_text=np.asarray([np.asarray([np.float(element) for element in row.split("\t")[0:3]]) for row in text[0:-1]])
	return new_text
