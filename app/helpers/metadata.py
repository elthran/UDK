class Buildings:
    Human = {
        "House": {"Singular": "Homestead",
                  "Plural": "Homesteads",
                  "Gold": 65,
                  "Wood": 20,
                  "Stone": 0,
                  "Output": 5,
                  "Description": "Each percent of land increases your birth rate by {0}%."},
        "Field": {"Singular": "Wheat Field",
                  "Plural": "Wheat Fields",
                  "Gold": 50,
                  "Wood": 10,
                  "Stone": 0,
                  "Output": 40,
                  "Description": "Provides enough grain to feed {0} people a day."},
        "Pasture": {"Singular": "Dairy Farm",
                    "Plural": "Dairy Farm",
                    "Gold": 75,
                    "Wood": 20,
                    "Stone": 0,
                    "Output": 60,
                    "Description": "Produces enough food to feed {0} people a day, but excess dairy is lost each day."},
    }
    Elf = {
        "House": {"Singular": "Sanctuary",
                  "Plural": "Sanctuaries",
                  "Gold": 65,
                  "Wood": 20,
                  "Stone": 0,
                  "Output": 5,
                  "Description": "Each percent of land increases your birth rate by {0}%."},
        "Field": {"Singular": "Rice Field",
                  "Plural": "Rice Fields",
                  "Gold": 50,
                  "Wood": 10,
                  "Stone": 0,
                  "Output": 40,
                  "Description": "Provides enough grain to feed {0} people a day."},
        "Pasture": {"Singular": "Dairy Pasture",
                    "Plural": "Dairy Pastures",
                    "Gold": 75,
                    "Wood": 20,
                    "Stone": 0,
                    "Output": 60,
                    "Description": "Produces enough food to feed {0} people a day, but excess dairy is lost each day."},
    }


class Units:

    UNARMOURED = "Unarmoured"
    LEATHER = "Leather"
    PLATE = "Plate"

    INFANTRY = "Infantry"
    CAVALRY = "Cavalry"
    SIEGE = "Siege"
    MONSTER = "Monster"

    Human = {
        "Peasant": {"Singular": "Man-at-arms",
                    "Plural": "Men-at-arms",
                    "Gold": 25,
                    "Wood": 5,
                    "Iron": 5,
                    "Upkeep": 5,
                    "Attack": 1,
                    "Defence": 1,
                    "Health": 1,
                    "Category": INFANTRY,
                    "Armour": UNARMOURED,
                    "Description": "Men-at-arms can be trained extremely quickly and have low upkeep."},
        "Soldier": {"Singular": "Footman",
                    "Plural": "Footmen",
                    "Gold": 50,
                    "Wood": 5,
                    "Iron": 15,
                    "Upkeep": 20,
                    "Attack": 4,
                    "Defence": 2,
                    "Health": 3,
                    "Category": INFANTRY,
                    "Armour": LEATHER,
                    "Description": "Footmen are strong attackers."},
        "Archer": {"Singular": "Musketeer",
                    "Plural": "Musketeers",
                    "Gold": 50,
                    "Wood": 5,
                    "Iron": 15,
                    "Upkeep": 20,
                    "Attack": 2,
                    "Defence": 4,
                    "Health": 3,
                    "Category": INFANTRY,
                    "Armour": UNARMOURED,
                    "Description": "Musketeers are excellent at defending."},
    }
