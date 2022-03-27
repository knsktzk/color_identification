from opentrons import protocol_api
import numpy as np

metadata = {
	'protocolName': 'My Protocol',
	'author': 'Kensuke Tozuka <knsktzkml@gmail.com>',
	'apiLevel': '2.0'
}

def run(protocol: protocol_api.ProtocolContext):
    
    # Labware
    tiprack   = protocol.load_labware('opentrons_96_tiprack_300ul', '1')
    container = protocol.load_labware('corning_6_wellplate_16.8ml_flat', '2')
    plate     = protocol.load_labware('corning_96_wellplate_360ul_flat', '3')
    pipetto   = protocol.load_instrument('p300_single_gen2', 'left', tip_racks=[tiprack])

    x_ls = range(1, 13)
    y_ls = "ABCDEFGH"

    well_ls = []
    for y in y_ls:
        for x in x_ls:
            well_ls.append("{}{}".format(y,x))

    split_well_ls = list(np.array_split(well_ls, 16))

    def dispence(pool, wells, mix_flag=False):

        pipetto.aspirate( 240, container[pool])

        for well in wells:
            pipetto.dispense( 40, plate[well])

        if mix_flag:
            for well in reversed(wells):
                pipetto.mix(1, 100, plate[well])


    # pools
    color_1_pools = ["A1", "B1"]
    color_2_pools = ["A2", "B2",]
    color_3_pools = ["A3", "B3",]


    # --- color_1 --- #
    pipetto.pick_up_tip()

    pool_num = 0
    for well_ls in split_well_ls:

        if pool_num % 2 == 0:
            dispence(color_1_pools[0], well_ls)
            pool_num +=1
        else:
            dispence(color_1_pools[1], well_ls)
            pool_num +=1

    pipetto.drop_tip()

    # --- color_2 --- #
    pool_num = 0
    for well_ls in split_well_ls:

        if pool_num % 2 == 0:
            pipetto.pick_up_tip()
            dispence(color_2_pools[0], well_ls)
            pipetto.drop_tip()

            pool_num +=1
        else:
            pipetto.pick_up_tip()
            dispence(color_2_pools[1], well_ls)
            pipetto.drop_tip()

            pool_num +=1

    # --- color_3 --- #
    pool_num = 0
    for well_ls in split_well_ls:

        if pool_num % 2 == 0:
            pipetto.pick_up_tip()
            dispence(color_3_pools[0], well_ls, True)
            pipetto.drop_tip()

            pool_num +=1
        else:
            pipetto.pick_up_tip()
            dispence(color_3_pools[1], well_ls, True)
            pipetto.drop_tip()

            pool_num +=1

