#include <stdio.h>
#include <time.h>

void generate_student_report(char name[], char usn[], float gpa) {
    FILE *fp;
    time_t t;
    time(&t);

