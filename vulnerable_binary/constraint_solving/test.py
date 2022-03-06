import angr
import claripy


def is_successful(state):
    return b"Solved!" in state.posix.dumps(1)


if __name__ == '__main__':
    p = angr.Project("./a.out")
    args = [claripy.BVS("arg{}".format(i), 32) for i in range(2)]
    initial_state = p.factory.entry_state(args=args)

    simgr = p.factory.simgr(initial_state)
    simgr.explore(find=is_successful)
    print(simgr)

    if simgr.found:
        solution = simgr.found[0]
        print(solution.posix.dumps(1))
    else:
        print("Not found")
