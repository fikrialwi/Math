def intKubik(x,data):
    return data[0][1]*(x-data[1][0])*(x-data[2][0])*(x-data[3][0])/((data[0][0]-data[1][0])*(data[0][0]-data[2][0])*(data[0][0]-data[3][0]))\
        +data[1][1]*(x-data[0][0])*(x-data[2][0])*(x-data[3][0])/((data[1][0]-data[0][0])*(data[1][0]-data[2][0])*(data[1][0]-data[3][0]))\
            +data[2][1]*(x-data[1][0])*(x-data[0][0])*(x-data[3][0])/((data[2][0]-data[1][0])*(data[2][0]-data[0][0])*(data[2][0]-data[3][0]))\
                +data[3][1]*(x-data[1][0])*(x-data[0][0])*(x-data[2][0])/((data[3][0]-data[1][0])*(data[3][0]-data[0][0])*(data[3][0]-data[2][0]))
