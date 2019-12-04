#include <stdio.h>

int is_matched(int number[6]){
    int i;
    for(i=0; i<4; i++){
        if(number[i] == number[i+1] && number[i+1] != number[i+2]){
            if(i != 0){
                if(number[i-1]!=number[i]){
                    //printf("debug1\n");
                    return 1;
                }
            }
            else
                return 1;
        }
        if(number[i] != number[i+1] && i==3 && number[i+1] == number[i+2])
            return 1;
        continue;
    }
    return 0;
}

int main(){
    int i;
    int same_flag = 0;
    int decrease_flag = 0;
    int num[6];
    FILE *fd = fopen("passwd.txt", "w"); //579381 
    for(i=125730; i<579381; i++){
        same_flag = 0;
        decrease_flag = 0;
        num[0] = i/100000;
        num[1] = i/10000 - num[0]*10;
        num[2] = i/1000 - num[0]*100 - num[1]*10;
        num[3] = i/100 - num[0]*1000 - num[1]*100 - num[2]*10;
        num[4] = i/10 - num[0]*10000 - num[1]*1000 - num[2]*100 - num[3]*10;
        num[5] = i%10;
        
        int j;
        for(j = 0; j<5; j++){
            if(num[j]>num[j+1])
                decrease_flag = 1;

        }
        //printf("nums are: %d %d %d %d %d %d \n", num[0], num[1], num[2], num[3], num[4], num[5]);
        same_flag = is_matched(num);

        if(same_flag ==1 && decrease_flag ==0)
            fprintf(fd, "%d\n", i);
    }
    fclose(fd);
    FILE *fp = fopen("passwd.txt", "r");
    int line_cnt = 0;
    char content[31];
    while(!feof(fp)){
        fgets(content, 32, fp);
        line_cnt ++;
    }
    printf("line_cnt = %d\n", line_cnt-1);
    fclose(fp);
    return 0;
}