
healer_links = (
    'https://www.wowhead.com/classic/guide/wow-classic-druid-healer-molten-core-phase-2-best-in-slot-gear',
    'https://www.wowhead.com/classic/guide/wow-classic-paladin-healer-molten-core-phase-2-best-in-slot-gear',
    'https://www.wowhead.com/classic/guide/wow-classic-priest-healing-molten-core-phase-2-best-in-slot-gear',
    'https://www.wowhead.com/classic/guide/wow-classic-shaman-healer-molten-core-phase-2-best-in-slot-gear'
)

dps_links = (
    'https://www.wowhead.com/classic/guide/wow-classic-balance-druid-dps-molten-core-phase-2-best-in-slot-gear',
    'https://www.wowhead.com/classic/guide/wow-classic-feral-druid-dps-molten-core-phase-2-best-in-slot-gear',
    'https://www.wowhead.com/classic/guide/wow-classic-hunter-dps-molten-core-phase-2-best-in-slot-gear',
    'https://www.wowhead.com/classic/guide/wow-classic-mage-dps-molten-core-phase-2-best-in-slot-gear',
    'https://www.wowhead.com/classic/guide/wow-classic-paladin-dps-molten-core-phase-2-best-in-slot-gear',
    'https://www.wowhead.com/classic/guide/wow-classic-shadow-priest-dps-molten-core-phase-2-best-in-slot-gear',
    'https://www.wowhead.com/classic/guide/wow-classic-rogue-dps-molten-core-phase-2-best-in-slot-gear',
    'https://www.wowhead.com/classic/guide/wow-classic-elemental-shaman-dps-molten-core-phase-2-best-in-slot-gear',
    'https://www.wowhead.com/classic/guide/wow-classic-enhancement-shaman-dps-molten-core-phase-2-best-in-slot-gear',
    'https://www.wowhead.com/classic/guide/wow-classic-warlock-dps-molten-core-phase-2-best-in-slot-gear',
    'https://www.wowhead.com/classic/guide/wow-classic-warrior-dps-molten-core-phase-2-best-in-slot-gear'
)

tank_links = (
    'https://www.wowhead.com/classic/guide/wow-classic-druid-tank-molten-core-phase-2-best-in-slot-gear',
    'https://www.wowhead.com/classic/guide/wow-classic-paladin-tank-molten-core-phase-2-best-in-slot-gear',
    'https://www.wowhead.com/classic/guide/wow-classic-warrior-tank-molten-core-phase-2-best-in-slot-gear'
)


all_links = [healer_links, dps_links, tank_links]

def get_link():
    return healer_links[0] # For now, im focusing on shamans healer.



# def export_all_links():
#     for role_links in all_links:
#         for link in role_links:
#             print(link)


# export_all_links()
