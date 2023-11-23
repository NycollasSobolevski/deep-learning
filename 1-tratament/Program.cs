using System.Drawing;
using System;

string path = args[0];

if (path == null)
{
    System.Console.WriteLine("Insert a valid directory in Args");
    System.Environment.Exit(0);
}
string[] diretorios = null;

try
{
    diretorios = Directory.GetDirectories(path);
}
catch (System.Exception)
{
    System.Console.WriteLine("Invalid Directory");
    System.Environment.Exit(0);
}

foreach (var folder in diretorios)
{
    var files = Directory.GetFiles(folder);
    foreach (var file in files)
    {
        try
        {
            var image = new Bitmap(file);
            image.Dispose();
        }
        catch (System.Exception)
        {
            try
            {
                File.Delete(file);
                System.Console.WriteLine($"Image '{file}' Deleted");
            }
            catch (System.Exception)
            {
                System.Console.WriteLine($"Unable to delete file: '{file}'");
            }
        }
    }
}