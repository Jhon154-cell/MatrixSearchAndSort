using System;
using System.Collections.Generic;

class Programa2
{
    static void Main()
    {
        LinkedList<int> lista1 = new LinkedList<int>();
        LinkedList<int> lista2 = new LinkedList<int>();

        Console.Write("¿Cuántos datos tendrá la primera lista?: ");
        int n1 = int.Parse(Console.ReadLine());

        for (int i = 0; i < n1; i++)
        {
            Console.Write($"Dato #{i + 1} para la lista 1: ");
            int dato = int.Parse(Console.ReadLine());
            lista1.AddFirst(dato);  // Inserción por el inicio
        }

        Console.Write("\n¿Cuántos datos tendrá la segunda lista?: ");
        int n2 = int.Parse(Console.ReadLine());

        for (int i = 0; i < n2; i++)
        {
            Console.Write($"Dato #{i + 1} para la lista 2: ");
            int dato = int.Parse(Console.ReadLine());
            lista2.AddFirst(dato);  // Inserción por el inicio
        }

        // Comparar tamaño
        if (lista1.Count != lista2.Count)
        {
            Console.WriteLine("\nLas listas NO tienen el mismo tamaño NI el mismo contenido.");
        }
        else
        {
            // Comparar contenido
            var nodo1 = lista1.First;
            var nodo2 = lista2.First;
            bool sonIguales = true;

            while (nodo1 != null)
            {
                if (nodo1.Value != nodo2.Value)
                {
                    sonIguales = false;
                    break;
                }
                nodo1 = nodo1.Next;
                nodo2 = nodo2.Next;
            }

            if (sonIguales)
                Console.WriteLine("\nLas listas son IGUALES en tamaño y en contenido.");
            else
                Console.WriteLine("\nLas listas son IGUALES en tamaño pero NO en contenido.");
        }
    }
}
