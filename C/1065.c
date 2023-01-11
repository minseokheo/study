#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main() {

	int N, hund, ten, one, hs = 0;

	scanf("%d", &N);

	for (int i = N; i >= 1; i--) {
		if (i / 10 == 0) {
			hs++;
		}
		else if (i / 100 == 0) {
			hs++;
		}
		else if (i / 1000 == 0) {
			hund = i / 100;
			ten = (i % 100) / 10;
			one = i % 10;

			if (hund - ten == ten - one) {
				hs++;
			}
		}
	}

	printf("%d", hs);

	return 0;
}