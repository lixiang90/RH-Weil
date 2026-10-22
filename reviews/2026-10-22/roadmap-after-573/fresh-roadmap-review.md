# 独立逆审：573后路线图与亏格二评价来源门

2026-10-22。fresh审查对象为root路线图、已执行首门、精确script/controls，以及
function-field-origins、positive-realization-admission两个独占稿。
本审查没有修改root原稿、STATE或cadence，没有生成新数学合同。
本代理先前撰写recent-lessons，仅以其作为已声明的经验输入；本次对另外两稿及root数学对象重新组织核查，
不将自己的经验稿当独立证明证书。

## 审查结论

**最终限定PASS；一处trace对象歧义已经root修复并现场核实。**
主路线图§4初稿“2Δ……其真实trace为16”应明确为
Tr((2Δ)⋆(2Δ)^t)=16；2Δ自身作用[2]在四维H1上的trace为8。
首门§3与来源分支§3已写正确的自伴复合算式，因此这是摘要对象的纠正，不改变实际局部/交数结论。
已把该点发给root；root已修为Tr((2Δ)⋆(2Δ)^t)=16，并现场重新读取确认。

除此以外，首门局部核算、excess的解释、source0归属与新路线的范围均通过本次核查。
PASS不认证新的曲线RH、经典ζ正性、独立容量或宏观Goal完成。

## 1. 亏格二局部、特殊性与真正厚点

曲线y²=x⁵−x+1在char5下右端导数−1，故可分二重覆盖的六个几何分支点简单，genus为2。
odd degree模型只有一个∞；dx/y及x dx/y的∞阶分别为2、0，确为canonical基。

非branch P=(a,b)处t=x−a，使用无零frame dx/y得到系数(1,a+t)，
长度二限制矩阵为[[1,a],[0,1]]（或转置约定），det1。
用dx frame会乘可逆局部因子；直接求导给det=b^(−2)，不是改了目标配对。
重复ordinary point evaluation两列相同，det0，确可被真jet修复。

branch P=(a,0)处令t=y、δ=x−a，精确方程t²=δ⁵−δ，
故δ=−t²+O(t^10)，dx/y=−2dt。在模t²系数中x=a，真实restriction rank1。
div(x−a)=2P−2∞，故2P canonical、h0(O(2P))2、h0(K−2P)1，
与rank1完全一致。这是真特殊性，不能由换basis/frame或再称“使用jet”恢复rank2。

reduced P+ιP亦canonical，两个几何点不同仍rank1；
Δ+Γι在Jacobian为零类，因此稿件明确不将它当非平凡Weil类严格正性的反例，范围正确。

精确复跑scripts/function_field_evaluation_moving_gate.py，捕获并解析其JSON，
与保存的evaluation-moving-controls.json逐对象相等：10个仿射非branch点、N1=11、全部double-jet det1、
branch rank1及两个reduced控制均一致。
脚本的branch检查只是模t4形式恒等式；完整几何branch论证由上述局部环证明承担，
文稿没有把有限点采样升级为全局moving、RR或RH。

## 2. 2Δ、self-composition与excess

实际Z=2Δ非零，Jacobian作用[2]，但ordinary评价重复列恒退化。
Z⋆Z^t=4Δ，两degree均4；Δ²=2−2g=−2，因而

Tr(Z⋆Z^t)=4+4−(4Δ·Δ)=16。

与H1上4I的trace16吻合。形式拆出2Δ后剩Y=2Δ，Y与Δ共有分量；
Y·Δ=−4是excess/self-intersection数据，不能称非负有限碰撞数。
稿件只反对“任意有效raw代表自动满足非零det/proper collision”的快捷消费，
没有据此否定Weil原定理或宣称CCM目标错误；这一范围缩限必要且已保留。

若使用Δ+Γι控制，其self-composition为2Δ+2Γι，
Γι与Δ在六个tame固定点proper相交，故Y=2Γι有交数12，整体trace0。
这也与零Jacobian作用相符，未偷入符号反例。

## 3. 独立来源与下一family比较

定点核Milne JVs §7 Thm7.6原件：实际degree-g line bundle family先在h0=1开集通过base change给相对有效除子；
特殊fiber用degree-zero twist移到该开集，随后利用Picard平移及overlap一致性完成functor比较。
文稿把它作为可移动族的正控制，而非“逐源任意挑一个有效代表”，符合原件责任。
原件没有给予classic源的uniform du/Dlog或坏chart切换费用；路线图与首门均明确另付。

