# 忠实零约定的冻结与整数自配对的有限重闭

2026-10-29。原 locator 的 module tensor 误写继续由 haran-locator-scope-correction.md 冻结。本记录追加另一项语义限域，不改两份独立原稿，也不把作者未核后章补充约定写成事实。

实际 Definition 2.1 要求 F→C 忠实，因而在对象1上 0≠id。Example1 的 F(F₂)、F(F₃) 都满足该忠实性。两份当前原稿分别由完整 tensor 双函子及分配公理推得：对每个 C，Hom(F(Z),C)至多一元，方向是**从**整数矩阵范畴出发，且在全部有限矩阵层成立。

若上述两个有限域矩阵对象有共同余锥，两条整数约化的复合必相同；整数3经F₂给id，经F₃给0，矛盾。因此，§7.1 Theorem7.1的“任意输入有fibred sum”不可在这个字面非退化类别中不加说明地消费。需要明确允许退化零范畴的忠实性例外，或限制可用输入。这里没有查遍作者全篇约定，故不称作者整体理论错误，也不声称这个有限反例排除紧化图表；具体Q子环图表可能有F(Q)共同目标。

自配对 M=F(Z) 不依赖这个一般存在性：M连同两个id自身满足自余积泛性质，因为每个目标中的两条 M→C 被迫相等。有态射时对角Hom→Hom×Hom为双射；无态射时两边都空。若选择另一模型 B=M⊚_F M，结构map相同，fold d:B→M与结构map互逆。因此本门 selfcase 已绕开一般7.1存在性缺口独立重闭；即便允许退化零对象来修复一般类别，该自配对论证仍成立。

可消费结论仅为 Spec(M⊚_F M)→Spec(M) 的仿射折叠同构，两槽无法提供独立横向整数副本。Spec反变；环侧初始F→M是epi，并非称M为初对象，也不是Hom(C,M)唯一。它不证明所有对应/余维类为零，不覆盖 compactified square 的边界与其它图表，不涉及作者2022/2024框架，更没有建立 physical r→D_r、405 principal消去、537保非根、mixedRR、原du-Dlog或完整Γ/properpowers/双pole身份。

前件读取限于印刷627–628 Def2.1/2.9、632 Example1及671–675的§7.1/7.2。附带§6尾、§8及Example2的曝光仍不消费。历史初门“不预准C064/601”不改；实际整门计轮待不同fresh与root比较新实际类别/strongest-old之后统一结算。此更正、有限域直接推论、代理和文件不另计轮。

## 追加：Spec箭头定向更正（先冻结上文这一箭头）

上文“Spec(M⊚_F M)→Spec(M) 的仿射折叠”把折叠的谱方向写反，不能按该标签消费。正确为：环侧 i:M→B 与 fold d:B→M 互逆；谱侧 projection Spec(i):Spec(B)→Spec(M) 与 diagonal Spec(d):Spec(M)→Spec(B) 互逆。二者均同构，但 projection 不能标成 Spec(d)。上文其余Hom方向、selfpushout、zero caveat及限于affine的结论不变。此处公开保留初稿并追加纠正，未将该错箭头输入新结果、cadence或旧600；root消费仅用本段正确方向重新闭合。
