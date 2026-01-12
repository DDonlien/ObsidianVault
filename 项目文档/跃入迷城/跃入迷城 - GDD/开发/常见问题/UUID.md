
**UUID**

**规则**

- 按照目前规划，UUID可以分为三部分: {开头三位字母表示物品类型} + {自动项} + {自增项}
- 例如WPN01010101：WPN（武器）01（阵营-劳旅）01（武器种类-巨锤）01（伤害类型-动能）01（品质-普通）
- 八位数字都由相关属性自动决定，因此被称为自动项。
- 当一个对象不能由自动项唯一确定时，为了区分它会需要自增项，比如技能：
- SKL01010001：SKL（技能）01（主被动）01（技能类型）0000（自增）
- 例如主动武器战技有很多，因此会用4位自增项来额外区别
- 这就带来一个问题，比如未来武器也需要自增项，假设2位自增项，那么武器会需要10位数字UUID，由于程序将UUID长度定死，这时有两个选择
- 去除定死的长度，不同类型有不同UUID长度，比如武器10位，义体12位，技能8位。这在目前看来是可能做到的，选择在策划手上。
- 所有UUID一起增减，比如武器导致UUID扩到10位，那义体、技能也要到10位。可能最后导致UUID特别长。
- 目前有python脚本可以半自动处理字母项和自动项
- ~~撰写了一个python脚本，可以严格按照规则生成UUID@龚政涛⏰2024-09-15 08:00~~

**UUID映射表**

- 虚幻资产，包含 1) 每张表的元数据; 2) UUID 到虚幻资产名的映射 (比如WPN01020102 => ID\_AR47\_2)
- 路径 /Game/Data/AutoScriptedDirectory\_DONT\_TOUCH/DA\_Uuid\_Registry (如文件夹名字提示，不要用自动化脚本以外的任何手段编辑这个文件)

![...](../../../跃入迷城%20-%20GDD/开发/常见问题/images/UUID.001.png)

- 用处: 
1. 武器、义体升级。由于Quality必在UUID自动项中有对应，目前升级用UUID来完成，根据Quality的搜索操作就需要UUID映射表
2. 作弊发物品 (未实现)。

![...](../../../跃入迷城%20-%20GDD/开发/常见问题/images/UUID.002.png)

- 元数据: 每张表一份的数据，放在这张表的第一行，目前用来存储Quality位的开始和长度，以及对象类型
- 规则：
- 从每张表的A1开始，横向布局，奇数列是数据名，偶数列是数据值；
- A1 B1必须是ItemType和类型名；
- 必须连续，例如如果G1 H1为空，那么后面项哪怕不为空也不会被识别。

```ItemType|类型名称，就是UUID前三位``` :- |
|<p>QualityBitStart</p><p></p>|品质位开始 (从右数，第一位算0，例如WPN010101**01**，从右第一位是品质位，那么QualityBitStart=0)|
|QualityBitLength|品质位长度 (WPN010101**01**，两位品质位，那么QualityBitLength=2)|
- 在表格里定义元数据的好处是不再需要保证程序和文档同步，比如Quality位的位置改了，重新导一次表就可以更新这个信息，而不是改c++代码
- 列名
- 第2行是便于程序识别的程序列名，纯英文，大驼峰
- 第4行是便于人阅读的列名，无所谓中英文空格
- 如果需要导表脚本识别，就必须在第二行为其定义程序列名，反之则可以空着
- 现在导表脚本用到的列名: 1. Name (物品英文名) 2. UUID 3. Quality (品质)
- 虚幻资产名
- 也就是ID资产，例如ID\_AR47\_2
- 导表脚本不知道项目里有哪些资产叫什么名字，因此只能两边约定俗成
- 目前规则是ID\_{Name}\_{Quality}，Name是物品英文名。
- 脚本会自动将WPN01010102和ID\_DSResolver\_02映射起来
- 工作流 (元数据和第二行程序列名可以完全交给程序员来定义，物品英文名程序员和策划都可以定义，只不过要注意遵守定义规则)
1. 确保要导出的表格定义好了元数据、程序列名，各物品的程序列都填上了数据
2. (飞书) 菜单 -> 表格 -> 下载为csv文件
3. 替换复制表格到本地workspace ProjFiber\ProjFiber\Data\Items\ 
4. 如果这不是武器/义体/技能表，那么还要检查一下脚本是否将其名称列入 (relative\_csv\_file\_path)

![...](../../../跃入迷城%20-%20GDD/开发/常见问题/images/UUID.003.png)

5. 打开UE编辑器
6. (Unreal Editor) Tools -> Execute Python Script -> 弹窗选择 ProjFiber\ProjFiber\Data\Items\ExportUuidList.py 
7. 观察一下log，正常会包含package / python / 版本管理 的日志，没有红色警告信息一般就说明成功了
1. 也可以直接打开 /Game/Data/AutoScriptedDirectory\_DONT\_TOUCH/DA\_Uuid\_Registry 检查

![...](../../../跃入迷城%20-%20GDD/开发/常见问题/images/UUID.004.png)

8. 如果已经运行过这个脚本，下次可以在Tools -> Recent Python Scripts 中快速运行
- ProjFiber\ProjFiber\Data\Items\已受Perforce管理，所以其中的csv文件和python脚本直接用perforce get就行
- 想要UUID映射表正确工作，必须要各ID资产中的UUID和导表的csv中的UUID能够对应上
- 如果对应不上，游戏还是能正常工作，例如csv中有很多策划规划了，但还没在编辑器中制作的物品，这些项目不会影响游戏运行
- 还有种很常见的情况是UUID含义改了，但游戏ID资产中的UUID还没调整，或是一个新物品资产根本没填入UUID，这些物品还能正常装备，打印，但不能升级。

**表格相关**

- 目前有UUID的表格：
- [物品列表](https://dikpa4hrtn9.feishu.cn/wiki/IbdswSAf1iFX9Ik5LRDcg02LnTb?sheet=02e41e) / [物品列表](https://dikpa4hrtn9.feishu.cn/wiki/IbdswSAf1iFX9Ik5LRDcg02LnTb?sheet=rw8RKn) (义体表) / [物品列表](https://dikpa4hrtn9.feishu.cn/wiki/IbdswSAf1iFX9Ik5LRDcg02LnTb?sheet=ocb1WE) (技能表)
- 其他物品例如电梯卡等也需要UUID，这类物品目前称为**通用物品**

