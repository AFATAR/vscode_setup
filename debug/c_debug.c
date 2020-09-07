#include <stdio.h>
void show() 
{
int value[]={11,33,51,70};
int *p=value;
printf(*(p+3));
}