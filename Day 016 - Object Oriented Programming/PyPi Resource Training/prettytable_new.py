import prettytable
table = prettytable.PrettyTable()
table.add_column("Pokemons", ["Pikachu", "Bulbasaur"])
table.add_column("Types", ["Electric", "Grass"])
table.align["Pokemons"] = 'l'
table.align["Pokemons"] = 'l'
print(table)
