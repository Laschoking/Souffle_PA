#include <cstdint>
#include <cfloat>
#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include <iostream>
#include <cstdio>

extern "C" {

float VarSimilarity(const char * str1, const char * str2){
    
    int32_t multiset1[256] = {0}; // Assuming ASCII characters
    int32_t multiset2[256] = {0};
    int32_t len1 = 0;
    // Populate multisets
    int32_t len2 = 0;
    for (int32_t i = 0; str1[i] != '\0'; i++) {
        multiset1[(unsigned char)str1[i]]++;
        len1++;
    }
    // printf("%d", len1);

    for (int32_t i = 0; str2[i] != '\0'; i++) {
        multiset2[(unsigned char)str2[i]]++;
        len2++;
    }
    // printf("%d", len2);

    int32_t commonElements = 0;

    // Calculate the number of common elements
    for (int32_t i = 0; i < 256; i++) {
        int32_t c1 = multiset1[i];
        int32_t c2 = multiset2[i];

        if (c1 > 0 && c2 > 0) {
            //take minimum of both entries
            if (c1 > c2)
                commonElements += c2;
            else commonElements += c1;

        }
    }

    if (commonElements == 0) {
        // Avoid division by zero
        return 0.0;
    }
    float intersectionSize = commonElements;
    float unionSize = strlen(str1) + strlen(str2) ;

    return 2 * intersectionSize / unionSize;
    }

int main(){
    //std::cout << str_to_float1("1.3451L");
    const char* a  = "hello";
    const char* b  = "this#_";
    char result[100];
    sprintf(result, "%f",VarSimilarity(a,b));
    printf("%s", result);
}

}