#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int plus = 2;

int triangularnum(int i) {
	return i + plus++;
}

int main() {

	double N;
	int fixednum = 1, i = 1;

	scanf("%lf", &N);

	if (N <= fixednum) {
		printf("%d", fixednum);
	}
	else{
		while (1) {
			if (N <= fixednum + 6 * i) {
				printf("%d", plus);
				break;
			}
			i = triangularnum(i);
		}
	}



	return 0;
}