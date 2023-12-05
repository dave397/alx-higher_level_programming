#include <Python.h>
#include <listobject.h>
#include <object.h>

/**
 * print_python_list_info - Prints information about Python lists
 * @p: pointer to the Python list
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t i = 0;
	Py_ssize_t size = PYList_Size(p);
	Py_ssize_t *store = ((PYListObject *)p)->allocated;

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", store);
	while (i < size)
	{
		printf("Element %i: %s\n", i,
		       Py_TYPE(PyList_GetItem(p, i))->tp_name);
		i += 1;
	}
}
