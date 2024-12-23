uncontrolled="""crc32(34, 2) == 0x5888fc1b
crc32(63, 2) == 0x66715919
crc32(78, 2) == 0x7cab8d64
crc32(8, 2) == 0x61089c5c
md5(0, 2) == "89484b14b36a8d5329426a3d944d2983"
md5(32, 2) == "738a656e8e8ec272ca17cd51e12f558b"
md5(50, 2) == "657dae0913ee12be6fb2a6f687aae1c7"
md5(76, 2) == "f98ed07a4d5f50f7de1410d905f1477f"
sha256(14, 2) == "403d5f23d149670348b147a15eeb7010914701a7e99aad2e43f90cfa0325c76f"
sha256(56, 2) == "593f2d04aab251f60c9e4b8bbc1e05a34e920980ec08351a18459b2bc7dbf2f6"
uint8(2) > 20
uint32(10) + 383041523 == 2448764514
uint32(17) - 323157430 == 1412131772
uint32(22) ^ 372102464 == 1879700858
uint32(28) - 419186860 == 959764852
uint32(3) ^ 298697263 == 2108416586
uint32(37) + 367943707 == 1228527996
uint32(41) + 404880684 == 1699114335
uint32(46) - 412326611 == 1503714457
uint32(52) ^ 425706662 == 1495724241
uint32(59) ^ 512952669 == 1908304943
uint32(66) ^ 310886682 == 849718389
uint32(70) + 349203301 == 2034162376
uint32(80) - 473886976 == 69677856
filesize ^ uint8(0) != 16
filesize ^ uint8(0) != 41
filesize ^ uint8(1) != 0
filesize ^ uint8(1) != 232
filesize ^ uint8(10) != 205
filesize ^ uint8(10) != 44
filesize ^ uint8(11) != 107
filesize ^ uint8(11) != 33
filesize ^ uint8(12) != 116
filesize ^ uint8(12) != 226
filesize ^ uint8(13) != 219
filesize ^ uint8(13) != 42
filesize ^ uint8(14) != 161
filesize ^ uint8(14) != 99
filesize ^ uint8(15) != 205
filesize ^ uint8(15) != 27
filesize ^ uint8(16) != 144
filesize ^ uint8(16) != 7
filesize ^ uint8(17) != 16
filesize ^ uint8(17) != 208
filesize ^ uint8(18) != 234
filesize ^ uint8(18) != 33
filesize ^ uint8(19) != 222
filesize ^ uint8(19) != 31
filesize ^ uint8(2) != 205
filesize ^ uint8(2) != 54
filesize ^ uint8(20) != 17
filesize ^ uint8(20) != 83
filesize ^ uint8(21) != 188
filesize ^ uint8(21) != 27
filesize ^ uint8(22) != 191
filesize ^ uint8(22) != 31
filesize ^ uint8(23) != 18
filesize ^ uint8(23) != 242
filesize ^ uint8(24) != 217
filesize ^ uint8(24) != 94
filesize ^ uint8(25) != 224
filesize ^ uint8(25) != 47
filesize ^ uint8(26) != 161
filesize ^ uint8(26) != 44
filesize ^ uint8(27) != 244
filesize ^ uint8(27) != 43
filesize ^ uint8(28) != 12
filesize ^ uint8(28) != 238
filesize ^ uint8(29) != 158
filesize ^ uint8(29) != 37
filesize ^ uint8(3) != 147
filesize ^ uint8(3) != 43
filesize ^ uint8(30) != 18
filesize ^ uint8(30) != 249
filesize ^ uint8(31) != 32
filesize ^ uint8(31) != 5
filesize ^ uint8(32) != 30
filesize ^ uint8(32) != 77
filesize ^ uint8(33) != 157
filesize ^ uint8(33) != 27
filesize ^ uint8(34) != 115
filesize ^ uint8(34) != 39
filesize ^ uint8(35) != 120
filesize ^ uint8(35) != 18
filesize ^ uint8(36) != 6
filesize ^ uint8(36) != 95
filesize ^ uint8(37) != 141
filesize ^ uint8(37) != 37
filesize ^ uint8(38) != 8
filesize ^ uint8(38) != 84
filesize ^ uint8(39) != 18
filesize ^ uint8(39) != 49
filesize ^ uint8(4) != 23
filesize ^ uint8(4) != 253
filesize ^ uint8(40) != 230
filesize ^ uint8(40) != 49
filesize ^ uint8(41) != 233
filesize ^ uint8(41) != 74
filesize ^ uint8(42) != 1
filesize ^ uint8(42) != 91
filesize ^ uint8(43) != 251
filesize ^ uint8(43) != 33
filesize ^ uint8(44) != 17
filesize ^ uint8(44) != 96
filesize ^ uint8(45) != 146
filesize ^ uint8(45) != 19
filesize ^ uint8(46) != 18
filesize ^ uint8(46) != 186
filesize ^ uint8(47) != 11
filesize ^ uint8(47) != 119
filesize ^ uint8(48) != 29
filesize ^ uint8(48) != 99
filesize ^ uint8(49) != 10
filesize ^ uint8(49) != 156
filesize ^ uint8(5) != 243
filesize ^ uint8(5) != 43
filesize ^ uint8(50) != 219
filesize ^ uint8(50) != 86
filesize ^ uint8(51) != 0
filesize ^ uint8(51) != 204
filesize ^ uint8(52) != 22
filesize ^ uint8(52) != 238
filesize ^ uint8(53) != 19
filesize ^ uint8(53) != 243
filesize ^ uint8(54) != 141
filesize ^ uint8(54) != 39
filesize ^ uint8(55) != 17
filesize ^ uint8(55) != 244
filesize ^ uint8(56) != 22
filesize ^ uint8(56) != 246
filesize ^ uint8(57) != 14
filesize ^ uint8(57) != 186
filesize ^ uint8(58) != 12
filesize ^ uint8(58) != 77
filesize ^ uint8(59) != 13
filesize ^ uint8(59) != 194
filesize ^ uint8(6) != 129
filesize ^ uint8(6) != 39
filesize ^ uint8(60) != 142
filesize ^ uint8(60) != 43
filesize ^ uint8(61) != 239
filesize ^ uint8(61) != 94
filesize ^ uint8(62) != 15
filesize ^ uint8(62) != 246
filesize ^ uint8(63) != 135
filesize ^ uint8(63) != 34
filesize ^ uint8(64) != 158
filesize ^ uint8(64) != 50
filesize ^ uint8(65) != 215
filesize ^ uint8(65) != 28
filesize ^ uint8(66) != 146
filesize ^ uint8(66) != 51
filesize ^ uint8(67) != 55
filesize ^ uint8(67) != 63
filesize ^ uint8(68) != 135
filesize ^ uint8(68) != 8
filesize ^ uint8(69) != 241
filesize ^ uint8(69) != 30
filesize ^ uint8(7) != 15
filesize ^ uint8(7) != 221
filesize ^ uint8(70) != 209
filesize ^ uint8(70) != 41
filesize ^ uint8(71) != 128
filesize ^ uint8(71) != 3
filesize ^ uint8(72) != 219
filesize ^ uint8(72) != 37
filesize ^ uint8(73) != 17
filesize ^ uint8(73) != 61
filesize ^ uint8(74) != 193
filesize ^ uint8(74) != 45
filesize ^ uint8(75) != 25
filesize ^ uint8(75) != 35
filesize ^ uint8(76) != 30
filesize ^ uint8(76) != 88
filesize ^ uint8(77) != 22
filesize ^ uint8(77) != 223
filesize ^ uint8(78) != 163
filesize ^ uint8(78) != 6
filesize ^ uint8(79) != 104
filesize ^ uint8(79) != 186
filesize ^ uint8(8) != 107
filesize ^ uint8(8) != 2
filesize ^ uint8(80) != 236
filesize ^ uint8(80) != 56
filesize ^ uint8(81) != 242
filesize ^ uint8(81) != 7
filesize ^ uint8(82) != 228
filesize ^ uint8(82) != 32
filesize ^ uint8(83) != 197
filesize ^ uint8(83) != 31
filesize ^ uint8(84) != 231
filesize ^ uint8(84) != 3
filesize ^ uint8(9) != 164
filesize ^ uint8(9) != 5
uint8(0) % 25 < 25
uint8(0) & 128 == 0
uint8(0) < 129
uint8(0) > 30
uint8(1) % 17 < 17
uint8(1) & 128 == 0
uint8(1) < 158
uint8(1) > 19
uint8(10) % 10 < 10
uint8(10) & 128 == 0
uint8(10) < 146
uint8(10) > 9
uint8(11) % 27 < 27
uint8(11) & 128 == 0
uint8(11) < 154
uint8(11) > 18
uint8(12) % 23 < 23
uint8(12) & 128 == 0
uint8(12) < 147
uint8(12) > 19
uint8(13) % 27 < 27
uint8(13) & 128 == 0
uint8(13) < 147
uint8(13) > 21
uint8(14) % 19 < 19
uint8(14) & 128 == 0
uint8(14) < 153
uint8(14) > 20
uint8(15) % 16 < 16
uint8(15) & 128 == 0
uint8(15) < 156
uint8(15) > 26
uint8(16) % 31 < 31
uint8(16) & 128 == 0
uint8(16) < 134
uint8(16) > 25
uint8(16) ^ 7 == 115
uint8(17) % 11 < 11
uint8(17) & 128 == 0
uint8(17) < 150
uint8(17) > 31
uint8(18) % 30 < 30
uint8(18) & 128 == 0
uint8(18) < 137
uint8(18) > 13
uint8(19) % 30 < 30
uint8(19) & 128 == 0
uint8(19) < 151
uint8(19) > 4
uint8(2) % 28 < 28
uint8(2) & 128 == 0
uint8(2) + 11 == 119
uint8(2) < 147
uint8(2) > 20
uint8(20) % 28 < 28
uint8(20) & 128 == 0
uint8(20) < 135
uint8(20) > 1
uint8(21) % 11 < 11
uint8(21) & 128 == 0
uint8(21) - 21 == 94
uint8(21) < 138
uint8(21) > 7
uint8(22) % 22 < 22
uint8(22) & 128 == 0
uint8(22) < 152
uint8(22) > 20
uint8(23) % 16 < 16
uint8(23) & 128 == 0
uint8(23) < 141
uint8(23) > 2
uint8(24) % 26 < 26
uint8(24) & 128 == 0
uint8(24) < 148
uint8(24) > 22
uint8(25) % 23 < 23
uint8(25) & 128 == 0
uint8(25) < 154
uint8(25) > 27
uint8(26) % 25 < 25
uint8(26) & 128 == 0
uint8(26) - 7 == 25
uint8(26) < 132
uint8(26) > 31
uint8(27) % 26 < 26
uint8(27) & 128 == 0
uint8(27) < 147
uint8(27) > 23
uint8(27) ^ 21 == 40
uint8(28) % 27 < 27
uint8(28) & 128 == 0
uint8(28) < 160
uint8(28) > 27
uint8(29) % 12 < 12
uint8(29) & 128 == 0
uint8(29) < 157
uint8(29) > 22
uint8(3) % 13 < 13
uint8(3) & 128 == 0
uint8(3) < 141
uint8(3) > 21
uint8(30) % 15 < 15
uint8(30) & 128 == 0
uint8(30) < 131
uint8(30) > 6
uint8(31) % 17 < 17
uint8(31) & 128 == 0
uint8(31) < 145
uint8(31) > 7
uint8(32) % 17 < 17
uint8(32) & 128 == 0
uint8(32) < 140
uint8(32) > 28
uint8(33) % 25 < 25
uint8(33) & 128 == 0
uint8(33) < 160
uint8(33) > 18
uint8(34) % 19 < 19
uint8(34) & 128 == 0
uint8(34) < 138
uint8(34) > 18
uint8(35) % 15 < 15
uint8(35) & 128 == 0
uint8(35) < 160
uint8(35) > 1
uint8(36) % 22 < 22
uint8(36) & 128 == 0
uint8(36) + 4 == 72
uint8(36) < 146
uint8(36) > 11
uint8(37) % 19 < 19
uint8(37) & 128 == 0
uint8(37) < 139
uint8(37) > 16
uint8(38) % 24 < 24
uint8(38) & 128 == 0
uint8(38) < 135
uint8(38) > 18
uint8(39) % 11 < 11
uint8(39) & 128 == 0
uint8(39) < 134
uint8(39) > 7
uint8(4) % 17 < 17
uint8(4) & 128 == 0
uint8(4) < 139
uint8(4) > 30
uint8(40) % 19 < 19
uint8(40) & 128 == 0
uint8(40) < 131
uint8(40) > 15
uint8(41) % 27 < 27
uint8(41) & 128 == 0
uint8(41) < 140
uint8(41) > 5
uint8(42) % 17 < 17
uint8(42) & 128 == 0
uint8(42) < 157
uint8(42) > 3
uint8(43) % 26 < 26
uint8(43) & 128 == 0
uint8(43) < 160
uint8(43) > 24
uint8(44) % 27 < 27
uint8(44) & 128 == 0
uint8(44) < 147
uint8(44) > 5
uint8(45) % 17 < 17
uint8(45) & 128 == 0
uint8(45) < 136
uint8(45) > 17
uint8(45) ^ 9 == 104
uint8(46) % 28 < 28
uint8(46) & 128 == 0
uint8(46) < 154
uint8(46) > 22
uint8(47) % 18 < 18
uint8(47) & 128 == 0
uint8(47) < 142
uint8(47) > 13
uint8(48) % 12 < 12
uint8(48) & 128 == 0
uint8(48) < 136
uint8(48) > 15
uint8(49) % 13 < 13
uint8(49) & 128 == 0
uint8(49) < 129
uint8(49) > 27
uint8(5) % 27 < 27
uint8(5) & 128 == 0
uint8(5) < 158
uint8(5) > 14
uint8(50) % 11 < 11
uint8(50) & 128 == 0
uint8(50) < 138
uint8(50) > 19
uint8(51) % 15 < 15
uint8(51) & 128 == 0
uint8(51) < 139
uint8(51) > 7
uint8(52) % 23 < 23
uint8(52) & 128 == 0
uint8(52) < 136
uint8(52) > 25
uint8(53) % 23 < 23
uint8(53) & 128 == 0
uint8(53) < 144
uint8(53) > 24
uint8(54) % 25 < 25
uint8(54) & 128 == 0
uint8(54) < 152
uint8(54) > 15
uint8(55) % 11 < 11
uint8(55) & 128 == 0
uint8(55) < 153
uint8(55) > 5
uint8(56) % 26 < 26
uint8(56) & 128 == 0
uint8(56) < 155
uint8(56) > 8
uint8(57) % 27 < 27
uint8(57) & 128 == 0
uint8(57) < 138
uint8(57) > 11
uint8(58) % 14 < 14
uint8(58) & 128 == 0
uint8(58) + 25 == 122
uint8(58) < 146
uint8(58) > 30
uint8(59) % 23 < 23
uint8(59) & 128 == 0
uint8(59) < 141
uint8(59) > 4
uint8(6) % 12 < 12
uint8(6) & 128 == 0
uint8(6) < 155
uint8(6) > 6
uint8(60) % 23 < 23
uint8(60) & 128 == 0
uint8(60) < 130
uint8(60) > 14
uint8(61) % 26 < 26
uint8(61) & 128 == 0
uint8(61) < 160
uint8(61) > 12
uint8(62) % 13 < 13
uint8(62) & 128 == 0
uint8(62) < 146
uint8(62) > 1
uint8(63) % 30 < 30
uint8(63) & 128 == 0
uint8(63) < 129
uint8(63) > 31
uint8(64) % 24 < 24
uint8(64) & 128 == 0
uint8(64) < 154
uint8(64) > 27
uint8(65) % 22 < 22
uint8(65) & 128 == 0
uint8(65) - 29 == 70
uint8(65) < 149
uint8(65) > 1
uint8(66) % 16 < 16
uint8(66) & 128 == 0
uint8(66) < 133
uint8(66) > 30
uint8(67) % 16 < 16
uint8(67) & 128 == 0
uint8(67) < 144
uint8(67) > 27
uint8(68) % 19 < 19
uint8(68) & 128 == 0
uint8(68) < 138
uint8(68) > 10
uint8(69) % 30 < 30
uint8(69) & 128 == 0
uint8(69) < 148
uint8(69) > 25
uint8(7) % 12 < 12
uint8(7) & 128 == 0
uint8(7) - 15 == 82
uint8(7) < 131
uint8(7) > 18
uint8(70) % 21 < 21
uint8(70) & 128 == 0
uint8(70) < 139
uint8(70) > 6
uint8(71) % 28 < 28
uint8(71) & 128 == 0
uint8(71) < 130
uint8(71) > 19
uint8(72) % 14 < 14
uint8(72) & 128 == 0
uint8(72) < 134
uint8(72) > 10
uint8(73) % 23 < 23
uint8(73) & 128 == 0
uint8(73) < 136
uint8(73) > 26
uint8(74) % 10 < 10
uint8(74) & 128 == 0
uint8(74) + 11 == 116
uint8(74) < 152
uint8(74) > 1
uint8(75) % 24 < 24
uint8(75) & 128 == 0
uint8(75) - 30 == 86
uint8(75) < 142
uint8(75) > 30
uint8(76) % 24 < 24
uint8(76) & 128 == 0
uint8(76) < 156
uint8(76) > 2
uint8(77) % 24 < 24
uint8(77) & 128 == 0
uint8(77) < 154
uint8(77) > 5
uint8(78) % 13 < 13
uint8(78) & 128 == 0
uint8(78) < 141
uint8(78) > 24
uint8(79) % 24 < 24
uint8(79) & 128 == 0
uint8(79) < 146
uint8(79) > 31
uint8(8) % 21 < 21
uint8(8) & 128 == 0
uint8(8) < 133
uint8(8) > 3
uint8(80) % 31 < 31
uint8(80) & 128 == 0
uint8(80) < 143
uint8(80) > 2
uint8(81) % 14 < 14
uint8(81) & 128 == 0
uint8(81) < 131
uint8(81) > 11
uint8(82) % 28 < 28
uint8(82) & 128 == 0
uint8(82) < 152
uint8(82) > 3
uint8(83) % 21 < 21
uint8(83) & 128 == 0
uint8(83) < 134
uint8(83) > 16
uint8(84) % 18 < 18
uint8(84) & 128 == 0
uint8(84) + 3 == 128
uint8(84) < 129
uint8(84) > 26
uint8(9) % 22 < 22
uint8(9) & 128 == 0
uint8(9) < 151
uint8(9) > 23"""

