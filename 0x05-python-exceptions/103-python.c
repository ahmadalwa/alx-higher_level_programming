#include <Python.h>
#include <stdio.h>

void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);
void print_python_list(PyObject *p);

/**
 * print_python_bytes - dadadasd
 * @p: dadadssad
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t s = 0, i = 0;
	char *string = NULL;

	fflush(stdout);
	printf("%s", "[.] bytes object info\n");
	if (!PyBytes_CheckExact(p))
	{
		printf("%s", "  [ERROR] Invalid Bytes Object\n");
		return;
	}
	s = PyBytes_Size(p);
	printf("  size: %zd\n", s);
	string = (assert(PyBytes_Check(p)), (((PyBytesObject *)(p))->ob_sval));
	printf("  trying string: %s\n", string);
	printf("  first %zd bytes:", s < 10 ? s + 1 : 10);
	while (i < s + 1 && i < 10)
	{
		printf(" %02hhx", string[i]);
		i += 1;
	}
	printf("%s", "\n");
}

/**
 * print_python_float - dadasd
 * @p: adassdasd
 */
void print_python_float(PyObject *p)
{
	double v = 0;
	char *s = NULL;

	fflush(stdout);
	printf("[.] float object info\n");
	if (!PyFloat_CheckExact(p))
	{
		printf("%s", "  [ERROR] Invalid Float Object\n");
		return;
	}
	v = ((PyFloatObject *)p)->ob_fval;
	s = PyOS_double_to_string(v, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);
	printf("  value: %s\n", s);
}


/**
 * print_python_list - dadadad
 * @p: dadasd
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t s = 0;
	PyObject *item;
	int i = 0;

	fflush(stdout);
	printf("%s", "[*] Python list info\n");
	if (PyList_CheckExact(p))
	{
		s = PyList_GET_SIZE(p);
		printf("[*] Size of the Python List = %zd\n", s);
		printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);
		while (s > i)
		{
			item = PyList_GET_ITEM(p, i);
			printf("Element %d: %s\n", i, item->ob_type->tp_name);
			if (PyBytes_Check(item))
			{
				print_python_bytes(item);
			}
			else if (PyFloat_Check(item))
			{
				print_python_float(item);
			}
			i++;
		}
	}
	else
	{
		printf("%s", "  [ERROR] Invalid List Object\n");
	}
}
