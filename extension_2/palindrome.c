#include <Python.h>

static PyObject *is_palindrome(PyObject *self,PyObject *args){
  int i,n;
  const char *text;
  int result;
  if (!PyArg_ParseTuple(args,"s",&text)){
    return NULL;
  }
  
  n=strlen(text);
  result=1;
  for(int i=0;i<=n/2;++i){
    if(text[i]!=text[n-i-1]){
      result=0;
      break;
    }
  }
  return Py_BuildValue("i",result);
}  
static PyMethodDef PalindromeMethods[]={
    {"is_palindrome",is_palindrome,METH_VARARGS,"Detect palindromes"},
    {NULL,NULL,0,NULL}
};

PyMODINIT_FUNC initpalindrome(){
  Py_InitModule("palindrome",PalindromeMethods);
}
