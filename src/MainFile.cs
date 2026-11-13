using MegaCrit.Sts2.Core.Modding;

namespace WowWatcher;

[ModInitializer(nameof(Initialize))]
public static class MainFile
{
    public static void Initialize()
    {
        // Both community implementations use the same assembly and manifest ID.
        // Version checks alone cannot distinguish them.
        var watcher = AppDomain.CurrentDomain.GetAssemblies()
            .FirstOrDefault(assembly => assembly.GetName().Name == "Watcher");
        if (watcher?.GetType("WatcherMod.WatcherRushdown", throwOnError: false) is null)
            throw new InvalidOperationException(
                "This WowWatcher build requires Boninall's Watcher (Steam Workshop 3747526116). " +
                "Select that Watcher implementation instead of lamali's The Watcher (3747492505).");
    }
}
