# Sample Hello World Beaker smart contract - the most basic starting point for an Algorand smart contract
import beaker
from pyteal import *; 

app = beaker.Application("caseAdd")


@app.external
def caseAdd(a: abi.Uint64,b: abi.Uint64, *, output: abi.Uint64) -> Expr:
    return  Seq(If(a.get() > b.get()).Then(output.set(a.get()+b.get())).Else(output.set(a.get()-b.get())))
     
