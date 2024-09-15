from typing import Callable

def fn_hola_mundo() -> str:
    return "Hola mundo"

def fn_print(f: Callable) -> None:
    print(f())
    
fn_print(fn_hola_mundo)

