<div align="center">

![Journalit Banner](https://github.com/user-attachments/assets/ab7232d4-1352-4658-a284-86029c0246f1)

**一款强大的本地优先 Obsidian 交易日志插件，帮助交易者跟踪、分析和提升交易表现。**

[![Obsidian Plugin](https://img.shields.io/badge/Obsidian-Plugin-purple?logo=obsidian)](https://obsidian.md/)
[![TypeScript](https://img.shields.io/badge/TypeScript-007ACC?logo=typescript&logoColor=white)](#)
[![React](https://img.shields.io/badge/React-20232A?logo=react&logoColor=61DAFB)](#)

*关键词：obsidian 交易日志，交易插件，交易跟踪，obsidian 交易模板，交易分析，MT5 同步，CSV 导入*

[功能特性](#功能特性) | [截图展示](#截图展示) | [安装说明](#安装说明) | [技术支持](#技术支持)

</div>

> **隐私优先**：所有手动交易记录都保存在您的本地库中。可选的 MT5 同步功能仅在自动获取交易时连接到 Journalit 服务器。[阅读我们的隐私政策](PRIVACY.md)

---

## 功能特性

### 核心交易日志
- **本地优先架构** - 所有交易数据安全地存储在您的 Obsidian 库中
- **全面的交易跟踪** - 记录带有详细元数据、心理笔记和丰富上下文的交易
- **R倍数风险跟踪** - 以风险单位衡量交易，自动从止损计算
- **多进出场支持** - 跟踪部分进出场和复杂头寸
- **心理跟踪** - 监控情绪、错误和行为模式

### 导入与同步
- **CSV 导入系统** - 从任何经纪商导入交易，内置 IBKR、Tradovate、TradeZero、TradingView 和 ByBit 适配器
- **AI 驱动的映射** - 可选的 OpenAI 辅助自定义 CSV 格式映射
- **模板共享** - JTT 代码实现社区模板分发
- **MetaTrader 5 集成** - 通过 FTP 自动同步 MT5 交易

### 审查系统 (V2)
- **基于模板的审查** - 每日、每周、每月、每季度和年度审查模板
- **布局构建器** - 创建带有拖放部分的自定义审查模板
- **20+ 小部件** - 性能图表、交易摘要、心理跟踪等
- **模板共享** - 与社区共享和导入审查模板

### 分析仪表板
- **可自定义主页** - 带有位置和大小控制的拖放小部件
- **交易热力图** - GitHub 风格的贡献图，显示每日盈亏表现
- **高级过滤** - 按账户、代码、设置、标签、日期范围和交易状态过滤
- **性能指标** - 胜率、回撤分析、平均持仓时间、滚动盈亏比
- **仓位计算器** - 内置计算器，支持多资产和盈亏比

### 交易日志
- **多选操作** - Shift 点击选择交易，批量工具栏执行批量操作
- **列自定义** - 选择、重新排序和调整列的大小以符合您的偏好
- **高级过滤** - 按状态、账户、设置、标签和自定义日期范围过滤
- **滚动持久化** - 导航离开时记住您的位置

### 账户管理
- **多账户** - 跟踪具有独立盈亏的独立交易账户
- **手动回撤跟踪** - 记录用于资金公司跟踪的日期回撤限制
- **交易历史** - 存款、取款和资产管理跟踪
- **跟单交易支持** - 用于跟单交易计算的盈亏乘数

### 附加功能
- **全局工具规格** - 一次定义跳价大小和合约规格，到处应用
- **回测交易系统** - 使用专用文件名单独跟踪模拟交易
- **TradingView 图像链接** - 通过 URL 附加图表快照
- **佣金跟踪** - 支持固定或百分比佣金
- **更新通知** - 通过应用内更新日志了解新版本

## 截图展示

### 主页视图
*可自定义的仪表板，带有拖放小部件、交易热力图和快速导航*

![Home View](https://github.com/user-attachments/assets/9ef0236f-686f-4511-a05f-925e51f1224a)

### 审查系统
*基于模板的审查，带有布局构建器和 20+ 小部件*

![Review System](https://github.com/user-attachments/assets/48bcc59a-2b17-4478-98b3-dce8677cca47)

![Review Layout Builder](https://github.com/user-attachments/assets/03f20e4b-37e7-43d9-94bf-fb444e43afbf)

### 交易日志
*多选操作、可自定义列和高级过滤*

![Trade Log](https://github.com/user-attachments/assets/84593d6b-9783-4df6-ad06-6201f101ffcd)

### CSV 导入
*从任何经纪商导入，智能重复检测*

![CSV Import](https://github.com/user-attachments/assets/5c272fb2-19c7-4db0-94c0-0fecf67281be)

### 账户仪表板
*财务管理，带有资产管理跟踪和交易历史*

![Account Dashboard](https://github.com/user-attachments/assets/10bea344-81da-465a-9ad6-55c1120c80ad)

### 账户页面
*跟踪每个交易账户的回撤、利润目标和月度成本*

![Account Pages](https://github.com/user-attachments/assets/e9630bc1-326e-4f1c-8e2f-40e7e022a642)

## 安装说明

### 方法 1：BRAT（推荐）

1. 下载并打开 [Obsidian](https://obsidian.md/download)
2. 进入 **设置 > 社区插件 > 打开社区插件**
3. 点击 **浏览**，搜索 **"BRAT"** 并安装 [BRAT 插件](https://github.com/TfTHacker/obsidian42-brat)
4. 打开 **BRAT 设置**并点击 **"添加 Beta 插件"**
5. 输入此仓库 URL：`Cursivez/journalit` 并选择 **"最新版本"**
6. 点击 **"添加插件"** 并在插件设置中启用它

### 方法 2：手动安装

1. 下载最新发布文件：`main.js` 和 `manifest.json`
2. 在您的 `.obsidian/plugins/` 目录中创建一个名为 `journalit` 的文件夹
3. 将下载的文件放入 `journalit` 文件夹
4. 重启 Obsidian 并在 **设置 > 社区插件**中启用插件

## 快速开始

1. **配置** - 打开 **设置 > Journalit** 设置您的交易日志
2. **第一笔交易** - 使用交易表单创建您的第一笔交易记录
3. **导入现有交易** - 使用 CSV 导入导入历史数据（Ctrl+P，搜索 "CSV"）
4. **设置审查** - 配置每日审查模板以进行结构化反思
5. **探索分析** - 检查仪表板以获取性能指标
6. **可选：MT5 同步** - 设置 MetaTrader 5 同步以自动收集交易

**推荐**：进入 设置 > 编辑器 > 显示 并将"文档中的属性"设置为 **隐藏**

## 使用场景

- 使用 Obsidian 的日内交易者需要结构化的交易模板
- 希望全面交易分析和日志记录的波段交易者
- 跟踪回撤和性能目标的资金公司交易者
- 使用 MetaTrader 5 并希望自动交易同步的交易者
- 寻找基于云的交易日志的本地替代方案的任何人
- 希望整合交易工作流程的 Obsidian 用户

## 技术支持

- **文档**：[journalit.co/docs](https://journalit.co/docs)
- **问题反馈**：通过 [GitHub Issues](https://github.com/Cursivez/journalit/issues) 报告错误或请求功能
- **社区**：加入我们的 [Discord 服务器](https://discord.gg/AkSw3D9h8b) 获取支持和讨论

## 隐私与数据

Journalit 以隐私为核心设计：

- **本地优先** - 核心功能完全离线工作
- **网络使用** - 仅当您启用可选的 MT5 同步时，插件才会发出网络请求（连接到 api.journalit.co 进行自动交易检索）
- **无手动交易收集** - 您手动创建的交易永远不会离开您的库
- **无遥测** - 插件默认不收集使用分析
- **透明** - 完整详细信息请参阅我们的[隐私政策](PRIVACY.md)

## 许可证

此插件是专有软件。编译的插件文件分发用于与 Obsidian 一起使用，但源代码不在开源许可下提供。

---

<div align="center">

**为交易社区构建**

*将您的 Obsidian 库转变为强大的交易日志*

</div>
