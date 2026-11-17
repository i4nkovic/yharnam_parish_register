# README
- program vygeneruje náhodnú csv "databázu" 20 ludi s atribútmi:
  - meno
  - vek
  - výška
  - adresa

- meno výstupného súboru: **obyvatelstvo.txt**

- vytvoríme si python virtual env a naištalujeme package

```bash
python -m venv <nas_lubovolny_nazov_virtual_env>
source <nas_vybrany_nazov_virtual_env>/bin/activate
pip install Faker
pip install dataclass-csv2
```

# TODO
- filtrovanie podľa rôznych parametrov
