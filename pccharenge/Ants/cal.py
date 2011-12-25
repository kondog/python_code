#! /usr/bin/python

def ant_solve( L, n, x ):
        #################
        #caliculate min.
        #################
    cntr_min = 0
    all_array_min = 0

    while cntr_min < n:
        if ( L - x[cntr_min] > x[cntr_min] ):
            a_array_min = x[cntr_min]
        else:
            a_array_min = L - x[cntr_min]
        if ( all_array_min < a_array_min ):
            all_array_min = a_array_min
        cntr_min = cntr_min + 1
    print "min = "+str(all_array_min)

    #############
    #caliculate max.
    #############
    cntr_max = 0
    all_array_max = 0

    while cntr_max < n:
        if ( L - x[cntr_max] > x[cntr_max] ):
            a_array_max = L - x[cntr_max]
        else:
            a_array_max = x[cntr_max]
        if( all_array_max < a_array_max ):
            all_array_max = a_array_max
        cntr_max = cntr_max+1
    print "max = "+str(all_array_max)

                                                                                                                                                                                                                                    
