#include <ArduinoJson.h>
#include <ArduinoJson.hpp>
//#include "AudioSamplePinkpanther60.h"


JsonDocument doc;
JsonDocument out;

///////////////////////////////////
// copy the Design Tool code here
///////////////////////////////////

#include <Audio.h>
#include <Wire.h>
#include <SPI.h>
#include <SD.h>
#include <SerialFlash.h>

// GUItool: begin automatically generated code
AudioSynthNoiseWhite     noise1;         //xy=205,1728
AudioSynthWaveformSine   sine1;          //xy=207,1608
AudioPlayMemory          playMem1;       //xy=208,1644
AudioAmplifier           channel_8_gain; //xy=585,1842
AudioAmplifier           channel_1_gain; //xy=586,1595
AudioAmplifier           channel_3_gain; //xy=586,1663
AudioAmplifier           channel_6_gain; //xy=586,1770
AudioAmplifier           channel_7_gain; //xy=586,1806
AudioAmplifier           channel_2_gain; //xy=587,1630
AudioAmplifier           channel_4_gain; //xy=587,1698
AudioAmplifier           channel_5_gain; //xy=588,1732
AudioAnalyzeRMS          channel_6_rms;  //xy=670,1234
AudioAnalyzeRMS          channel_4_rms;  //xy=672,1155
AudioAnalyzeRMS          channel_7_rms;  //xy=672,1270
AudioAnalyzeRMS          channel_5_rms;  //xy=675,1193
AudioAnalyzeRMS          channel_8_rms;  //xy=675,1304
AudioAnalyzeRMS          channel_3_rms;  //xy=676,1120
AudioAnalyzeRMS          channel_2_rms;  //xy=677,1083
AudioAnalyzeRMS          channel_1_rms;  //xy=679,1050
AudioFilterBiquad        channel_1_eq;   //xy=749,1601
AudioFilterBiquad        channel_2_eq;   //xy=749,1635
AudioFilterBiquad        channel_3_eq;   //xy=750,1668
AudioFilterBiquad        channel_4_eq;   //xy=751,1701
AudioFilterBiquad        channel_5_eq;   //xy=751,1736
AudioFilterBiquad        channel_6_eq;   //xy=753,1769
AudioFilterBiquad        channel_7_eq;   //xy=754,1804
AudioFilterBiquad        channel_8_eq;   //xy=756,1836
AudioAnalyzePeak         channel_7_peak; //xy=877,1200
AudioAnalyzePeak         channel_6_peak; //xy=879,1164
AudioAnalyzePeak         channel_8_peak; //xy=879,1237
AudioAnalyzePeak         channel_5_peak; //xy=880,1128
AudioAnalyzePeak         channel_4_peak; //xy=882,1093
AudioAnalyzePeak         channel_2_peak; //xy=884,1025
AudioAnalyzePeak         channel_1_peak; //xy=885,992
AudioAnalyzePeak         channel_3_peak; //xy=885,1060
AudioAmplifier           channel_2_dist; //xy=943,1636
AudioAmplifier           channel_6_dist; //xy=943,1771
AudioAmplifier           channel_5_dist; //xy=945,1738
AudioAmplifier           channel_8_dist; //xy=945,1835
AudioAmplifier           channel_4_dist; //xy=946,1703
AudioAmplifier           channel_7_dist; //xy=946,1803
AudioAmplifier           channel_1_dist; //xy=947,1603
AudioAmplifier           channel_3_dist; //xy=947,1669
AudioMixer4              matrix_in_1;    //xy=1236,1140
AudioMixer4              matrix_in_2;    //xy=1237,1205
AudioMixer4              matrix_in_3;    //xy=1237,1287
AudioMixer4              matrix_in_7;    //xy=1236,1594
AudioMixer4              fft_1_r1;       //xy=1239,1010
AudioMixer4              matrix_in_4;    //xy=1238,1352
AudioMixer4              matrix_in_8;    //xy=1237,1659
AudioMixer4              fft_1_r2;       //xy=1240,1073
AudioMixer4              matrix_in_5;    //xy=1239,1439
AudioMixer4              matrix_in_9;    //xy=1239,1749
AudioMixer4              matrix_in_6;    //xy=1240,1504
AudioMixer4              matrix_in_10;   //xy=1240,1814
AudioMixer4              matrix_in_11;   //xy=1240,1918
AudioMixer4              matrix_in_13;   //xy=1240,2063
AudioMixer4              matrix_in_12;   //xy=1241,1983
AudioMixer4              matrix_in_14;   //xy=1241,2128
AudioMixer4              matrix_in_15;   //xy=1242,2218
AudioMixer4              matrix_in_16;   //xy=1243,2283
AudioMixer4              fft_1_r3;       //xy=1392,1051
AudioMixer4              matrix_in_comb_5; //xy=1414,1770
AudioMixer4              matrix_in_comb_3; //xy=1416,1457
AudioMixer4              matrix_in_comb_4; //xy=1416,1613
AudioMixer4              matrix_in_comb_6; //xy=1417,1937
AudioMixer4              matrix_in_comb_2; //xy=1423,1306
AudioMixer4              matrix_in_comb_1; //xy=1430,1159
AudioMixer4              matrix_in_comb_7; //xy=1429,2081
AudioMixer4              matrix_in_comb_8; //xy=1431,2234
AudioAnalyzeFFT1024      fft_1;          //xy=1602,1051
AudioMixer4              matrix_out_15;  //xy=1925,2202
AudioMixer4              matrix_out_16;  //xy=1925,2272
AudioMixer4              matrix_out_3;   //xy=1931,1305
AudioMixer4              matrix_out_4;   //xy=1931,1375
AudioMixer4              matrix_out_1;   //xy=1939,1161
AudioMixer4              matrix_out_5;   //xy=1938,1454
AudioMixer4              matrix_out_2;   //xy=1939,1231
AudioMixer4              matrix_out_6;   //xy=1938,1524
AudioMixer4              matrix_out_7;   //xy=1938,1614
AudioMixer4              matrix_out_8;   //xy=1938,1684
AudioMixer4              matrix_out_13;  //xy=1941,2054
AudioMixer4              matrix_out_14;  //xy=1941,2124
AudioMixer4              matrix_out_9;   //xy=1943,1757
AudioMixer4              matrix_out_10;  //xy=1943,1827
AudioMixer4              matrix_out_11;  //xy=1948,1905
AudioMixer4              matrix_out_12;  //xy=1948,1975
AudioMixer4              matrix_out_comb_2; //xy=2125,1325
AudioMixer4              matrix_out_comb_1; //xy=2130,1189
AudioMixer4              matrix_out_comb_8; //xy=2127,2223
AudioMixer4              matrix_out_comb_4; //xy=2136,1640
AudioMixer4              matrix_out_comb_3; //xy=2137,1477
AudioMixer4              matrix_out_comb_7; //xy=2136,2077
AudioMixer4              matrix_out_comb_5; //xy=2140,1780
AudioMixer4              matrix_out_comb_6; //xy=2151,1926
AudioAmplifier           output_2_gain;  //xy=2291,1328
AudioAmplifier           output_4_gain;  //xy=2292,1638
AudioAmplifier           output_8_gain;  //xy=2290,2223
AudioAmplifier           output_1_gain;  //xy=2296,1184
AudioAmplifier           output_3_gain;  //xy=2297,1477
AudioAmplifier           output_5_gain;  //xy=2299,1780
AudioAmplifier           output_7_gain;  //xy=2301,2077
AudioAmplifier           output_6_gain;  //xy=2311,1925
AudioFilterBiquad        output_1_eq;    //xy=2419,1183
AudioFilterBiquad        output_2_eq;    //xy=2420,1328
AudioFilterBiquad        output_4_eq;    //xy=2421,1639
AudioFilterBiquad        output_3_eq;    //xy=2422,1475
AudioFilterBiquad        output_5_eq;    //xy=2421,1780
AudioFilterBiquad        output_8_eq;    //xy=2424,2222
AudioFilterBiquad        output_7_eq;    //xy=2426,2077
AudioFilterBiquad        output_6_eq;    //xy=2435,1925
AudioAnalyzePeak         output_1_peak;  //xy=2500,517
AudioAnalyzePeak         output_6_peak;  //xy=2504,695
AudioAnalyzePeak         output_2_peak;  //xy=2507,550
AudioAnalyzePeak         output_4_peak;  //xy=2507,621
AudioAnalyzePeak         output_5_peak;  //xy=2507,660
AudioAnalyzePeak         output_7_peak;  //xy=2507,735
AudioAnalyzePeak         output_8_peak;  //xy=2507,777
AudioAnalyzePeak         output_3_peak;  //xy=2509,583
AudioAmplifier           output_2_dist;  //xy=2619,1329
AudioAmplifier           output_4_dist;  //xy=2622,1643
AudioAmplifier           output_1_dist;  //xy=2624,1185
AudioAmplifier           output_3_dist;  //xy=2625,1477
AudioAmplifier           output_5_dist;  //xy=2626,1781
AudioAmplifier           output_7_dist;  //xy=2630,2082
AudioAmplifier           output_8_dist;  //xy=2631,2229
AudioAmplifier           output_6_dist;  //xy=2639,1926
AudioAnalyzeRMS          output_1_rms;   //xy=2727,522
AudioAnalyzeRMS          output_2_rms;   //xy=2728,558
AudioAnalyzeRMS          output_3_rms;   //xy=2730,591
AudioAnalyzeRMS          output_4_rms;   //xy=2735,631
AudioMixer4              fft_2_r1;       //xy=2739,975
AudioMixer4              fft_2_r2;       //xy=2740,1038
AudioAnalyzeRMS          output_6_rms;   //xy=2742,698
AudioAnalyzeRMS          output_5_rms;   //xy=2745,665
AudioAnalyzeRMS          output_7_rms;   //xy=2747,733
AudioAnalyzeRMS          output_8_rms;   //xy=2753,771
AudioMixer4              fft_2_r3;       //xy=2952,1003
AudioOutputMQS           mqs1;           //xy=3135,1488
AudioAnalyzeFFT1024      fft_2;          //xy=3142,1003
AudioOutputTDM           tdm_out;        //xy=3141,1633
AudioConnection          patchCord1(noise1, channel_3_gain);
AudioConnection          patchCord2(noise1, channel_4_gain);
AudioConnection          patchCord3(noise1, channel_5_gain);
AudioConnection          patchCord4(noise1, channel_6_gain);
AudioConnection          patchCord5(noise1, channel_7_gain);
AudioConnection          patchCord6(noise1, channel_8_gain);
AudioConnection          patchCord7(sine1, channel_1_gain);
AudioConnection          patchCord8(playMem1, channel_2_gain);
AudioConnection          patchCord9(channel_8_gain, channel_8_eq);
AudioConnection          patchCord10(channel_1_gain, channel_1_eq);
AudioConnection          patchCord11(channel_3_gain, channel_3_eq);
AudioConnection          patchCord12(channel_6_gain, channel_6_eq);
AudioConnection          patchCord13(channel_7_gain, channel_7_eq);
AudioConnection          patchCord14(channel_2_gain, channel_2_eq);
AudioConnection          patchCord15(channel_4_gain, channel_4_eq);
AudioConnection          patchCord16(channel_5_gain, channel_5_eq);
AudioConnection          patchCord17(channel_1_eq, channel_1_dist);
AudioConnection          patchCord18(channel_1_eq, 0, fft_1_r1, 0);
AudioConnection          patchCord19(channel_1_eq, channel_1_peak);
AudioConnection          patchCord20(channel_1_eq, channel_1_rms);
AudioConnection          patchCord21(channel_2_eq, channel_2_dist);
AudioConnection          patchCord22(channel_2_eq, 0, fft_1_r1, 1);
AudioConnection          patchCord23(channel_2_eq, channel_2_peak);
AudioConnection          patchCord24(channel_2_eq, channel_2_rms);
AudioConnection          patchCord25(channel_3_eq, channel_3_dist);
AudioConnection          patchCord26(channel_3_eq, 0, fft_1_r1, 2);
AudioConnection          patchCord27(channel_3_eq, channel_3_peak);
AudioConnection          patchCord28(channel_3_eq, channel_3_rms);
AudioConnection          patchCord29(channel_4_eq, channel_4_dist);
AudioConnection          patchCord30(channel_4_eq, 0, fft_1_r1, 3);
AudioConnection          patchCord31(channel_4_eq, channel_4_peak);
AudioConnection          patchCord32(channel_4_eq, channel_4_rms);
AudioConnection          patchCord33(channel_5_eq, channel_5_dist);
AudioConnection          patchCord34(channel_5_eq, 0, fft_1_r2, 0);
AudioConnection          patchCord35(channel_5_eq, channel_5_peak);
AudioConnection          patchCord36(channel_5_eq, channel_5_rms);
AudioConnection          patchCord37(channel_6_eq, channel_6_dist);
AudioConnection          patchCord38(channel_6_eq, 0, fft_1_r2, 1);
AudioConnection          patchCord39(channel_6_eq, channel_6_peak);
AudioConnection          patchCord40(channel_6_eq, channel_6_rms);
AudioConnection          patchCord41(channel_7_eq, channel_7_dist);
AudioConnection          patchCord42(channel_7_eq, 0, fft_1_r2, 2);
AudioConnection          patchCord43(channel_7_eq, channel_7_peak);
AudioConnection          patchCord44(channel_7_eq, channel_7_rms);
AudioConnection          patchCord45(channel_8_eq, channel_8_dist);
AudioConnection          patchCord46(channel_8_eq, 0, fft_1_r2, 3);
AudioConnection          patchCord47(channel_8_eq, channel_8_peak);
AudioConnection          patchCord48(channel_8_eq, channel_8_rms);
AudioConnection          patchCord49(channel_2_dist, 0, matrix_in_1, 1);
AudioConnection          patchCord50(channel_2_dist, 0, matrix_in_3, 1);
AudioConnection          patchCord51(channel_2_dist, 0, matrix_in_5, 1);
AudioConnection          patchCord52(channel_2_dist, 0, matrix_in_7, 1);
AudioConnection          patchCord53(channel_2_dist, 0, matrix_in_9, 1);
AudioConnection          patchCord54(channel_2_dist, 0, matrix_in_11, 1);
AudioConnection          patchCord55(channel_2_dist, 0, matrix_in_13, 1);
AudioConnection          patchCord56(channel_2_dist, 0, matrix_in_15, 1);
AudioConnection          patchCord57(channel_6_dist, 0, matrix_in_2, 1);
AudioConnection          patchCord58(channel_6_dist, 0, matrix_in_4, 1);
AudioConnection          patchCord59(channel_6_dist, 0, matrix_in_6, 1);
AudioConnection          patchCord60(channel_6_dist, 0, matrix_in_8, 1);
AudioConnection          patchCord61(channel_6_dist, 0, matrix_in_10, 1);
AudioConnection          patchCord62(channel_6_dist, 0, matrix_in_12, 1);
AudioConnection          patchCord63(channel_6_dist, 0, matrix_in_14, 1);
AudioConnection          patchCord64(channel_6_dist, 0, matrix_in_16, 1);
AudioConnection          patchCord65(channel_5_dist, 0, matrix_in_2, 0);
AudioConnection          patchCord66(channel_5_dist, 0, matrix_in_4, 0);
AudioConnection          patchCord67(channel_5_dist, 0, matrix_in_6, 0);
AudioConnection          patchCord68(channel_5_dist, 0, matrix_in_8, 0);
AudioConnection          patchCord69(channel_5_dist, 0, matrix_in_10, 0);
AudioConnection          patchCord70(channel_5_dist, 0, matrix_in_12, 0);
AudioConnection          patchCord71(channel_5_dist, 0, matrix_in_14, 0);
AudioConnection          patchCord72(channel_5_dist, 0, matrix_in_16, 0);
AudioConnection          patchCord73(channel_8_dist, 0, matrix_in_2, 3);
AudioConnection          patchCord74(channel_8_dist, 0, matrix_in_4, 3);
AudioConnection          patchCord75(channel_8_dist, 0, matrix_in_6, 3);
AudioConnection          patchCord76(channel_8_dist, 0, matrix_in_10, 3);
AudioConnection          patchCord77(channel_8_dist, 0, matrix_in_12, 3);
AudioConnection          patchCord78(channel_8_dist, 0, matrix_in_14, 3);
AudioConnection          patchCord79(channel_8_dist, 0, matrix_in_16, 3);
AudioConnection          patchCord80(channel_4_dist, 0, matrix_in_1, 3);
AudioConnection          patchCord81(channel_4_dist, 0, matrix_in_3, 3);
AudioConnection          patchCord82(channel_4_dist, 0, matrix_in_5, 3);
AudioConnection          patchCord83(channel_4_dist, 0, matrix_in_7, 3);
AudioConnection          patchCord84(channel_4_dist, 0, matrix_in_9, 3);
AudioConnection          patchCord85(channel_4_dist, 0, matrix_in_11, 3);
AudioConnection          patchCord86(channel_4_dist, 0, matrix_in_13, 3);
AudioConnection          patchCord87(channel_4_dist, 0, matrix_in_15, 3);
AudioConnection          patchCord88(channel_7_dist, 0, matrix_in_16, 2);
AudioConnection          patchCord89(channel_7_dist, 0, matrix_in_14, 2);
AudioConnection          patchCord90(channel_7_dist, 0, matrix_in_10, 2);
AudioConnection          patchCord91(channel_7_dist, 0, matrix_in_8, 2);
AudioConnection          patchCord92(channel_7_dist, 0, matrix_in_6, 2);
AudioConnection          patchCord93(channel_7_dist, 0, matrix_in_4, 2);
AudioConnection          patchCord94(channel_7_dist, 0, matrix_in_2, 2);
AudioConnection          patchCord95(channel_7_dist, 0, matrix_in_12, 2);
AudioConnection          patchCord96(channel_1_dist, 0, matrix_in_1, 0);
AudioConnection          patchCord97(channel_1_dist, 0, matrix_in_3, 0);
AudioConnection          patchCord98(channel_1_dist, 0, matrix_in_5, 0);
AudioConnection          patchCord99(channel_1_dist, 0, matrix_in_7, 0);
AudioConnection          patchCord100(channel_1_dist, 0, matrix_in_9, 0);
AudioConnection          patchCord101(channel_1_dist, 0, matrix_in_11, 0);
AudioConnection          patchCord102(channel_1_dist, 0, matrix_in_13, 0);
AudioConnection          patchCord103(channel_1_dist, 0, matrix_in_15, 0);
AudioConnection          patchCord104(channel_3_dist, 0, matrix_in_15, 2);
AudioConnection          patchCord105(channel_3_dist, 0, matrix_in_13, 2);
AudioConnection          patchCord106(channel_3_dist, 0, matrix_in_9, 2);
AudioConnection          patchCord107(channel_3_dist, 0, matrix_in_7, 2);
AudioConnection          patchCord108(channel_3_dist, 0, matrix_in_5, 2);
AudioConnection          patchCord109(channel_3_dist, 0, matrix_in_3, 2);
AudioConnection          patchCord110(channel_3_dist, 0, matrix_in_1, 2);
AudioConnection          patchCord111(channel_3_dist, 0, matrix_in_11, 2);
AudioConnection          patchCord112(matrix_in_1, 0, matrix_in_comb_1, 0);
AudioConnection          patchCord113(matrix_in_2, 0, matrix_in_comb_1, 1);
AudioConnection          patchCord114(matrix_in_3, 0, matrix_in_comb_2, 0);
AudioConnection          patchCord115(matrix_in_7, 0, matrix_in_comb_4, 0);
AudioConnection          patchCord116(fft_1_r1, 0, fft_1_r3, 0);
AudioConnection          patchCord117(matrix_in_4, 0, matrix_in_comb_2, 1);
AudioConnection          patchCord118(matrix_in_8, 0, matrix_in_comb_4, 1);
AudioConnection          patchCord119(fft_1_r2, 0, fft_1_r3, 1);
AudioConnection          patchCord120(matrix_in_5, 0, matrix_in_comb_3, 0);
AudioConnection          patchCord121(matrix_in_9, 0, matrix_in_comb_5, 0);
AudioConnection          patchCord122(matrix_in_6, 0, matrix_in_comb_3, 1);
AudioConnection          patchCord123(matrix_in_10, 0, matrix_in_comb_5, 1);
AudioConnection          patchCord124(matrix_in_11, 0, matrix_in_comb_6, 0);
AudioConnection          patchCord125(matrix_in_13, 0, matrix_in_comb_7, 0);
AudioConnection          patchCord126(matrix_in_12, 0, matrix_in_comb_6, 1);
AudioConnection          patchCord127(matrix_in_14, 0, matrix_in_comb_7, 1);
AudioConnection          patchCord128(matrix_in_15, 0, matrix_in_comb_8, 0);
AudioConnection          patchCord129(matrix_in_16, 0, matrix_in_comb_8, 1);
AudioConnection          patchCord130(fft_1_r3, fft_1);
AudioConnection          patchCord131(matrix_in_comb_5, 0, matrix_out_2, 0);
AudioConnection          patchCord132(matrix_in_comb_5, 0, matrix_out_4, 0);
AudioConnection          patchCord133(matrix_in_comb_5, 0, matrix_out_6, 0);
AudioConnection          patchCord134(matrix_in_comb_5, 0, matrix_out_8, 0);
AudioConnection          patchCord135(matrix_in_comb_5, 0, matrix_out_10, 0);
AudioConnection          patchCord136(matrix_in_comb_5, 0, matrix_out_12, 0);
AudioConnection          patchCord137(matrix_in_comb_5, 0, matrix_out_14, 0);
AudioConnection          patchCord138(matrix_in_comb_5, 0, matrix_out_16, 0);
AudioConnection          patchCord139(matrix_in_comb_3, 0, matrix_out_1, 2);
AudioConnection          patchCord140(matrix_in_comb_3, 0, matrix_out_3, 2);
AudioConnection          patchCord141(matrix_in_comb_3, 0, matrix_out_5, 2);
AudioConnection          patchCord142(matrix_in_comb_3, 0, matrix_out_7, 2);
AudioConnection          patchCord143(matrix_in_comb_3, 0, matrix_out_9, 2);
AudioConnection          patchCord144(matrix_in_comb_3, 0, matrix_out_11, 2);
AudioConnection          patchCord145(matrix_in_comb_3, 0, matrix_out_13, 2);
AudioConnection          patchCord146(matrix_in_comb_3, 0, matrix_out_15, 2);
AudioConnection          patchCord147(matrix_in_comb_4, 0, matrix_out_1, 3);
AudioConnection          patchCord148(matrix_in_comb_4, 0, matrix_out_3, 3);
AudioConnection          patchCord149(matrix_in_comb_4, 0, matrix_out_5, 3);
AudioConnection          patchCord150(matrix_in_comb_4, 0, matrix_out_7, 3);
AudioConnection          patchCord151(matrix_in_comb_4, 0, matrix_out_9, 3);
AudioConnection          patchCord152(matrix_in_comb_4, 0, matrix_out_11, 3);
AudioConnection          patchCord153(matrix_in_comb_4, 0, matrix_out_13, 3);
AudioConnection          patchCord154(matrix_in_comb_4, 0, matrix_out_15, 3);
AudioConnection          patchCord155(matrix_in_comb_6, 0, matrix_out_2, 1);
AudioConnection          patchCord156(matrix_in_comb_6, 0, matrix_out_4, 1);
AudioConnection          patchCord157(matrix_in_comb_6, 0, matrix_out_6, 1);
AudioConnection          patchCord158(matrix_in_comb_6, 0, matrix_out_8, 1);
AudioConnection          patchCord159(matrix_in_comb_6, 0, matrix_out_10, 1);
AudioConnection          patchCord160(matrix_in_comb_6, 0, matrix_out_12, 1);
AudioConnection          patchCord161(matrix_in_comb_6, 0, matrix_out_14, 1);
AudioConnection          patchCord162(matrix_in_comb_6, 0, matrix_out_16, 1);
AudioConnection          patchCord163(matrix_in_comb_2, 0, matrix_out_1, 1);
AudioConnection          patchCord164(matrix_in_comb_2, 0, matrix_out_3, 1);
AudioConnection          patchCord165(matrix_in_comb_2, 0, matrix_out_5, 1);
AudioConnection          patchCord166(matrix_in_comb_2, 0, matrix_out_7, 1);
AudioConnection          patchCord167(matrix_in_comb_2, 0, matrix_out_9, 1);
AudioConnection          patchCord168(matrix_in_comb_2, 0, matrix_out_11, 1);
AudioConnection          patchCord169(matrix_in_comb_2, 0, matrix_out_13, 1);
AudioConnection          patchCord170(matrix_in_comb_2, 0, matrix_out_15, 1);
AudioConnection          patchCord171(matrix_in_comb_1, 0, matrix_out_1, 0);
AudioConnection          patchCord172(matrix_in_comb_1, 0, matrix_out_3, 0);
AudioConnection          patchCord173(matrix_in_comb_1, 0, matrix_out_5, 0);
AudioConnection          patchCord174(matrix_in_comb_1, 0, matrix_out_7, 0);
AudioConnection          patchCord175(matrix_in_comb_1, 0, matrix_out_9, 0);
AudioConnection          patchCord176(matrix_in_comb_1, 0, matrix_out_11, 0);
AudioConnection          patchCord177(matrix_in_comb_1, 0, matrix_out_13, 0);
AudioConnection          patchCord178(matrix_in_comb_1, 0, matrix_out_15, 0);
AudioConnection          patchCord179(matrix_in_comb_7, 0, matrix_out_2, 2);
AudioConnection          patchCord180(matrix_in_comb_7, 0, matrix_out_4, 2);
AudioConnection          patchCord181(matrix_in_comb_7, 0, matrix_out_6, 2);
AudioConnection          patchCord182(matrix_in_comb_7, 0, matrix_out_8, 2);
AudioConnection          patchCord183(matrix_in_comb_7, 0, matrix_out_10, 2);
AudioConnection          patchCord184(matrix_in_comb_7, 0, matrix_out_12, 2);
AudioConnection          patchCord185(matrix_in_comb_7, 0, matrix_out_14, 2);
AudioConnection          patchCord186(matrix_in_comb_7, 0, matrix_out_16, 2);
AudioConnection          patchCord187(matrix_in_comb_8, 0, matrix_out_2, 3);
AudioConnection          patchCord188(matrix_in_comb_8, 0, matrix_out_4, 3);
AudioConnection          patchCord189(matrix_in_comb_8, 0, matrix_out_6, 3);
AudioConnection          patchCord190(matrix_in_comb_8, 0, matrix_out_8, 3);
AudioConnection          patchCord191(matrix_in_comb_8, 0, matrix_out_10, 3);
AudioConnection          patchCord192(matrix_in_comb_8, 0, matrix_out_12, 3);
AudioConnection          patchCord193(matrix_in_comb_8, 0, matrix_out_14, 3);
AudioConnection          patchCord194(matrix_in_comb_8, 0, matrix_out_16, 3);
AudioConnection          patchCord195(matrix_out_15, 0, matrix_out_comb_8, 0);
AudioConnection          patchCord196(matrix_out_16, 0, matrix_out_comb_8, 1);
AudioConnection          patchCord197(matrix_out_3, 0, matrix_out_comb_2, 0);
AudioConnection          patchCord198(matrix_out_4, 0, matrix_out_comb_2, 1);
AudioConnection          patchCord199(matrix_out_1, 0, matrix_out_comb_1, 0);
AudioConnection          patchCord200(matrix_out_5, 0, matrix_out_comb_3, 0);
AudioConnection          patchCord201(matrix_out_2, 0, matrix_out_comb_1, 1);
AudioConnection          patchCord202(matrix_out_6, 0, matrix_out_comb_3, 1);
AudioConnection          patchCord203(matrix_out_7, 0, matrix_out_comb_4, 0);
AudioConnection          patchCord204(matrix_out_8, 0, matrix_out_comb_4, 1);
AudioConnection          patchCord205(matrix_out_13, 0, matrix_out_comb_7, 0);
AudioConnection          patchCord206(matrix_out_14, 0, matrix_out_comb_7, 1);
AudioConnection          patchCord207(matrix_out_9, 0, matrix_out_comb_5, 0);
AudioConnection          patchCord208(matrix_out_10, 0, matrix_out_comb_5, 1);
AudioConnection          patchCord209(matrix_out_11, 0, matrix_out_comb_6, 0);
AudioConnection          patchCord210(matrix_out_12, 0, matrix_out_comb_6, 1);
AudioConnection          patchCord211(matrix_out_comb_2, output_2_gain);
AudioConnection          patchCord212(matrix_out_comb_1, output_1_gain);
AudioConnection          patchCord213(matrix_out_comb_8, output_8_gain);
AudioConnection          patchCord214(matrix_out_comb_4, output_4_gain);
AudioConnection          patchCord215(matrix_out_comb_3, output_3_gain);
AudioConnection          patchCord216(matrix_out_comb_7, output_7_gain);
AudioConnection          patchCord217(matrix_out_comb_5, output_5_gain);
AudioConnection          patchCord218(matrix_out_comb_6, output_6_gain);
AudioConnection          patchCord219(output_2_gain, output_2_eq);
AudioConnection          patchCord220(output_4_gain, output_4_eq);
AudioConnection          patchCord221(output_8_gain, output_8_eq);
AudioConnection          patchCord222(output_1_gain, output_1_eq);
AudioConnection          patchCord223(output_3_gain, output_3_eq);
AudioConnection          patchCord224(output_5_gain, output_5_eq);
AudioConnection          patchCord225(output_7_gain, output_7_eq);
AudioConnection          patchCord226(output_6_gain, output_6_eq);
AudioConnection          patchCord227(output_1_eq, output_1_dist);
AudioConnection          patchCord228(output_1_eq, 0, fft_2_r1, 0);
AudioConnection          patchCord229(output_1_eq, output_1_rms);
AudioConnection          patchCord230(output_1_eq, output_1_peak);
AudioConnection          patchCord231(output_2_eq, output_2_dist);
AudioConnection          patchCord232(output_2_eq, 0, fft_2_r1, 1);
AudioConnection          patchCord233(output_2_eq, output_2_rms);
AudioConnection          patchCord234(output_2_eq, output_2_peak);
AudioConnection          patchCord235(output_4_eq, output_4_dist);
AudioConnection          patchCord236(output_4_eq, 0, fft_2_r1, 3);
AudioConnection          patchCord237(output_4_eq, output_4_rms);
AudioConnection          patchCord238(output_4_eq, output_4_peak);
AudioConnection          patchCord239(output_3_eq, output_3_dist);
AudioConnection          patchCord240(output_3_eq, 0, fft_2_r1, 2);
AudioConnection          patchCord241(output_3_eq, output_3_rms);
AudioConnection          patchCord242(output_3_eq, output_3_peak);
AudioConnection          patchCord243(output_5_eq, output_5_dist);
AudioConnection          patchCord244(output_5_eq, 0, fft_2_r2, 0);
AudioConnection          patchCord245(output_5_eq, output_5_rms);
AudioConnection          patchCord246(output_5_eq, output_5_peak);
AudioConnection          patchCord247(output_8_eq, output_8_dist);
AudioConnection          patchCord248(output_8_eq, 0, fft_2_r2, 3);
AudioConnection          patchCord249(output_8_eq, output_8_rms);
AudioConnection          patchCord250(output_8_eq, output_8_peak);
AudioConnection          patchCord251(output_7_eq, output_7_dist);
AudioConnection          patchCord252(output_7_eq, 0, fft_2_r2, 2);
AudioConnection          patchCord253(output_7_eq, output_7_rms);
AudioConnection          patchCord254(output_7_eq, output_7_peak);
AudioConnection          patchCord255(output_6_eq, output_6_dist);
AudioConnection          patchCord256(output_6_eq, 0, fft_2_r2, 1);
AudioConnection          patchCord257(output_6_eq, output_6_rms);
AudioConnection          patchCord258(output_6_eq, output_6_peak);
AudioConnection          patchCord259(output_2_dist, 0, mqs1, 1);
AudioConnection          patchCord260(output_4_dist, 0, tdm_out, 6);
AudioConnection          patchCord261(output_1_dist, 0, mqs1, 0);
AudioConnection          patchCord262(output_3_dist, 0, tdm_out, 4);
AudioConnection          patchCord263(output_5_dist, 0, tdm_out, 8);
AudioConnection          patchCord264(output_7_dist, 0, tdm_out, 12);
AudioConnection          patchCord265(output_8_dist, 0, tdm_out, 14);
AudioConnection          patchCord266(output_6_dist, 0, tdm_out, 10);
AudioConnection          patchCord267(fft_2_r1, 0, fft_2_r3, 0);
AudioConnection          patchCord268(fft_2_r2, 0, fft_2_r3, 1);
AudioConnection          patchCord269(fft_2_r3, fft_2);
AudioControlCS42448      cs42448_1;      //xy=315,1385
// GUItool: end automatically generated code





