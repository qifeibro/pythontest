#include <stdio.h>

int main() {
    char str[] = "SoloLearn";
    char *p = &str[1];
    char *q = p + 1;
    printf("%c%c%c\n", *(str + 2), *(p + 3), *(q));
}