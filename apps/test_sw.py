from rw_emb_comp_funcs import RWEmbCompFuncs as RW

rw = RW()

while True:
    print(f"\n- read switches: {rw.read_switches()}\n- read buttons: {rw.read_button()}")
