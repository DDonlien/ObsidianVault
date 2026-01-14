
**对Mac环境编译**

**准备环境**

1. 安装p4v和ue引擎 
1. 在windows上，p4和p4v会在安装p4 client的同时被安装，前者是命令行工具，后者是可视化客户端，但在mac上，这两者需要分开安装，并且有着完全不同的安装地址，在后续rider连接perforce的过程中，这一点非常重要
2. p4的安装过程如下：https://g.co/gemini/share/40059ad13037
2. 安装Xcode，以及对应的Xcode command line工具 
1. 使用terminal检查是否正确安装
3. 安装Rider，任意启动一个ue项目，安装Rider ue link插件 
1. 目前来看，使用Rider启动编译，是mac编译ue c++项目成功率最高的方案

**下载项目**

1. 用p4v下载项目
2. 注意**网络设置**：如果你安装了vpn，可能导致p4v识别到错误的hostname，在你切换vpn状态后导致hostname不一致无法打开workspace，建议的做法是确保vpn处于关闭状态再创建connection，并在创建workspace时，删除hostname，或者确保hostname与terminal中hostname指令返回的name一致

**检查插件**

1. 原则上来说，所有工程必须的插件都会被add到p4的depot里，如果没有，在能够启动编译的电脑上确认插件并add
2. 但由于mac的bug，有概率出现depot里存在某个插件，但get latest不能正确下载的问题
3. 通过对depot里的plugins文件夹进行checkout → revert操作，可以修复该问题，正确下载所有plugins 
1. 期间可能会出现p4v无法找到对应地址的报错，但这很正常，因为你电脑上没有对应文件，第二次checkout应该就不会出现报错，可以作为检查方案
4. 除非你很清楚自己在做什么，否则**不要**在ue引擎层面手动安装任何插件，否则可能会出现同一个插件被2次引用的情况，导致无法在rider生成解决方案

**修改projectname.uproject**

1. 用文本编辑打开projectname.uproject
2. 检查其中的TergetPlatforms，确保形如：

```TOML
"TargetPlatforms": [
        "Windows",
        "Mac"
]```
1. 如果不存在该段落，建议添加到Plugins最后的]后，注意要给Plugins的]后添加,
2. 保存并退出

**修改DefaultEngine.ini**

1. 用文本编辑打开DefaultEngine.ini
2. 检查其中包含如下设置：

```TOML
[/Script/MacTargetPlatform.XcodeProjectSettings]
bUseModernXcode=True ```
**清理项目**

1. 删除项目文件夹下的以下文件夹 
- Intermediate
- Binaries
- Saved
- DerivedDataCache
- Build
- 任何旧的 .xcworkspace 文件

**编译工程**

1. 打开Terminal
2. 用以下指令进入引擎UBT工具目录(路径可能需要根据你的安装确认，但下面是默认目录)

```TOML
cd "/Users/Shared/Epic Games/UE\_5.3/Engine/Binaries/DotNET/UnrealBuildTool/"```
1. 执行生成命令 (注意路径和参数)

```TOML
dotnet UnrealBuildTool.dll -projectfiles -project="ProjectWorkspace/ProjectName.uproject" -game -platforms=Mac -progress```


