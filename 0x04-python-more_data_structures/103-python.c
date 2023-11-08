#include <Python.h>
void print_python_bytes(PyObject *p);
/**
 * print_python_list - print python list
 * @p: PyObject list
 * Return: no return
*/
void print_python_list(PyObject *p)
{
	int size, locate, ndx;
	PyVarObject *variable = (PyVarObject *)p;
	PyListObject *list = (PyListObject *)p;
	const char *object;

	size = variable->ob_size;
	locate = list->allocated;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", locate);
	for (ndx = 0; ndx < size; ndx++)
	{
		object = list->ob_item[ndx]->ob_type->tp_name;
		printf("Element %d: %s\n", ndx, object);
		if (strcmp(object, "bytes") == 0)
		{
			print_python_bytes(list->ob_item[ndx]);
		}
	}
}
/**
 * print_python_bytes - print python bytes
 * @p: PyObject byte
 * Return: no return
*/
void print_python_bytes(PyObject *p)
{
	int size, ndx;
	PyBytesObject *bytes = (PyBytesObject *)p;

	printf("[.] bytes object info\n");
	if (strcmp(p->ob_type->tp_name, "bytes") != 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	printf("  size: %ld\n", ((PyVarObject *)p)->ob_size);
	printf("  trying string: %s\n", bytes->ob_sval);
	if (((PyVarObject *)p)->ob_size > 10)
	{
		size = 10;
	}
	else
	{
		size = ((PyVarObject *)p)->ob_size + 1;
	}
	printf("  first %d bytes: ", size);
	for (ndx = 0; ndx < size; ndx++)
	{
		printf("%02hhx", bytes->ob_sval[ndx]);
		if (ndx == (size - 1))
		{
			printf("\n");
		}
		else
		{
			printf(" ");
		}
	}
}
