flag_leer = 0

with open("_2021 suda 06 chile-brasil.dvw") as f:
   i = 0
   for line in f:
    i += 1
    if '[3SCOUT]' in line:
        flag_leer = 1
    if '[' in line:
        flag_leer_leer = 0
    if flag_leer == 1:
    #    print(f"{i} ->  {len(line.split(';'))}")
        print(line.split(';'))