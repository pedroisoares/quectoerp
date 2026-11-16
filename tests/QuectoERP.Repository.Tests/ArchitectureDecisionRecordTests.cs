using System.Text.RegularExpressions;

namespace QuectoErp.Repository.Tests;

/// <summary>The rules in docs/adr/README.md: numbering, title, status and index.</summary>
public sealed partial class ArchitectureDecisionRecordTests
{
    private const string Folder = "docs/adr";

    private static readonly string[] s_englishStatuses = ["Proposed", "Accepted", "Rejected", "Deprecated"];
    private static readonly string[] s_portugueseStatuses = ["Proposto", "Aceito", "Rejeitado", "Obsoleto"];

    private static readonly (int Number, string Name)[] s_records = RepositoryFiles.Markdown
        .Where(f => f.StartsWith(Folder + "/", StringComparison.Ordinal))
        .Select(Path.GetFileName)
        .Select(name => (Match: EnglishFileName().Match(name!), Name: name!))
        .Where(x => x.Match.Success)
        .Select(x => (Number: int.Parse(x.Match.Groups["number"].Value, System.Globalization.CultureInfo.InvariantCulture), x.Name))
        .OrderBy(x => x.Number)
        .ToArray();

    public static TheoryData<string> Records() => new(s_records.Select(r => r.Name));

    [Fact]
    public void Records_exist_and_are_numbered_from_0001_without_gaps()
    {
        Assert.NotEmpty(s_records);
        Assert.Equal(Enumerable.Range(1, s_records.Length), s_records.Select(r => r.Number));
    }

    [Theory]
    [MemberData(nameof(Records))]
    public void Record_has_title_and_valid_status_in_both_languages(string file)
    {
        var number = file[..4];
        var portuguese = file[..^".md".Length] + ".pt-BR.md";

        var english = Header(file);
        Assert.StartsWith($"ADR-{number}: ", english.Title, StringComparison.Ordinal);
        Assert.True(IsValidStatus(english.Status, s_englishStatuses, "Superseded by ADR-"), $"{file}: invalid status '{english.Status}'");

        var translated = Header(portuguese);
        Assert.StartsWith($"ADR-{number}: ", translated.Title, StringComparison.Ordinal);
        Assert.True(IsValidStatus(translated.Status, s_portugueseStatuses, "Substituído pelo ADR-"), $"{portuguese}: invalid status '{translated.Status}'");
    }

    [Theory]
    [MemberData(nameof(Records))]
    public void Record_is_listed_in_both_indexes_with_its_status(string file)
    {
        var portuguese = file[..^".md".Length] + ".pt-BR.md";

        AssertListed("README.md", file, Header(file).Status);
        AssertListed("README.pt-BR.md", portuguese, Header(portuguese).Status);
    }

    private static void AssertListed(string index, string file, string status)
    {
        var row = RepositoryFiles.Read($"{Folder}/{index}")
            .Split('\n')
            .FirstOrDefault(line => line.Contains($"]({file})", StringComparison.Ordinal));

        Assert.True(row is not null, $"{Folder}/{index} does not list {file}");
        Assert.True(row!.TrimEnd().EndsWith($"| {status} |", StringComparison.Ordinal), $"{Folder}/{index}: status of {file} should be '{status}'");
    }

    private static bool IsValidStatus(string status, string[] allowed, string supersededPrefix) =>
        allowed.Contains(status) || SupersededPattern().IsMatch(status) && status.StartsWith(supersededPrefix, StringComparison.Ordinal);

    private static (string Title, string Status) Header(string file)
    {
        var lines = RepositoryFiles.Read($"{Folder}/{file}").Split('\n').Select(l => l.TrimEnd()).ToArray();
        var title = lines.FirstOrDefault(l => l.StartsWith("# ", StringComparison.Ordinal))?[2..] ?? string.Empty;
        var status = lines.FirstOrDefault(l => l.StartsWith("- **Status:** ", StringComparison.Ordinal))?["- **Status:** ".Length..] ?? string.Empty;
        return (title, status);
    }

    [GeneratedRegex(@"^(?<number>\d{4})-[a-z0-9]+(?:-[a-z0-9]+)*\.md$")]
    private static partial Regex EnglishFileName();

    [GeneratedRegex(@"ADR-\d{4}$")]
    private static partial Regex SupersededPattern();
}