#define SDCARD_CS_PIN    BUILTIN_SDCARD
#define SDCARD_MOSI_PIN  11  // not actually used
#define SDCARD_SCK_PIN   13  // not actually used

int inputChannels = 8;
int outputChannels = 8;


AudioMixer4* matrixIns[] = { &matrix_in_1, &matrix_in_2, &matrix_in_3, &matrix_in_4, &matrix_in_5, &matrix_in_6, &matrix_in_7, &matrix_in_8, &matrix_in_9, &matrix_in_10, &matrix_in_11, &matrix_in_12, &matrix_in_13, &matrix_in_14, &matrix_in_15, &matrix_in_16 };

AudioMixer4* matrixOuts[] = { &matrix_out_1, &matrix_out_2, &matrix_out_3, &matrix_out_4, &matrix_out_5, &matrix_out_6, &matrix_out_7, &matrix_out_8, &matrix_out_9, &matrix_out_10, &matrix_out_11, &matrix_out_12, &matrix_out_13, &matrix_out_14, &matrix_out_15, &matrix_out_16 };


const double sampleRate = 44100.0;



double amplitudeToDB(double amplitude) {
    return 20 * log10(amplitude);
}


double* calculatePeakingEQCoefficients(double centerFreq, double Q, double gain, double sampleRate) {
  static double coefficients[5];  // Static array to return

  // Convert gain from dB to linear
  double A = pow(10, gain / 40);

  // Calculate normalized angular frequency
  double omega = 2 * PI * centerFreq / sampleRate;

  // Calculate alpha (bandwidth factor)
  double alpha = sin(omega) / (2 * Q);

  // Calculate raw coefficients
  double b0 = 1 + alpha * A;
  double b1 = -2 * cos(omega);
  double b2 = 1 - alpha * A;
  double a0 = 1 + alpha / A;
  double a1 = -2 * cos(omega);
  double a2 = 1 - alpha / A;

  // Normalize coefficients by a0
  coefficients[0] = b0 / a0;  // b0
  coefficients[1] = b1 / a0;  // b1
  coefficients[2] = b2 / a0;  // b2
  coefficients[3] = a1 / a0;  // a1
  coefficients[4] = a2 / a0;  // a2

  return coefficients;
}


