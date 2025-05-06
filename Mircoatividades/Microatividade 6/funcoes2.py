def loginUsuario(perfil):
    if perfil.lower() == 'admin':
        print("Bem vindo Administrador")
    else:
        print("Bem-vindo, Usuário")
        
loginUsuario("Admin")
loginUsuario("admin")
loginUsuario("User")
loginUsuario("usuario")
loginUsuario("etc")