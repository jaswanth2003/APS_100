#include <stdio.h>

int get_caesar_shift(char* s, char* t) {
    int len = 0, i, shift;
    char *ps = s, *pt = t;

    // Calculate the length of the strings and check if they are equal
    while (*ps && *pt) {
        len++;
        ps++;
        pt++;
    }
    if (*ps || *pt) {
        return -1;
    }
    

    // Calculate the shift required for each letter
    shift = (*t - *s + 'A' - 1) % 26 + 1;
    for (i = 1; i < len; i++) {
        if ((*t - *s + 'A' - 1) % 26 + 1 != shift) {
            return -1;
        }
        s++;
        t++;
    }

    return shift;
}

int main() {
    int q, i;
    char s[101], t[101];

    // Reading input
    scanf("%d", &q);
    for (i = 0; i < q; i++) {
        scanf("%s %s", s, t);
        printf("%d\n", get_caesar_shift(s, t));
    }

    return 0;
}