double* band_1_coff = calculatePeakingEQCoefficients(400, 1, 0, sampleRate);
double* band_2_coff = calculatePeakingEQCoefficients(1000, 1, 0, sampleRate);
double* band_3_coff = calculatePeakingEQCoefficients(5000, 1, 0, sampleRate);
double* band_4_coff = calculatePeakingEQCoefficients(10000, 1, 0, sampleRate);


void routeMatrix(int inChannel, int outChannel, float gainIn, float gainOut) {
int nO;
if (inChannel == 1)
{
  matrix_in_1.gain(0, gainIn);
  nO = 0;
}
if (inChannel == 2)
{
  matrix_in_2.gain(0, gainIn);
  nO = 0;
}
if (inChannel == 3)
{
  matrix_in_3.gain(0, gainIn);
  nO = 0;
}
if (inChannel == 4)
{
  matrix_in_4.gain(0, gainIn);
  nO = 0;
}
if (inChannel == 5)
{
  matrix_in_5.gain(0, gainIn);
  nO = 1;
}
if (inChannel == 6)
{
  matrix_in_6.gain(0, gainIn);
  nO = 1;
}
if (inChannel == 7)
{
  matrix_in_7.gain(0, gainIn);
  nO = 1;
}
if (inChannel == 8)
{
  matrix_in_8.gain(0, gainIn);
  nO = 1;
}



if (outChannel == 1)
{
  if (nO < 5) {
  matrix_out_1.gain(inChannel-1, gainOut);
  }
  else
  {
  matrix_out_1.gain(inChannel-5, gainOut);
  }
}
if (outChannel == 2)
{
  if (nO < 5) {
  matrix_out_2.gain(inChannel-1, gainOut);
  }
  else
  {
  matrix_out_2.gain(inChannel-5, gainOut);
  }
}
if (outChannel == 3)
{
  if (nO < 5) {
  matrix_out_3.gain(inChannel-1, gainOut);
  }
  else
  {
  matrix_out_3.gain(inChannel-5, gainOut);
  }
}
if (outChannel == 4)
{
  if (nO < 5) {
  matrix_out_4.gain(inChannel-1, gainOut);
  }
  else
  {
  matrix_out_4.gain(inChannel-5, gainOut);
  }
}
if (outChannel == 5)
{
  if (nO < 5) {
  matrix_out_5.gain(inChannel-1, gainOut);
  }
  else
  {
  matrix_out_5.gain(inChannel-5, gainOut);
  }
}
if (outChannel == 6)
{
  if (nO < 5) {
  matrix_out_6.gain(inChannel-1, gainOut);
  }
  else
  {
  matrix_out_6.gain(inChannel-5, gainOut);
  }
}
if (outChannel == 7)
{
  if (nO < 5) {
  matrix_out_7.gain(inChannel-1, gainOut);
  }
  else
  {
  matrix_out_7.gain(inChannel-5, gainOut);
  }
}
if (outChannel == 8)
{
  if (nO < 5) {
  matrix_out_8.gain(inChannel-1, gainOut);
  }
  else
  {
  matrix_out_8.gain(inChannel-5, gainOut);
  }
}

}



