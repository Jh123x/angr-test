import os
import sys
import angr
import argparse
import claripy


def is_successful(state):
	output = state.posix.dumps(sys.stdout.fileno()) #grab the screen output everytime Angr thinks we have a solution
	if b'Solved!' in output: #make sure it says 'Solved'!
		return True
	return False


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Static Analyser")
    parser.add_argument("binary", help="Path to the binary to analyse")
    args = parser.parse_args()

    # Get vars
    binary_path = os.path.normpath(args.binary) # Normalize path

    # Creating project and exploring
    print(f"[+] Creating angr project with '{binary_path}'")
    argv1 = claripy.BVS("a",32)
    argv2 = claripy.BVS("b",32)
    p = angr.Project(binary_path)

    state = p.factory.entry_state(args=[binary_path, argv1, argv2], add_options={angr.options.LAZY_SOLVES})
    simgr = p.factory.simgr(state)
    print(f"[+] Exploring path...")
    simgr.explore(find=is_successful)
    if len(simgr.found) > 0:
        print("[+] Vulnerability found")
        for state in simgr.found:
            print(state.solver.eval(state))
    elif simgr.errored:
        print("[+] Error found")
        for state in simgr.errored:
            print(state)
    else:
        print("[-] No vulnerability found")



    
    
