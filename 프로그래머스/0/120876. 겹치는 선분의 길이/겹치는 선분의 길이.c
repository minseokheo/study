#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// lines_rows는 2차원 배열 lines의 행 길이, lines_cols는 2차원 배열 lines의 열 길이입니다.
int solution(int** lines, size_t lines_rows, size_t lines_cols) {
    int answer = 0;
    int arr[300] = {0, };
    int size = sizeof(arr) / sizeof(arr[0]);
    int a = 0;
    int b = 0;
    for(int i=0; i < 3; i++){
        for(int k=lines[i][0] + 100; k<lines[i][1] + 100; k++){
            arr[k] = arr[k] + 1;
        }
    }
    for(int j=0; j<size; j++){
        if (arr[j] >= 2){
            answer = answer + 1;
        }
    }
    return answer;
}