void initMatrix() {

  // Loop through the array to initialize or configure the mixers
  for (int i = 0; i < 16; i++) {
    for (int j = 0; j < 4; j++) { // Mixers have 4 inputs
      matrixIns[i]->gain(j, 0); // Set the gain for each input
    }
  }
  
  for (int i = 0; i < 16; i++) {
    for (int j = 0; j < 4; j++) { // Mixers have 4 inputs
      matrixOuts[i]->gain(j, 0); // Set the gain for each input
    }
  }



  matrix_in_comb_1.gain(0, 1);
  matrix_in_comb_1.gain(1, 1);

  matrix_in_comb_2.gain(0, 1);
  matrix_in_comb_2.gain(1, 1);

  matrix_in_comb_3.gain(0, 1);
  matrix_in_comb_3.gain(1, 1);

  matrix_in_comb_4.gain(0, 1);
  matrix_in_comb_4.gain(1, 1);

  matrix_in_comb_5.gain(0, 1);
  matrix_in_comb_5.gain(1, 1);

  matrix_in_comb_6.gain(0, 1);
  matrix_in_comb_6.gain(1, 1);

  matrix_in_comb_7.gain(0, 1);
  matrix_in_comb_7.gain(1, 1);

  matrix_in_comb_8.gain(0, 1);
  matrix_in_comb_8.gain(1, 1);
}

