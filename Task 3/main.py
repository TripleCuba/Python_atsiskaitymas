# Turimas "audi" dict.

# Parašykite funkciją "show_object_values", kuri kaip argumentą priims objektą
# ir grąžins visus jo "values" list'e.

audi = {
  "make": 'audi',
  "model": 'A6',
  "year": 2005,
  "color": 'white',
}

def show_object_values(dict):
  my_vals = dict.values()
  new_list = []
  for val in my_vals:
    new_list.append(val)
  print(new_list)
  return new_list

show_object_values(audi)

