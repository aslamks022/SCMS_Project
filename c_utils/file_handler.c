#include <stdio.h>
#include <string.h>

void write_marks(char usn[], float marks[], int n) {
    FILE *fp;
    fp = fopen("marks.txt", "a");
    if(fp == NULL) {
        printf("Error opening file");
        return;
