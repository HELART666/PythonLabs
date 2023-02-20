
class Transport:
    def __init__(self, name: str, wheels_count: int, season: str, is_need_to_permission: bool):
        self.name = name,
        self.wheels_count = wheels_count,
        self.season = season,
        self.is_need_to_permission = is_need_to_permission

    def ride(self):
        print("Transport is ride")

    def ride(self, destination: str):
        print("Transport is ride to" f"{destination}")




