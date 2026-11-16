namespace QuectoErp.Repository.Tests;

/// <summary>Finds the repository root and the documentation files the tests check.</summary>
internal static class RepositoryFiles
{
    private static readonly string[] s_ignoredDirectories = [".git", "bin", "obj", "node_modules", ".vs", ".idea"];

    public static string Root { get; } = FindRoot();

    /// <summary>Markdown files, as repository-relative paths with forward slashes.</summary>
    public static IReadOnlyList<string> Markdown { get; } = Enumerate(Root)
        .Where(path => path.EndsWith(".md", StringComparison.Ordinal))
        .Order(StringComparer.Ordinal)
        .ToArray();

    public static string FullPath(string relativePath) => Path.Combine(Root, relativePath.Replace('/', Path.DirectorySeparatorChar));

    public static string Read(string relativePath) => File.ReadAllText(FullPath(relativePath));

    private static string FindRoot()
    {
        for (var dir = new DirectoryInfo(AppContext.BaseDirectory); dir is not null; dir = dir.Parent)
        {
            if (File.Exists(Path.Combine(dir.FullName, "QuectoERP.slnx")))
            {
                return dir.FullName;
            }
        }

        throw new InvalidOperationException("Repository root (QuectoERP.slnx) not found above " + AppContext.BaseDirectory);
    }

    private static IEnumerable<string> Enumerate(string root)
    {
        var pending = new Stack<string>([root]);
        while (pending.Count > 0)
        {
            var dir = pending.Pop();
            foreach (var sub in Directory.EnumerateDirectories(dir))
            {
                if (!s_ignoredDirectories.Contains(Path.GetFileName(sub)))
                {
                    pending.Push(sub);
                }
            }

            foreach (var file in Directory.EnumerateFiles(dir))
            {
                yield return Path.GetRelativePath(root, file).Replace(Path.DirectorySeparatorChar, '/');
            }
        }
    }
}
