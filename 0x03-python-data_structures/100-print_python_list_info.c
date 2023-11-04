#include <Python.h>
#include <stdio.h>
/**
 * print_python_list_info - prints python list info
 * @p: PyObject
 * Return: No return
*/
void print_python_list_info(PyObject *p)
{
	int size, locate, ndx;
	PyObject *object;

	size = Py_SIZE(p);
	locate = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", locate);
	for (ndx = 0; ndx < size; ndx++)
	{
		object = PyList_GetItem(p, ndx);
		printf("Element %d: %s\n", ndx, Py_TYPE(object)->tp_name);
	}
}
