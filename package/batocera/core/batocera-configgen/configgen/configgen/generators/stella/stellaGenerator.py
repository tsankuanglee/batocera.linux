from __future__ import annotations

import logging
from typing import TYPE_CHECKING

from ... import Command
from ...controller import generate_sdl_game_controller_config
from ..Generator import Generator

if TYPE_CHECKING:
    from configgen.types import HotkeysContext

eslog = logging.getLogger(__name__)

class StellaGenerator(Generator):

    def getHotkeysContext(self) -> HotkeysContext:
        return {
            "name": "stella",
            "keys": { "exit": ["KEY_LEFTALT", "KEY_F4"] }
        }

    def generate(self, system, rom, playersControllers, metadata, guns, wheels, gameResolution):
        # Launch Stella
        commandArray = ["stella " , rom ]

        return Command.Command(
            array=commandArray,
            env={
                'SDL_GAMECONTROLLERCONFIG': generate_sdl_game_controller_config(playersControllers)
            }
        )
