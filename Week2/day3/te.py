magicians_names = ['Harry Houdini', 'David Blaine','Criss Angel']

def show_magicioans(*args):
    for name in magicians_names:
     print(name)

show_magicioans()

def make_great(magicians_names):
 for name in magicians_names:
    print(f'the Great {name}')

make_great(magicians_names)
show_magicioans=make_great(magicians_names)