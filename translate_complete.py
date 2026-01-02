#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Journalit 插件完整汉化脚本
"""

import re
import sys

def translate_main_js_complete(input_file, output_file):
    """完整翻译 main.js 文件中的英文文本"""

    # 读取文件
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # 定义翻译映射（包括带引号和不带引号的版本）
    translations = {
        # 主页快捷链接
        'Add Trade': '添加交易',
        'Trade Log': '交易日志',
        'Trading Dashboard': '交易仪表板',
        'Account Dashboard': '账户仪表板',
        "Today's DRC": '今日 DRC',
        'This Week Review': '本周回顾',
        'This Month Review': '本月回顾',
        'CSV Import': 'CSV 导入',
        'Layout Builder': '布局构建器',

        # 每周审查问题
        'What worked well this week?': '这周哪些方面做得好？',
        "What didn't work this week?": '这周哪些方面做得不好？',
        'Which setups were most profitable?': '哪些设置最赚钱？',
        'What mistakes cost me most money?': '哪些错误让我损失最多？',
        'What could I improve for next week?': '下周我可以改进什么？',

        # 每月审查问题
        'What were key lessons from this month?': '这个月的主要教训是什么？',
        'Which strategies performed best?': '哪些策略表现最好？',
        'What patterns do I notice in my trading?': '我在交易中注意到什么模式？',
        'What are my goals for next month?': '下个月我的目标是什么？',
        'How can I improve my risk management?': '我如何改进风险管理？',

        # 每季度审查问题
        'What were major wins and losses this quarter?': '这个季度的主要盈亏是什么？',
        'Which trading strategies performed best over quarter?': '这个季度哪些交易策略表现最好？',
        'What market conditions did I handle well or poorly?': '我处理得很好或很差的市场条件是什么？',
        'What are my goals for next quarter?': '下个季度我的目标是什么？',
        'How has my trading evolved compared to previous quarters?': '与之前几个季度相比，我的交易如何演变？',

        # 每年审查问题
        'What were my biggest wins and losses this year?': '今年我最大的盈亏是什么？',
        'Which trading strategies performed best over year?': '今年哪些交易策略表现最好？',
        'How did I handle different market conditions throughout year?': '我如何处理全年的不同市场条件？',
        'What are my goals for next year?': '明年的目标是什么？',
        'How has my trading evolved compared to previous years?': '与前几年相比，我的交易如何演变？',
        'What key lessons did I learn this year?': '今年我学到了什么关键教训？',

        # DRC 检查清单
        'Review market conditions': '审查市场条件',
        'Check economic calendar': '检查经济日历',
        'Set risk limits for the day': '设定当天的风险限制',
        "Review previous day's trades": '审查前一天的交易',

        # DRC 审查问题
        'What did I do well today?': '今天我做得好的地方是什么？',
        'What could I improve on?': '我可以改进什么？',
        'What will I focus on for the next session?': '下一次会议我将专注于什么？',

        # 交易模板
        'What will you pay attention to? How will you behave?': '您会注意什么？您将如何表现？',
        'What are your next steps?': '您的下一步是什么？',
        '**Final Check**': '**最终检查**',
        "If you feel **tilted**, take a break from the screen and play guitar, play with Leo, or get something to eat": '如果您感到**情绪失控**，请从屏幕前休息一下，弹吉他、和 Leo 玩耍，或者吃点东西',
        "If you feel **fine**, do not enter a trade until at least the next candle": '如果您感觉**良好**，请至少等到下一根 K 线再进入交易',
        '**Overall Trade Thoughts:**': '**整体交易想法：**',
        'Any additional thoughts about this trade?': '关于这笔交易还有什么其他想法？',

        # 其他交易模板文本
        "Do **NOT** start looking at entering a position until you have completed this loss review.": '在完成此亏损审查之前，**不要**开始考虑进入头寸。',
        'Say out loud to yourself, **"losses are part of the process, there are endless opportunities in the market."**': '大声对自己说，**"亏损是过程的一部分，市场中有无尽的机会。"**',
        'Did you stick to your trading plan without mistakes?': '您是否毫无错误地坚持了您的交易计划？',
        "If **yes**; there is nothing to be mad about, not every trade is going to work out regardless of how good your thesis is": '如果**是**；没有什么可生气的，无论您的论点有多好，并非每笔交易都会成功',
        "If **no**; figure out what went wrong, learn from it and don't do it again": '如果**否**；找出出了什么问题，从中学习，不要再这样做',
        'Be honest about how you feel and note down your emotions:': '诚实地表达您的感受并记录您的情绪：',
        'How are you feeling about this loss?': '您对这次亏损有什么感觉？',
        "If the loss was reasonable, write down the best things you did during the trade and ways of repeating those:": '如果亏损是合理的，写下您在交易中做得最好的事情和重复这些的方法：',
        'What went well that you can repeat?': '哪些方面做得好，可以重复？',
        "If the loss was unreasonable, note where you went wrong and how you'll improve next time:": '如果亏损是不合理的，记录您哪里出错了，以及下次如何改进：',
        'What went wrong and how will you improve?': '出了什么问题，您将如何改进？',
        "Outline what you'll do based on the previous questions and follow the plan.": '根据之前的问题概述您将做什么，并遵循计划。',
        "You might choose to step back from the charts if it's your third loss in a row.": '如果您连续第三次亏损，您可能会选择从图表前退后。',
        "Or you might want to continue trading if it's the first one.": '或者如果是第一次，您可能想继续交易。',

        # 更新日志
        'Major update: CSV Import, R-Multiple tracking, and critical stability improvements.': '重大更新：CSV 导入、R 倍数跟踪和关键稳定性改进。',
        'Import trades from any broker directly into your vault': '直接将任何经纪商的交易导入到您的库中',
        'Built-in broker adapters - IBKR and Tradovate support': '内置经纪商适配器 - 支持 IBKR 和 Tradovate',
        'Smart duplicate detection - Prevents re-importing via time/price matching': '智能重复检测 - 通过时间/价格匹配防止重复导入',
        'AI-powered mapping - Optional OpenAI assistance for custom formats': 'AI 驱动的映射 - 可选的 OpenAI 辅助自定义格式',
        'Manual mapping - Map any CSV for unsupported brokers': '手动映射 - 为不支持的经纪商映射任何 CSV',
        'Template sharing - JTT codes enable community template distribution': '模板共享 - JTT 代码实现社区模板分发',
        'Access via homepage `Customize -> restore hidden` or `Ctrl+P` search `CSV`': '通过主页 `自定义 -> 恢复隐藏` 或 `Ctrl+P` 搜索 `CSV` 访问',
        'Snapshot system - Log dated drawdown limits manually': '快照系统 - 手动记录带日期的回撤限制',
        'Stepped chart - Visualize how limits change over time': '阶梯图表 - 可视化限制随时间的变化',
        'Progress tracking - Auto-calculates remaining room and percentage used': '进度跟踪 - 自动计算剩余空间和已使用百分比',
        'Perfect for prop firms with live equity trailing drawdowns': '非常适合具有实时权益回撤的资金公司',
        'Measure trades in risk units instead of currency': '以风险单位而不是货币衡量交易',
        'Stop Loss field - Auto-calculates risk from entry-to-stop distance': '止损字段 - 自动从进场到止损的距离计算风险',
        'Manual override - Set custom risk amounts with preview': '手动覆盖 - 设置自定义风险金额并预览',
        'Default risk - Pre-fills from settings': '默认风险 - 从设置预填充',
        'Display toggle - View ALL metrics in R-multiples instead of currency': '显示切换 - 以 R 倍数而不是货币查看所有指标',
        'Define a range for breakeven instead of exact zero': '定义盈亏平衡的范围而不是精确的零',
        'Fixed "plugin gone away" errors on reload': '修复了重新加载时的"插件消失"错误',
        'Fixed date mismatches for UTC-1 to UTC-12 timezones': '修复了 UTC-1 到 UTC-12 时区的日期不匹配',
        'Fixed TradeLog creating duplicate trades with random suffixes': '修复了 TradeLog 创建带有随机后缀的重复交易',
        'Cross-platform workspace compatibility': '跨平台工作区兼容性',
        'Custom options persistence': '自定义选项持久化',
        'Reviewed trades filtering': '已审查交易过滤',
        'Plus more under the hood improvements': '以及更多底层改进',
        'Trade sync optimization': '交易同步优化',
        'UI performance improvements': 'UI 性能改进',
        'Bug fixes': '错误修复',
        'Removed automatic folder migration code when changing Journalit folder location in vault': '删除了在库中更改 Journalit 文件夹位置时的自动文件夹迁移代码',
        'Replaced with manual move of existing files': '替换为手动移动现有文件',
        'New trades will automatically be created in new folder location of choice': '新交易将自动在所选的新文件夹位置创建',
        'Complete account filtering across all review components (DRC, Weekly Review, Monthly Review)': '在所有审查组件（DRC、每周回顾、每月回顾）中完成账户过滤',
        'Smart cache management to prevent calculation conflicts and improve performance': '智能缓存管理以防止计算冲突并提高性能',
        'Filter your data by specific accounts to get focused insights on individual trading strategies': '按特定账户过滤数据，以获得对个人交易策略的专注见解',
        'Added trade status filtering with open/closed/win/loss/breakeven options in Trade Log': '在交易日志中添加了带有开仓/平仓/盈利/亏损/盈亏平衡选项的交易状态过滤',
        'Added "This Quarter" time range filter button': '添加了"本季度"时间范围过滤按钮',
        'Fast date/time input system with combined format support for quicker trade entry': '快速日期/时间输入系统，支持组合格式以加快交易录入',
        'Drag-and-drop customisable quick links for personalised navigation': '可拖放的自定义快速链接，用于个性化导航',
        'Easily remove any of the homepage navigation buttons you don\'t want': '轻松删除任何您不想要的主页导航按钮',
        'Customisable journal folder location with complete migration system': '可自定义的日志文件夹位置，具有完整的迁移系统',
        'Safety enhancements to prevent data loss during folder changes': '安全增强，防止文件夹更改期间的数据丢失',
        'Centralised folder path management for better organisation': '集中式文件夹路径管理，以便更好地组织',
        'Take full control of where your trading journal data is stored within your vault': '完全控制您的交易日志数据在库中的存储位置',
        'Eliminated phantom trade counts that were inflating statistics': '消除了虚增统计数据的幽灵交易计数',
    }

    # 执行替换
    for english, chinese in translations.items():
        content = content.replace(english, chinese)

    # 写入文件
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"完整翻译完成！输出文件：{output_file}")

if __name__ == "__main__":
    input_file = "main.js"
    output_file = "main.js"

    if len(sys.argv) > 1:
        input_file = sys.argv[1]
    if len(sys.argv) > 2:
        output_file = sys.argv[2]

    translate_main_js_complete(input_file, output_file)
