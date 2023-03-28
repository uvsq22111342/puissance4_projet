liste1 =[((200, 500), (300, 600)), ((300, 400), (400, 500)), 
         ((500, 500), (600, 600)), ((400, 300), (500, 400)), 
         ((100, 500), (200, 600)), ((0, 300), (100, 400)), 
         ((600, 400), (700, 500)), ((500, 300), (600, 400)), 
         ((400, 200), (500, 300)), ((600, 200), (700, 300)), 
         ((200, 400), (300, 500)), ((100, 400), (200, 500)), 
         ((0, 200), (100, 300))]





def tri(liste): # liste ressemblant à [((200, 500), (300, 600)), ((200, 300), (300, 400)), ((200, 100), (300, 200))]
    l = len(liste)
    coord_abs = [liste[i][0][0] for i in range(l)]
    coord_ord = [liste[i][0][1] for i in range (l)]
    for i in range(1,l+1):
        s = i
        while coord_abs[-s] <= coord_abs[-s-1]:
            coord_abs[-s],coord_abs[-s-1] = coord_abs[-s-1], coord_abs[-s]

    print(coord_abs)
    print(coord_ord)

tri(liste1)