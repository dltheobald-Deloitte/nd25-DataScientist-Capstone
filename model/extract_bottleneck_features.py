def extract_VGG16(tensor):
	""" Converts a tensor of an image into the features used in the VGG16 prediction.

	Parameters:
	tensor (np.array): A tensor to describe the contents of an image

	Returns:
	np.array: An array of features generated by the VGG16 model
	"""
	from keras.applications.vgg16 import VGG16, preprocess_input
	return VGG16(weights='imagenet', include_top=False).predict(preprocess_input(tensor))

def extract_VGG19(tensor):
	""" Converts a tensor of an image into the features used in the VGG19 prediction.

	Parameters:
	tensor (np.array): A tensor to describe the contents of an image

	Returns:
	np.array: An array of features generated by the VGG19 model
	"""
	from keras.applications.vgg19 import VGG19, preprocess_input
	return VGG19(weights='imagenet', include_top=False).predict(preprocess_input(tensor))

def extract_Resnet50(tensor):
	""" Converts a tensor of an image into the features used in the ResNet50 prediction.

	Parameters:
	tensor (np.array): A tensor to describe the contents of an image

	Returns:
	np.array: An array of features generated by the ResNet50 model
	"""
	from keras.applications.resnet50 import ResNet50, preprocess_input
	return ResNet50(weights='imagenet', include_top=False).predict(preprocess_input(tensor))

def extract_Xception(tensor):
	""" Converts a tensor of an image into the features used in the Xception prediction.

	Parameters:
	tensor (np.array): A tensor to describe the contents of an image

	Returns:
	np.array: An array of features generated by the Xception model
	"""
	from keras.applications.xception import Xception, preprocess_input
	return Xception(weights='imagenet', include_top=False).predict(preprocess_input(tensor))

def extract_InceptionV3(tensor):
	""" Converts a tensor of an image into the features used in the InceptionV3 prediction.

	Parameters:
	tensor (np.array): A tensor to describe the contents of an image

	Returns:
	np.array: An array of features generated by the InceptionV3 model
	"""
	from keras.applications.inception_v3 import InceptionV3, preprocess_input
	return InceptionV3(weights='imagenet', include_top=False).predict(preprocess_input(tensor))