import hashlib
import zlib


filesize=85
conditions= [0] * filesize
for i in range(0,filesize):
    conditions[i]=set()

a = [0x20] * filesize

eq=2448764514 - 383041523
a[10] =eq
a[11] =eq
a[12] =eq
a[13] =eq
a[13] =(a[13] & 0xFF000000) >> 24
a[12] =(a[12] & 0xFF0000) >> 16
a[11] =(a[11] & 0xFF00) >> 8
a[10] =a[10] & 0xFF


eq=1412131772+323157430
a[17] =eq
a[18] =eq
a[19] =eq
a[20] =eq
a[20] =(a[20] & 0xFF000000) >> 24
a[19] =(a[19] & 0xFF0000) >> 16
a[18] =(a[18] & 0xFF00) >> 8
a[17] =a[17] & 0xFF

eq= 959764852+419186860
a[28] =eq
a[29] =eq
a[30] =eq
a[31] =eq
a[31] =(a[31] & 0xFF000000) >> 24
a[30] =(a[30] & 0xFF0000) >> 16
a[29] =(a[29] & 0xFF00) >> 8
a[28] =a[28] & 0xFF


eq=1228527996-367943707
a[37] =eq
a[38] =eq
a[39] =eq
a[40] =eq
a[40]=(a[40] & 0xFF000000) >> 24
a[39] =(a[39] & 0xFF0000) >> 16
a[38] =(a[38] & 0xFF00) >> 8
a[37] =a[37] & 0xFF

