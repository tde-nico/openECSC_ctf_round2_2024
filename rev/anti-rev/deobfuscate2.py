with open('./anti-rev', 'rb') as f:
	program = f.read()

to_patch = bytes.fromhex('E8000000004883042406c3')

program = program.replace(to_patch, b'\x90' * len(to_patch))

with open('anti-rev-patched', 'wb') as f:
	f.write(program)
