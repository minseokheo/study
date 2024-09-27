#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// numbers_len은 배열 numbers의 길이입니다.
int solution(int numbers[], size_t numbers_len) {
    int answer = 0;
    int check[10] = {0, };
    
    for(int i=0; i<numbers_len; i++){
        check[numbers[i]] += 1;
    }
    
    for(int i=0; i<10; i++){
        if(check[i] == 0){
            answer += i;
        }
    }
    
    return answer;
}