eq=1699114335 - 404880684
a[41] =eq
a[42] =eq
a[43] =eq
a[44] =eq
a[44] =(a[44] & 0xFF000000) >> 24
a[43] =(a[43] & 0xFF0000) >> 16
a[42] =(a[42] & 0xFF00) >> 8
a[41] =a[41] & 0xFF

eq=1503714457 - 412326611
a[46] =eq
a[47] =eq
a[48] =eq
a[49] =eq
a[49] =(a[49] & 0xFF000000) >> 24
a[48] =(a[48] & 0xFF0000) >> 16
a[47] =(a[47] & 0xFF00) >> 8
a[46] =a[46] & 0xFF

eq=2034162376 - 349203301
a[70] =eq
a[71] =eq
a[72] =eq
a[73] =eq
a[73] =(a[73] & 0xFF000000) >> 24
a[72] =(a[72] & 0xFF0000) >> 16
a[71] =(a[71] & 0xFF00) >> 8
a[70] =a[70] & 0xFF

eq=69677856 + 473886976
a[80] =eq
a[81] =eq
a[82] =eq
a[83] =eq
a[83] =(a[83] & 0xFF000000) >> 24
a[82] =(a[82] & 0xFF0000) >> 16
a[81] =(a[81] & 0xFF00) >> 8
a[80] =a[80] & 0xFF


