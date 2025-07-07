using System;
using System.Collections.Generic;

class Programa1
{
    static void Main()
    {
        LinkedList<double> listaPrincipal = new LinkedList<double>();
        LinkedList<double> listaMenoresIgual = new LinkedList<double>();
        LinkedList<double> listaMayores = new LinkedList<double>();

        Console.Write("¿Cuántos datos deseas ingresar?: ");
        int cantidad = int.Parse(Console.ReadLine());

        for (int i = 0; i < cantidad; i++)
        {
            Console.Write($"Ingrese el dato #{i + 1}: ");
            double dato = double.Parse(Console.ReadLine());
            listaPrincipal.AddLast(dato);
        }

        // Calcular el promedio
        double suma = 0;
        foreach (double num in listaPrincipal)
        {
            suma += num;
        }
        double promedio = suma / cantidad;

        // Separar los datos
        foreach (double num in listaPrincipal)
        {
            if (num <= promedio)
                listaMenoresIgual.AddLast(num);
            else
                listaMayores.AddLast(num);
        }

        // Mostrar resultados
        Console.WriteLine("\n--- Resultados ---");
        Console.WriteLine("Datos cargados en la lista principal:");
        foreach (double num in listaPrincipal)
            Console.Write(num + " ");

        Console.WriteLine($"\n\nPromedio: {promedio:F2}");

        Console.WriteLine("\nDatos menores o iguales al promedio:");
        foreach (double num in listaMenoresIgual)
            Console.Write(num + " ");

        Console.WriteLine("\n\nDatos mayores al promedio:");
        foreach (double num in listaMayores)
            Console.Write(num + " ");
    }
}
