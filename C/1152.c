#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main() {
	int i = 0;
	char c;
	char before = NULL;
	
	while (c = getchar()) {
		if (c == ' ' && before != NULL && before != ' ') {
			i++;
		}
		else if (c == '\n') {
			if (before == ' ') {
				break;
			}
			else {
				i++;
				break;
			}
		}
		before = c;
	}
	
	printf("%d", i);

	return 0;
}