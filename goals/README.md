# 长期研究恢复入口

当前[Goal](GOAL.20261014.md)，已有≤538成果固定为新基线。
[跨轮总结](reviews/2026-10-14-macro-refresh-and-causal-budget.md)与
[宏观前沿](MACRO_FRONTIER.md)保存因果图、准确范围、未付前件和选择理由。
先读[短状态](STATE.json)，运行：

    python scripts/research_state.py check
    python scripts/research_state.py show

再读当前Goal、宏观前沿、状态指定的唯一主合同、最近决策及所需证据。
压缩／中断后同样恢复，不先从巨大历史文件推断优先级。
[通用流程](RESEARCH_WORKFLOW.md)适用于长期重型研究；
[决策](DECISIONS.md)、[轮数](review-cadence.json)和[复盘](REVIEW_PROTOCOL.md)职责分开。
STATE是当前执行状态唯一编辑源，show只是由它与cadence显示的视图。
checkpoint记录核心文件哈希，不证明数学或工具运行态。

旧[Goal](GOAL.20260909.md)、[NEXT](NEXT.20260909.md)、[PROGRESS](PROGRESS.md)
和[archive](archive/)保持历史。scripts/sync_goal.py原用于上级源的旧版
[镜像manifest](manifest.json)，不维护新Goal／STATE；
2026-10-13核查时上级GOAL.20260909.md缺失，旧同步检查不可执行。
本仓历史文件按基线保持，新入口不依赖这些外部源文件。
新目标和状态直接以本仓为编辑源，不向上级写重复副本。
保存、启动与有限检查通过不等于长期Goal完成。
成果从原证明的前件闭合记录消费；最新549的完整label费仍未支付实际全1方向。
连续source/非核心合同后先核三句准入；缺核心桥时只保一个原件定位的来源审查。

上版[Goal](GOAL.20261013.md)及535方法边界完成收据为历史；
537/538 fixed-window全源正性与真正底态排序继续可消费，但不能再次完成本版。
组织启动不重置原cadence，当前运行Goal必须用实际工具查询，文件不代替运行态。
