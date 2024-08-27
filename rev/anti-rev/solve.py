from z3 import *

s = Solver()

LEN = 30
flag = [BitVec(f'char_{i}', 8) for i in range(LEN)]


s.add(flag[0] == ord('o'))
s.add(flag[1] == ord('p'))
s.add(flag[2] == ord('e'))
s.add(flag[3] == ord('n'))
s.add(flag[4] == ord('E'))
s.add(flag[5] == ord('C'))
s.add(flag[6] == ord('S'))
s.add(flag[7] == ord('C'))
s.add(flag[8] == ord('{'))
s.add(flag[29] == ord('}'))


s.add(59 * flag[28] + -7 * flag[24] + 124 * flag[19] + -4 * flag[14] + -57 * flag[10] + 17 * flag[9] - 125 == 0xD2)
s.add(-39 * flag[28] + -118 * flag[19] + -107 * flag[12] + 18 * flag[10] + 50 * flag[9] + 106 == 119)
s.add(36 * flag[27] + 31 * flag[24] + 103 * flag[22] + (flag[18] << 7) + -81 * flag[12] - 48 == 0x97)
s.add(-84 * flag[21] + -107 * flag[20] + -78 * flag[19] + -102 * flag[16] + -16 * flag[14] + 65 * flag[12] + -64 * flag[9] - 74 == 66)
s.add(-73 * flag[27] + 120 * flag[12] - 23 == 0xA2)
s.add(flag[26] + -82 * flag[20] + -112 * flag[18] + -73 * flag[17] + 40 * flag[16] + -81 * flag[15] + -69 * flag[14] + 71 * flag[10] + 37 == 78)
s.add(-116 * flag[28] + -68 * flag[25] + -64 * flag[24] + -25 * flag[20] + -23 * flag[17] + -15 * flag[12] + -50 * flag[9] - 110 == 74)
s.add(107 * flag[25] + 67 * flag[24] + 46 * flag[22] + 117 * flag[19] + 61 == 89)
s.add(-118 * flag[25] + 113 * flag[20] + -4 * flag[16] + 5 == 48)
s.add(25 * flag[18] + -64 * flag[16] + 101 * flag[11] - 15 == 0x84)
s.add(47 * flag[28] + 17 * flag[25] + -5 * flag[20] + 39 * flag[19] + 16 * flag[15] + 127 * flag[14] + 67 * flag[11] + 45 == 0xBA)
s.add(-34 * flag[22] + -121 * flag[9] + 37 == 0xE5)
s.add(-4 * flag[28] + -103 * flag[26] + 4 * flag[15] + -91 * flag[13] - 121 == 0x90)
s.add(88 * flag[27] + 11 * flag[26] + 23 * flag[22] + 34 * flag[20] + 20 * flag[19] + 13 * flag[15] + 97 * flag[14] + -99 * flag[11] + 39 - flag[23] == 0xE5)
s.add(-35 * flag[27] + 56 * flag[25] + -117 * flag[21] + 10 * flag[17] + -90 * flag[12] + 5 == 121)
s.add(-57 * flag[15] + -96 * flag[11] - 62 == 4)
s.add(-70 * flag[28] + 83 * flag[26] + -15 * flag[10] - 33 == 0x8F)
s.add(81 * flag[19] + -61 * flag[17] + -38 * flag[16] + 25 * flag[14] + 43 * flag[13] + -93 * flag[11] - 12 == 57)
s.add(88 * flag[27] + 113 * flag[26] + 98 * flag[23] + 55 == 31)
s.add(-79 * flag[24] + 11 * flag[20] + 117 * flag[16] + -100 * flag[10] + -11 * flag[9] + 64 == 56)


if s.check() == sat:
	m = s.model()
	win = ''.join([chr(m[char].as_long()) for char in flag])
	print(win)

# openECSC{f4nCy_n0p5!_e5f5f470}
