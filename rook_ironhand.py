rook_ironhand = {
    # Basic character info
    "basic_info": {
        "name": "Rook Ironhand",
        "class": "Artificer",
        "level": 4,
        "race": "Custom Lineage",
        "hp": 34,
        "ac": 15,
        "initiative": 0,
        "proficiency_bonus": 2,
        "speed": "30 ft",
        "hit_dice": "4d8",
    },

    # Ability scores with modifiers
    "ability_scores": {
        "Strength": {"score": 13, "modifier": 1},
        "Dexterity": {"score": 10, "modifier": 0},
        "Constitution": {"score": 16, "modifier": 3},
        "Intelligence": {"score": 18, "modifier": 4},
        "Wisdom": {"score": 10, "modifier": 0},
        "Charisma": {"score": 10, "modifier": 0},
    },

    # Saving throws with proficiency
    "saving_throws": {
        "Strength": {"modifier": 1, "proficient": False},
        "Dexterity": {"modifier": 0, "proficient": False},
        "Constitution": {"modifier": 5, "proficient": True},
        "Intelligence": {"modifier": 6, "proficient": True},
        "Wisdom": {"modifier": 0, "proficient": False},
        "Charisma": {"modifier": 0, "proficient": False},
    },

    # Skills with proficiency and expertise
    "skills": {
        "Acrobatics": {"modifier": 0, "proficient": False, "expertise": False},
        "Animal Handling": {"modifier": 0, "proficient": False, "expertise": False},
        "Arcana": {"modifier": 4, "proficient": False, "expertise": False},
        "Athletics": {"modifier": 3, "proficient": True, "expertise": False},
        "Deception": {"modifier": 0, "proficient": False, "expertise": False},
        "History": {"modifier": 4, "proficient": False, "expertise": False},
        "Insight": {"modifier": 2, "proficient": True, "expertise": False},
        "Intimidation": {"modifier": 0, "proficient": False, "expertise": False},
        "Investigation": {"modifier": 8, "proficient": True, "expertise": True},
        "Medicine": {"modifier": 0, "proficient": False, "expertise": False},
        "Nature": {"modifier": 4, "proficient": False, "expertise": False},
        "Perception": {"modifier": 2, "proficient": True, "expertise": False},
        "Performance": {"modifier": 0, "proficient": False, "expertise": False},
        "Persuasion": {"modifier": 2, "proficient": True, "expertise": False},
        "Religion": {"modifier": 4, "proficient": False, "expertise": False},
        "Sleight of Hand": {"modifier": 0, "proficient": False, "expertise": False},
        "Stealth": {"modifier": 0, "proficient": False, "expertise": False},
        "Survival": {"modifier": 0, "proficient": False, "expertise": False},
    },

    # Tool proficiencies
    "tool_proficiencies": [
        "Thieves' Tools",
        "Tinker’s Tools",
        "Carpenter’s Tools",
        "Weaver’s Tools",
        "Smith’s Tools",
    ],

    # Languages known
    "languages": ["Common", "Giant", "Gnomish"],

    # Attacks and cantrips
    "attacks": {
        "Thunder Gauntlets": {
            "to_hit": 6,
            "damage": "1d8 + 4 thunder",
            "special": "Creatures hit have disadvantage on attacks against targets other than you until your next turn",
        },
        "Fire Bolt": {
            "to_hit": 6,
            "damage": "1d10 fire",
            "range": "120 ft",
        },
    },

    # Spellcasting details
    "spellcasting": {
        "spell_save_dc": 13,
        "spells_known": [
            "Absorb Elements",
            "Cure Wounds",
            "Expeditious Retreat",
            "Faerie Fire",
            "Feather Fall",
            "Grease",
        ],
        "cantrips_known": ["Fire Bolt", "Mending"],
        "spell_slots": {"1st_level": 3},
        "bonus_spells": ["Thunderwave", "Magic Missile"],
    },

    # Infusions with current status
    "infusions": {
        "known": [
            "Enhanced Defense",
            "Wand of Secrets",
            "Homunculus Servant",
            "Sending Stones",
        ],
        "active": ["Enhanced Defense", "Wand of Secrets"],
        "inactive": ["Homunculus Servant", "Sending Stones"],
    },

    # Class features and descriptions
    "features": {
        "Magical Tinkering": (
            "Imbue a Tiny nonmagical object with minor magical properties such as "
            "shedding light, emitting sounds or odors, or displaying images."
        ),
        "Arcane Armor (Guardian Model)": {
            "armor_lacks_strength_requirement": True,
            "acts_as_spellcasting_focus": True,
            "attach_and_doff": "Armor attaches and can be donned/doffed as an action",
            "thunder_gauntlets": "Melee weapons using Intelligence modifier",
            "defensive_field": "Bonus action to gain temporary HP equal to class level; usable twice per long rest",
        },
    },
}
