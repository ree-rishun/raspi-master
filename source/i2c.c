// I2C maste test
// g++ i2cMasterTest.cpp -lwiringPi
#include <stdio.h>
#include <errno.h>
#include <string.h>
#include <wiringPi.h>
#include <wiringPiI2C.h>
int main() {

    // 
    if(wiringPiSetup()<0) {  // WiringPi が初期化できなかったらエラー表示して終了
        fprintf(stderr,"Error: can not init wiringPi.\n");
        fprintf(stderr,"errno=%d\n",errno);
        fprintf(stderr,"%s\n",strerror(errno));
        return -1;
    }
    // スレーブ側の I2C アドレスの入力
    int addr;
    printf("input target addr: ");
    scanf("%02x",&addr);  // とりあえず…
    printf("TARGET Addr=0x%02X[=%d]\n",addr,addr);
    // 対象の I2C デバイスへの通信路を開く
    int fd=wiringPiI2CSetup(addr);
    if(fd<0) {
        fprintf(stderr,"ERROR: "  // 長いので 2 行に分けた
                       "Can not start to communicate I2C device %0x02X.\n",addr);
        return -1;
    }
    // 対象のレジスタ（List1 にはそんなものは無いが送信のために必要なので…）の入力
    // ここで入力したバイト値も、次に入力する 16 ビット値の前に送信される。
    int reg;
    printf("input target reg: ");
    scanf("%02x",&reg);
    printf("TARGET Reg=0x%02X[=%d]\n",reg,reg);
    // 送信するデータ
    int data;
    printf("input send data (16bit): ");
    scanf("%04x",&data);
    printf("SEND Data=0x%04X[=%d]\n",data,data);
    // エンディアンの問題で、実際に送信してみると上位バイトと下位バイトが入れ替わるので
    // 送信前に入れ替えておく（0x1234 を送ってみると 0x34 0x12 と受信されてしまうので）。
    //data=(data&0xFF)*0x100+((data>>8)&0xFF);
    // 送信！
    int result=wiringPiI2CWriteReg16(fd,reg,data);
    if(result<0) {
        fprintf(stderr,"Error: can not write to the target.\n");
        fprintf(stderr,"errno=%d\n",errno);
        fprintf(stderr,"%s\n",strerror(errno));
        return -1;
    }
    return 0;
}