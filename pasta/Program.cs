string path = args[0];
string destiny = args[1];

string[] directories = Directory.GetDirectories(path);

foreach (var dirPath in directories)
{  
    if (dirPath == destiny)
    {
        continue;
    }
    var files = Directory.GetFiles(dirPath);
    foreach (var item in files)
    {
        System.Console.WriteLine(item);
    }
}