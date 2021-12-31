#include <stdio.h>
#include <stdlib.h>
#include <string.h>


int main(){
    char *cmd_str = "echo %s";
    char buf[30], cmd[30];
    scanf_s("%30s", buf);
    printf("Input: %s\n", buf);
    
    sprintf(cmd, cmd_str, buf);
    printf("Executing command: \"%s\"\n", cmd);
    system(cmd);
    return 0;
}