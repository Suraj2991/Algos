def tower(no_discs, frompeg, topeg, auxpeg):
    #print(no_discs)
    if(no_discs == 1):
        print("Move disk 1 from peg ", frompeg, " to peg ", topeg)
        return
    #print('done1')
    tower(no_discs - 1, frompeg, auxpeg, topeg)
    #print(no_discs)
    print("Move disk ", str(no_discs), " from peg ", frompeg, " to peg ", topeg)
    #print('done2')
    tower(no_discs - 1, auxpeg, topeg, frompeg)
def main():
    no_disc = int(input('Enter the number of Discs'))
    print('We want to move ', str(no_disc), ' discs from Peg A to Peg C via Peg B')
    tower(no_disc, 'A', 'C', 'B')