eq=2108416586 ^ 298697263
a[3] =eq
a[4] =eq
a[5] =eq
a[6] =eq
a[6] =(a[6] & 0xFF000000) >> 24
a[5] =(a[5] & 0xFF0000) >> 16
a[4] =(a[4] & 0xFF00) >> 8
a[3] =a[3] & 0xFF


eq=1495724241 ^ 425706662
a[52] =eq
a[53] =eq
a[54] =eq
a[55] =eq
a[55] =(a[55] & 0xFF000000) >> 24
a[54] =(a[54] & 0xFF0000) >> 16
a[53] =(a[53] & 0xFF00) >> 8
a[52] =a[52] & 0xFF

eq=1908304943 ^ 512952669
a[59] =eq
a[60] =eq
a[61] =eq
a[62] =eq
a[62] =(a[62] & 0xFF000000) >> 24
a[61] =(a[61] & 0xFF0000) >> 16
a[60] =(a[60] & 0xFF00) >> 8
a[59] =a[59] & 0xFF

eq=849718389 ^ 310886682
a[66] =eq
a[67] =eq
a[68] =eq
a[69] =eq
a[69] =(a[69] & 0xFF000000) >> 24
a[68] =(a[68] & 0xFF0000) >> 16
a[67] =(a[67] & 0xFF00) >> 8
a[66] =a[66] & 0xFF

