# class ControlTower:
#     __instance = None
#     def __new__(cls):
#         if cls.__instance is None:
#             cls.__instance = super().__new__(cls)
#             # cls.__instance.name= name
#             print('Control tower at work')
#         return cls.__instance
#     def checkIncomingFlight(self,flights):
#         print(f'Please hold {flights}')
# T1 = ControlTower()
# T2 = ControlTower()
#
# T1.checkIncomingFlight('TK655')
# T2.checkIncomingFlight('QR314')
#
# # print(h2.name)
# print(T1 is T2 )
class Kebab:
    def prepare(self):
        raise NotImplementedError('')
class AdanaKebab(Kebab):
    def prepare(self):
        return "please we are making your adana kebab"

class TavukKebab(Kebab):
    def prepare(self):
        return 'please hold while we make your kebab'

class MixKebab(Kebab):
    def prepare(self):
        return 'please hold for your Mixkebab'

class kebabhouse(Kebab):
    @staticmethod
    def make_kebab(kebab_type):

        if kebab_type == 'Adana':
            return AdanaKebab()
        elif  kebab_type == 'Tavuk':
            return TavukKebab()
        elif kebab_type == 'Mix':
            return MixKebab()
        else:
            raise ValueError('Please select  from the three kebab we have')

def main():
    try:
        customer_input = 'Adana'
        kebab =kebabhouse.make_kebab(customer_input)
        print(kebab.prepare())

    except ValueError as e:
        print(e)

main()