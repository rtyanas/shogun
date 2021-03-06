from tools.load import LoadMatrix
from sg import sg
lm=LoadMatrix()


traindat=lm.load_numbers('../data/fm_train_real.dat')
testdat=lm.load_numbers('../data/fm_test_real.dat')
train_label=lm.load_labels('../data/label_train_multiclass.dat')
parameter_list=[[traindat,testdat, train_label,10,2.1,10.,1e-5,False],
		[traindat,testdat,train_label,10,2.1,11.,1e-4,False]]

def classifier_libsvm_multiclass (fm_train_real=traindat,fm_test_real=testdat,
			label_train_multiclass=train_label,
			size_cache=10, width=2.1,C=10.,
			epsilon=1e-5,use_bias=False):

	sg('set_features', 'TRAIN', fm_train_real)
	sg('set_kernel', 'GAUSSIAN', 'REAL', size_cache, width)

	sg('set_labels', 'TRAIN', label_train_multiclass)
	sg('new_classifier', 'LIBSVM_MULTICLASS')
	sg('svm_epsilon', epsilon)
	sg('c', C)
	sg('svm_use_bias', use_bias)
	sg('train_classifier')

	sg('set_features', 'TEST', fm_test_real)
	result=sg('classify')
	kernel_matrix = sg('get_kernel_matrix', 'TEST')
	return result, kernel_matrix

if __name__=='__main__':
	print('LibSVMMulticlass')
	classifier_libsvm_multiclass(*parameter_list[0])
