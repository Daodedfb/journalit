#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Journalit 插件最终汉化脚本 - 处理所有剩余的英文文本
"""

import re
import sys

def translate_main_js_final(input_file, output_file):
    """最终翻译 main.js 文件中的所有英文文本"""

    # 读取文件
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # 定义翻译映射
    translations = {
        # 剩余的每周/每月/每季度/每年审查问题
        'What mistakes cost me most money?': '哪些错误让我损失最多？',
        'What were key lessons from this month?': '这个月的主要教训是什么？',
        'Which trading strategies performed best over quarter?': '这个季度哪些交易策略表现最好？',
        'Which trading strategies performed best over year?': '今年哪些交易策略表现最好？',
        'What will I focus on for next session?': '下一次会议我将专注于什么？',

        # 交易模板标题
        '**Review Your Plan**': '**审查您的计划**',
        '**Write Down Your Feelings**': '**写下您的感受**',
        '**Learn From This Loss**': '**从这次亏损中学习**',
        '**Decide The Next Steps**': '**决定下一步**',

        # 交易模板问题（剩余）
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
        'What will you pay attention to? How will you behave?': '您会注意什么？您将如何表现？',
        'What are your next steps?': '您的下一步是什么？',
        '**Final Check**': '**最终检查**',
        "If you feel **tilted**, take a break from the screen and play guitar, play with Leo, or get something to eat": '如果您感到**情绪失控**，请从屏幕前休息一下，弹吉他、和 Leo 玩耍，或者吃点东西',
        "If you feel **fine**, do not enter a trade until at least the next candle": '如果您感觉**良好**，请至少等到下一根 K 线再进入交易',
        '**Overall Trade Thoughts:**': '**整体交易想法：**',
        'Any additional thoughts about this trade?': '关于这笔交易还有什么其他想法？',

        # 其他可能的文本
        "Don't start looking at entering a position until you have completed this loss review.": '在完成此亏损审查之前，不要开始考虑进入头寸。',
        "Say out loud to yourself, \"losses are part of the process, there are endless opportunities in the market.\"": '大声对自己说，"亏损是过程的一部分，市场中有无尽的机会。"',
    }

    # 执行替换
    count = 0
    for english, chinese in translations.items():
        old_content = content
        content = content.replace(english, chinese)
        if content != old_content:
            count += 1
            print(f"已翻译: {english[:50]}...")

    # 写入文件
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"\n最终翻译完成！共翻译了 {count} 处文本。")
    print(f"输出文件：{output_file}")

if __name__ == "__main__":
    input_file = "main.js"
    output_file = "main.js"

    if len(sys.argv) > 1:
        input_file = sys.argv[1]
    if len(sys.argv) > 2:
        output_file = sys.argv[2]

    translate_main_js_final(input_file, output_file)
