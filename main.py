from SegundoTrabajo.Clases import *


usuario = user("gonzalo","zeiss",'123456','nog.gonzalo@gmail.com','2944783009', 0)
vendedor = seller("gonzalo","zeiss",'123456','nog.gonzalo@gmail.com','2944783009', 1)

it = item('nintendo64','consola','30.000', 1, 0)

usuario.addFavorite(0)
print(usuario.favorites)
usuario.displayCompleteInformation()
print(usuario)


vendedor.newSold()
vendedor.newSold()

print(vendedor.getSold())

vendedor.newItem(0)

print(vendedor.getItemList())

print(vendedor.reputation)

vendedor.reputationChange(-10)

print(vendedor.reputation)