void initChannels() {

  channel_1_dist.gain(1);
  channel_2_dist.gain(1);
  channel_3_dist.gain(1);
  channel_4_dist.gain(1);
  channel_5_dist.gain(1);
  channel_6_dist.gain(1);
  channel_7_dist.gain(1);
  channel_8_dist.gain(1);

  channel_1_gain.gain(0);
  channel_2_gain.gain(0);
  channel_3_gain.gain(0);
  channel_4_gain.gain(0);
  channel_5_gain.gain(0);
  channel_6_gain.gain(0);
  channel_7_gain.gain(0);
  channel_8_gain.gain(0);

  channel_1_eq.setCoefficients(0, band_1_coff);
  channel_1_eq.setCoefficients(1, band_2_coff);
  channel_1_eq.setCoefficients(2, band_3_coff);
  channel_1_eq.setCoefficients(3, band_4_coff);

  channel_2_eq.setCoefficients(0, band_1_coff);
  channel_2_eq.setCoefficients(1, band_2_coff);
  channel_2_eq.setCoefficients(2, band_3_coff);
  channel_2_eq.setCoefficients(3, band_4_coff);

  channel_3_eq.setCoefficients(0, band_1_coff);
  channel_3_eq.setCoefficients(1, band_2_coff);
  channel_3_eq.setCoefficients(2, band_3_coff);
  channel_3_eq.setCoefficients(3, band_4_coff);

  channel_4_eq.setCoefficients(0, band_1_coff);
  channel_4_eq.setCoefficients(1, band_2_coff);
  channel_4_eq.setCoefficients(2, band_3_coff);
  channel_4_eq.setCoefficients(3, band_4_coff);

  channel_5_eq.setCoefficients(0, band_1_coff);
  channel_5_eq.setCoefficients(1, band_2_coff);
  channel_5_eq.setCoefficients(2, band_3_coff);
  channel_5_eq.setCoefficients(3, band_4_coff);

  channel_6_eq.setCoefficients(0, band_1_coff);
  channel_6_eq.setCoefficients(1, band_2_coff);
  channel_6_eq.setCoefficients(2, band_3_coff);
  channel_6_eq.setCoefficients(3, band_4_coff);

  channel_7_eq.setCoefficients(0, band_1_coff);
  channel_7_eq.setCoefficients(1, band_2_coff);
  channel_7_eq.setCoefficients(2, band_3_coff);
  channel_7_eq.setCoefficients(3, band_4_coff);

  channel_8_eq.setCoefficients(0, band_1_coff);
  channel_8_eq.setCoefficients(1, band_2_coff);
  channel_8_eq.setCoefficients(2, band_3_coff);
  channel_8_eq.setCoefficients(3, band_4_coff);
}

