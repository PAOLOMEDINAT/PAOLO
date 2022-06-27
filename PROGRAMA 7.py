print("BIENVENIDO AL CAJERO")
i=0
while i<3:
      usuario=input("Por favor, ingrese su nombre de usuario:")
      i=i +1
      if usuario=="PAOLOMEDINAT":
            print("USUARIO CORRECTO")
            clave=input("Por favor, ingrese su clave:")
            if str(clave)=="1199":
                  print("BIENVENIDO AL PROGRAMA, PAOLO")
                  break
            else:
                  print("CLAVE INCORRECTA, VUELVE A INTENTARLO.")
                  if    i==3:
                        print("INTENTOS AGOTADOS. CUENTA BLOQUEADA.")
                        break
      else:
            print("USUARIO INCORRECTO, VUELVE A INTENTARLO.")
            if    i==3:
                  print("INTENTOS AGOTADOS. CUENTA BLOQUEADA")



