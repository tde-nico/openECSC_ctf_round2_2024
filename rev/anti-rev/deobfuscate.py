import idautils
from idc import *

to_patch = bytes.fromhex('E8000000004883042406c3')
start = 0x11A9
end = 0x1D9F

for i in range(start, end):
	if get_bytes(i, len(to_patch)) == to_patch:
		for j in range(len(to_patch)):
			patch_byte(i + j, 0x90)
	#print(i)
