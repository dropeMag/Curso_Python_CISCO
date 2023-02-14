class Veiculo:
    pass


class VeiculoTerra(Veiculo):
    pass


class VeiculoComRodas(VeiculoTerra):
    pass


for cls1 in [Veiculo, VeiculoTerra, VeiculoComRodas]:
    for cls2 in [Veiculo, VeiculoTerra, VeiculoComRodas]:
        print(issubclass(cls1, cls2), end="\t")
    print()
