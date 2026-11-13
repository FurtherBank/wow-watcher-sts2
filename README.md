# 哇 观者！ / Wah Watcher!

为《杀戮尖塔 2》**测试版 v0.113.0** 的愚者添加一张观者联动稀有牌，带原生「哇」旋律标签。

![哇 观者！专属卡图](WowWatcher/images/wah_watcher.png)

## 本次更新

v0.1.5 修正面罩卡图，移除面罩上不应显示的嘴部弧线。

v0.1.4 中文名改为「哇 观者！」（哇后保留一个空格），补齐十种语言。移除真言随机牌，调整卡牌描述，并重绘红、蓝、紫三色光下观者闪亮登场的卡图。保留 v0.1.3 的贴图生命周期修复。

## 卡图兼容性

v0.1.3 修复查看卡牌大图后切换房间、再次抽到此牌时可能发生的卡死。已与 `midori_black_card` 原版一起复现旧版故障，并验证修复版跨 12 次贴图清理后仍可正常显示；另已运行带该卡面 Mod 和 RegentFemPortraits 的战斗抽牌、出牌验证。结果见 [贴图生命周期回归](verification/portrait-lifecycle-results.txt)。更新后需完全退出并重新启动游戏，当前进程中已失效的贴图缓存无法通过替换文件恢复。

## 卡牌效果

**哇 观者！** · 稀有 · 0 费技能 · 哇 · 消耗

在手牌中生成以下四张牌。

- 随机一张能够进入愤怒的牌。
- 随机一张能够进入平静的牌。
- 猛虎下山。
- 渎神。

**升级后，生成的四张牌全部升级。** 生成牌保留自身费用；手牌已满时，多出的牌进入弃牌堆。支持观者 Mod 当前提供的简体中文、英语、日语、韩语、德语、法语、意大利语、波兰语和俄语，另保留繁体中文支持。卡名、姿态和固定生成牌的译名参照前置 Mod 及原生「哇」系列；繁体中文环境下，观者 Mod 的牌名可能回退为英文。

愤怒和平静的随机池排除观者初始牌与带消耗的姿态牌；条件触发及延迟触发的姿态牌仍可生成。固定生成的两张牌不受此限制。

| 类别 | 随机范围 |
| --- | --- |
| 愤怒 | Indignation（义愤）、Tantrum（发脾气）、SimmeringFury（煞怒） |
| 平静 | FearNoEvil（不惧邪恶）、InnerPeace（内心平静）、Meditate（冥想） |

## 下载与安装

