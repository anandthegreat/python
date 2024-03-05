"""
*args allows you to pass a varying no of positional arguments
Gives us an iterable tuple object - tuples are immutable
* is an unpacking operator that can be used on any iterable

**kwargs allows you to pass a varying no of keyword arguments
Gives us an iterable dictionary object
** is an unpacking operator that can be used on dictionaries
"""

def concatenate(*args,**kwargs):
    res = ""
    for word in kwargs.values():
        res += word
        res += " "
    return res

if __name__ == "__main__":
    # Jai Ho Bajrangbali
    print(concatenate(x='Jai',y="Ho",z="Bajrangbali"))

    naam_list = ["Ram","Radha","Shiv","Krishna"]
    ram_naam = "RamRamRamRam...."

    # * operator unpacks the list and prints its elements

    # Ram Radha Shiv Krishna
    print(*naam_list)

    # R a m R a m R a m R a m . . . .
    print(*ram_naam)

    val_dict1 = {"Ram": "Perfection", "Hanuman": "Bal Buddhi", "Mata": "Creator Nurterer"}
    val_dict2 = {"Shiv": "Protector", "Narayan": "Supreme"}

    val_dict = {**val_dict1, **val_dict2}
    print(val_dict)