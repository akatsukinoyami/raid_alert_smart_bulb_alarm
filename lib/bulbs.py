from os import getenv as env
from json import loads
from time import sleep
from typing import Dict, Tuple

from tinytuya import BulbDevice


class Bulbs():
    def __init__(self):
        print("Start devices initialization")

        self.bulbs_creds = loads(env("TUYA_BULBS"))
        self.bulbs = {
            dev_id: self.initialize_bulb(dev_id, local_key)
            for dev_id, local_key in self.bulbs_creds
        }
        self.state = {}

        print("Initialized all devices")

    @staticmethod
    def initialize_bulb(dev_id, local_key):
        bulb = BulbDevice(dev_id=dev_id, address="Auto", local_key=local_key)
        print(f"Initialized bulb {dev_id}")
        return bulb

    def set_brightness(self, brightness: int):
        for bulb in self.bulbs.values():
            bulb.set_brightness(brightness)

    def set_colour(self, *colour) -> None:
        for bulb in self.bulbs.values():
            bulb.set_colour(*colour)

    def turn_on(self) -> None:
        for bulb in self.bulbs.values():
            bulb.turn_on()

    def turn_off(self) -> None:
        for bulb in self.bulbs.values():
            bulb.turn_off()

    def flash(
            self,
            times: int,
            sleep_time: int | float,
            colour: Tuple[int, int, int]
            ) -> None:
        self.save_previous_state()

        self.set_brightness(1000)
        self.set_colour(*colour)

        for _ in range(times):
            self.turn_on()
            sleep(sleep_time)
            self.turn_off()
            sleep(sleep_time)

        self.restore_previous_state()

    def save_previous_state(self) -> Dict[str, Dict[str, str]]:
        self.state = {
            bulb_id: {
                **bulb.state(),
                "colour": bulb.colour_rgb()
            }
            for bulb_id, bulb in self.bulbs.items()
        }

    def restore_previous_state(self) -> None:
        for bulb_id, bulb in self.bulbs.items():
            bulb_state = self.state[bulb_id]
            bulb.set_mode(mode=bulb_state["mode"])

            if bulb_state['is_on']:
                match bulb_state["mode"]:
                    case "colour":
                        bulb.set_colour(bulb_state["colour"])
                    case "white":
                        bulb.set_white()
            else:
                bulb.turn_off()
