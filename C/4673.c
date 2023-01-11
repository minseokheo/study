#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int selfnumber(int i) {
	int snum = 0;

	if (i / 10 == 0) {
		snum = i + i;
	}
	else if (i / 100 == 0) {
		snum = i + (i / 10) + (i % 10);
	}
	else if (i / 1000 == 0) {
		snum = i + (i % 10) + ((i % 100) / 10) + (i / 100);
	}
	else {
		snum = i + (i % 10) + ((i % 100) / 10) + ((i % 1000) / 100) + (i / 1000);

		if (snum >= 10000) {
			snum = 0;
		}
	}

	return snum;
}

int main() {

	int arr[10000], count = 0;

	for (int i = 0; i < 10000; i++) {
		arr[count++] = i;
	}

	count = 0;

	for (int i = 1; i < 10000; i++) {
		arr[selfnumber(i)] = 0;
	}

	for (int i = 1; i < 10000; i++) {
		if (arr[i] != 0) {
			printf("%d\n", arr[i]);
		}
	}


	return 0;
}