import curses

from greibach.greibach import *
from pda.pda import *



def get_unique_numbers(numbers):

    list_of_unique_numbers = []

    unique_numbers = set(numbers)

    for number in unique_numbers:
        list_of_unique_numbers.append(number)

    return list_of_unique_numbers

def pegar_saída(p):
    v = []
    prod = {}
    for key in p.keys():
        prodaux = []
        v.append(key)
        for rhs in p[key]:
            prodaux.append(rhs)
        prod[key] = prodaux

    lowercase1 = []
    for i in prod.values():
        for j in i:
            for k in j:
                if k.islower():
                    lowercase1.append(k)

    lowercase2 = get_unique_numbers(lowercase1)
    t = lowercase2
    s = v[0]
    return v,t,prod,s

def pegar_delta(v,t,p,s):
    delta = {}
    delt1 = []
    delt2 = []
    for j in t:
        delt1.append((j, "epsilon", j, "q0"))
    delt1.append(("epsilon", "epsilon", "epsilon", "q1"))
    delta["q0"] = delt1

    for i in t:
        delt2.append((i,i,"epsilon","q1"))

    delt2.append(("?", "?", "epsilon", "qf"))
    delta["q1"] = delt2

    print(delta)
    return delta


if __name__ == "__main__":
    pp = pprint.PrettyPrinter()
    ### Example 1
    print("Exemplo 1")
    v_0 = ["A", "S"]
    t = ["a", "b"]
    p_0 = {"S": [["A", "A"], ["a"]], "A": [["S", "S"], ["b"]]}
    s = "S"
    var = mk_example(1, v_0, p_0)
    v,t,p,s=pegar_saída(var)
    Sigma = t
    Q = {"q0","q1","qf"}
    q0 = "q0"
    F = {"qf"}
    delta = pegar_delta(v,t,p,s)
    V = t
    w = "abba"
    pp.pprint(lifted_delta_clos([(w, "q0", [])], delta))


    ### Example 2
    print("Exemplo 2")
    v1 = ["A", "B", "C"]
    t1 = ["a", "b"]
    p1 = {"A": [["B", "C"]], "B": [["C", "A"], ["b"]], "C": [["A", "B"], ["a"]]}
    s1 = "A"
    var = mk_example(2, v1, p1)
    v, t, p, s = pegar_saída(var)
    Sigma = t
    Q = {"q0", "q1", "qf"}
    q0 = "q0"
    F = {"qf"}
    delta = pegar_delta(v, t, p, s)
    V = t
    w = "aabb"
    pp.pprint(lifted_delta_clos([(w, "q0", [])], delta))