这种family设施仍不等于正极化：真实有效性／乘法／RR或ample mixed交数先付符号，
完整Frobenius图／点数trace再与Weil型识别。307、563、566、567的已有degree/H/heat/RR资产准确去重。
一般高维Deligne纯性没有被等同于所有标准Hodge正性或原Frobenius半单性。

主路线图选择实际DGA模块操作与这一degree-zero移动/overlap结构作下一有界比较，
有具体输入、首个交付和停止条件。它是待准入来源门，不是已构造新的classic line family。
若只回源指数unit、旧marked-section recipe或另加任意闭cycle，则停止；
没有预建C037、未知RR合同或自动串下一论文。因此当前“唯一next”可以独立恢复。

## 4. determinant doubling和tensor审计的准确强度

对旧连续族取两个副本，C_d²=−dI，p(C_d)=aI+bC_d，
故det p(C_d⊕C_d)=(a²+db²)²，而Tr(p p†)=4(a²+db²)。
d=−1/16、p=X给−1/4；d=+1/16给+1/4。
所有real polynomial determinant非负确不能替代mixed Rosati trace正性。
det(I+tCC†)=(1−t/16)^4虽处处非负，0处导数仍−1/4，运算正确。

这只是已给源模型的doubling及有限代数恒等式：不产生实际isogeny degree、ample geometry或新的广泛方法类排除。
稿件明确称degree-like数值反测，且保留determinant所有混合系数独立几何来源的更强可能。
因此归标准/旧模型消费source0合理；若以后改称“新完整容量方法类边界”则必须重新核准入及轮数，
不能沿用本PASS。

连续W的偶次幂在两段均非负；Laplace展开极点在负段含不可抵消的最右点2kr，
在正段全为虚轴点。统一k pole上界若仅由目标增长率定义，就是等价责任。
函数域W是Dirac分布，稿件不直接取分布点wise幂，而先取全递推a_n=Tr U^n再构造U tensor powers。
这个global H1张量与Deligne对基底各closed point的local lisse-sheaf tensor Euler product明确分开，
没有把形式tensor determinant误当已给cohomological pole theorem。

## 5. 冻结边界、范数与结算

完整Γ/contact、所有prime powers、双pole及complex mixed仍是目标；
本地曲线核算没有被消费为经典这些项的新预算身份。
物理r=e^(u/2)f、原du/Dlog、关系/Pan与Q-radical、compact/扩张域角色保留。
fixed-window或代表元upper没有被升级为cofinal实际源必要费用，ambient坏逆也没有被当成source lower。

573范围正确保留：固定430扩大A、原Ω单商下降反测；pair确保−4但未给raw-source首腿闭合；
较小原u/E域、新非标量边、不同relative pair、source families、强拓扑和有费无限传递均未排。
最强旧542+555→557 whole4/5是负惯性上预算；本轮未改善core/coupling/Ξ，未报告实际负谱lower。

本轮战略复核、标准局部来源计算及旧模型直接推论0新增轮，573仍最新数学迭代，cadence保持2且cycle14不重置，
符合当前交付的实际强度。没有把多份子稿或脚本执行当研究轮；没有把宏观Goal标complete。
trace摘要现已修正，可按这一范围root消费和同步；若新增强结论、对象或费用，应另行审查。

## 6. 最终范围绑定

以下均为最终读取版本的规范LF SHA256；hash绑定审查范围，不认证证明。

| 文件 | LF SHA256 |
|---|---|
| goals/reviews/2026-10-22-generalized-weil-roadmap-after-573.md | 5ce1b8018e645b6448978977d397bc0c92498c816aecc2b91f7840daf2002d6f |
| goals/reviews/2026-10-22-function-field-evaluation-moving-source-gate.md | f0dc61bc9a30479e97011728bbddb4a076a334b1cf0876ce16bd733bd27541f8 |
| scripts/function_field_evaluation_moving_gate.py | a21e3dc4482b1b93a3c4aedad4b127b70a7d79dfd623ddfd916c1f6b7498c9fd |
| reviews/2026-10-22/roadmap-after-573/evaluation-moving-controls.json | 479fb06ed7c8295af09e834c94df4112f49f41d430c88db43976fc3fe41fc65c |
| reviews/2026-10-22/roadmap-after-573/function-field-origins.md | d184a906fa2a7363dfa4e667b4b0abaa6b1ab24077310dad80ae324c589b881b |
| reviews/2026-10-22/roadmap-after-573/positive-realization-admission.md | b1600f187c77998b9ab42aa6193b81f21abd5bf8ef01d5ae79a493cc7b0a17b4 |
