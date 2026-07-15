
#Type definitionn in python
n : int = 5
name : str = "Harry"

def sum(a:int,b:int) -> int:
    return a+b

from typing import List,Tuple,Dict,Union

number : List[int] = [1,2,3]
personn :Tuple[int,str] = (1,"x5")
score : dict[str,int] = {"usman",5}
iden: Union[int,str] = "x5"