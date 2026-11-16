using System.Globalization;
using System.Text.RegularExpressions;

namespace QuectoErp.Repository.Tests;

/// <summary>Both roadmap files stay in step (ROADMAP.md, "How to change this roadmap").</summary>
public sealed partial class RoadmapTests
{
    private static readonly string s_english = RepositoryFiles.Read("ROADMAP.md");
    private static readonly string s_portuguese = RepositoryFiles.Read("ROADMAP.pt-BR.md");

    [Fact]
    public void Both_languages_have_the_same_last_updated_date()
    {
        var english = DateOnly.ParseExact(EnglishDate().Match(s_english).Groups["date"].Value, "yyyy-MM-dd", CultureInfo.InvariantCulture);
        var portuguese = DateOnly.ParseExact(PortugueseDate().Match(s_portuguese).Groups["date"].Value, "dd/MM/yyyy", CultureInfo.InvariantCulture);

        Assert.Equal(english, portuguese);
    }

    [Fact]
    public void Both_languages_have_the_same_checklist()
    {
        Assert.Equal(Checkboxes(s_english), Checkboxes(s_portuguese));
    }

    /// <summary>The sequence of done (x) and open ( ) items, in document order.</summary>
    private static string Checkboxes(string markdown) =>
        string.Concat(Checkbox().Matches(markdown).Select(m => m.Groups["state"].Value == "x" ? 'x' : '.'));

    [GeneratedRegex(@"\*\*Last updated:\*\* (?<date>\d{4}-\d{2}-\d{2})")]
    private static partial Regex EnglishDate();

    [GeneratedRegex(@"\*\*Última atualização:\*\* (?<date>\d{2}/\d{2}/\d{4})")]
    private static partial Regex PortugueseDate();

    [GeneratedRegex(@"^\s*- \[(?<state>[ x])\]", RegexOptions.Multiline)]
    private static partial Regex Checkbox();
}
