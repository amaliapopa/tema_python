import pandas as pd
import matplotlib.pyplot as plt

# Incarcam fisierul CSV
data_file_path = 'data.csv'  
data = pd.read_csv(data_file_path)

X = 4  # POPA
Y = 11 # AMALIAIOANA

# Primul grafic cu toate valorile din fisierul CSV
plt.figure(figsize=(10, 6))
plt.plot(data.index, data['Durata'], label='Durata', marker='o', color="yellow")
plt.plot(data.index, data['Puls'], label='Puls', marker='x', color="green")
plt.title('Toate Valorile')
plt.xlabel('Index')
plt.ylabel('Valori')
plt.legend(title = "Legenda")
plt.grid(True)
plt.show()

# Al doilea grafic cu primele 4 valori din fisierul CSV
plt.figure(figsize=(10, 6))
plt.plot(data.head(X).index, data.head(X)['Durata'], label='Durata', marker='v')
plt.plot(data.head(X).index, data.head(X)['Puls'], label='Puls', marker='3')
plt.title(f'Primele {X} Valori')
plt.xlabel('Index')
plt.ylabel('Valori')
plt.legend()
plt.grid(True)
plt.show()

# Al treilea grafic cu ultimele 11 valori din fisierul CSV
plt.figure(figsize=(10, 6))
plt.plot(data.tail(Y).index, data.tail(Y)['Durata'], label='Durata', marker='s')
plt.plot(data.tail(Y).index, data.tail(Y)['Puls'], label='Puls', marker='d')
plt.title(f'Ultimele {Y} Valori')
plt.xlabel('Index')
plt.ylabel('Valori')
plt.legend()
plt.grid(True)
plt.show()
