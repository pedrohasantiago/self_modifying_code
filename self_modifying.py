from typing import List, IO

LINE_TO_MODIFY = 4

to_return = 1

def get_file(mode: str) -> IO:
    return open(__file__, mode)

def read_code() -> List[str]:
    with get_file('r') as f:
        return f.readlines()

def modify_code(code_as_list: List[str]) -> str:
    new_val = 1 if to_return == 0 else 0
    code_as_list[LINE_TO_MODIFY] = code_as_list[LINE_TO_MODIFY][:-2] + str(new_val) + '\n'
    return ''.join(code_as_list)

def save_code(new_code: str):
    with get_file('w') as f:
        f.writelines(new_code)

if __name__ == "__main__":
    old_to_return = to_return
    curr_code = read_code()
    new_code = modify_code(curr_code)
    save_code(new_code)
    exec('\n'.join(new_code.split('\n')[:LINE_TO_MODIFY + 1]))
    print(f'If {old_to_return} is different from {to_return}, this means this program has read its own source code, '
           'modified it and interpreted the modification.\n'
           'If these values change in the next execution of the program, this means it has replaced its own source code '
           'with the modified version.')
