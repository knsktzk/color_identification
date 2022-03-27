from opentrons import protocol_api

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

    ls = iter(well_ls)
    pair_ls = []
    for i, j in zip(ls, ls):
        pair_ls.append([i, j])


    def func(pool, pair_ls):

        pipetto.pick_up_tip()

        for p in pair_ls:

            pipetto.aspirate( 240, container[pool])
            pipetto.dispense( 120, plate[p[0]])
            pipetto.dispense( 120, plate[p[1]])

        pipetto.drop_tip()

    
    # container well places
    # pools = ["A1", "B1"] # red
    # pools = ["A2", "B2", "A2"] # green
    pools = ["A3", "B3", "A3"] # blue
    
    start = 0
    end   = 16
    for pool in pools:
        func(pool, pair_ls[start:end])

        start = end
        end += 16
