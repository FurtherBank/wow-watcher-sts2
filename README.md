# 假如愚者是观者

为《杀戮尖塔 2》**测试版 v0.113.0** 的愚者添加稀有技能「哇 观者！」，带原生「哇」旋律标签。

**本分支适配 Boninall 的 [观者 Watcher](https://steamcommunity.com/sharedfiles/filedetails/?id=3747526116)，工坊 ID 为 3747526116。** 当前 Mod 版本为 v0.2.0，已对照该观者的 v0.10.10 实现。

lamali 的 The Watcher 版完整保留在 [backup/lamali-v0.1.4](https://github.com/FurtherBank/wow-watcher-sts2/tree/backup/lamali-v0.1.4)；原安装包仍可从 [v0.1.4 Release](https://github.com/FurtherBank/wow-watcher-sts2/releases/tag/v0.1.4) 获取。

两版观者使用相同的内部 Mod 标识及程序集文件名，安装本分支时只启用 Boninall 的上述条目。请按所使用的观者实现选择对应安装包。

![观者在红蓝紫三色光中登场](WowWatcher/images/wah_watcher.png)

## 卡牌效果

**哇 观者！** · 稀有 · 0 费技能 · 哇 · 消耗

将一张随机的愤怒、平静牌以及猛虎下山和渎神加入手牌。

愤怒牌和平静牌各一张，加上猛虎下山和渎神，共四张。升级后另起一行显示「加入的牌均已升级」。

| 类别 | Boninall 观者版随机范围 |
| --- | --- |
| 愤怒 | 义愤填膺、发泄、怒火中烧 |
| 平静 | 不惧妖邪、内心宁静、冥想 |

愤怒、平静随机池排除初始牌和带消耗的姿态牌，保留条件触发及延迟触发的姿态牌。生成牌保留自身费用；手牌已满时，多出的牌进入弃牌堆。

沿用原有卡图与十种语言支持，固定牌名和姿态用语已对照本版观者更新。支持简体中文、繁体中文、英语、日语、韩语、德语、法语、意大利语、波兰语和俄语；前置 Mod 的其他语言不代表本卡也已提供对应翻译。

## 安装

切换游戏到 `public-beta`，安装并启用以下前置。

| 前置 | 已验证版本 |
| --- | --- |
| [BaseLib](https://steamcommunity.com/sharedfiles/filedetails/?id=3737335127) | 3.4.8 |
| [观者 Watcher，作者 Boninall](https://steamcommunity.com/sharedfiles/filedetails/?id=3747526116) | 0.10.10 |

使用本分支构建生成的 `WowWatcher-0.2.0.zip`，将其中 `WowWatcher` 文件夹放入游戏 `mods` 目录，覆盖旧版三个同名运行文件并完全重启游戏。

- macOS 位于 `SlayTheSpire2.app/Contents/MacOS/mods/WowWatcher/`。
- Windows、Linux 位于游戏安装目录下的 `mods/WowWatcher/`。

目录内应直接包含 `WowWatcher.dll`、`WowWatcher.pck` 和 `WowWatcher.json`。本版本的游戏内 Mod 名称为「假如愚者是观者 / If the Fool Were the Watcher」，卡牌名称不变。

运行时会识别观者的具体实现。如果加载了错误的观者前置，会在启动日志中提示需要 Boninall 版及其工坊 ID。

当前验证环境为 macOS、游戏测试版 v0.113.0。Windows、Linux 尚未实机验证。切换观者实现时，应新开一局验证；两种实现的卡牌 ID 不同，旧版观者运行中的存档不承诺可迁移。

## 验证

本分支的验证结果见 [Boninall 版验证记录](verification/boninall-results.txt)，卡图预览见 [普通版](verification/boninall-card-0.png) 和 [升级版](verification/boninall-card-1.png)。历史 v0.1.x 的验证文件仅对应 lamali 版。

除卡牌生成、升级、消耗、满手溢出和语言显示外，本分支还验证生成后的观者卡牌能在愚者身上产生姿态与能力效果。

贴图仍沿用 v0.1.3 的生命周期修复，普通与大图共用持久纹理，避免卡面替换 Mod 缓存已释放贴图造成卡死。

## 从源码构建

需要 .NET 9、Python 3，以及本地游戏、BaseLib 和 Boninall 观者的程序集。

macOS 默认从当前用户的 Steam 安装位置读取引用。其他位置可在仓库根目录创建被 Git 忽略的 `local.props`。

```xml
<Project>
  <PropertyGroup>
    <GameData>/path/to/directory/containing/sts2.dll</GameData>
    <Workshop>/path/to/steamapps/workshop/content/2868840</Workshop>
  </PropertyGroup>
</Project>
```

`Workshop` 目录需要包含 `3737335127/BaseLib/BaseLib.dll` 与 `3747526116/Watcher.dll`。

```sh
./scripts/build.sh
```

如果 .NET 不在 PATH 中，可设置 `DOTNET_BIN` 为本机 `dotnet` 可执行文件路径。输出为 `dist/WowWatcher/` 和 `dist/WowWatcher-0.2.0.zip`。

## 创意工坊材料

[发布流程](workshop/发布流程.txt)、[中文介绍](workshop/description.zh-CN.bbcode.txt)、[英文介绍](workshop/description.en.bbcode.txt) 与上传配置均对应本分支的 Boninall 版。初始可见性为私密，首次创建后应先通过工坊订阅安装验收再公开。

```sh
python3 scripts/prepare_workshop.py
```

该命令仅刷新 `workshop/content/` 并检查材料，不会连接或上传 Steam。

## 卡图与致谢

专属卡图使用 imagegen 生成，参考愚者「哇」牌与观者的原作造型和视觉语言。图片和 [提示词](art/generation-prompt.txt) 已收录，纹理资源保留原图像素。

普通构建无需重新生成卡图。替换 PNG 后，可使用 .NET 版 Godot 4.5 执行 `godot --headless --path . --script scripts/import_art.gd` 更新纹理，再构建。

本项目为非官方同人 Mod。《杀戮尖塔 2》及其角色属于 Mega Crit；本分支依赖的观者由 Boninall 制作。感谢 BaseLib 的作者。本仓库不包含游戏和前置 Mod 程序集。
