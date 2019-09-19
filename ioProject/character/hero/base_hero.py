
class BaseHero:
    name = None
    _name_ = None
    _level_ = 0
    _vitality_ = 0
    _speed_ = 0
    _magic_power_ = 0
    _physical_power_ = 0
    _magic_defensive_power_ = 0
    _physical_defensive_power_ = 0
    _race_ = None   # 种族
    _describe_ = None
    _rank_ = None

    def __init__(self, **kwargs):
        self._name_ = kwargs.get("name")
        self._level_ = kwargs.get("level")
        self._vitality_ = kwargs.get("vitality")
        self._speed_ = kwargs.get("speed")
        self._magic_power_ = kwargs.get("magic_power")
        self._physical_power_ = kwargs.get("physical_power")
        self._magic_defensive_power_ = kwargs.get("magic_defensive_power")
        self._physical_defensive_power_ = kwargs.get("physical_defensive_power")
        self._race_ = kwargs.get("race")
        # race = {
        #     "protoss": "普罗托斯 神族",
        #     "theImmortal": "仙族",
        #     "demon": "妖",
        #     "terran": "人",
        # }

    def __get_attributes__(self):
        attributes = {
            "name": self._name_,
            "level": self._level_,
            "vitality": self._vitality_,
            "speed": self._speed_,
            "magic_power": self._magic_power_,
            "physical_power": self._physical_power_,
            "magic_defensive_power": self._magic_defensive_power_,
            "physical_defensive_power": self._physical_defensive_power_,
            "race": self._race_,
            "describe": self._describe_,
        }
        return attributes

    def __get_describe__(self):
        return self._describe_

    def __set_describe__(self, describe):
        self._describe_ = describe


my_hero = BaseHero(name="althna", level=15)
option = my_hero.__get_attributes__()
for elem in option.items():
    print(elem)
