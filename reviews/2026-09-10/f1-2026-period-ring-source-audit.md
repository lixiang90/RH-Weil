# 2026原件：period ring、复Tate曲线及下降边界

2026-09-10。Singer，只读内部子代理；主代理整合。非外部同行评审。
原件[2606.06604v1](../../literature/f1/cc-absolute-geometry-2606.06604v1.pdf)，
SHA256：0a9c63f97dbf6888c6a9cb4a9283087e71f716b26249fe17f3af0e9a9af7cd7d。
选择性核读§3–5、查看关键公式原页；正文页码与PDF页序一致。
不认证全文perfectoid／FF定理，不以本文献替代实际ζ的算术比较。

| 原文 | 实际采用的输入 | 尚未提供的接口 |
|---|---|---|
| p.11 Def.3.5、Prop.3.6 | H在所选赋值拓扑下稠密于Q_v，目标完备Hausdorff群；local为连续，等价于唯一延拓到Q_v | 不是局部来自有限圆层的解析性 |
| pp.12–16 Prop.3.7、Thm.3.9、Cor.3.10 | 根链x_n^p=x_(n−1)；剩余特征p的perfectoid域C给局部点与1+m_(C^flat)的对应 | 不是复值解析环；tilt加法需要p.14式(9)的极限运算 |
| pp.16–19 Prop.3.12、Cor.3.14–3.15 | F代数闭、perfectoid、特征p；(1+m_F)\{1}给带cyclotomic embedding的untilt；商Z_p^×及p^Z对应FF闭点 | 主要使用Lurie Lecture8；点分类不等于结构层、线丛或上同调比较 |
| pp.20–22 Thm.3.16–3.17 | 不同素数局部点的轨道分类及额外平凡tilt点 | 未得跨素数的函数层／RR粘合；额外特征p点不在通常Q_p上的FF曲线中 |
| pp.23–26 Prop.4.1、Rem.4.2、§4.1.2 | H_p实拓扑到通常C^×的连续字符为exp(zt)；非平凡z∈C^×，Frobenius z→pz，商E_p=C^×/p^Z；p.26给其亚纯函数域及Weierstrass生成元 | E_p与复solenoid不是已识别的同一解析对象 |
| pp.25–27 Cor.4.3、正文Theorem5 | E_p≃C_p×S¹为实一维流形乘积；ω=dλ/λ+i dθ | 不是结构层／Pic／RR的下降同构；导言相应结果编号Theorem4 |
| p.28 Prop.4.4 | H_p改用p-adic拓扑，目标仍为通常C；连续同态取值μ_(p^∞)，参数为Q_p | 不能据此把摘要的Q_p^×/p^Z当成已建完整刚性解析函数层 |
| pp.28–29 §5 Outlook及无编号命题 | adic覆盖环来自A_inf[1/p,1/[varpi]]的Gauss完备化；引用Lurie Lecture11 Prop.5，对未完备环中非零f给v_s(f)凹、PL、整数斜率 | B^(φ=p)等特征空间向C_p下降及与CC3关系明确留给未来；未给单位、除子、有效截面或RR比较 |

复Tate曲线可直接使用经典椭圆曲线理论。例如Λ=(log p)Z+2πiZ，
a不属于(1/2)Λ时，wp_Λ(log z)−wp_Λ(a)在E_p上有主除子[P]+[P^-1]−2[O]。
正次数线丛的经典RR是已有输入；不是本文新证明了C_p或solenoid的RR。

period ring中xi=1+[x^(1/p)]+…+[x^((p−1)/p)]用于A_inf/(xi)构造untilt。
这种主理想生成元没有被证明下降为目标C_p的全局亚纯函数。
B^(φ=p)带Frobenius权重，不能当作不变函数空间。
赋值保乘法，但对加法只满足三角不等式；零点、次数及线性系统仍需另建比较。

记号审查：pp.15、22使用“x_0=1”指平凡点时，混合特征下应区分整条恒等根链
与首坐标为1。p.17的cyclotomic根链(1,ζ_p,ζ_(p²),…)首坐标也是1，但并非恒等链。
后续引用采用x^flat=1表示删去的平凡链，不据此否定原文全部分类定理。

下一几何比较见[371](../../notes/371-f1-tate-curve-frobenius-weight.md)。
本审查没有复审内部369或370，也没有验证完整FF结构层的PL定理依赖。