void initOutputs() {
  output_1_dist.gain(1);
  output_2_dist.gain(1);
  output_3_dist.gain(1);
  output_4_dist.gain(1);
  output_5_dist.gain(1);
  output_6_dist.gain(1);
  output_7_dist.gain(1);
  output_8_dist.gain(1);

  output_1_gain.gain(0);
  output_2_gain.gain(0);
  output_3_gain.gain(0);
  output_4_gain.gain(0);
  output_5_gain.gain(0);
  output_6_gain.gain(0);
  output_7_gain.gain(0);
  output_8_gain.gain(0);


  output_1_eq.setCoefficients(0, band_1_coff);
  output_1_eq.setCoefficients(1, band_2_coff);
  output_1_eq.setCoefficients(2, band_3_coff);
  output_1_eq.setCoefficients(3, band_4_coff);

  output_2_eq.setCoefficients(0, band_1_coff);
  output_2_eq.setCoefficients(1, band_2_coff);
  output_2_eq.setCoefficients(2, band_3_coff);
  output_2_eq.setCoefficients(3, band_4_coff);

  output_3_eq.setCoefficients(0, band_1_coff);
  output_3_eq.setCoefficients(1, band_2_coff);
  output_3_eq.setCoefficients(2, band_3_coff);
  output_3_eq.setCoefficients(3, band_4_coff);

  output_4_eq.setCoefficients(0, band_1_coff);
  output_4_eq.setCoefficients(1, band_2_coff);
  output_4_eq.setCoefficients(2, band_3_coff);
  output_4_eq.setCoefficients(3, band_4_coff);

  output_5_eq.setCoefficients(0, band_1_coff);
  output_5_eq.setCoefficients(1, band_2_coff);
  output_5_eq.setCoefficients(2, band_3_coff);
  output_5_eq.setCoefficients(3, band_4_coff);

  output_6_eq.setCoefficients(0, band_1_coff);
  output_6_eq.setCoefficients(1, band_2_coff);
  output_6_eq.setCoefficients(2, band_3_coff);
  output_6_eq.setCoefficients(3, band_4_coff);

  output_7_eq.setCoefficients(0, band_1_coff);
  output_7_eq.setCoefficients(1, band_2_coff);
  output_7_eq.setCoefficients(2, band_3_coff);
  output_7_eq.setCoefficients(3, band_4_coff);

  output_8_eq.setCoefficients(0, band_1_coff);
  output_8_eq.setCoefficients(1, band_2_coff);
  output_8_eq.setCoefficients(2, band_3_coff);
  output_8_eq.setCoefficients(3, band_4_coff);
}
void setInputChannelGain(int channel, float gain) {
  float lgain = pow(10, (gain / 10));


  switch (channel) {
    case 1:
      channel_1_gain.gain(lgain);
      break;
    case 2:
      channel_2_gain.gain(lgain);
      break;
    case 3:
      channel_3_gain.gain(lgain);
      break;
    case 4:
      channel_4_gain.gain(lgain);
      break;
    case 5:
      channel_5_gain.gain(lgain);
      break;
    case 6:
      channel_6_gain.gain(lgain);
      break;
    case 7:
      channel_7_gain.gain(lgain);
      break;
    case 8:
      channel_8_gain.gain(lgain);
      break;
  }
}



