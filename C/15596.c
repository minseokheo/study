#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

long long sum(int* a, int n) {
	long long ans = 0;

	for (int i = 0; i < n; i++) {
		ans += a[i];
	}
	return ans;
}

int main() {

	int n, ans;
	int a[1000];

	scanf("%d", &n);

	for (int i = 0; i < n; i++) {
		scanf("%d", a[i]);
	}

	ans = sum(a, n);

	return 0;
}