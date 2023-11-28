#include <stdio.h>
#include <stdlib.h>
#include <Python.h>
#include <unicodeobject.h>
#include <locale.h>
#include <wchar.h>
/**
 * print_python_string - print python string
 * @p: pyobject struct address
 * Return: no return
*/
void print_python_string(PyObject *p)
{
	wprintf(L"[.] string object info\n");
	if (strcmp(p->ob_type->tp_name, "str"))
	{
		wprintf(L"  [ERROR] Invalid String Object\n");
		return;
	}
	if (PyUnicode_IS_COMPACT_ASCII(p))
	{
		wprintf(L"  type: compact ascii\n");
	}
	else
	{
		wprintf(L"  type: compact unicode object\n");
	}
	wprintf(L"  length: %lu\n", PyUnicode_GET_LENGTH(p));
	wprintf(L"  value: %lu\n", PyUnicode_AS_UNICODE(p));
}
