using System.Text.RegularExpressions;

namespace QuectoErp.Repository.Tests;

/// <summary>Relative links in Markdown point to files or folders that exist.</summary>
public sealed partial class MarkdownLinkTests
{
    public static TheoryData<string> Files() => new(RepositoryFiles.Markdown);

    [Theory]
    [MemberData(nameof(Files))]
    public void Relative_links_resolve(string file)
    {
        var directory = Path.GetDirectoryName(RepositoryFiles.FullPath(file))!;
        var broken = new List<string>();

        foreach (var target in RelativeLinks(RepositoryFiles.Read(file)))
        {
            var path = Path.GetFullPath(Path.Combine(directory, Uri.UnescapeDataString(target)));
            if (!File.Exists(path) && !Directory.Exists(path))
            {
                broken.Add(target);
            }
        }

        Assert.True(broken.Count == 0, $"{file} has broken links: {string.Join(", ", broken)}");
    }

    internal static IEnumerable<string> RelativeLinks(string markdown)
    {
        var inFence = false;
        foreach (var line in markdown.Split('\n'))
        {
            if (line.TrimStart().StartsWith("```", StringComparison.Ordinal))
            {
                inFence = !inFence;
                continue;
            }

            if (inFence)
            {
                continue;
            }

            foreach (Match match in LinkPattern().Matches(InlineCode().Replace(line, string.Empty)))
            {
                var target = match.Groups["target"].Value;
                if (target.Contains("://", StringComparison.Ordinal) || target.StartsWith('#') || target.StartsWith("mailto:", StringComparison.Ordinal))
                {
                    continue;
                }

                var end = target.IndexOfAny(['#', '?']);
                yield return end < 0 ? target : target[..end];
            }
        }
    }

    // [text](target) or [text](target "title")
    [GeneratedRegex(@"\]\((?<target>[^)\s]+)(?:\s+""[^""]*"")?\)")]
    private static partial Regex LinkPattern();

    [GeneratedRegex("`[^`]*`")]
    private static partial Regex InlineCode();
}
