namespace QuectoErp.Repository.Tests;

/// <summary>
/// User-facing documentation has an English file (NAME.md) and a Brazilian Portuguese twin (NAME.pt-BR.md),
/// each linking to the other on its first line (CONTRIBUTING.md, "Languages").
/// </summary>
public sealed class BilingualDocumentationTests
{
    private const string PortugueseSuffix = ".pt-BR.md";

    /// <summary>Files written for tools or GitHub, kept in a single language on purpose.</summary>
    private static readonly string[] s_singleLanguage = ["CLAUDE.md"];

    public static TheoryData<string> EnglishFiles() => new(RepositoryFiles.Markdown.Where(f => IsBilingual(f) && !IsPortuguese(f)));

    public static TheoryData<string> PortugueseFiles() => new(RepositoryFiles.Markdown.Where(IsPortuguese));

    [Theory]
    [MemberData(nameof(EnglishFiles))]
    public void English_file_has_a_Portuguese_twin_and_links_to_it(string file)
    {
        var twin = file[..^".md".Length] + PortugueseSuffix;
        Assert.True(File.Exists(RepositoryFiles.FullPath(twin)), $"{file} has no Portuguese version {twin}");

        var expected = $"**English** | [Português (Brasil)]({Path.GetFileName(twin)})";
        Assert.Equal(expected, FirstLine(file));
    }

    [Theory]
    [MemberData(nameof(PortugueseFiles))]
    public void Portuguese_file_has_an_English_twin_and_links_to_it(string file)
    {
        var twin = file[..^PortugueseSuffix.Length] + ".md";
        Assert.True(File.Exists(RepositoryFiles.FullPath(twin)), $"{file} has no English version {twin}");

        var expected = $"[English]({Path.GetFileName(twin)}) | **Português (Brasil)**";
        Assert.Equal(expected, FirstLine(file));
    }

    private static bool IsPortuguese(string file) => file.EndsWith(PortugueseSuffix, StringComparison.Ordinal);

    private static bool IsBilingual(string file) =>
        !file.StartsWith(".github/", StringComparison.Ordinal) && !s_singleLanguage.Contains(file);

    private static string FirstLine(string file) =>
        File.ReadLines(RepositoryFiles.FullPath(file)).FirstOrDefault()?.TrimEnd() ?? string.Empty;
}