从 [Releases](https://github.com/FurtherBank/wow-watcher-sts2/releases) 下载 `WowWatcher-0.1.5.zip`。

使用前请切换到游戏测试分支，并安装、启用以下前置 Mod。

| 前置 Mod | 已验证版本 |
| --- | --- |
| [BaseLib](https://steamcommunity.com/sharedfiles/filedetails/?id=3737335127) | 3.4.8 |
| [The Watcher](https://steamcommunity.com/sharedfiles/filedetails/?id=3747492505) | 1.5.16 |

解压安装包，将 `WowWatcher` 文件夹放入游戏的 `mods` 目录。该文件夹内应直接包含 `WowWatcher.dll`、`WowWatcher.pck`、`WowWatcher.json` 三个文件。启用本 Mod 并重启游戏，即可在愚者牌池中获得此牌。

- Windows、Linux：游戏安装目录下的 `mods/WowWatcher`。
- macOS：`SlayTheSpire2.app/Contents/MacOS/mods/WowWatcher`。

当前验证范围为 **macOS、测试版 v0.113.0**。安装包不包含游戏或前置 Mod 的文件。

## 游戏内预览

![升级版卡牌及原生稀有金框](verification/card-1.png)

## 从源码构建

需要 .NET 9 SDK、Python 3、Godot 4.5.1 的 .NET SDK（由项目自动还原），以及本地的游戏和前置 Mod。游戏程序集、BaseLib 和 Watcher 均通过本地文件引用，不随源码分发。

macOS 默认使用当前用户的标准 Steam 安装目录。其他位置或平台可在仓库根目录创建已被 Git 忽略的 `local.props`。

```xml
<Project>
  <PropertyGroup>
    <GameData>/path/to/directory/containing/sts2.dll</GameData>
    <Workshop>/path/to/steamapps/workshop/content/2868840</Workshop>
  </PropertyGroup>
</Project>
```

`Workshop` 目录需要包含 `3737335127/BaseLib/BaseLib.dll` 和 `3747492505/Watcher.dll`。`GameData` 目录还应包含游戏随附的 `0Harmony.dll`。

```sh
./scripts/build.sh
```

若 .NET 不在 PATH 中，可设置 `DOTNET_BIN` 为本机 `dotnet` 可执行文件的路径。Windows 可使用 Git Bash 或 WSL 执行脚本，并安装相应环境下可用的 .NET 和 Python。

输出为 `dist/WowWatcher/` 和 `dist/WowWatcher-0.1.5.zip`。ZIP 内只有运行所需的 DLL、PCK 和清单。

## 卡图与资源

专属卡图使用 imagegen 生成，参考愚者「哇」牌与观者牌的角色造型和视觉语言，展示观者在红、蓝、紫三色光中闪亮登场的瞬间。

- [生成原图](WowWatcher/images/wah_watcher.png)
- [生成提示词](art/generation-prompt.txt)
- `WowWatcher/images/wah_watcher.res` 为保留原图像素的 Godot 纹理资源。

PNG 和 `.res` 均已包含在仓库中，普通构建无需重新生成。若替换 PNG，先用 .NET 版 Godot 4.5 更新纹理，再重新构建。

```sh
godot --headless --path . --script scripts/import_art.gd
```

将 `godot` 替换为本机 Godot .NET 编辑器的可执行文件名或路径。

本项目是非官方同人 Mod。《杀戮尖塔 2》及其角色属于 Mega Crit；观者移植 Mod 由 lamali 制作。本仓库未收录参考卡图或游戏程序集；游戏截图仅用于展示 Mod 的实际效果。

## 验证记录

已使用独立游戏副本和独立存档，从愚者选角、开局、进入战斗到实际出牌，验证以下行为。

- 注册到愚者牌池，稀有度、中文名称和描述正确。
- 专属卡图在普通版和升级版中正确显示，原生金框正常。
- 0 费，愤怒、平静随机牌各一张，固定生成猛虎下山和渎神。
- 原版生成未升级牌，升级版生成四张升级牌。
- 打出后消耗，原生旋律系统识别为「哇」。
- 手牌接近满额时，溢出的牌进入弃牌堆。
- 十种语言均能加载卡名、格式化升级描述并显示牌面。

本次结果见 [v0.1.4 端到端及语言验证](verification/v0.1.4-results.txt)。历史记录包括 [初版功能验证](verification/results.txt)、[初版卡图验证](verification/art-results.txt)、[v0.1.2 卡池验证](verification/pool-results.txt)。测试进程退出码为 0；退出时出现 Godot 渲染资源释放提示，未影响上述断言通过。当前仓库收录验证结果和截图，未提供自动执行这些游戏场景的测试工具。

## 创意工坊发布准备

工坊条目名称拟为「假如愚者是观者」，卡牌名称仍为「哇 观者！」。已准备 [发布流程](workshop/发布流程.txt)、[中文介绍](workshop/description.zh-CN.bbcode.txt)、[英文介绍](workshop/description.en.bbcode.txt) 和图片素材，上传配置初始设为私密。

在项目根目录运行 `python3 scripts/prepare_workshop.py` 可刷新 `workshop/content/` 并检查材料；此命令不会连接或上传 Steam。完成首次工坊订阅安装验收后，再将条目公开。