// Use these with the Teensy Audio Shield

// Use these with the Teensy 3.5 & 3.6 & 4.1 SD card
#define SDCARD_CS_PIN    BUILTIN_SDCARD
#define SDCARD_MOSI_PIN  11  // not actually used
#define SDCARD_SCK_PIN   13  // not actually used

// Use these for the SD+Wiz820 or other adaptors
//#define SDCARD_CS_PIN    4
//#define SDCARD_MOSI_PIN  11
//#define SDCARD_SCK_PIN   13


void printFFT()
{
  if (fft_1.available())
  {
    for (int i = 0; i<512; i++)
    {
      if (i == 511)
      {
        Serial.println(fft_1.read(i));
      }
      else
      {
        Serial.print(fft_1.read(i));
        Serial.print(",");
      }
    }
  }
}



void setup() {
  Serial.begin(9600);
  AudioMemory(128);


  initChannels();
  initMatrix();
  initOutputs();



  // Parameters for the peaking EQ
  const double sampleRate = 44100.0;  // Sample rate in Hz
  const double centerFreq = 1000.0;   // Center frequency in Hz
  const double Q = 3.0;               // Quality factor
  const double gain = 0.0;            // Gain in dB

  // Get the coefficients as double
  double* doubleCoefficients = calculatePeakingEQCoefficients(centerFreq, Q, gain, sampleRate);

  noise1.amplitude(1);

  setInputChannelGain(1, -70);
  setInputChannelGain(2, -70);
  setInputChannelGain(3, -70);


  //matrix_in_1.gain(0, 1);
  matrix_out_1.gain(0, 1);
  matrix_out_1.gain(1, 1);
  matrix_out_1.gain(2, 1);
  matrix_out_1.gain(3, 1);

  matrix_out_2.gain(0, 1);
  matrix_out_2.gain(1, 1);
  matrix_out_2.gain(2, 1);
  matrix_out_2.gain(3, 1);
  //matrix_in_3.gain(1, 1);
  //matrix_out_3.gain(1, 1);

  //matrix_in_5.gain(2, 1);
  

  output_2_gain.gain(1);
  output_1_gain.gain(1);

  sine1.frequency(1000);
  sine1.amplitude(1);

  //playSdWav1.play("SDTEST1");
  //playMem1.play(AudioSamplePinkpanther60); -- VERY IMPORTANT
}


