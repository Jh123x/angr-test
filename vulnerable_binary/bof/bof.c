#include <stdio.h>


int main(){
    char buffer[100];
    printf("Enter a string: ");
    scanf("%s", buffer); // Vulnerable Section.
    printf("You entered: %s\n", buffer);
    return 0;
}