eq=1879700858 ^ 372102464
a[22] =eq
a[23] =eq
a[24] =eq
a[25] =eq
a[25] =(a[25] & 0xFF000000) >> 24
a[24] =(a[24] & 0xFF0000) >> 16
a[23] =(a[23] & 0xFF00) >> 8
a[22] =a[22] & 0xFF



"""
tail="@flare-on.com"
for i in range(0,len(tail)):
    a[i+72]=ord(tail[i])
"""


condition_set_stage=True
current_statement=""
current_target=0

def condition_setter(i):
    if current_target==i:
        conditions[i].add(current_statement)

def crc32(i,k):
    if condition_set_stage:
        condition_setter(i)
        return 1
    var=(((a[i] << 8) & 0xFF00) + (a[i+1] & 0xFF))
    return str(hex(zlib.crc32(int(var).to_bytes(2, 'big', signed=True))))

def md5(i,k):
    if condition_set_stage:
        condition_setter(i)
        return 1
    var=(((a[i] << 8) & 0xFF00) + (a[i+1] & 0xFF))
    return hashlib.md5(int(var).to_bytes(2, 'big', signed=True)).hexdigest()

def sha256(i,k):
    if condition_set_stage:
        condition_setter(i)
        return 1
    var=(((a[i] << 8) & 0xFF00) + (a[i+1] & 0xFF))
    return hashlib.sha256(int(var).to_bytes(2, 'big', signed=True)).hexdigest()