int lastUpdate = 0;

void loop() {
  //printFFT();
  if (channel_1_peak.available()){
  out["1"] = amplitudeToDB(channel_1_peak.read());

  }
  if (channel_2_peak.available()){
  out["2"] = amplitudeToDB(channel_2_peak.read());

  }
  if (channel_3_peak.available()){
  out["3"] = amplitudeToDB(channel_3_peak.read());
  
  }
  if (channel_4_peak.available()){
  out["4"] = amplitudeToDB(channel_4_peak.read());

  }
  if (channel_5_peak.available()){
  out["5"] = amplitudeToDB(channel_5_peak.read());

  }
  if (channel_6_peak.available()){
  out["6"] = amplitudeToDB(channel_6_peak.read());
  
  }
  if (channel_7_peak.available()){
  out["7"] = amplitudeToDB(channel_7_peak.read());

  }
  if (channel_8_peak.available()){
  out["8"] = amplitudeToDB(channel_8_peak.read());

  }

  if (millis()-lastUpdate>80)
  {
    serializeJson(out,Serial);
    Serial.println("");
    lastUpdate = millis();
  }

  
  
  if (Serial.available()) {
    deserializeJson(doc,Serial);
    setInputChannelGain(1, doc["1"]);
    setInputChannelGain(2, doc["2"]);
    setInputChannelGain(3, doc["3"]);
    setInputChannelGain(4, doc["4"]);
    setInputChannelGain(5, doc["5"]);
    setInputChannelGain(6, doc["6"]);
    setInputChannelGain(7, doc["7"]);
    setInputChannelGain(8, doc["8"]);


    for (int i = 0; i<4; i++)
    {
     matrix_in_1.gain(i, float(doc["matrixIns"]["1"][String(i+1)]));
    }

  }
}
