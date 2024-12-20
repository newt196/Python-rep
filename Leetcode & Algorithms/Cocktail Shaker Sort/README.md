A little lesson for a thing called the cocktail sort.

This is based off of the bubble sort, but it sorts from both directions here. When looking
at the visualization, we see that two indexes are selected and swapped to sort the elements and this is 
done until the left>right. Once the end is reached we go from left to right to right to left and its sorted from right to left. 

I am thinking if that the case, what the point of bubble sort. 

From https://www.geeksforgeeks.org/python-program-for-cocktail-sort/

The code example is 

    def cocktailSort(a):
        n = len(a)
        swapped = True
        start = 0
        end = n-1
        while (swapped==True):
 
        # reset the swapped flag on entering the loop,
        # because it might be true from a previous
        # iteration.
        swapped = False
 
        # loop from left to right same as the bubble
        # sort
        for i in range (start, end):
            if (a[i] > a[i+1]) :
                a[i], a[i+1]= a[i+1], a[i]
                swapped=True
 
        # if nothing moved, then array is sorted.
        if (swapped==False):
            break
 
        # otherwise, reset the swapped flag so that it
        # can be used in the next stage
        swapped = False
 
        # move the end point back by one, because
        # item at the end is in its rightful spot
        end = end-1
 
        # from right to left, doing the same
        # comparison as in the previous stage
        for i in range(end-1, start-1,-1):
            if (a[i] > a[i+1]):
                a[i], a[i+1] = a[i+1], a[i]
                swapped = True
 
        # increase the starting point, because
        # the last stage would have moved the next
        # smallest number to its rightful spot.
        start = start+1
 
# Driver code to test above
a = [5, 1, 4, 2, 8, 0, 2]
cocktailSort(a)
print("Sorted array is:")
for i in range(len(a)):
    print ("%d" %a[i]),

Will try to explain "every" or main points the program takes uses to sort "a". To be fair, there are 110 steps provided.

Breakdown goes as follows:

Global frame 
cocktail Sort	---->     coctailSort(a)
a  -------> [5,1,4,2,8,0,2]


cocktailSort(a)  -----> 5
n -----> 7 (remember n=len(a)
swapped == True
start == 0
end == 6 (remember n-1)

swapped == False (? Unsure why we set to False after just setting it to True)


for i in range (start, end):   
i == 0 
a[i], a[i+1]= a[i+1], a[i]
[5,1]----->   [1,5]

Second iteration 
i == 1 
if (a[1] > a[1+1]) :
is run with 
a[i], a[i+1]= a[i+1], a[i] (main engine to swap the two indexes)
[5,4] -----> [4,5]

This is done until the array loops through and the swapped flag finished with false and then breaks. 

Reviewed in https://pythontutor.com/render.html#code=def%20cocktailSort%28a%29%3A%0A%20%20%20%20n%20%3D%20len%28a%29%0A%20%20%20%20swapped%20%3D%20True%0A%20%20%20%20start%20%3D%200%0A%20%20%20%20end%20%3D%20n-1%0A%20%20%20%20while%20%28swapped%3D%3DTrue%29%3A%0A%20%0A%20%20%20%20%20%20%20%20%23%20reset%20the%20swapped%20flag%20on%20entering%20the%20loop,%0A%20%20%20%20%20%20%20%20%23%20because%20it%20might%20be%20true%20from%20a%20previous%0A%20%20%20%20%20%20%20%20%23%20iteration.%0A%20%20%20%20%20%20%20%20swapped%20%3D%20False%0A%20%0A%20%20%20%20%20%20%20%20%23%20loop%20from%20left%20to%20right%20same%20as%20the%20bubble%0A%20%20%20%20%20%20%20%20%23%20sort%0A%20%20%20%20%20%20%20%20for%20i%20in%20range%20%28start,%20end%29%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20if%20%28a%5Bi%5D%20%3E%20a%5Bi%2B1%5D%29%20%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20a%5Bi%5D,%20a%5Bi%2B1%5D%3D%20a%5Bi%2B1%5D,%20a%5Bi%5D%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20swapped%3DTrue%0A%20%0A%20%20%20%20%20%20%20%20%23%20if%20nothing%20moved,%20then%20array%20is%20sorted.%0A%20%20%20%20%20%20%20%20if%20%28swapped%3D%3DFalse%29%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20break%0A%20%0A%20%20%20%20%20%20%20%20%23%20otherwise,%20reset%20the%20swapped%20flag%20so%20that%20it%0A%20%20%20%20%20%20%20%20%23%20can%20be%20used%20in%20the%20next%20stage%0A%20%20%20%20%20%20%20%20swapped%20%3D%20False%0A%20%0A%20%20%20%20%20%20%20%20%23%20move%20the%20end%20point%20back%20by%20one,%20because%0A%20%20%20%20%20%20%20%20%23%20item%20at%20the%20end%20is%20in%20its%20rightful%20spot%0A%20%20%20%20%20%20%20%20end%20%3D%20end-1%0A%20%0A%20%20%20%20%20%20%20%20%23%20from%20right%20to%20left,%20doing%20the%20same%0A%20%20%20%20%20%20%20%20%23%20comparison%20as%20in%20the%20previous%20stage%0A%20%20%20%20%20%20%20%20for%20i%20in%20range%28end-1,%20start-1,-1%29%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20if%20%28a%5Bi%5D%20%3E%20a%5Bi%2B1%5D%29%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20a%5Bi%5D,%20a%5Bi%2B1%5D%20%3D%20a%5Bi%2B1%5D,%20a%5Bi%5D%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20swapped%20%3D%20True%0A%20%0A%20%20%20%20%20%20%20%20%23%20increase%20the%20starting%20point,%20because%0A%20%20%20%20%20%20%20%20%23%20the%20last%20stage%20would%20have%20moved%20the%20next%0A%20%20%20%20%20%20%20%20%23%20smallest%20number%20to%20its%20rightful%20spot.%0A%20%20%20%20%20%20%20%20start%20%3D%20start%2B1%0A%20%0A%23%20Driver%20code%20to%20test%20above%0Aa%20%3D%20%5B5,%201,%204,%202,%208,%200,%202%5D%0AcocktailSort%28a%29%0Aprint%28%22Sorted%20array%20is%3A%22%29%0Afor%20i%20in%20range%28len%28a%29%29%3A%0A%20%20%20%20print%20%28%22%25d%22%20%25a%5Bi%5D%29,&cumulative=false&curInstr=87&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=311&rawInputLstJSON=%5B%5D&textReferences=false










