def slice_less(my_list, lesser):
	res = list(filter(lambda x: x > lesser, my_list))
	my_list = sorted(res, reverse=True)
	return my_list
