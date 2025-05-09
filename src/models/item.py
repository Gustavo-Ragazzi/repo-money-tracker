from enum import Enum
from dataclasses import dataclass
from typing import Dict


class Item(Enum):
    BASEBALL_BAT = "Baseball Bat"
    BOLTZAP = "Boltzap"
    CART = "C.A.R.T."
    DUCK_BUCKET = "Duck Bucket"
    DUCT_TAPED_GRENADE = "Duct Taped Grenade"
    ENERGY_CRYSTAL = "Energy Crystal"
    EXPLOSIVE_MINE = "Explosive Mine"
    EXTRA_JUMP_UPGRADE = "Extra Jump Upgrade"
    EXTRACTION_TRACKER = "Extraction Tracker"
    FEATHER_DRONE = "Feather Drone"
    FRYING_PAN = "Frying Pan"
    GRENADE = "Grenade"
    GUN = "Gun"
    HEALTH_UPGRADE = "Health Upgrade"
    HUMAN_GRENADE = "Human Grenade"
    INDESTRUCTIBLE_DRONE = "Indestructible Drone"
    INFLATABLE_HAMMER = "Inflatable Hammer"
    LARGE_HEALTH_PACK = "Large Health Pack"
    MAP_PLAYER_COUNT_UPGRADE = "Map Player Count Upgrade"
    MEDIUM_HEALTH_PACK = "Medium Health Pack"
    POCKET_CART = "Pocket C.A.R.T."
    PRODZAP = "Prodzap"
    PULSE_PISTOL = "Pulse Pistol"
    RANGE_UPGRADE = "Range Upgrade"
    RECHARGE_DRONE = "Recharge Drone"
    ROLL_DRONE = "Roll Drone"
    RUBBER_DUCK = "Rubber Duck"
    SHOTGUN = "Shotgun"
    SHOCK_GRENADE = "Shock Grenade"
    SHOCKWAVE_MINE = "Shockwave Mine"
    SLEDGE_HAMMER = "Sledge Hammer"
    SMALL_HEALTH_PACK = "Small Health Pack"
    SPRINT_SPEED_UPGRADE = "Sprint Speed Upgrade"
    STAMINA_UPGRADE = "Stamina Upgrade"
    STRENGTH_UPGRADE = "Strength Upgrade"
    STUN_GRENADE = "Stun Grenade"
    STUN_MINE = "Stun Mine"
    SWORD = "Sword"
    TRANQ_GUN = "Tranq Gun"
    TUMBLE_LAUNCH_UPGRADE = "Tumble Launch Upgrade"
    VALUABLE_TRACKER = "Valuable Tracker"
    ZERO_GRAVITY_DRONE = "Zero Gravity Drone"
    ZERO_GRAVITY_ORB = "Zero Gravity Orb"


class Category(Enum):
    MELEE = "Melee"
    RANGED = "Ranged"
    EXPLOSIVE = "Explosive"
    UTILITY = "Utility"
    DRONE = "Drone"
    HEALTH = "Health"
    UPGRADE = "Upgrade"
    TRACKER = "Tracker"


@dataclass
class ItemMetadata:
    category: Category


ItemMetadataMap = Dict[Item, ItemMetadata]

ITEM_METADATA: ItemMetadataMap = {
    Item.BASEBALL_BAT: ItemMetadata(Category.MELEE),
    Item.BOLTZAP: ItemMetadata(Category.RANGED),
    Item.CART: ItemMetadata(Category.UTILITY),
    Item.DUCK_BUCKET: ItemMetadata(Category.UTILITY),
    Item.DUCT_TAPED_GRENADE: ItemMetadata(Category.EXPLOSIVE),
    Item.ENERGY_CRYSTAL: ItemMetadata(Category.UTILITY),
    Item.EXPLOSIVE_MINE: ItemMetadata(Category.EXPLOSIVE),
    Item.EXTRA_JUMP_UPGRADE: ItemMetadata(Category.UPGRADE),
    Item.EXTRACTION_TRACKER: ItemMetadata(Category.TRACKER),
    Item.FEATHER_DRONE: ItemMetadata(Category.DRONE),
    Item.FRYING_PAN: ItemMetadata(Category.MELEE),
    Item.GRENADE: ItemMetadata(Category.EXPLOSIVE),
    Item.GUN: ItemMetadata(Category.RANGED),
    Item.HEALTH_UPGRADE: ItemMetadata(Category.UPGRADE),
    Item.HUMAN_GRENADE: ItemMetadata(Category.EXPLOSIVE),
    Item.INDESTRUCTIBLE_DRONE: ItemMetadata(Category.DRONE),
    Item.INFLATABLE_HAMMER: ItemMetadata(Category.MELEE),
    Item.LARGE_HEALTH_PACK: ItemMetadata(Category.HEALTH),
    Item.MAP_PLAYER_COUNT_UPGRADE: ItemMetadata(Category.UPGRADE),
    Item.MEDIUM_HEALTH_PACK: ItemMetadata(Category.HEALTH),
    Item.POCKET_CART: ItemMetadata(Category.UTILITY),
    Item.PRODZAP: ItemMetadata(Category.RANGED),
    Item.PULSE_PISTOL: ItemMetadata(Category.RANGED),
    Item.RANGE_UPGRADE: ItemMetadata(Category.UPGRADE),
    Item.RECHARGE_DRONE: ItemMetadata(Category.DRONE),
    Item.ROLL_DRONE: ItemMetadata(Category.DRONE),
    Item.RUBBER_DUCK: ItemMetadata(Category.UTILITY),
    Item.SHOTGUN: ItemMetadata(Category.RANGED),
    Item.SHOCK_GRENADE: ItemMetadata(Category.EXPLOSIVE),
    Item.SHOCKWAVE_MINE: ItemMetadata(Category.EXPLOSIVE),
    Item.SLEDGE_HAMMER: ItemMetadata(Category.MELEE),
    Item.SMALL_HEALTH_PACK: ItemMetadata(Category.HEALTH),
    Item.SPRINT_SPEED_UPGRADE: ItemMetadata(Category.UPGRADE),
    Item.STAMINA_UPGRADE: ItemMetadata(Category.UPGRADE),
    Item.STRENGTH_UPGRADE: ItemMetadata(Category.UPGRADE),
    Item.STUN_GRENADE: ItemMetadata(Category.EXPLOSIVE),
    Item.STUN_MINE: ItemMetadata(Category.EXPLOSIVE),
    Item.SWORD: ItemMetadata(Category.MELEE),
    Item.TRANQ_GUN: ItemMetadata(Category.RANGED),
    Item.TUMBLE_LAUNCH_UPGRADE: ItemMetadata(Category.UPGRADE),
    Item.VALUABLE_TRACKER: ItemMetadata(Category.TRACKER),
    Item.ZERO_GRAVITY_DRONE: ItemMetadata(Category.DRONE),
    Item.ZERO_GRAVITY_ORB: ItemMetadata(Category.UTILITY),
}
