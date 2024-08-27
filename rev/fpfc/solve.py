#!/usr/bin/env python3

from pwn import *

p64 = lambda x: util.packing.p64(x, endian='little')
u64 = lambda x: util.packing.u64(x, endian='little')
p32 = lambda x: util.packing.p32(x, endian='little')
u32 = lambda x: util.packing.u32(x, endian='little')

exe = ELF("./FPFC")

context.binary = exe
context.terminal = ['tmux', 'splitw', '-h', '-F' '#{pane_pid}', '-P']


def conn():
	if args.GDB:
		r = gdb.debug([exe.path])
	elif args.REMOTE:
		r = remote("fpfc.challs.open.ecsc2024.it", 38015)
	else:
		r = process([exe.path])
	return r

r = conn()


def main():
	solution = b'RIZZTMZZUMZZNAZZSBZZSBZZWHZZIIZZIIZZKVZZUYZZUYOONAGG'
	r.sendlineafter(b'solution: \n', solution)
	r.recvuntil(b'flag: ')
	flag = r.recvline().strip().decode()
	print(flag)

	r.interactive()


if __name__ == "__main__":
	main()

# openECSC{4lm0s7_l1k3_p1ng_pwng_0n_th3_w4llz_0ff3f76e}
