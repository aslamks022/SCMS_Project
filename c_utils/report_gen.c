#include <stdio.h>
#include <time.h>

void generate_student_report(char name[], char usn[], float gpa) {
    FILE *fp;
    time_t t;
    time(&t);

    fp = fopen("report.txt", "w");
    if(fp == NULL) return;

    fprintf(fp, "============================\n");
    fprintf(fp, "   STUDENT REPORT CARD\n");
    fprintf(fp, "============================\n");
    fprintf(fp, "Date: %s", ctime(&t));
    fprintf(fp, "Name: %s\n", name);
    fprintf(fp, "USN: %s\n", usn);
