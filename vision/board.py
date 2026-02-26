
#checks position of detected , and compare if its in this cell put it .

#take from camera and seperate it into 3 colums and rows 

# use numpy.shape?, frame.shape? 

def ArrayInf (inf):

    
    # we want to take boxes from inf 

    results=inf[0].boxes

    #loop throgh results
    for x in results:
        x_min,y_min,x_max,y_max,conf,cls=x

    return x_min,y_min,x_max,y_max,conf,cls









def Get_cell_index(frame,arr): #should i write result from detector.py?
   
    h,w=frame.shape[:2]
    cell__height=h/3      # row
    cell_Width=w/3       #col


    arr=ArrayInf()

    #calc center of infered box 
    x_center=(arr.x_min+arr.x_max)/2 #
    y_center=(arr.y_min+arr.y_max)/2

    #ex : How many times does 300 fully fit inside 650?

    '''
        How many groups of this size fit inside this amount?

        And the number of full groups = the index.
    '''''

    row=int(x_center//cell_Width)
    col=int(y_center//cell__height)


    row=min(max(row,0),2)
    col=min(max(col,0),2)

    return row,col





#this works with one inferenec jow multiple ? they are stored as json

# we need to know number of detections? or no for each yea .
#store var inference 
'''
inf_arr=[]

# take inf make them separt eor into arrays .
def get_inference(Inference_res):

    for x in Inference_res:
        inf_arr[x]=Inference_res

    pr    

    return inf_arr

'''


'''
def Get_cell_index(frame): #should i write result from detector.py?
   
    h,w=frame.shape[:2]
    cell__height=h/3      # row
    cell_Width=w/3       #col



    ARRAY=get_inference()
    for x in ARRAY:
        for y in lol:

            x_center=int()
            y_center=int()

    '''



'''
    #calc center of infered box 
    x_center=(Inference_res.x_min+Inference_res.x_max)/2
    y_center=(Inference_res.y_min+Inference_res.y_max)/2
'''

    #ex : How many times does 300 fully fit inside 650?

'''\'''
        How many groups of this size fit inside this amount?

        And the number of full groups = the index.
    '''''


'''
    row=int(x_center//cell_Width)
    col=int(y_center//cell__height)


    row=min(max(row,0),2)
    col=min(max(col,0),2)

    return row,col
'''