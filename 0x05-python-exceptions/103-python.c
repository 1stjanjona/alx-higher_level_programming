#include <Python.h>
#include <floatobject.h>
#include <stdlib.h>
#include <stdio.h>
void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);
/**
 * print_python_list - print python list
 * @p: adrees of PyList
 * Return: no return
*/
void print_python_list(PyObject *p)
{
	int x;

	setbuf(stdout, NULL);
        printf("[*] Python list info\n");
	if (strcmp(p->ob_type->tp_name, "list"))
	{
		printf("  [ERROR] Invalid list Object\n");
		return;
	}
	printf("[*] Size of the Python List = %ld\n", ((PyVarObject *)p)->ob_size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);
	for (x = 0; x < ((PyVarObject *)p)->ob_size; x++)
	{
		printf("Element %d: %s\n", x,
				((PyListObject *)p)->ob_item[x]->ob_type->tp_name);
		if (!strcmp(((PyListObject *)p)->ob_item[x]->ob_type->tp_name, "bytes"))
		{
			print_python_bytes(((PyListObject *)p)->ob_item[x]);
		}
		else if (!strcmp(((PyListObject *)p)->ob_item[x]->ob_type->tp_name, "float"))
		{
			print_python_float(((PyListObject *)p)->ob_item[x]);
		}
	}
}
/**
 * print_python_bytes - print python bytes
 * @p: address of PyBytes
 * Return: no return
*/
void print_python_bytes(PyObject *p)
{
	size_t x, lngth, size;
	char *s;

	setbuf(stdout, NULL);
	printf("[.] bytes Object info\n");
	if (!strcmp(p->ob_type->tp_name, "bytes"))
	{
		printf("   [ERROR] Invalid Bytes Object\n");
		return;
	}
	size = ((PyVarObject *)p)->ob_size;
	s = ((PyBytesObject *)p)->ob_sval;
	lngth = (size_t)size;
	printf("   size: %ld\n", size);
	printf("   trying string: %s\n", s);
	if (lngth < 10)
	{
		printf("   first %ld bytes: ", lngth + 1);
	}
	else
	{
		printf ("   first 10 bytes:");
	}
	for (x = 0; x < lngth && x < 10; x++)
	{
		printf("%02hhx\n", s[x]);
		if ((x + 1) < lngth)
		{
			printf(" ");
		}
	}
	printf("\n");
}
/**
 * print_python_float - print python float
 * @p: address of PyFloatObject
 * Return: no return
*/
void print_python_float(PyObject *p)
{
	double flt;

	setbuf(stdout, NULL);
	printf("[.] float object info\n");
	if (!strcmp(p->ob_type->tp_name, "float"))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}
	flt = ((PyFloatObject *)p)->ob_fval;
	printf("  value: %s\n", PyOS_double_to_string(flt, 'r', 0, Py_DTSF_ADD_DOT_0,
			       	NULL));
}
