class Veiculo:
    pass


class VeiculoTerra(Veiculo):
    pass


class Trator(VeiculoTerra):
    pass


my_vehicle = Veiculo()
my_land_vehicle = VeiculoTerra()
my_tracked_vehicle = Trator()

for obj in [my_vehicle, my_land_vehicle, my_tracked_vehicle]:
    for cls in [Veiculo, VeiculoTerra, Trator]:
        print(isinstance(obj, cls), end="\t")
    print()
