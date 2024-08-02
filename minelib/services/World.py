from minelib.minecraft.mcfunction import mcfunction, get_current_mcf, set_current_mcf
from minelib.types.Core.Location import Location
from minelib.types.Core.EntitySpecifier import EntitySpecifier
from enum import Enum
import json

class ModifyDataOperation(Enum):
    APPEND = "append"
    INSERT = "insert"
    MERGE = "merge"
    PREPEND = "prepend"
    SET = "set"

class World:
    def __init__(self):
        pass

    def set_time_of_day(self, time: int):
        __mcf = get_current_mcf()
        __mcf.content.append(f"time set {time}t")
        set_current_mcf(__mcf)

    def set_block(self, loc: Location, block_id: str):
        __mcf = get_current_mcf()
        __mcf.content.append(f"setblock {loc.X} {loc.Y} {loc.Z} {block_id}")
        set_current_mcf(__mcf)

    def set_block_relative(self, player: EntitySpecifier, loc: Location, block_id: str):
        __mcf = get_current_mcf()
        __mcf.content.append(f"execute as {player.to_string()} at @s run setblock ~{loc.X if loc.X != 0 else ''} ~{loc.Y if loc.Y != 0 else ''} ~{loc.Z if loc.Z != 0 else ''} {block_id}")
        set_current_mcf(__mcf)

    def summon_entity(self, entity_id: str, loc: Location):
        __mcf = get_current_mcf()
        __mcf.content.append(f"summon {entity_id} {loc.to_string()}")
        set_current_mcf(__mcf)

    def summon_entity_relative(self, entity_id: str, player: str | EntitySpecifier, loc: Location):
        __mcf = get_current_mcf()
        __mcf.content.append(f"execute as {player.value if isinstance(player, EntitySpecifier) else player} at @s run summon {entity_id} ~{loc.X if loc.X != 0 else ''} ~{loc.Y if loc.Y != 0 else ''} ~{loc.Z if loc.Z != 0 else ''}")
        set_current_mcf(__mcf)
    
    def spawn_particle(self, particle_id: str, loc: Location, delta: Location, speed: int, count: int):
        __mcf = get_current_mcf()
        __mcf.content.append(f"particle {particle_id} {loc.to_string()} {delta.to_string()} {speed} {count}")
        set_current_mcf(__mcf)

    def merge_data_in_block(self, loc: Location, nbt: any):
        __mcf = get_current_mcf()
        __mcf.content.append(f"data merge block {loc.to_string()} {json.dumps(nbt)}")
        set_current_mcf(__mcf)

    #TODO: implement the entire data command