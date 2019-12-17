import math
import copy

speed_base  = 3

def update_speed(moon_list):
    for item in moon_list:
        for comp in moon_list:
            if(comp == item):
                continue
            else:
                for i in range(3):
                    if(comp[i] > item[i]):
                        item[speed_base+i] += 1
                    elif(comp[i] < item[i]):
                        item[speed_base+i] -= 1
                    else:
                        pass

def update_loc(moon_list):
    for item in moon_list:
        for i in range(3):
            item[i] += item[speed_base+i]
    

def get_energy(moon_list):
    static_energy = 0
    kinetic_energy = 0
    energy = []
    total_en = 0
    for item in moon_list:
        static_energy = 0
        kinetic_energy = 0
        for i in range(3):
            static_energy += abs(item[i])
            kinetic_energy += abs(item[speed_base+i])
        energy.append(static_energy*kinetic_energy)
    #print(energy)
    for en in energy:
        total_en += en
    return total_en

if __name__ == "__main__":
    f = open("input.txt", "r")
    moons = []
    for line in f.readlines():
        moon = []
        tmp = line.strip('<').strip('\n').strip('>').split(', ')
        for tmp_val in tmp:
            moon.append(int(tmp_val[2:]))
        moon.extend([0,0,0])
        moons.append(moon)
    
    '''
    moons_rec = copy.deepcopy(moons)
    iteration  = 1
    update_speed(moons)
    update_loc(moons)

    while(moons != moons_rec):
        update_speed(moons)
        update_loc(moons)
        iteration += 1
    
    print(iteration)
    '''
    for iter in range(1000):
        print(moons)
        print('\n')
        update_speed(moons)
        update_loc(moons)
    
    total_en = get_energy(moons)

    print(total_en)
    
    f.close()
    

    

    
    