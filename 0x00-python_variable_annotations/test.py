from typing import Union,Tuple, List

def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    return(k, v**2)