def uint32(i):
    if condition_set_stage:
        condition_setter(i)
        return 1
    return ( ((a[i] << 24)& 0xFF000000)   + ((a[i+1] << 16) & 0xFF0000) + ((a[i+2] << 8) & 0xFF00) + (a[i+3] & 0xFF))

def uint8(i):
    if condition_set_stage:
        condition_setter(i)
        return 1
    return a[i] & 0xFF


for i in range(0,filesize):
    current_target=i
    for evil in uncontrolled.split("\n"):
        current_statement=evil
        eval(evil)


condition_set_stage=False


skipbytes=0


for i in range(0,85):
    print("Now on",i)

    cumulative=True
    candi0=0

    cumulative0=True
    candi1=0

    cumulative3=True
    candi2=0
    candi3=0

    if skipbytes!=0:
        skipbytes=skipbytes-1
        continue


    for condition in conditions[i]:
        if "md" in condition or "sha" in condition or "crc" in condition:
            skipbytes=1
            print("checksum detected")
        elif "uint32" in condition:
            skipbytes=3
            print("uint detected")

    if skipbytes==3:
        continue


    for b0 in range(0x20,0x7f):
        cumulative=True
        if skipbytes>0:
            for b1 in range(0x20,0x7f):
                cumulative0=True
                if skipbytes==3:
                    for b2 in range(0x20,0x7f):
                        for b3 in range(0x20,0x7f):
                            cumulative3=True
                            for condition in conditions[i]:
                                a[i]=b0
                                a[i+1]=b1
                                a[i+2]=b2
                                a[i+3]=b3

                                cumulative3=cumulative3 & eval(condition)
                            if cumulative3:
                                candi0=b0
                                candi1=b1
                                candi2=b2
                                candi3=b3
                                break

                else:
                    for condition in conditions[i]:
                        a[i]=b0
                        a[i+1]=b1

                        cumulative0=cumulative0 & eval(condition)
                    if cumulative0:
                        candi0=b0
                        candi1=b1
                        break
        else:
            for condition in conditions[i]:
                a[i]=b0
                cumulative=cumulative & eval(condition)

            if cumulative:
                candi0=b0
                break

    if candi1!=0:
        a[i]=candi0

    if candi1!=0:
        a[i+1]=candi1

    if candi2!=0:
        a[i+2]=candi2

    if candi3!=0:
        a[i+3]=candi3

    a[7]=ord('a')
    a[8]=ord('r')
    a[9]=ord('e')
    a[15]=ord('s')
    a[16]=ord('t')
    a[17]=ord('r')
    a[21]=ord('s')

    a[34]=ord('e')
    a[35]=65


    a[56]=ord('f')
    a[57]=ord('l')
    a[58]=ord('a')
    a[63]=ord('n')
    a[64]=ord('.')
    a[65]=ord('c')

    a[74]=ord('i')
    a[75]=ord('t')
    a[76]=ord('i')
    a[77]=ord('o')
    a[78]=ord('n')

    print(a,i)

print(conditions[46])

print(a[46])
print(a[47])
print(a[48])
print(a[49])
