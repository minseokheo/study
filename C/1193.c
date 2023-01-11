#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int plus = 1;

int tnum(int i) {
	return i + ++plus;
}

int main() {

	double X;
	int i = 1, son = 1, mother = 1, gap = 0;

	scanf("%lf", &X);

	if (X == 1) {
		printf("%d/%d", son, mother);
	}
	else {
		while (1) {
			i = tnum(i);
			if (X <= i) {
				while (X != i) {
					gap++;
					i--;
				}
			}

			if (X == i) {
				if (plus % 2 == 0) {
					printf("%d/%d", plus - gap, mother + gap);
					break;
				}
				else {
					printf("%d/%d", son + gap, plus - gap);
					break;
				}
			}
		}
	}

	return 0;
}