todos_los_casos = {"login", "logout", "registro", "checkout", "perfil"}
casos_ejecutados = {"login", "logout", "checkout"}
casos_faltan = todos_los_casos - casos_ejecutados
print(casos_faltan)