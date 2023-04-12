capitales = ["Berlín", "Tokio", "París", "Helsinki", "Ottawa", "Canberra"]
paises = ["Alemania", "Japón", "Francia", "Finlandia", "Canadá", "Australia"]

for cap, pais in zip(capitales,paises):
    print(f"La capital de {pais} es {cap}")