def amaliat(mostatil,morabaa,daiere,dasatoor):
    if dastoor== "mostatil"
        def mostatil(tol, arz, dastoor):

            if dastoor == "mohit":
                mohit= (tol + arz) * 2
                print("mohite mostatil = ", mohit)
            elif dastoor == "masahat":
                masahat= tol * arz
                print("masahat mostatil = ", masahat)


        tol= int(input("tol ra vared konid\n"))
        arz= int(input("arz ra vared konid\n"))
        dastoor= input("mohit ya masahat?\n")
        mostatil(tol, arz, dastoor)

    if dastoor== "morabaa"
        def morabaa(ye_zel, dastoor):
            if dastoor == "mohit":
                mohit= 4*ye_zel
                print("mohite morabaa = ", mohit)
            elif dastoor == "masahat":
                masahat= ye_zel** 2
                print("masahat morabaa = ", masahat)

        ye_zel= int(input("ye_zel ra vared konid\n"))
        dastoor= input("mohit ya masahat?\n")
        morabaa(ye_zel, dastoor)

    if dastoor== "daiere"
        def daiere(shoaa,dastoor):
            if dastoor == "mohit":
                mohit= 2*3.14*shoaa
                print("mohite daiere = ", mohit)
            elif dastoor == "masahat":
                masahat= 3.14*(shoaa**2)
                print("masahat daiere = ", masahat)

        shoaa= int(input("shoaa ra vared konid\n"))
        dastoor= input("mohit ya masahat?\n")
        morabaa(shoaa, dastoor)

mostatil=input()
morabaa=input()
daiere=input()
dastoor=input("nov amaliat ra moshakhas konid")
amaliat(mostatil,morabaa,daiere,dasatoor)
