import pandas as pd
import tkinter as tk
from tkinter import ttk
import numpy as np
import argparse

def generar_matriz(semilla=None):
    """Genera una matriz 8x8 con valores aleatorios para pruebas"""
    if semilla is not None:
        np.random.seed(semilla)
    
    data = np.random.randint(1, 100, size=(8, 8))
    df = pd.DataFrame(data)
    return df

def mostrar_estadisticas(df, frame):
    """Muestra estadísticas básicas del DataFrame"""
    stats = {
        "Máximo": df.max().max(),
        "Mínimo": df.min().min(),
        "Promedio": round(df.mean().mean(), 2),
        "Moda": df.mode().iloc[0, 0]  # Primer valor de la moda
    }
    
    for i, (key, value) in enumerate(stats.items()):
        ttk.Label(frame, text=f"{key}: {value}").grid(row=0, column=i, padx=10, pady=5)

def crear_interfaz(semilla=None):
    """Crea la interfaz gráfica con Tkinter"""
    root = tk.Tk()
    root.title("Ejemplo de Instalación")
    
    # Frame principal
    main_frame = ttk.Frame(root, padding="10")
    main_frame.pack(fill=tk.BOTH, expand=True)
    
    # Título
    ttk.Label(main_frame, text="Matriz 8x8 con Datos Aleatorios", 
             font=('Helvetica', 14, 'bold')).grid(row=0, column=0, columnspan=8, pady=10)
    
    # Generar y mostrar matriz
    df = generar_matriz(semilla)
    
    # Mostrar DataFrame como tabla
    for i in range(8):
        for j in range(8):
            ttk.Label(main_frame, text=str(df.iloc[i, j]), 
                     relief=tk.RIDGE, width=5).grid(row=i+1, column=j, padx=2, pady=2)
    
    # Frame para estadísticas
    stats_frame = ttk.Frame(root, padding="10")
    stats_frame.pack(fill=tk.X)
    mostrar_estadisticas(df, stats_frame)
    
    # Botón de salir
    ttk.Button(root, text="Salir", command=root.destroy).pack(pady=10)
    
    root.mainloop()

def main():
    """Función principal para el comando tkprueba"""
    parser = argparse.ArgumentParser(description='Genera una matriz aleatoria con interfaz gráfica')
    parser.add_argument('semilla', nargs='?', type=int, 
                      help='Semilla para los números aleatorios (opcional)')
    args = parser.parse_args()
    
    crear_interfaz(args.semilla)

if __name__ == "__main__":
    main()
