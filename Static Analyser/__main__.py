import os
import angr
import argparse
import claripy


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Static Analyser")
    parser.add_argument("binary", help="Path to the binary to analyse")
    parser.add_argument("no_input", type=int, help="Number of inputs")
    parser.add_argument("-b", "--base", help="Base address of the binary", type=hex, default=0x00)
    parser.add_argument("-t", "--target", help="Target address to to reach", type=hex, default=0x00)
    
    args = parser.parse_args()

    # Get vars
    binary_path = os.path.normpath(args.binary) # Normalize path
    base = args.base
    target = args.target
    no_inputs = args.no_input

    # Creating project and exploring
    p = angr.Project(binary_path, main_opts={'base_addr': base})
    variables = []

    for index in range(no_inputs):
        variables.append(claripy.BVS(f'val{index}', 64))

    entry_state = p.factory.full_init_state(args=[f"./{binary_path}"], variables)
    simgr = p.factory.simulation_manager(entry_state)
    simgr.explore(find=target)
    if len(simgr.found) > 0:
        for state in simgr.found:
            state.solver.eval()



    
    
