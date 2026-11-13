using BaseLib.Abstracts;
using BaseLib.Utils;
using MegaCrit.Sts2.Core.Commands;
using MegaCrit.Sts2.Core.Entities.Cards;
using MegaCrit.Sts2.Core.GameActions.Multiplayer;
using MegaCrit.Sts2.Core.HoverTips;
using MegaCrit.Sts2.Core.Models;
using MegaCrit.Sts2.Core.Models.CardPools;
using MegaCrit.Sts2.Core.Nodes.Vfx;
using WatcherMod;

namespace WowWatcher;

[Pool(typeof(FoolCardPool))]
public sealed class WahWatcher() : CustomCardModel(0, CardType.Skill, CardRarity.Rare, TargetType.Self)
{
    protected override HashSet<CardTag> CanonicalTags => [CardTag.Wah];
    public override IEnumerable<CardKeyword> CanonicalKeywords => [CardKeyword.Exhaust];
    // Reuse this portrait for large previews. Registering the same texture as
    // CustomPortraitPath lets the native large-art cache dispose the shared image.
    public override string PortraitPath => "res://WowWatcher/images/wah_watcher.res";
    public override string BetaPortraitPath => PortraitPath;
    protected override IEnumerable<string> ExtraRunAssetPaths => NWahVfx.AssetPaths;
    protected override IEnumerable<IHoverTip> ExtraHoverTips =>
        [HoverTipFactory.FromCard<WatcherRushdown>(IsUpgraded), HoverTipFactory.FromCard<WatcherBlasphemy>(IsUpgraded)];

    // Stance pools exclude starter cards and cards with Exhaust.
    // Conditional and delayed stance entries remain eligible.
    public static IReadOnlyList<CardModel> WrathCards =>
        [ModelDb.Card<WatcherIndignation>(), ModelDb.Card<WatcherTantrum>(), ModelDb.Card<WatcherSimmeringFury>()];
    public static IReadOnlyList<CardModel> CalmCards =>
        [ModelDb.Card<WatcherFearNoEvil>(), ModelDb.Card<WatcherInnerPeace>(), ModelDb.Card<WatcherMeditate>()];

    protected override async Task OnPlay(PlayerChoiceContext choiceContext, CardPlay cardPlay)
    {
        if (CombatState is not { } combat) return;
        await MelodyCmd.PlayMelodyVfx(Owner.Creature, CardTag.Wah);
        var rng = Owner.RunState.Rng.CombatCardGeneration;
        CardModel[] templates =
        [WrathCards[rng.NextInt(WrathCards.Count)], CalmCards[rng.NextInt(CalmCards.Count)],
         ModelDb.Card<WatcherRushdown>(), ModelDb.Card<WatcherBlasphemy>()];
        var cards = templates.Select(template => combat.CreateCard(template, Owner)).ToArray();
        foreach (var card in cards)
            if (IsUpgraded) CardCmd.Upgrade(card);
        await CardPileCmd.AddGeneratedCardsToCombat(cards, PileType.Hand, Owner);
    }

    protected override void OnUpgrade() { }
}
